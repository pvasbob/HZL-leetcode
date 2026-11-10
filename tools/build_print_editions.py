#!/usr/bin/env python3
"""Create and validate compact 9-point Word/PDF print editions for all categories.

Run with the dependencies in requirements-print.txt. Needs g++ and Poppler's
pdftotext. --categories 2 3 ... limits rebuilding; default: all twelve categories.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from docx import Document
import build_array_string_print as b

ROOT = b.ROOT
OUTPUT_NAMES = [
    '01_Array_and_String_Print', '02_Hash_Table_Print', '03_Linked_List_Print',
    '04_Stack_and_Queue_Print', '05_Binary_Tree_and_BST_Print', '06_Graph_Print',
    '07_Binary_Search_Print', '08_Backtracking_Print', '09_Dynamic_Programming_Print',
    '10_Greedy_Algorithms_Print', '11_Heap_and_Priority_Queue_Print',
    '12_Bit_Manipulation_and_Math_Print',
]


def validate(base: Path, problems, pages, heights, capacity):
    pdf = base.with_suffix('.pdf')
    docx = base.with_suffix('.docx')
    placements = {p.number: set() for p in problems}
    for pi, page in enumerate(pages, 1):
        for ci, column in enumerate(page, 1):
            for line in column:
                if line.kind != 'gap':
                    assert line.size == 9
                    placements[line.problem].add((pi, ci))
    assert len(placements) == 50 and all(len(p) == 1 for p in placements.values())
    assert all(h <= capacity + 1e-6 for h in heights)
    document = Document(docx)
    assert len(document.tables) == len(pages)
    seen = set()
    for pi, table in enumerate(document.tables, 1):
        for ci in (0, 2):
            for paragraph in table.rows[0].cells[ci].paragraphs:
                for run in paragraph.runs:
                    if run.text.strip():
                        assert run.font.size.pt == 9
                match = re.match(r'\d+\s+LC\s+(\d+)\s+\|', paragraph.text)
                if match:
                    number = int(match[1]); assert number not in seen; seen.add(number)
                    assert placements[number] == {(pi, ci//2+1)}
    assert seen == set(placements)
    body_text = '\n'.join(p.text for t in document.tables for c in t.rows[0].cells for p in c.paragraphs)
    for problem in problems:
        assert f'({problem.difficulty})' in body_text
    with zipfile.ZipFile(docx) as package:
        assert not any(re.match(r'word/(?:header|footer)\d+\.xml$', n) for n in package.namelist())
        xml = ET.fromstring(package.read('word/document.xml'))
        wn = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        assert not xml.findall('.//w:fldSimple', wn)
        assert len(xml.findall('.//w:br[@w:type="page"]', wn)) == len(pages)-1
    with tempfile.TemporaryDirectory(prefix='hzl-print-pdf-') as folder:
        raw, bbox = Path(folder)/'text.txt', Path(folder)/'bbox.html'
        subprocess.run(['pdftotext', '-raw', str(pdf), str(raw)], check=True)
        subprocess.run(['pdftotext', '-bbox', str(pdf), str(bbox)], check=True)
        text = raw.read_text()
        assert text.count('Problem:') == 50 and text.count('Constraints:') == 50
        for excluded in ('01 / ARRAY & STRING', '50 PROBLEMS', 'Adapted from Doocs',
                         'creativecommons.org', 'No warranties', 'solution continued'):
            assert excluded not in text
        ns = {'h': 'http://www.w3.org/1999/xhtml'}
        tree = ET.parse(bbox)
        assert len(tree.findall('.//h:page', ns)) == len(pages)
        words = 0
        for word in tree.findall('.//h:word', ns):
            x1,y1,x2,y2 = [float(word.attrib[k]) for k in ['xMin','yMin','xMax','yMax']]
            assert 20 <= x1 < x2 <= 593 and 19 <= y1 < y2 <= 773, (word.text, word.attrib)
            words += 1
    return placements, words


def build(source: Path, outdir: Path, index: int):
    problems, preamble = b.read_problems(source)
    category = source.read_text().splitlines()[0].removeprefix('# ').split(' — ')[0]
    pages, heights, width, capacity = b.layout(problems, (612,792), 2)
    base = outdir/OUTPUT_NAMES[index-1]
    b.render_pdf(base.with_suffix('.pdf'), pages, (612,792), width, category)
    b.render_docx(base.with_suffix('.docx'), pages, (612,792), width, category)
    compiled = b.verify_code(problems, pages, preamble)
    placements, words = validate(base, problems, pages, heights, capacity)
    total = sum(sum(line.leading for line in header+code)
                for problem in problems for header,code in [b.problem_lines(problem,width-2)])
    mincols = math.ceil((total+b.PROBLEM_GAP*len(problems))/(capacity+b.PROBLEM_GAP))
    minimum = math.ceil(mincols/2)
    report = {
        'category':category, 'source':str(source.relative_to(ROOT)),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'problems':50, 'pages':len(pages), 'layout':'US Letter portrait, two columns',
        'font_size_pt':9, 'code_font':'Liberation Mono', 'body_font':'Liberation Sans',
        'line_spacing_pt':10, 'margins_inches':.3, 'gutter_inches':.2,
        'difficulty_beside_every_title':True,
        'difficulty_counts':{d:sum(p.difficulty==d for p in problems) for d in ['Easy','Medium','Hard']},
        'printed_headers':False,'printed_footers':False,'printed_page_numbers':False,
        'problem_order':'repacked by size; original rank labels and LC IDs retained',
        'page_lower_bound_for_this_typography':minimum,
        'matches_page_lower_bound':len(pages)==minimum,
        'solutions_kept_in_one_column':50,'split_solutions':[],
        'solution_placements':{str(k):list(next(iter(v))) for k,v in placements.items()},
        'column_heights_pt':[round(x,2) for x in heights], 'column_capacity_pt':capacity,
        'code_submissions_token_matched_and_compiled':compiled,
        'pdf_validation':{'pages':len(pages),'problem_descriptions':50,'constraints_sections':50,
                          'words_checked_inside_page_bounds':words,'overflowing_words':0},
        'word_validation':{'page_tables':len(pages),'explicit_page_breaks':len(pages)-1,
                           'visible_body_font_size_pt':9,'header_parts':0,'footer_parts':0,
                           'page_number_fields':0,'complete_single_column_problems':50,
                           'native_word_renderer_available':False},
        'page_problem_ids':[[list(dict.fromkeys(l.problem for l in col if l.kind!='gap')) for col in page]for page in pages],
    }
    base.with_suffix('.layout.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f'{index:02d}: {len(pages)} pages; 50 problems with difficulty; code and layout validated. Lower bound {minimum}.',flush=True)
    return report


def write_index(outdir):
    reports=[]
    for name in OUTPUT_NAMES:
        path=outdir/(name+'.layout.json')
        if path.exists():reports.append((name,json.loads(path.read_text())))
    lines=['# Compact LeetCode print editions','',
           'All documents use **9-point text**, compact **10-point line spacing**, two columns, and 0.3-inch margins. Every title includes **Easy, Medium, or Hard**. Each complete problem and solution stays in a single column on one page. There are **no printed headers, footers, page numbers, attribution blocks, explanations, or complexity analyses**.','',
           'Problems are repacked by size to reduce unused space. Original rank labels and LeetCode IDs are retained, but the reading order changes. Descriptions are condensed when necessary without dropping requirements; constraints and complete solution code are retained. Especially long code may have brace-only lines compacted; the C++ token sequence is verified unchanged.','',
           '| Category | Word | PDF | Pages |','|---|---|---|---:|']
    for name,r in reports:
        lines.append(f'| {r["category"]} | [Word]({name}.docx) | [PDF]({name}.pdf) | {r["pages"]} |')
    total=sum(r['pages'] for _,r in reports)
    lines+=['',f'**{len(reports)} categories, {50*len(reports)} entries, {total} PDF pages.**',
            '', '[Download every Word and PDF document](LeetCode_All_12_Print_Editions.zip).',
            '', 'Print the PDFs at actual size / 100%, duplex with long-edge flipping. PDFs contain embedded fonts and are the verified print proofs. Word uses the same measured lines and explicit column/page divisions, but pagination may vary if fonts are substituted. `.docx` is the modern Word format.',
            '', 'Validation checks all 50 entries in each document, difficulty labels, 9-point Word runs, intact single-column problems, code-token preservation and strict C++20 compilation, absence of header/footer/page-number parts, and every PDF word bounding box. Each `.layout.json` records results and page placements. These checks verify formatting; they do not replace the original collection’s algorithm tests or LeetCode’s hidden tests.',
            '', 'Rebuild all categories with `python tools/build_print_editions.py` after installing `tools/requirements-print.txt`; GCC and Poppler (`pdftotext`) are also required. The original category Markdown files are unchanged.',
            '', '## Attribution and license — companion notes only',
            '', 'Statements, constraints, and baseline code are adapted from **Doocs and its contributors**, [Doocs LeetCode](https://github.com/doocs/leetcode), reference commit `d234cf451a6bdf182ef9fccad9071faa7eb9af6b`. Copyright belongs to the Doocs community. The collection and adapted print editions are distributed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); see the [full license](../docs/REFERENCE_LICENSE.txt). Changes include description editing, C++20/algorithm improvements documented in the collection, print typography, reflow, and whole-problem packing. Distributed without warranties. Attribution remains in these notes and nonprinting document properties.']
    (outdir/'README.md').write_text('\n'.join(lines)+'\n')
    if len(reports)==12:
        archive=outdir/'LeetCode_All_12_Print_Editions.zip'
        with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as bundle:
            for name,_ in reports:
                for suffix in ['.docx','.pdf']:
                    path=outdir/(name+suffix);bundle.write(path,path.name)
            readme=(outdir/'README.md').read_text().replace('../docs/REFERENCE_LICENSE.txt','REFERENCE_LICENSE.txt')
            bundle.writestr('README.md',readme)
            bundle.write(ROOT/'docs/REFERENCE_LICENSE.txt','REFERENCE_LICENSE.txt')
        print(f'Archive: {archive.name}; total {total} pages.',flush=True)
    return reports


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--categories',nargs='+',type=int,default=list(range(1,13)))
    parser.add_argument('--output-dir',type=Path,default=ROOT/'print')
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    sources=sorted((ROOT/'solutions').glob('[0-9][0-9]_*.md'))
    assert len(sources)==12
    for index in args.categories:
        if not 1<=index<=12:parser.error('category numbers must be between 1 and 12')
        build(sources[index-1],args.output_dir,index)
    write_index(args.output_dir)

if __name__=='__main__':main()
