# Solution collection notes

## Scope and sources

The 12 files in `solutions/` reproduce the original category order and all 600 entries, including the original list's intentional overlaps. There are 515 distinct problem IDs. Checkmarked `x.` entries are included and are numbered by their list position.

Problem statements, numeric constraints, baseline explanations, implementations, and example inputs/outputs are adapted from Doocs and its contributors at commit `d234cf451a6bdf182ef9fccad9071faa7eb9af6b`. Every problem links to that pinned page and the corresponding official LeetCode page. Descriptions retain the input/output requirements; source worked examples are omitted from the study files. Follow-up requirements are retained with the constraints when present. Difficulty labels follow the user's list.

The additions are licensed under CC BY-SA 4.0, with the upstream license reproduced in [REFERENCE_LICENSE.txt](REFERENCE_LICENSE.txt). Source: [Doocs LeetCode](https://github.com/doocs/leetcode). Copyright belongs to the Doocs community. Adaptations are distributed without warranties. The license applies to this adapted collection and related tests, not to pre-existing repository files. Constraint values reflect the pinned reference snapshot, rather than a claim that all 515 live official pages were independently checked.

## Algorithm choices

The goal is a strong solution under the stated constraints, considering running time, auxiliary storage, clarity, and implementation reliability. There is no single universal meaning of “best”: some problems have time/space tradeoffs, average-case selection algorithms, or advanced theoretical algorithms that are unnecessary at the given bounds. Complexity statements identify these distinctions where relevant. They are not a proof of global optimality for every problem.

Selected improvements over the baseline include:

- Manacher's linear-time palindrome radii for LC 5 and LC 647.
- Constant-space two-pointer rainwater accumulation for LC 42.
- Rolling DP for edit distance, LCS, regular-expression matching, palindrome subsequences, and several grid/counting problems.
- Bottom-up constant-space linked-list merge sort; inorder list-to-BST construction; constant-space perfect-tree next pointers; in-place list filtering/compaction.
- Linear expected-time frequency buckets for top-k elements, Floyd cycle detection for the duplicate number, and prefix-XOR aggregation for triplet counts.
- O(n log n) Fenwick-tree queue reconstruction, residue-group DP for beautiful subsets, and bulk leveling for increments before modular multiplication.
- Knuth's O(c²) interval-DP optimization for stick cutting, validated against cubic DP on randomized cases.
- O(sqrt(n))-time number-theoretic perfect-square counting and a constant-space Catalan recurrence.
- Structural subtree interning, linear token-KMP subtree matching, and iterative bridge detection to avoid a 100000-frame recursive DFS.
- Owning standard containers for LRU/LFU caches and linked-list design, with randomized comparison against simple reference models.
- Unbiased standard-library random distributions instead of `rand() % bound`.
- Separate index updates in LC 2462, eliminating reliance on function-argument evaluation order.

C++20 changes include range algorithms, container membership tests, standard bit operations, `std::midpoint`, defaulted structural equality, standard heap-storage vectors in place of runtime-sized stack arrays, and generic self-recursive lambdas instead of C++23 explicit-object lambdas. The collection does not require C++23 or C++26.

Some counting problems guarantee only that the final answer fits `int`. Counts for unused prefixes or unreachable intermediate totals can grow much larger. LC 63, LC 115, LC 377, and LC 518 safely saturate intermediate additions at `INT_MAX`; their nonnegative addition recurrences preserve the exact final answer whenever it is below or equal to that cap. Ugly-number candidate products use 64-bit arithmetic even when the selected result fits 32 bits.

## Submission conventions

Each C++ block is a complete **judge submission**, independent of other blocks. It is not a standalone executable and does not contain `main`. The standard-library preamble at the top of each category is sufficient for the standard-library facilities used. Add the exact judge-defined node types and API interfaces when compiling locally. Tests provide signature stubs for these interfaces, not implementations of the judge service.

Complexity excludes returned output unless the entry explicitly includes it. Recursion stacks count as auxiliary space. Hash-table lookup bounds are expected/amortized. Sorting can mutate the input. Algorithms that relink lists or trees may change the original structures; review pointer ownership before freeing returned structures. Generated BST variants may share subtrees, so independently deleting every returned tree can double-free shared nodes.

## Validation evidence and limits

`python3 tools/validate_solutions.py` verifies all 12 files, exactly 50 entries per file, exact category/problem order against the original list, required content sections, and identical code for repeated IDs. It compiles all 515 distinct submissions with `g++ -std=c++20 -pedantic-errors -fsyntax-only` using problem-type signature stubs. See [COMPILE_REPORT.json](COMPILE_REPORT.json).

`python3 tools/smoke_test_solutions.py` extracts the actual code from the Markdown and runs 971 deterministic reference examples plus 24 boundary/randomized suites, 995 test groups in total, across 418 distinct problems. Runtime builds enable `-fsanitize=undefined -fno-sanitize-recover=undefined -D_GLIBCXX_ASSERTIONS`. See [SMOKE_TEST_REPORT.json](SMOKE_TEST_REPORT.json). Test fixtures are in `tools/smoke_cases.json` and `tools/regression_cases.json`.

The randomized suites use fixed seeds and independent slow models or structural checks, including palindrome enumeration, cubic cut DP, queue-order constraints, subset enumeration, one-at-a-time heap increments, brute-force XOR triplets, list/vector comparison, LRU/LFU models, edge-deletion bridge detection, and worker-selection simulation. Additional cases check overflow-prone intermediate counts and a 100000-node bridge chain. A balanced-BST case checks inorder values and balance rather than requiring one arbitrary tree shape. Tree/list outputs are compared structurally, not by pointer identity; unordered outputs are normalized only where the problem allows it.

All compiled snippets passed; all 995 runtime groups passed. Runtime coverage is not exhaustive. Interactive API problems, many design-operation sequences, graph/node identity questions, and some problems with multiple valid outputs are not included in the automatic example conversion. These checks do not assert acceptance by LeetCode's hidden tests. Recursive solutions still require stack space proportional to their documented depth; the compiler check does not measure judge-specific stack limits.

Compiler used: GCC 11.4.0 on Linux, strict C++20. Python tools require Python 3.10 or later and use only the standard library. Temporary compilation products are created outside the repository and cleaned up automatically. The test harness intentionally does not check leaks in judge-owned/output nodes; UBSan checks arithmetic and other instrumented undefined behavior, not ownership.
