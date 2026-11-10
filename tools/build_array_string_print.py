#!/usr/bin/env python3
"""Build a dense, paginated Word/PDF print edition of category 01.

Dependencies: python-docx, reportlab. Uses installed Liberation fonts.
Outputs share the same measured lines/column breaks. The PDF is the print proof;
Word pagination can vary slightly with font substitution in another environment.
Descriptions are concise editorial summaries; constraints and code derive from
solutions/01_array_and_string.md. See docs/REFERENCE_LICENSE.txt (CC BY-SA 4.0).
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from functools import lru_cache
import json
import math
from pathlib import Path
import re
import subprocess
import tempfile
import time

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'solutions/01_array_and_string.md'
FONT_DIR = Path('/usr/share/fonts/truetype/liberation2')
FONTS = {'Body': ('LiberationSans-Regular.ttf', 'Liberation Sans'),
         'Bold': ('LiberationSans-Bold.ttf', 'Liberation Sans'),
         'Code': ('LiberationMono-Regular.ttf', 'Liberation Mono')}
for name, (filename, _) in FONTS.items():
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))

BODY_SIZE, BODY_LEADING = 9.0, 10.0
CODE_SIZE, CODE_LEADING = 9.0, 10.0
TITLE_SIZE, TITLE_LEADING = 9.0, 10.0
MARGIN = 0.3 * 72
GUTTER = 0.2 * 72
TOP = MARGIN
BOTTOM_RESERVE = MARGIN
PAGE_SAFETY = 4.0
PROBLEM_GAP = 4.0

@dataclass
class Line:
    kind: str
    text: str
    size: float
    leading: float
    problem: int
    source_line: int = -1

@dataclass
class Problem:
    rank: int
    number: int
    title: str
    description: str
    constraints: str
    code: str
    difficulty: str = 'Medium'


def plain(text: str) -> str:
    text = re.sub(r'!\[[^]]*\]\([^)]*\)', '', text)
    text = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('**', '').replace('`', '').replace('\u200b', '').replace('\ufeff', '')
    return re.sub(r'\s+', ' ', text).strip()


def read_problems(source: Path = SOURCE) -> tuple[list[Problem], str]:
    text = source.read_text()
    summaries = json.loads((ROOT / 'tools/array_string_print_descriptions.json').read_text())
    extra = ROOT / 'tools/print_description_overrides.json'
    if extra.exists():
        summaries.update(json.loads(extra.read_text()))
    problems = []
    for m in re.finditer(r'<a id="lc-(\d+)"></a>\n## (\d+)\. LC \d+ — (.*?) \((Easy|Medium|Hard)\)\n(.*?)(?=\n---|\Z)', text, re.S):
        number, rank, title, difficulty, section = m.groups()
        description = section.split('### Problem description\n\n')[1].split('\n### ')[0]
        description = re.split(r'\*\*Custom Judge:', description)[0]
        description = summaries.get(number, plain(description))
        constraints = section.split('### Constraints\n\n')[1].split('\n### ')[0]
        # Optional follow-up discussions are not part of the compact print edition.
        constraints = re.split(r'(?:\*\*)?Follow[ -]?up:', constraints, flags=re.I)[0]
        constraints = re.split(r'\*\*Note:\*\* This question is the same as', constraints)[0]
        bullets = [plain(x) for x in re.split(r'\n\s*-\s+', '\n' + constraints)[1:]]
        assert bullets, number
        code = re.search(r'```cpp\n(.*?)\n```', section, re.S)[1]
        problems.append(Problem(int(rank), int(number), title, description, '; '.join(bullets), code, difficulty))
    assert len(problems) == 50
    preamble = re.search(r'```cpp\n(.*?)\n```', text, re.S)[1]
    return problems, preamble


def wrap_text(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines, line = [], ''
    for word in words:
        candidate = f'{line} {word}' if line else word
        if pdfmetrics.stringWidth(candidate, font, size) <= width:
            line = candidate
        else:
            if line:
                lines.append(line)
            if pdfmetrics.stringWidth(word, font, size) > width:
                raise ValueError(f'Text token is too wide: {word!r}')
            line = word
    if line:
        lines.append(line)
    return lines


def code_without_comments(code: str) -> str:
    # C++ literals are kept atomically, including escaped quotes and whitespace.
    lexer = re.compile(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|//[^\n]*|/\*.*?\*/', re.S)
    return lexer.sub(lambda m: '' if m[0].startswith(('//', '/*')) else m[0], code)


def words_outside_literals(line: str) -> list[str]:
    words, word, quote, escaped = [], '', None, False
    for ch in line:
        if quote:
            word += ch
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == quote:
                quote = None
        elif ch in ('"', "'"):
            quote = ch
            word += ch
        elif ch.isspace():
            if word:
                words.append(word)
                word = ''
        else:
            word += ch
    if word:
        words.append(word)
    return words


def wrap_code(code: str, width: float, number: int, compact_closers: bool = False) -> list[Line]:
    result = []
    originals = code_without_comments(code).splitlines()
    if compact_closers:
        compacted = []
        for original in originals:
            if re.fullmatch(r'\s*};?\s*', original) and compacted:
                compacted[-1] += ' ' + original.strip()
            elif original.strip():
                compacted.append(original)
        originals = compacted
    for source_line, original in enumerate(originals):
        if not original.strip():
            continue
        indent = len(original) - len(original.lstrip())
        base = ' ' * (indent // 2)  # Four-space source indent -> two-space print indent.
        words = []
        for word in words_outside_literals(original.lstrip()):
            if pdfmetrics.stringWidth(' ' * (len(base) + 2) + word, 'Code', CODE_SIZE) > width and not any(q in word for q in ['"', "'"]):
                # C++ permits whitespace after delimiters. Split oversized
                # expressions there, never inside an identifier or literal.
                words.extend(x for x in re.split(r'(?<=[,({])', word) if x)
            else:
                words.append(word)
        current = base
        # Wrapped statements stay visibly inside their original nesting level.
        # Never dedent a deep continuation just to save horizontal space.
        continuation = ' ' * (len(base) + 2)
        for word in words:
            candidate = current + (' ' if current.strip() else '') + word
            if pdfmetrics.stringWidth(candidate, 'Code', CODE_SIZE) <= width:
                current = candidate
                continue
            if current.strip():
                result.append(Line('code', current, CODE_SIZE, CODE_LEADING, number, source_line))
            current = continuation + word
            if pdfmetrics.stringWidth(current, 'Code', CODE_SIZE) > width:
                raise ValueError(f'Code token too wide at its proper indentation in LC {number}: {word}')
        if current.strip():
            result.append(Line('code', current, CODE_SIZE, CODE_LEADING, number, source_line))
    return result


def problem_lines(problem: Problem, width: float) -> tuple[list[Line], list[Line]]:
    header = [Line('title', t, TITLE_SIZE, TITLE_LEADING, problem.number)
              for t in wrap_text(f'{problem.rank:02d}  LC {problem.number}  |  {problem.title} ({problem.difficulty})', 'Bold', TITLE_SIZE, width)]
    header += [Line('body', t, BODY_SIZE, BODY_LEADING, problem.number)
               for t in wrap_text('Problem: ' + problem.description, 'Body', BODY_SIZE, width)]
    header += [Line('constraints', t, BODY_SIZE, BODY_LEADING, problem.number)
               for t in wrap_text('Constraints: ' + problem.constraints, 'Body', BODY_SIZE, width)]
    header.append(Line('gap', '', 1, 3, problem.number))
    code = wrap_code(problem.code, width, problem.number)
    if sum(line.leading for line in header + code) > 792 - TOP - BOTTOM_RESERVE - PAGE_SAFETY:
        code = wrap_code(problem.code, width, problem.number, compact_closers=True)
    return header, code


@lru_cache(maxsize=64)
def tighter_packing(weights, capacity, target):
    """Try a smaller page count with bounded, symmetry-pruned bin packing.

    Return a complete feasible assignment or None; a timeout never changes a
    previously valid layout. Sizes include one gap, also added to capacity.
    """
    order = sorted(range(len(weights)), key=lambda i: (-weights[i], i))
    remaining = [capacity] * target
    groups = [[] for _ in range(target)]
    suffix = [0] * (len(weights) + 1)
    for i in range(len(weights)-1, -1, -1):
        suffix[i] = suffix[i+1] + weights[order[i]]
    if suffix[0] > capacity * target:
        return None
    deadline = time.monotonic() + 1.5
    states = set()
    visits = 0
    def search(index):
        nonlocal visits
        visits += 1
        if visits % 256 == 0 and time.monotonic() > deadline:
            raise TimeoutError
        if index == len(order):
            return True
        state = (index, tuple(sorted(remaining, reverse=True)))
        if state in states:
            return False
        weight = weights[order[index]]
        minimum = weights[order[-1]]
        if sum(space for space in remaining if space >= minimum) < suffix[index]:
            return False
        tried = set()
        for bucket in sorted(range(target), key=lambda i: remaining[i]):
            space = remaining[bucket]
            if space < weight or space in tried:
                continue
            tried.add(space)
            remaining[bucket] -= weight
            groups[bucket].append(order[index])
            if search(index+1):
                return True
            groups[bucket].pop()
            remaining[bucket] += weight
            if space == capacity:
                break
        if len(states) < 100000:
            states.add(state)
        return False
    try:
        if search(0):
            assert sorted(i for group in groups for i in group) == list(range(len(weights)))
            assert all(sum(weights[i] for i in group) <= capacity for group in groups)
            return tuple(tuple(group) for group in groups if group)
    except TimeoutError:
        pass
    return None


def layout(problems: list[Problem], page_size: tuple[float, float], columns: int):
    page_w, page_h = page_size
    col_width = (page_w - 2 * MARGIN - (columns - 1) * GUTTER) / columns
    # Tiny measurement tolerances, rather than header/footer reservations.
    width = col_width - 2
    available = page_h - TOP - BOTTOM_RESERVE - PAGE_SAFETY
    blocks = []
    for problem in problems:
        header, code = problem_lines(problem, width)
        # A complete problem is atomic: never continue its solution in another
        # column or page. Fail explicitly if a future solution cannot fit.
        block = header + code
        block_height = sum(x.leading for x in block)
        if block_height > available:
            raise ValueError(
                f'LC {problem.number} needs {block_height:.1f} pt, '
                f'exceeding the {available:.1f} pt column capacity; '
                'the solution will not be split or reduced below 9 pt.'
            )
        blocks.append((problem.rank, block_height, block))
    # Best-fit decreasing uses the otherwise wasted tails of columns. Original
    # rank/LC labels remain visible, but reading order may change to save paper.
    bins, loads = [], []
    for item in sorted(blocks, key=lambda item: (-item[1], item[0])):
        eligible = [i for i, load in enumerate(loads)
                    if load + PROBLEM_GAP + item[1] <= available + 1e-7]
        if eligible:
            target = max(eligible, key=lambda i: loads[i])
            bins[target].append(item)
            loads[target] += PROBLEM_GAP + item[1]
        else:
            bins.append([item])
            loads.append(item[1])
    # Reduce the number of pages, rather than merely the number of columns.
    # Weight/capacity are integer points for the approved 9/10-point typography.
    weights = tuple(round(item[1] + PROBLEM_GAP) for item in blocks)
    cap = math.floor(available + PROBLEM_GAP)
    lower = max(math.ceil(sum(weights)/cap),
                max(math.ceil(sum(w > cap/k for w in weights)/(k-1))
                    for k in range(2,20)))
    target = columns * (math.ceil(len(bins)/columns)-1)
    while target >= lower:
        assignment = tighter_packing(weights, cap, target)
        if assignment is None:
            break
        bins = [[blocks[i] for i in group] for group in assignment]
        loads = [sum(item[1] for item in items) + PROBLEM_GAP*(len(items)-1) for items in bins]
        target = columns * (math.ceil(len(bins)/columns)-1)
    # Improve visual balance without increasing the minimum page count found.
    # Move a whole problem only when it reduces squared unused column space.
    while True:
        best = None
        for donor, items in enumerate(bins):
            if len(items) <= 1:
                continue
            for receiver in range(len(bins)):
                if donor == receiver:
                    continue
                for index, item in enumerate(items):
                    new_receiver = loads[receiver] + item[1] + PROBLEM_GAP
                    if new_receiver > available + 1e-7:
                        continue
                    new_donor = loads[donor] - item[1] - PROBLEM_GAP
                    gain = (loads[donor]**2 + loads[receiver]**2
                            - new_donor**2 - new_receiver**2)
                    if gain > 1e-6 and (best is None or gain > best[0]):
                        best = (gain, donor, receiver, index, new_donor, new_receiver)
        if best is None:
            break
        _, donor, receiver, index, loads[donor], loads[receiver] = best
        bins[receiver].append(bins[donor].pop(index))
    bins.sort(key=lambda items: min(item[0] for item in items))
    stream, heights = [], []
    for items in bins:
        lines = []
        for _, _, block in sorted(items, key=lambda item: item[0]):
            if lines:
                lines.append(Line('gap', '', 1, PROBLEM_GAP, block[0].problem))
            lines.extend(block)
        stream.append(lines)
        heights.append(sum(line.leading for line in lines))
    while len(stream) % columns:
        stream.append([])
        heights.append(0.0)
    pages = [stream[i:i+columns] for i in range(0, len(stream), columns)]
    return pages, heights, col_width, available


def render_pdf(path: Path, pages, page_size, col_width, category='01 Array & String'):
    page_w, page_h = page_size
    pdf = canvas.Canvas(str(path), pagesize=page_size, pageCompression=1)
    pdf.setTitle(category + ' — compact C++20 print edition')
    pdf.setAuthor('HZL LeetCode study collection; adapted from Doocs contributors')
    pdf.setSubject('50 problems: descriptions, constraints, solutions; CC BY-SA 4.0')
    pdf.setKeywords('Adapted from Doocs contributors; https://github.com/doocs/leetcode; '
                    'CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/; '
                    'modified descriptions and typography; no warranties')
    for columns in pages:
        for col_index, lines in enumerate(columns):
            x = MARGIN + col_index * (col_width + GUTTER)
            top = page_h - TOP
            for line in lines:
                if line.kind == 'gap':
                    top -= line.leading
                    continue
                font = 'Code' if line.kind == 'code' else 'Bold' if line.kind in ('title', 'continued') else 'Body'
                if line.kind == 'title':
                    pdf.setFillColorRGB(.92, .92, .92)
                    pdf.rect(x, top - line.leading + 1, col_width, line.leading, stroke=0, fill=1)
                pdf.setFillColorRGB(0, 0, 0)
                pdf.setFont(font, line.size)
                pdf.drawString(x, top - line.size, line.text)
                top -= line.leading
        pdf.showPage()
    pdf.save()


def set_font(run, family, size, bold=False):
    run.font.name = family
    run.font.size = Pt(size)
    run.bold = bold
    fonts = run._element.get_or_add_rPr().get_or_add_rFonts()
    for key in ('ascii', 'hAnsi', 'eastAsia', 'cs'):
        fonts.set(qn('w:' + key), family)


def spacing(paragraph, leading):
    pf = paragraph.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = Pt(leading)
    pf.keep_together = True
    pf.keep_with_next = False
    pf.widow_control = False
    pf.left_indent = Pt(0)
    pf.right_indent = Pt(0)
    ppr = paragraph._p.get_or_add_pPr()
    # Do not snap to a document character/line grid.
    snap = OxmlElement('w:snapToGrid')
    snap.set(qn('w:val'), '0')
    ppr.append(snap)


def render_docx(path: Path, pages, page_size, col_width, category='01 Array & String'):
    doc = Document()
    section = doc.sections[0]
    page_w, page_h = page_size
    section.page_width = Pt(page_w)
    section.page_height = Pt(page_h)
    section.left_margin = section.right_margin = Pt(MARGIN)
    section.top_margin = Pt(TOP)
    section.bottom_margin = Pt(BOTTOM_RESERVE)
    section.header_distance = section.footer_distance = Pt(0)
    normal = doc.styles['Normal']
    normal.font.name = 'Liberation Sans'
    normal.font.size = Pt(BODY_SIZE)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = Pt(BODY_LEADING)
    # Disable automatic inter-paragraph layout adjustments.
    settings = doc.settings.element
    compatibility = settings.find(qn('w:compat'))
    if compatibility is None:
        compatibility = OxmlElement('w:compat'); settings.append(compatibility)
    compat_setting = OxmlElement('w:compatSetting')
    compat_setting.set(qn('w:name'), 'compatibilityMode')
    compat_setting.set(qn('w:uri'), 'http://schemas.microsoft.com/office/word')
    compat_setting.set(qn('w:val'), '15')
    compatibility.append(compat_setting)
    doc.core_properties.title = category + ' — compact C++20 print edition'
    doc.core_properties.author = 'HZL LeetCode study collection; Doocs contributors'
    doc.core_properties.subject = '50 problems; descriptions, constraints, C++20 solutions'
    doc.core_properties.comments = ('Adapted from Doocs contributors, https://github.com/doocs/leetcode, '
        'under CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/. '
        'Modified descriptions and typography; no warranties. See print/README.md.')
    for page_index, columns in enumerate(pages):
        if page_index:
            pagebreak = doc.add_paragraph()
            spacing(pagebreak, 1)
            set_font(pagebreak.add_run(), 'Liberation Sans', 1)
            # A manual page break in a dedicated one-point paragraph.
            pagebreak.add_run().add_break(__import__('docx').enum.text.WD_BREAK.PAGE)
        count = 2*len(columns) - 1
        table = doc.add_table(rows=1, cols=count)
        table.alignment = WD_TABLE_ALIGNMENT.LEFT
        table.autofit = False
        widths = [col_width if i % 2 == 0 else GUTTER for i in range(count)]
        for gridcol, width in zip(table._tbl.tblGrid.gridCol_lst, widths):
            gridcol.set(qn('w:w'), str(round(width*20)))
        properties = table._tbl.tblPr
        borders = OxmlElement('w:tblBorders')
        for side in ('top','left','bottom','right','insideH','insideV'):
            edge = OxmlElement('w:' + side); edge.set(qn('w:val'), 'nil'); borders.append(edge)
        properties.append(borders)
        table_width = properties.find(qn('w:tblW'))
        table_width.set(qn('w:w'), str(round(sum(widths)*20)))
        table_width.set(qn('w:type'), 'dxa')
        rowpr = table.rows[0]._tr.get_or_add_trPr()
        rowpr.append(OxmlElement('w:cantSplit'))
        for i, (cell, width) in enumerate(zip(table.rows[0].cells, widths)):
            cell.width = Pt(width)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            tcpr = cell._tc.get_or_add_tcPr()
            margins = OxmlElement('w:tcMar')
            for side in ('top','left','bottom','right'):
                margin = OxmlElement('w:' + side); margin.set(qn('w:w'), '0'); margin.set(qn('w:type'), 'dxa'); margins.append(margin)
            tcpr.append(margins)
            lines = columns[i//2] if i % 2 == 0 else []
            if not lines:
                spacing(cell.paragraphs[0], 1)
                set_font(cell.paragraphs[0].add_run(), 'Liberation Sans', 1)
            for j, line in enumerate(lines):
                p = cell.paragraphs[0] if j == 0 else cell.add_paragraph()
                spacing(p, line.leading)
                # Word must keep all paragraphs in the same problem together,
                # even if the document is edited after generation.
                p.paragraph_format.keep_with_next = (
                    j + 1 < len(lines) and line.kind != 'gap'
                    and lines[j + 1].kind != 'gap'
                    and lines[j + 1].problem == line.problem
                )
                family = 'Liberation Mono' if line.kind == 'code' else 'Liberation Sans'
                set_font(p.add_run(line.text or ' '), family, line.size,
                         line.kind in ('title', 'continued'))
                if line.kind == 'title':
                    shade = OxmlElement('w:shd'); shade.set(qn('w:fill'), 'EBEBEB'); p._p.get_or_add_pPr().append(shade)
    doc.save(path)


def verify_code(problems, pages, preamble):
    printed = {p.number: [] for p in problems}
    for page in pages:
        for column in page:
            for line in column:
                if line.kind == 'code': printed[line.problem].append(line.text)
    token_pattern = r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|\w+|\S'
    with tempfile.TemporaryDirectory(prefix='hzl-print-code-') as folder:
        from validate_solutions import STUBS
        source = [preamble, STUBS]
        for p in problems:
            a = re.findall(token_pattern, code_without_comments(p.code))
            b = re.findall(token_pattern, '\n'.join(printed[p.number]))
            assert a == b, f'Printed code changed tokens: LC {p.number}'
            source += [f'namespace lc{p.number} {{', '\n'.join(printed[p.number]), '}']
        path = Path(folder)/'print_code.cpp'
        path.write_text('\n'.join(source))
        check = subprocess.run(['g++', '-std=c++20', '-pedantic-errors', '-fsyntax-only', str(path)], capture_output=True, text=True)
        if check.returncode:
            raise RuntimeError(check.stderr)
    return len(problems)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT/'print')
    args = parser.parse_args()
    problems, preamble = read_problems()
    candidates = []
    for label, size, columns in [('letter-portrait-2', (612,792),2),
                                  ('letter-landscape-2',(792,612),2),
                                  ('letter-landscape-3',(792,612),3),
                                  ('letter-portrait-1',(612,792),1)]:
        try:
            pages, heights, width, available = layout(problems,size,columns)
            candidates.append({'layout':label,'pages':len(pages),'column_width_pt':round(width,2),
                               'utilization':round(sum(heights)/(len(heights)*available),3)})
        except ValueError as e:
            candidates.append({'layout':label,'error':str(e)})
    # Preserve readable portrait two-column pages even when a landscape alternative ties.
    size = (612,792)
    pages, heights, width, available = layout(problems,size,2)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    basename = args.output_dir/'01_Array_and_String_Print'
    render_pdf(basename.with_suffix('.pdf'),pages,size,width)
    render_docx(basename.with_suffix('.docx'),pages,size,width)
    checked = verify_code(problems,pages,preamble)
    placements = {}
    for page_index, columns in enumerate(pages, 1):
        for column_index, lines in enumerate(columns, 1):
            for line in lines:
                if line.kind == 'code':
                    placements.setdefault(line.problem, set()).add((page_index, column_index))
    assert len(placements) == 50 and all(len(p) == 1 for p in placements.values())
    total_block_height = sum(sum(line.leading for line in header + code)
                             for p in problems
                             for header, code in [problem_lines(p, width - 2)])
    column_lower_bound = math.ceil(
        (total_block_height + PROBLEM_GAP * len(problems)) / (available + PROBLEM_GAP)
    )
    page_lower_bound = math.ceil(column_lower_bound / 2)
    report = {'source':str(SOURCE.relative_to(ROOT)), 'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'problems':len(problems), 'pages':len(pages), 'layout':'US Letter portrait, two columns',
              'code_font':'Liberation Mono, 9 pt, exact 10 pt line spacing',
              'body_font':'Liberation Sans, 9 pt, exact 10 pt line spacing',
              'title_font':'Liberation Sans Bold, 9 pt',
              'all_problem_content_font_size_pt':9,
              'printed_headers':False,'printed_footers':False,'printed_page_numbers':False,
              'packing':'best-fit decreasing whole problems; balanced columns; original rank labels retained',
              'problem_order':'reordered to fill available column space',
              'page_lower_bound_for_this_typography':page_lower_bound,
              'matches_page_lower_bound':len(pages)==page_lower_bound,
              'solutions_kept_in_one_column':50,
              'split_solutions':[],
              'solution_placements':{str(k):list(next(iter(v))) for k,v in placements.items()},
              'margins_inches':.3, 'gutter_inches':.2,
              'code_submissions_token_matched_and_compiled':checked,
              'column_heights_pt':[round(x,2) for x in heights],
              'column_capacity_pt':round(available,2),'layout_comparison':candidates,
              'page_problem_ids':[[list(dict.fromkeys(line.problem for line in column if line.kind!='gap')) for column in page] for page in pages]}
    basename.with_suffix('.layout.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
