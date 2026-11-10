#!/usr/bin/env python3
"""Check coverage and strictly compile every distinct Markdown C++20 submission.

Usage: python3 tools/validate_solutions.py [--jobs 4] [--only 1 2 ...]
Needs Python 3.10+ and g++ with C++20 support. No network/dependencies required.
Judge stubs model type signatures only; syntax checks do not prove correctness.
"""
import argparse
import concurrent.futures
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUBS = r'''
struct ListNode {
    int val; ListNode* next;
    ListNode(int v=0, ListNode* p=nullptr):val(v),next(p){}
};
struct TreeNode {
    int val; TreeNode *left, *right;
    TreeNode(int v=0, TreeNode* l=nullptr, TreeNode* r=nullptr):val(v),left(l),right(r){}
};
class Node {
public:
    int val=0;
    Node *left=nullptr, *right=nullptr, *next=nullptr;
    Node *random=nullptr, *prev=nullptr, *child=nullptr;
    vector<Node*> neighbors;
    Node()=default;
    Node(int v):val(v){}
    Node(int v, vector<Node*> ns):val(v),neighbors(move(ns)){}
    Node(int v, Node* l, Node* r, Node* n):val(v),left(l),right(r),next(n){}
};
class MountainArray {
public:
    int get(int index);
    int length();
};
bool isBadVersion(int version);
'''

def extract():
    source = (ROOT / 'LeetCode_Top_50_Per_Category_with_Difficulty.txt').read_text()
    expected = [int(x) for x in re.findall(r'LC\s+(\d+)', source)]
    files = sorted((ROOT / 'solutions').glob('[0-9][0-9]_*.md'))
    if len(files) != 12:
        raise ValueError(f'Expected 12 category files; found {len(files)}')
    found, snippets, preamble = [], {}, None
    for path in files:
        text = path.read_text()
        blocks = re.findall(r'```cpp\n(.*?)\n```', text, re.S)
        if preamble is None:
            preamble = blocks[0]
        if blocks[0] != preamble:
            raise ValueError(f'{path}: inconsistent preamble')
        entries = re.split(r'<a id="lc-(\d+)"></a>', text)[1:]
        if len(entries) != 100:
            raise ValueError(f'{path}: expected 50 entries')
        for key, section in zip(entries[::2], entries[1::2]):
            problem = int(key)
            found.append(problem)
            for heading in ('Problem description', 'Constraints', 'Approach and complexity', 'C++20 solution'):
                if f'### {heading}\n\n' not in section:
                    raise ValueError(f'LC {problem}: missing {heading}')
            for heading in ('Problem description', 'Constraints', 'Approach and complexity'):
                body = section.split(f'### {heading}\n\n', 1)[1].split('\n### ', 1)[0].strip()
                if len(body) < 15:
                    raise ValueError(f'LC {problem}: empty {heading}')
            code = re.findall(r'```cpp\n(.*?)\n```', section, re.S)
            if len(code) != 1:
                raise ValueError(f'LC {problem}: expected one complete submission')
            if problem in snippets and snippets[problem] != code[0]:
                raise ValueError(f'LC {problem}: inconsistent repeated submission')
            snippets[problem] = code[0]
    if found != expected:
        raise ValueError('Problem IDs/order differ from the original list')
    return snippets, preamble

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jobs', type=int, default=4)
    parser.add_argument('--only', nargs='*', type=int)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    snippets, preamble = extract()
    print(f'Coverage: 12 files, 600 entries, {len(snippets)} unique submissions.', flush=True)
    if args.only is not None:
        snippets = {i: snippets[i] for i in args.only}
    with tempfile.TemporaryDirectory(prefix='hzl-cpp20-') as folder:
        temp = Path(folder)
        header = temp / 'preamble.hpp'
        header.write_text(preamble + '\n')
        setup = subprocess.run(['g++', '-std=c++20', '-pedantic-errors', '-x', 'c++-header', str(header)], capture_output=True, text=True)
        if setup.returncode:
            raise RuntimeError(setup.stderr)
        def check(item):
            number, code = item
            path = temp / f'lc_{number}.cpp'
            path.write_text('#include "preamble.hpp"\n' + STUBS + '\n' + code + '\n')
            result = subprocess.run(['g++', '-std=c++20', '-pedantic-errors', '-fsyntax-only', '-fmax-errors=8', str(path)], capture_output=True, text=True)
            return number, result.returncode, result.stderr.replace(str(temp) + '/', '')
        failures = {}
        done = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
            for number, status, message in executor.map(check, sorted(snippets.items())):
                done += 1
                if status:
                    failures[number] = message
                    print(f'FAIL LC {number}:\n{message}', flush=True)
                elif done % 50 == 0:
                    print(f'Checked {done}/{len(snippets)}', flush=True)
        report = {'checked': len(snippets), 'passed': len(snippets)-len(failures), 'failures': failures}
        if args.report:
            args.report.write_text(json.dumps(report, indent=2) + '\n')
        print(f'Compilation: {report["passed"]}/{report["checked"]} passed.', flush=True)
        return bool(failures)

if __name__ == '__main__':
    raise SystemExit(main())
