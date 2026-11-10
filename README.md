# HZL-leetcode

C++20 study collection for all 600 entries in [the original top-50 list](LeetCode_Top_50_Per_Category_with_Difficulty.txt), covering 515 distinct problems.

Each category file contains 50 problems, with descriptions, constraints, complete judge submissions, algorithm explanations, and time/space analysis. Repeated problems appear in full in each relevant category.

## Category files

| Category | Problems |
|---|---:|
| [1. ARRAY & STRING](solutions/01_array_and_string.md) | 50 |
| [2. HASH TABLE](solutions/02_hash_table.md) | 50 |
| [3. LINKED LIST](solutions/03_linked_list.md) | 50 |
| [4. STACK & QUEUE](solutions/04_stack_and_queue.md) | 50 |
| [5. BINARY TREE & BST](solutions/05_binary_tree_and_bst.md) | 50 |
| [6. GRAPH](solutions/06_graph.md) | 50 |
| [7. BINARY SEARCH](solutions/07_binary_search.md) | 50 |
| [8. BACKTRACKING](solutions/08_backtracking.md) | 50 |
| [9. DYNAMIC PROGRAMMING](solutions/09_dynamic_programming.md) | 50 |
| [10. GREEDY ALGORITHMS](solutions/10_greedy_algorithms.md) | 50 |
| [11. HEAP / PRIORITY QUEUE](solutions/11_heap_and_priority_queue.md) | 50 |
| [12. BIT MANIPULATION & MATH](solutions/12_bit_manipulation_and_math.md) | 50 |

## Using the solutions

Open a category file and use its contents links to jump to a problem. Compile submissions as **C++20**. Each snippet is independent; paste one into its corresponding LeetCode editor. The standard-library preamble is included at the top of each file for local compilation. LeetCode provides problem-specific node types and APIs; the design-class submissions include their own internal data structures.

Examples of C++20 facilities used include `std::ranges` algorithms, associative-container `contains`, `std::popcount`, `std::bit_floor`, `std::midpoint`, and defaulted equality. Algorithm choice and correctness take precedence over newer syntax.

## Validation

All **515 distinct submissions** pass strict C++20 syntax checks with GCC 11.4. **971 reference examples and 24 boundary/randomized suites** pass across **418 distinct problems**, with undefined-behavior sanitization and standard-library assertions enabled. These checks do not represent a submission to LeetCode or its hidden tests.

Run from the repository root:

```bash
python3 tools/validate_solutions.py
python3 tools/smoke_test_solutions.py
```

See [validation and algorithm notes](docs/SOLUTION_NOTES.md), [compilation results](docs/COMPILE_REPORT.json), and [runtime results](docs/SMOKE_TEST_REPORT.json).

## Attribution

The collection adapts statements, constraints, explanations, and baseline implementations from [Doocs LeetCode](https://github.com/doocs/leetcode), with changes for C++20, algorithm selection, correctness, ownership, and organization. Each entry links to the pinned source and official problem. The new collection and its adapted example tests are distributed under [CC BY-SA 4.0](docs/REFERENCE_LICENSE.txt), with attribution to Doocs and its contributors; this does not relicense pre-existing repository files.
