#!/usr/bin/env python3
"""Run reference examples against C++20 snippets extracted from the Markdown.

Examples adapted from Doocs LeetCode, CC BY-SA 4.0; see docs/SOLUTION_NOTES.md.
Only supported deterministic signatures are tested here. Nonunique outputs require
separate semantic checks; this suite is not a substitute for the LeetCode judge.
"""
import concurrent.futures
import json
import subprocess
import tempfile
from pathlib import Path
from validate_solutions import ROOT, STUBS, extract

SUPPORT = r'''
#include <stdexcept>
ListNode* makeList(initializer_list<int> values) {
    ListNode dummy; auto tail = &dummy;
    for (int x : values) { tail->next = new ListNode(x); tail = tail->next; }
    return dummy.next;
}
vector<int> listValues(ListNode* node) {
    vector<int> result;
    while (node && result.size() < 10000) { result.push_back(node->val); node=node->next; }
    return result;
}
TreeNode* makeTree(initializer_list<optional<int>> input) {
    vector<optional<int>> values(input);
    if (values.empty() || !values[0]) return nullptr;
    auto root = new TreeNode(*values[0]); queue<TreeNode*> q; q.push(root);
    size_t index=1;
    while (!q.empty() && index < values.size()) {
        auto node=q.front(); q.pop();
        if (values[index]) {node->left=new TreeNode(*values[index]);q.push(node->left);} ++index;
        if (index<values.size() && values[index]) {node->right=new TreeNode(*values[index]);q.push(node->right);} ++index;
    }
    return root;
}
vector<optional<int>> treeValues(TreeNode* root) {
    vector<optional<int>> result; queue<TreeNode*> q; q.push(root);
    while (!q.empty() && result.size()<10000) {
        auto node=q.front();q.pop();
        if (!node) result.emplace_back(nullopt);
        else {result.emplace_back(node->val);q.push(node->left);q.push(node->right);}
    }
    while (!result.empty() && !result.back()) result.pop_back();
    return result;
}
auto normalizeNodes(const vector<TreeNode*>& nodes) {
    vector<vector<optional<int>>> values;
    for (auto node : nodes) values.push_back(treeValues(node));
    return values;
}
auto normalizeNodes(const vector<ListNode*>& nodes) {
    vector<vector<int>> values;
    for (auto node : nodes) values.push_back(listValues(node));
    return values;
}
template<class T> auto canonical(T value, bool inner) {
    if (inner) for (auto& item:value) {
        if constexpr(requires { ranges::sort(item); }) ranges::sort(item);
    }
    ranges::sort(value); return value;
}
bool near(double a,double b) {return abs(a-b)<=1e-5*max({1.0,abs(a),abs(b)});}
bool near(const vector<double>& a,const vector<double>& b) {
    if(a.size()!=b.size())return false;
    for(size_t i=0;i<a.size();++i)if(!near(a[i],b[i]))return false;
    return true;
}
'''

def main():
    snippets, preamble = extract()
    cases = json.loads((ROOT/'tools/smoke_cases.json').read_text())
    cases += json.loads((ROOT/'tools/regression_cases.json').read_text())
    ids = sorted({case['id'] for case in cases})
    batches = [ids[i:i+30] for i in range(0,len(ids),30)]
    with tempfile.TemporaryDirectory(prefix='hzl-smoke-') as folder:
        temp=Path(folder)
        (temp/'preamble.hpp').write_text(preamble+'\n')
        subprocess.run(['g++','-std=c++20','-x','c++-header',str(temp/'preamble.hpp')],check=True,capture_output=True)
        def run(item):
            batch_index,batch=item
            source=['#include "preamble.hpp"',STUBS,SUPPORT]
            for i in batch:
                source.append(f'namespace lc{i} {{\n'+snippets[i]+'\n}')
            calls=[]
            for j,case in enumerate(cases):
                i=case['id']
                if i not in batch:continue
                source.append(f'void test{j}() {{ using namespace lc{i};\n'+case['body']+'\n}')
                calls.append(f'cerr << "RUN {i}:{j}\\n"; try {{ test{j}(); cout << "PASS {i}:{j}\\n"; }} catch (const exception& e) {{ cout << "FAIL {i}:{j}: " << e.what() << "\\n"; ++failed; }}')
            source.append('int main() { int failed=0;\n'+'\n'.join(calls)+'\nreturn failed ? 1 : 0;}')
            path=temp/f'batch{batch_index}.cpp';exe=temp/f'batch{batch_index}'
            path.write_text('\n'.join(source))
            compile_result=subprocess.run(['g++','-std=c++20','-pedantic-errors','-O0','-g0','-fsanitize=undefined','-fno-sanitize-recover=undefined','-D_GLIBCXX_ASSERTIONS',str(path),'-o',str(exe)],capture_output=True,text=True)
            if compile_result.returncode:return {'batch':batch,'compile_error':compile_result.stderr.replace(str(temp)+'/','')}
            result=subprocess.run([str(exe)],capture_output=True,text=True,timeout=120)
            failures=[line for line in result.stdout.splitlines() if line.startswith('FAIL')]
            record={'batch':batch,'passed':result.stdout.count('PASS '),'failures':failures,'exit':result.returncode}
            if result.returncode and not failures:record['runtime_error']='\n'.join(result.stderr.splitlines()[-8:])
            return record
        results=[]
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            for result in executor.map(run,enumerate(batches)):
                results.append(result)
                print(json.dumps(result),flush=True)
        report={'cases':len(cases),'problems':len(ids),'passed':sum(r.get('passed',0) for r in results),'batches':results}
        (ROOT/'docs/SMOKE_TEST_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
        print(f'Examples passed: {report["passed"]}/{len(cases)} across {len(ids)} problems.',flush=True)
        return any(r.get('compile_error') or r.get('exit',1) for r in results)

if __name__=='__main__':
    raise SystemExit(main())
