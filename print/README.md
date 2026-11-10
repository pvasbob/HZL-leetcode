# Compact LeetCode print editions

All documents use **9-point text**, compact **10-point line spacing**, two columns, and 0.3-inch margins. Every title includes **Easy, Medium, or Hard**. Each complete problem and solution stays in a single column on one page. There are **no printed headers, footers, page numbers, attribution blocks, explanations, or complexity analyses**.

Problems are repacked by size to reduce unused space. Original rank labels and LeetCode IDs are retained, but the reading order changes. Descriptions are condensed when necessary without dropping requirements; constraints and complete solution code are retained. Especially long code may have brace-only lines compacted; the C++ token sequence is verified unchanged.

| Category | Word | PDF | Pages |
|---|---|---|---:|
| 1. Array & String | [Word](01_Array_and_String_Print.docx) | [PDF](01_Array_and_String_Print.pdf) | 9 |
| 2. Hash Table | [Word](02_Hash_Table_Print.docx) | [PDF](02_Hash_Table_Print.pdf) | 11 |
| 3. Linked List | [Word](03_Linked_List_Print.docx) | [PDF](03_Linked_List_Print.pdf) | 12 |
| 4. Stack & Queue | [Word](04_Stack_and_Queue_Print.docx) | [PDF](04_Stack_and_Queue_Print.pdf) | 12 |
| 5. Binary Tree & Bst | [Word](05_Binary_Tree_and_BST_Print.docx) | [PDF](05_Binary_Tree_and_BST_Print.pdf) | 11 |
| 6. Graph | [Word](06_Graph_Print.docx) | [PDF](06_Graph_Print.pdf) | 17 |
| 7. Binary Search | [Word](07_Binary_Search_Print.docx) | [PDF](07_Binary_Search_Print.pdf) | 11 |
| 8. Backtracking | [Word](08_Backtracking_Print.docx) | [PDF](08_Backtracking_Print.pdf) | 13 |
| 9. Dynamic Programming | [Word](09_Dynamic_Programming_Print.docx) | [PDF](09_Dynamic_Programming_Print.pdf) | 10 |
| 10. Greedy Algorithms | [Word](10_Greedy_Algorithms_Print.docx) | [PDF](10_Greedy_Algorithms_Print.pdf) | 10 |
| 11. Heap / Priority Queue | [Word](11_Heap_and_Priority_Queue_Print.docx) | [PDF](11_Heap_and_Priority_Queue_Print.pdf) | 12 |
| 12. Bit Manipulation & Math | [Word](12_Bit_Manipulation_and_Math_Print.docx) | [PDF](12_Bit_Manipulation_and_Math_Print.pdf) | 8 |

**12 categories, 600 entries, 136 PDF pages.**

[Download every Word and PDF document](LeetCode_All_12_Print_Editions.zip).

Print the PDFs at actual size / 100%, duplex with long-edge flipping. PDFs contain embedded fonts and are the verified print proofs. Word uses the same measured lines and explicit column/page divisions, but pagination may vary if fonts are substituted. `.docx` is the modern Word format.

Validation checks all 50 entries in each document, difficulty labels, 9-point Word runs, intact single-column problems, code-token preservation and strict C++20 compilation, absence of header/footer/page-number parts, and every PDF word bounding box. Each `.layout.json` records results and page placements. These checks verify formatting; they do not replace the original collection’s algorithm tests or LeetCode’s hidden tests.

Rebuild all categories with `python tools/build_print_editions.py` after installing `tools/requirements-print.txt`; GCC and Poppler (`pdftotext`) are also required. The original category Markdown files are unchanged.

## Attribution and license — companion notes only

Statements, constraints, and baseline code are adapted from **Doocs and its contributors**, [Doocs LeetCode](https://github.com/doocs/leetcode), reference commit `d234cf451a6bdf182ef9fccad9071faa7eb9af6b`. Copyright belongs to the Doocs community. The collection and adapted print editions are distributed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); see the [full license](../docs/REFERENCE_LICENSE.txt). Changes include description editing, C++20/algorithm improvements documented in the collection, print typography, reflow, and whole-problem packing. Distributed without warranties. Attribution remains in these notes and nonprinting document properties.
