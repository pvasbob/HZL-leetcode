# 8. Backtracking — C++20 solutions

50 problems, in the order of the original category list. Each solution is independent: paste only its code into the corresponding LeetCode editor. Repeated problems are deliberately included in every applicable category.

**C++20 setup.** LeetCode supplies standard headers and problem-specific types (`ListNode`, `TreeNode`, `Node`, `MountainArray`) and APIs such as `isBadVersion`. For local compilation, add the following standard-library preamble and the exact types/API from the problem. A snippet is a judge submission, not a standalone executable.

```cpp
#include <algorithm>
#include <array>
#include <bit>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <optional>
#include <queue>
#include <random>
#include <ranges>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <string_view>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
```

**Conventions.** Complexity excludes returned output unless explicitly stated; recursion stacks count as auxiliary space. Hash-table bounds are expected/amortized, not worst-case guarantees. Sorting may change the input and normally uses O(log n) stack space. A returned structure owns newly allocated output nodes; do not independently free shared subtrees. Newer syntax is used where it helps, especially C++20 ranges, container `contains`, and `<bit>`.

**Sources and license.** Statements, constraints, and baseline explanations/code are adapted from [Doocs LeetCode](https://github.com/doocs/leetcode), by the Doocs contributors, under [CC BY-SA 4.0](../docs/REFERENCE_LICENSE.txt). This adapted collection is distributed under the same license, without warranties. Changes include category organization, C++20 normalization, algorithm replacements, and validation fixes. Each entry links to its pinned reference and official problem. Constraints reflect the reference snapshot; consult the official link for subsequent changes. See [validation notes](../docs/SOLUTION_NOTES.md).

## Contents

1. [LC 46 — Permutations](#lc-46)
2. [LC 78 — Subsets](#lc-78)
3. [LC 39 — Combination Sum](#lc-39)
4. [LC 77 — Combinations](#lc-77)
5. [LC 22 — Generate Parentheses](#lc-22)
6. [LC 79 — Word Search](#lc-79)
7. [LC 51 — N-Queens](#lc-51)
8. [LC 37 — Sudoku Solver](#lc-37)
9. [LC 90 — Subsets II](#lc-90)
10. [LC 47 — Permutations II](#lc-47)
11. [LC 40 — Combination Sum II](#lc-40)
12. [LC 216 — Combination Sum III](#lc-216)
13. [LC 17 — Letter Combinations of a Phone Number](#lc-17)
14. [LC 131 — Palindrome Partitioning](#lc-131)
15. [LC 93 — Restore IP Addresses](#lc-93)
16. [LC 784 — Letter Case Permutation](#lc-784)
17. [LC 698 — Partition to K Equal Sum Subsets](#lc-698)
18. [LC 473 — Matchsticks to Square](#lc-473)
19. [LC 526 — Beautiful Arrangement](#lc-526)
20. [LC 1079 — Letter Tile Possibilities](#lc-1079)
21. [LC 1239 — Maximum Length of a Concatenated String with Unique Characters](#lc-1239)
22. [LC 1415 — The k-th Lexicographical String of All Happy Strings of Length n](#lc-1415)
23. [LC 1593 — Split a String Into the Max Number of Unique Substrings](#lc-1593)
24. [LC 1863 — Sum of All Subset XOR Totals](#lc-1863)
25. [LC 2044 — Count Number of Maximum Bitwise-OR Subsets](#lc-2044)
26. [LC 2305 — Fair Distribution of Cookies](#lc-2305)
27. [LC 2597 — The Number of Beautiful Subsets](#lc-2597)
28. [LC 2698 — Find the Punishment Number of an Integer](#lc-2698)
29. [LC 1980 — Find Unique Binary String](#lc-1980)
30. [LC 282 — Expression Add Operators](#lc-282)
31. [LC 301 — Remove Invalid Parentheses](#lc-301)
32. [LC 140 — Word Break II](#lc-140)
33. [LC 212 — Word Search II](#lc-212)
34. [LC 126 — Word Ladder II](#lc-126)
35. [LC 332 — Reconstruct Itinerary](#lc-332)
36. [LC 491 — Non-decreasing Subsequences](#lc-491)
37. [LC 842 — Split Array into Fibonacci Sequence](#lc-842)
38. [LC 797 — All Paths From Source to Target](#lc-797)
39. [LC 980 — Unique Paths III](#lc-980)
40. [LC 1219 — Path with Maximum Gold](#lc-1219)
41. [LC 1255 — Maximum Score Words Formed by Letters](#lc-1255)
42. [LC 1601 — Maximum Number of Achievable Transfer Requests](#lc-1601)
43. [LC 1718 — Construct the Lexicographically Largest Valid Sequence](#lc-1718)
44. [LC 1849 — Splitting a String Into Descending Consecutive Values](#lc-1849)
45. [LC 2375 — Construct Smallest Number From DI String](#lc-2375)
46. [LC 967 — Numbers With Same Consecutive Differences](#lc-967)
47. [LC 306 — Additive Number](#lc-306)
48. [LC 60 — Permutation Sequence](#lc-60)
49. [LC 89 — Gray Code](#lc-89)
50. [LC 95 — Unique Binary Search Trees II](#lc-95)

---

<a id="lc-46"></a>
## 1. LC 46 — Permutations (Medium)

[Official problem](https://leetcode.com/problems/permutations) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0046.Permutations/README_EN.md)

### Problem description

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

### Constraints

- `1 <= nums.length <= 6`

- `-10 <= nums[i] <= 10`

- All the integers of `nums` are **unique**.

### Approach and complexity

We design a function $\textit{dfs}(i)$ to represent that the first $i$ positions have been filled, and now we need to fill the $i+1$ position. We enumerate all possible numbers, if this number has not been filled, we fill in this number, and then continue to fill the next position, until all positions are filled.

The time complexity is $O(nn!)$, where $n$ is the length of the array. There are $n!$ permutations in total, and each permutation takes $O(n)$ time to construct.

Similar problems:

- [47. Permutations II](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0047.Permutations%20II/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        vector<int> t(n);
        vector<bool> vis(n);
        auto dfs = [&](auto&& dfs, int i) -> void {
            if (i == n) {
                ans.emplace_back(t);
                return;
            }
            for (int j = 0; j < n; ++j) {
                if (!vis[j]) {
                    vis[j] = true;
                    t[i] = nums[j];
                    dfs(dfs, i + 1);
                    vis[j] = false;
                }
            }
        };
        dfs(dfs, 0);
        return ans;
    }
};
```

---

<a id="lc-78"></a>
## 2. LC 78 — Subsets (Medium)

[Official problem](https://leetcode.com/problems/subsets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0078.Subsets/README_EN.md)

### Problem description

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Constraints

- `1 <= nums.length <= 10`

- `-10 <= nums[i] <= 10`

- All the numbers of `nums` are **unique**.

### Approach and complexity

We design a function $\textit{dfs}(i)$, which represents starting the search from the $i$th element of the array for all subsets. The execution logic of the function $\textit{dfs}(i)$ is as follows:

- If $i = n$, it means the current search has ended. Add the current subset $t$ to the answer array $\textit{ans}$, and then return.
- Otherwise, we can choose not to select the current element and directly execute $\textit{dfs}(i + 1)$; or we can choose the current element, i.e., add the current element $\textit{nums}[i]$ to the subset $t$, and then execute $\textit{dfs}(i + 1)$. Note that we need to remove $\textit{nums}[i]$ from the subset $t$ after executing $\textit{dfs}(i + 1)$ (backtracking).

In the main function, we call $\textit{dfs}(0)$, i.e., start searching all subsets from the first element of the array. Finally, return the answer array $\textit{ans}$.

The time complexity is $O(n 2^n)$, and the space complexity is $O(n)$, where $n$ is the length of the array. There are a total of $2^n$ subsets, and each subset takes $O(n)$ time to construct.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int)> dfs = [&](int i) -> void {
            if (i == nums.size()) {
                ans.push_back(t);
                return;
            }
            dfs(i + 1);
            t.push_back(nums[i]);
            dfs(i + 1);
            t.pop_back();
        };
        dfs(0);
        return ans;
    }
};
```

---

<a id="lc-39"></a>
## 3. LC 39 — Combination Sum (Medium)

[Official problem](https://leetcode.com/problems/combination-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0039.Combination%20Sum/README_EN.md)

### Problem description

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

### Constraints

- `1 <= candidates.length <= 30`

- `2 <= candidates[i] <= 40`

- All elements of `candidates` are **distinct**.

- `1 <= target <= 40`

### Approach and complexity

Sort candidates and recurse on nondecreasing candidate indices. Reusing the current index permits unlimited copies; stop once the next value exceeds the remaining target.

Let T be target, a the minimum candidate, c the candidate count, and d=floor(T/a). A conservative time bound is O(c^(d+1)+R·d) for R outputs, plus sorting; auxiliary space O(d+c). The bound depends on target, not just the number of candidates.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        ranges::sort(candidates);
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int, int)> dfs = [&](int i, int s) {
            if (s == 0) {
                ans.emplace_back(t);
                return;
            }
            if (s < candidates[i]) {
                return;
            }
            for (int j = i; j < candidates.size(); ++j) {
                t.push_back(candidates[j]);
                dfs(j, s - candidates[j]);
                t.pop_back();
            }
        };
        dfs(0, target);
        return ans;
    }
};
```

---

<a id="lc-77"></a>
## 4. LC 77 — Combinations (Medium)

[Official problem](https://leetcode.com/problems/combinations) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0077.Combinations/README_EN.md)

### Problem description

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

You may return the answer in **any order**.

### Constraints

- `1 <= n <= 20`

- `1 <= k <= n`

### Approach and complexity

We design a function $\textit{dfs}(i)$, which represents starting the search from number $i$, with the current search path as $t$, and the answer as $\textit{ans}$.

The execution logic of the function $\textit{dfs}(i)$ is as follows:

- If the length of the current search path $t$ equals $k$, then add the current search path to the answer and return.
- If $i \gt n$, it means the search has ended, return.
- Otherwise, we can choose to add the number $i$ to the search path $t$, and then continue the search, i.e., execute $\textit{dfs}(i + 1)$, and then remove the number $i$ from the search path $t$; or we do not add the number $i$ to the search path $t$, and directly execute $\textit{dfs}(i + 1)$.

The above method is actually enumerating whether to select the current number or not, and then recursively searching the next number. We can also enumerate the next number $j$ to be selected, where $i \leq j \leq n$. If the next number to be selected is $j$, then we add the number $j$ to the search path $t$, and then continue the search, i.e., execute $\textit{dfs}(j + 1)$, and then remove the number $j$ from the search path $t$.

In the main function, we start the search from number $1$, i.e., execute $\textit{dfs}(1)$.

The time complexity is $O(k \times C_n^k)$, and the space complexity is $O(k)$, where $C_n^k$ represents the combination number.

Similar problems:

- [39. Combination Sum](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0039.Combination%20Sum/README_EN.md)
- [40. Combination Sum II](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0040.Combination%20Sum%20II/README_EN.md)
- [216. Combination Sum III](https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0216.Combination%20Sum%20III/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int)> dfs = [&](int i) {
            if (t.size() == k) {
                ans.emplace_back(t);
                return;
            }
            if (i > n) {
                return;
            }
            t.emplace_back(i);
            dfs(i + 1);
            t.pop_back();
            dfs(i + 1);
        };
        dfs(1);
        return ans;
    }
};
```

---

<a id="lc-22"></a>
## 5. LC 22 — Generate Parentheses (Medium)

[Official problem](https://leetcode.com/problems/generate-parentheses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0022.Generate%20Parentheses/README_EN.md)

### Problem description

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Constraints

- `1 <= n <= 8`

### Approach and complexity

The range of $n$ in the problem is $[1, 8]$, so we can directly solve this problem through "brute force search + pruning".

We design a function $\textit{dfs}(l, r, t)$, where $l$ and $r$ represent the number of left and right brackets respectively, and $t$ represents the current bracket sequence. Then we can get the following recursive structure:

- If $l \gt n$ or $r \gt n$ or $l \lt r$, then the current bracket combination $t$ is invalid, return directly;
- If $l = n$ and $r = n$, then the current bracket combination $t$ is valid, add it to the answer array `ans`, and return directly;
- We can choose to add a left bracket, and recursively execute `dfs(l + 1, r, t + "(")`;
- We can also choose to add a right bracket, and recursively execute `dfs(l, r + 1, t + ")")`.

The time complexity is $O(n 2^{2n})$, and the space complexity is $O(n)$.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        auto dfs = [&](auto&& dfs, int l, int r, string t) -> void {
            if (l > n || r > n || l < r) {
                return;
            }
            if (l == n && r == n) {
                ans.push_back(t);
                return;
            }
            dfs(dfs, l + 1, r, t + "(");
            dfs(dfs, l, r + 1, t + ")");
        };
        dfs(dfs, 0, 0, "");
        return ans;
    }
};
```

---

<a id="lc-79"></a>
## 6. LC 79 — Word Search (Medium)

[Official problem](https://leetcode.com/problems/word-search) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0079.Word%20Search/README_EN.md)

### Problem description

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Constraints

- `m == board.length`

- `n = board[i].length`

- `1 <= m, n <= 6`

- `1 <= word.length <= 15`

- `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

### Approach and complexity

We can enumerate each position $(i, j)$ in the grid as the starting point of the search, and then start a depth-first search from the starting point. If we can search to the end of the word, it means the word exists, otherwise, it means the word does not exist.

Therefore, we design a function $\textit{dfs}(i, j, k)$, which represents whether we can successfully search from the $(i, j)$ position of the grid, starting from the $k$th character of the word. The execution steps of the function $\textit{dfs}(i, j, k)$ are as follows:

- If $k = |\textit{word}|-1$, it means that we have searched to the last character of the word. At this time, we only need to judge whether the character at the $(i, j)$ position of the grid is equal to $\textit{word}[k]$. If they are equal, it means the word exists, otherwise, it means the word does not exist. Whether the word exists or not, there is no need to continue to search, so return the result directly.
- Otherwise, if the $\textit{word}[k]$ character is not equal to the character at the $(i, j)$ position of the grid, it means that the search failed this time, so return `false` directly.
- Otherwise, we temporarily store the character at the $(i, j)$ position of the grid in $c$, and then modify the character at this position to a special character `'0'`, indicating that the character at this position has been used to prevent it from being reused in subsequent searches. Then we start from the up, down, left, and right directions of the $(i, j)$ position to search for the $k+1$th character in the grid. If any direction is successful, it means the search is successful, otherwise, it means the search failed. At this time, we need to restore the character at the $(i, j)$ position of the grid, that is, put $c$ back to the $(i, j)$ position (backtracking).

In the main function, we enumerate each position $(i, j)$ in the grid as the starting point. If calling $\textit{dfs}(i, j, 0)$ returns `true`, it means the word exists, otherwise, it means the word does not exist, so return `false`.

The time complexity is $O(mn 3^k)$, and the space complexity is $O(\min(mn, k))$, where $m$ and $n$ are the number of rows and columns of the grid, respectively; and $k$ is the length of the string $\textit{word}$.

### C++20 solution

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        int dirs[5] = {-1, 0, 1, 0, -1};
        function<bool(int, int, int)> dfs = [&](int i, int j, int k) -> bool {
            if (k == word.size() - 1) {
                return board[i][j] == word[k];
            }
            if (board[i][j] != word[k]) {
                return false;
            }
            char c = board[i][j];
            board[i][j] = '0';
            for (int u = 0; u < 4; ++u) {
                int x = i + dirs[u], y = j + dirs[u + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] != '0' && dfs(x, y, k + 1)) {
                    return true;
                }
            }
            board[i][j] = c;
            return false;
        };
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dfs(i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

---

<a id="lc-51"></a>
## 7. LC 51 — N-Queens (Hard)

[Official problem](https://leetcode.com/problems/n-queens) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0051.N-Queens/README_EN.md)

### Problem description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the **n-queens puzzle**. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

### Constraints

- `1 <= n <= 9`

### Approach and complexity

We define three arrays $\textit{col}$, $dg$, and $\textit{udg}$ to represent whether there is a queen in the column, the main diagonal, and the anti-diagonal, respectively. If there is a queen at position $(i, j)$, then $\textit{col}[j]$, $dg[i + j]$, and $\textit{udg}[n - i + j]$ are all $1$. In addition, we use an array $g$ to record the current state of the chessboard, where all elements in $g$ are initially `'.'`.

Next, we define a function $\textit{dfs}(i)$, which represents placing queens starting from the $i$th row.

In $\textit{dfs}(i)$, if $i = n$, it means that we have completed the placement of all queens. We put the current $g$ into the answer array and end the recursion.

Otherwise, we enumerate each column $j$ of the current row. If there is no queen at position $(i, j)$, that is, $\textit{col}[j]$, $dg[i + j]$, and $\textit{udg}[n - i + j]$ are all $0$, then we can place a queen, that is, change $g[i][j]$ to `'Q'`, and set $\textit{col}[j]$, $dg[i + j]$, and $\textit{udg}[n - i + j]$ to $1$. Then we continue to search the next row, that is, call $\textit{dfs}(i + 1)$. After the recursion ends, we need to change $g[i][j]$ back to `'.'` and set $\textit{col}[j]$, $dg[i + j]$, and $\textit{udg}[n - i + j]$ to $0$.

In the main function, we call $\textit{dfs}(0)$ to start recursion, and finally return the answer array.

The time complexity is $O(n^2n!)$, and the space complexity is $O(n)$, where $n$ is the integer given in the problem.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> col(n);
        vector<int> dg(n << 1);
        vector<int> udg(n << 1);
        vector<vector<string>> ans;
        vector<string> t(n, string(n, '.'));
        function<void(int)> dfs = [&](int i) -> void {
            if (i == n) {
                ans.push_back(t);
                return;
            }
            for (int j = 0; j < n; ++j) {
                if (col[j] + dg[i + j] + udg[n - i + j] == 0) {
                    t[i][j] = 'Q';
                    col[j] = dg[i + j] = udg[n - i + j] = 1;
                    dfs(i + 1);
                    col[j] = dg[i + j] = udg[n - i + j] = 0;
                    t[i][j] = '.';
                }
            }
        };
        dfs(0);
        return ans;
    }
};
```

---

<a id="lc-37"></a>
## 8. LC 37 — Sudoku Solver (Hard)

[Official problem](https://leetcode.com/problems/sudoku-solver) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0037.Sudoku%20Solver/README_EN.md)

### Problem description

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

- Each of the digits `1-9` must occur exactly once in each row.

- Each of the digits `1-9` must occur exactly once in each column.

- Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

### Constraints

- `board.length == 9`

- `board[i].length == 9`

- `board[i][j]` is a digit or `'.'`.

- It is **guaranteed** that the input board has only one solution.

### Approach and complexity

Backtracking records used digits for each row, column, and box. Try only legal digits for an empty cell and undo occupancy on failure; a completed board satisfies every constraint.

With E empty cells, O(9^E) worst-case search; auxiliary space O(E+81).

### C++20 solution

```cpp
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        bool row[9][9] = {false};
        bool col[9][9] = {false};
        bool block[3][3][9] = {false};
        bool ok = false;
        vector<pair<int, int>> t;
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') {
                    t.push_back({i, j});
                } else {
                    int v = board[i][j] - '1';
                    row[i][v] = col[j][v] = block[i / 3][j / 3][v] = true;
                }
            }
        }
        auto dfs = [&](auto&& dfs, int k) -> void {
            if (k == t.size()) {
                ok = true;
                return;
            }
            int i = t[k].first, j = t[k].second;
            for (int v = 0; v < 9; ++v) {
                if (!row[i][v] && !col[j][v] && !block[i / 3][j / 3][v]) {
                    row[i][v] = col[j][v] = block[i / 3][j / 3][v] = true;
                    board[i][j] = v + '1';
                    dfs(dfs, k + 1);
                    row[i][v] = col[j][v] = block[i / 3][j / 3][v] = false;
                }
                if (ok) {
                    return;
                }
            }
        };
        dfs(dfs, 0);
    }
};
```

---

<a id="lc-90"></a>
## 9. LC 90 — Subsets II (Medium)

[Official problem](https://leetcode.com/problems/subsets-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0090.Subsets%20II/README_EN.md)

### Problem description

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Constraints

- `1 <= nums.length <= 10`

- `-10 <= nums[i] <= 10`

### Approach and complexity

We can first sort the array $\textit{nums}$ to facilitate deduplication.

Then, we design a function $\textit{dfs}(i)$, which represents the current search for subsets starting from the $i$-th element. The execution logic of the function $\textit{dfs}(i)$ is as follows:

If $i \geq n$, it means all elements have been searched, add the current subset to the answer array, and end the recursion.

If $i < n$, add the $i$-th element to the subset, execute $\textit{dfs}(i + 1)$, then remove the $i$-th element from the subset. Next, we check if the $i$-th element is the same as the next element. If they are the same, skip the element in a loop until we find the first element different from the $i$-th element, then execute $\textit{dfs}(i + 1)$.

Finally, we only need to call $\textit{dfs}(0)$ and return the answer array.

The time complexity is $O(n 2^n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        ranges::sort(nums);
        vector<vector<int>> ans;
        vector<int> t;
        int n = nums.size();
        auto dfs = [&](auto&& dfs, int i) {
            if (i >= n) {
                ans.push_back(t);
                return;
            }
            t.push_back(nums[i]);
            dfs(dfs, i + 1);
            t.pop_back();
            while (i + 1 < n && nums[i + 1] == nums[i]) {
                ++i;
            }
            dfs(dfs, i + 1);
        };
        dfs(dfs, 0);
        return ans;
    }
};
```

---

<a id="lc-47"></a>
## 10. LC 47 — Permutations II (Medium)

[Official problem](https://leetcode.com/problems/permutations-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0047.Permutations%20II/README_EN.md)

### Problem description

Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations **in any order**.

### Constraints

- `1 <= nums.length <= 8`

- `-10 <= nums[i] <= 10`

### Approach and complexity

We can first sort the array so that duplicate numbers are placed together, making it easier to remove duplicates.

Then, we design a function $\textit{dfs}(i)$, which represents the current number to be placed at the $i$-th position. The specific implementation of the function is as follows:

- If $i = n$, it means we have filled all positions, add the current permutation to the answer array, and then return.
- Otherwise, we enumerate the number $\textit{nums}[j]$ for the $i$-th position, where the range of $j$ is $[0, n - 1]$. We need to ensure that $\textit{nums}[j]$ has not been used and is different from the previously enumerated number to ensure that the current permutation is not duplicated. If the conditions are met, we can place $\textit{nums}[j]$ and continue to recursively fill the next position by calling $\textit{dfs}(i + 1)$. After the recursive call ends, we need to mark $\textit{nums}[j]$ as unused to facilitate subsequent enumeration.

In the main function, we first sort the array, then call $\textit{dfs}(0)$ to start filling from the 0th position, and finally return the answer array.

The time complexity is $O(nn!)$, and the space complexity is $O(n)$, where $n$ is the length of the array. We need to perform $n!$ enumerations, and each enumeration requires $O(n)$ time to check for duplicates. Additionally, we need a marker array to mark whether each position has been used, so the space complexity is $O(n)$.

Similar problems:

- [46. Permutations](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0046.Permutations/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        ranges::sort(nums);
        int n = nums.size();
        vector<vector<int>> ans;
        vector<int> t(n);
        vector<bool> vis(n);
        auto dfs = [&](auto&& dfs, int i) {
            if (i == n) {
                ans.emplace_back(t);
                return;
            }
            for (int j = 0; j < n; ++j) {
                if (vis[j] || (j && nums[j] == nums[j - 1] && !vis[j - 1])) {
                    continue;
                }
                t[i] = nums[j];
                vis[j] = true;
                dfs(dfs, i + 1);
                vis[j] = false;
            }
        };
        dfs(dfs, 0);
        return ans;
    }
};
```

---

<a id="lc-40"></a>
## 11. LC 40 — Combination Sum II (Medium)

[Official problem](https://leetcode.com/problems/combination-sum-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0040.Combination%20Sum%20II/README_EN.md)

### Problem description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

### Constraints

- `1 <= candidates.length <= 100`

- `1 <= candidates[i] <= 50`

- `1 <= target <= 30`

### Approach and complexity

We can first sort the array to facilitate pruning and skipping duplicate numbers.

Next, we design a function $\textit{dfs}(i, s)$, which means starting the search from index $i$ with a remaining target value of $s$. Here, $i$ and $s$ are both non-negative integers, the current search path is $t$, and the answer is $\textit{ans}$.

In the function $\textit{dfs}(i, s)$, we first check whether $s$ is $0$. If it is, we add the current search path $t$ to the answer $\textit{ans}$, and then return. If $i \geq n$ or $s \lt \textit{candidates}[i]$, the path is invalid, so we return directly. Otherwise, we start the search from index $i$, and the search index range is $j \in [i, n)$, where $n$ is the length of the array $\textit{candidates}$. During the search, if $j \gt i$ and $\textit{candidates}[j] = \textit{candidates}[j - 1]$, it means that the current number is the same as the previous number, we can skip the current number because the previous number has been searched. Otherwise, we add the current number to the search path $t$, recursively call the function $\textit{dfs}(j + 1, s - \textit{candidates}[j])$, and after the recursion ends, we remove the current number from the search path $t$.

We can also change the implementation logic of the function $\textit{dfs}(i, s)$ to another form. If we choose the current number, we add the current number to the search path $t$, then recursively call the function $\textit{dfs}(i + 1, s - \textit{candidates}[i])$, and after the recursion ends, we remove the current number from the search path $t$. If we do not choose the current number, we can skip all numbers that are the same as the current number, then recursively call the function $\textit{dfs}(j, s)$, where $j$ is the index of the first number that is different from the current number.

In the main function, we just need to call the function $\textit{dfs}(0, \textit{target})$ to get the answer.

The time complexity is $O(2^n n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{candidates}$. Due to pruning, the actual time complexity is much less than $O(2^n n)$.

Similar problems:

- [39. Combination Sum](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0039.Combination%20Sum/README_EN.md)
- [77. Combinations](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0077.Combinations/README_EN.md)
- [216. Combination Sum III](https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0216.Combination%20Sum%20III/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        ranges::sort(candidates);
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int, int)> dfs = [&](int i, int s) {
            if (s == 0) {
                ans.emplace_back(t);
                return;
            }
            if (i >= candidates.size() || s < candidates[i]) {
                return;
            }
            for (int j = i; j < candidates.size(); ++j) {
                if (j > i && candidates[j] == candidates[j - 1]) {
                    continue;
                }
                t.emplace_back(candidates[j]);
                dfs(j + 1, s - candidates[j]);
                t.pop_back();
            }
        };
        dfs(0, target);
        return ans;
    }
};
```

---

<a id="lc-216"></a>
## 12. LC 216 — Combination Sum III (Medium)

[Official problem](https://leetcode.com/problems/combination-sum-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0216.Combination%20Sum%20III/README_EN.md)

### Problem description

Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

- Only numbers `1` through `9` are used.

- Each number is used **at most once**.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

### Constraints

- `2 <= k <= 9`

- `1 <= n <= 60`

### Approach and complexity

Choose increasing distinct digits from 1 through 9, pruning when the remaining sum or selected count cannot succeed. Increasing order prevents duplicate combinations.

The digit domain is fixed; a conservative time bound O(2^9·9) and auxiliary space O(9), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int, int)> dfs = [&](int i, int s) {
            if (s == 0) {
                if (t.size() == k) {
                    ans.emplace_back(t);
                }
                return;
            }
            if (i > 9 || i > s || t.size() >= k) {
                return;
            }
            t.emplace_back(i);
            dfs(i + 1, s - i);
            t.pop_back();
            dfs(i + 1, s);
        };
        dfs(1, n);
        return ans;
    }
};
```

---

<a id="lc-17"></a>
## 13. LC 17 — Letter Combinations of a Phone Number (Medium)

[Official problem](https://leetcode.com/problems/letter-combinations-of-a-phone-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0017.Letter%20Combinations%20of%20a%20Phone%20Number/README_EN.md)

### Problem description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![Problem illustration](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0017.Letter%20Combinations%20of%20a%20Phone%20Number/images/1200px-telephone-keypad2svg.png)

### Constraints

- `1 <= digits.length <= 4`

- `digits[i]` is a digit in the range `['2', '9']`.

### Approach and complexity

We can use the method of depth-first search to enumerate all possible letter combinations. Suppose that a part of the letter combination has been generated, but some digits have not been exhausted. At this time, we take out the letters corresponding to the next digit, and then enumerate each letter corresponding to this digit one by one, add them to the letter combination that has been generated before, to form all possible combinations.

The time complexity is $O(4^n)$, and the space complexity is $O(n)$, where $n$ is the length of the input digits.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        vector<string> d = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> ans;
        string t;
        function<void(int)> dfs = [&](int i) {
            if (i >= digits.size()) {
                ans.push_back(t);
                return;
            }
            for (auto& c : d[digits[i] - '2']) {
                t.push_back(c);
                dfs(i + 1);
                t.pop_back();
            }
        };
        dfs(0);
        return ans;
    }
};
```

---

<a id="lc-131"></a>
## 14. LC 131 — Palindrome Partitioning (Medium)

[Official problem](https://leetcode.com/problems/palindrome-partitioning) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0131.Palindrome%20Partitioning/README_EN.md)

### Problem description

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

### Constraints

- `1 <= s.length <= 16`

- `s` contains only lowercase English letters.

### Approach and complexity

We can use dynamic programming to preprocess whether any substring in the string is a palindrome, i.e., $f[i][j]$ indicates whether the substring $s[i..j]$ is a palindrome.

Next, we design a function $\textit{dfs}(i)$, which represents starting from the $i$-th character of the string and partitioning it into several palindromic substrings, with the current partition scheme being $t$.

If $i = |s|$, it means the partitioning is complete, and we add $t$ to the answer array and then return.

Otherwise, we can start from $i$ and enumerate the end position $j$ from small to large. If $s[i..j]$ is a palindrome, we add $s[i..j]$ to $t$, then continue to recursively call $\textit{dfs}(j+1)$. When backtracking, we need to pop $s[i..j]$.

The time complexity is $O(n 2^n)$, and the space complexity is $O(n^2)$, where $n$ is the length of the string.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = s.size();
        vector<vector<char>> f = vector<vector<char>>(n, vector<char>(n, 1));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i + 1; j < n; ++j) {
                f[i][j] = s[i] == s[j] && f[i + 1][j - 1];
            }
        }
        vector<vector<string>> ans;
        vector<string> t;
        auto dfs = [&](auto&& dfs, int i) -> void {
            if (i == n) {
                ans.emplace_back(t);
                return;
            }
            for (int j = i; j < n; ++j) {
                if (f[i][j]) {
                    t.emplace_back(s.substr(i, j - i + 1));
                    dfs(dfs, j + 1);
                    t.pop_back();
                }
            }
        };
        dfs(dfs, 0);
        return ans;
    }
};
```

---

<a id="lc-93"></a>
## 15. LC 93 — Restore IP Addresses (Medium)

[Official problem](https://leetcode.com/problems/restore-ip-addresses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0093.Restore%20IP%20Addresses/README_EN.md)

### Problem description

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

- For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return all possible valid IP addresses that can be formed by inserting dots into `s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

### Constraints

- `1 <= s.length <= 20`

- `s` consists of digits only.

### Approach and complexity

We define a function $\textit{dfs}(i)$, which represents the list of IP addresses that can be formed starting from the $i$th position of string $s$.

The execution steps of function $\textit{dfs}(i)$ are as follows:

If $i$ is greater than or equal to the length of string $s$, it means that we have completed the splicing of four segments of the IP address. At this point, we need to check whether it meets the requirements of the four segments of the IP address. If it does, add the current $\textit{IP}$ to the answer.

If $i$ is less than the length of string $s$, it means that we still need to splice a segment of the IP address. At this point, we need to determine the value of this segment of the IP address. If the value is greater than $255$, or the current position $i$ is $0$ and the value of several positions after $i$ is greater than $0$, it means that it does not meet the requirements, so we return directly. Otherwise, add it to the IP address list, and continue to search for the next segment of the IP address.

The time complexity is $O(3^4 n)$, and the space complexity is $O(n)$, where $n$ is the length of string $s$.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        int n = s.size();
        vector<string> ans;
        vector<string> t;
        function<void(int)> dfs = [&](int i) {
            if (i >= n && t.size() == 4) {
                ans.push_back(t[0] + "." + t[1] + "." + t[2] + "." + t[3]);
                return;
            }
            if (i >= n || t.size() >= 4) {
                return;
            }
            int x = 0;
            for (int j = i; j < min(n, i + 3); ++j) {
                x = x * 10 + s[j] - '0';
                if (x > 255 || (j > i && s[i] == '0')) {
                    break;
                }
                t.push_back(s.substr(i, j - i + 1));
                dfs(j + 1);
                t.pop_back();
            }
        };
        dfs(0);
        return ans;
    }
};
```

---

<a id="lc-784"></a>
## 16. LC 784 — Letter Case Permutation (Medium)

[Official problem](https://leetcode.com/problems/letter-case-permutation) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0784.Letter%20Case%20Permutation/README_EN.md)

### Problem description

Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in **any order**.

### Constraints

- `1 <= s.length <= 12`

- `s` consists of lowercase English letters, uppercase English letters, and digits.

### Approach and complexity

Since each letter in $s$ can be converted to uppercase or lowercase, we can use the DFS (Depth-First Search) method to enumerate all possible cases.

Specifically, traverse the string $s$ from left to right. For each letter encountered, you can choose to convert it to uppercase or lowercase, and then continue to traverse the subsequent letters. When you reach the end of the string, you get a conversion scheme and add it to the answer.

The method of converting case can be implemented using bitwise operations. For a letter, the difference between the ASCII codes of its lowercase and uppercase forms is $32$, so we can achieve case conversion by XORing the ASCII code of the letter with $32$.

The time complexity is $O(n 2^n)$, where $n$ is the length of the string $s$. For each letter, we can choose to convert it to uppercase or lowercase, so there are $2^n$ conversion schemes in total. For each conversion scheme, we need $O(n)$ time to generate a new string.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> letterCasePermutation(string s) {
        string t = s;
        vector<string> ans;
        auto dfs = [&](auto&& dfs, int i) -> void {
            if (i >= t.size()) {
                ans.push_back(t);
                return;
            }
            dfs(dfs, i + 1);
            if (isalpha(t[i])) {
                t[i] ^= 32;
                dfs(dfs, i + 1);
            }
        };
        dfs(dfs, 0);
        return ans;
    }
};
```

---

<a id="lc-698"></a>
## 17. LC 698 — Partition to K Equal Sum Subsets (Medium)

[Official problem](https://leetcode.com/problems/partition-to-k-equal-sum-subsets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0698.Partition%20to%20K%20Equal%20Sum%20Subsets/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `k`, return `true` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.

### Constraints

- `1 <= k <= nums.length <= 16`

- `1 <= nums[i] <= 10^4`

- The frequency of each element is in the range `[1, 4]`.

### Approach and complexity

We can use dynamic programming to solve this problem.

We define $f[i]$ to represent whether there exists $k$ subsets that meet the requirements when the current selected numbers' state is $i$. Initially, $f[0] = \textit{true}$, and the answer is $f[2^n - 1]$, where $n$ is the length of the array $\textit{nums}$. Additionally, we define $\textit{cur}[i]$ to represent the sum of the last subset when the current selected numbers' state is $i$.

We enumerate the states $i$ in the range $[0, 2^n]$. For each state $i$, if $f[i]$ is $\textit{false}$, we skip it. Otherwise, we enumerate any number $\textit{nums}[j]$ in the array $\textit{nums}$. If $\textit{cur}[i] + \textit{nums}[j] > s$, we break the enumeration loop because the subsequent numbers are larger and cannot be placed in the current subset. Otherwise, if the $j$-th bit of the binary representation of $i$ is $0$, it means the current $\textit{nums}[j]$ has not been selected. We can place it in the current subset, change the state to $i | 2^j$, update $\textit{cur}[i | 2^j] = (\textit{cur}[i] + \textit{nums}[j]) \bmod s$, and set $f[i | 2^j] = \textit{true}$.

Finally, we return $f[2^n - 1]$.

The time complexity is $O(n 2^n)$, and the space complexity is $O(2^n)$, where $n$ represents the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        if (s % k) {
            return false;
        }
        s /= k;
        ranges::sort(nums);
        int n = nums.size();
        vector<char> f = vector<char>(1 << n, 0);
        vector<int> cur = vector<int>(1 << n, 0);
        f[0] = 1;
        for (int i = 0; i < 1 << n; ++i) {
            if (!f[i]) {
                continue;
            }
            for (int j = 0; j < n; ++j) {
                if (cur[i] + nums[j] > s) {
                    break;
                }
                if ((i >> j & 1) == 0) {
                    f[i | 1 << j] = true;
                    cur[i | 1 << j] = (cur[i] + nums[j]) % s;
                }
            }
        }
        return f[(1 << n) - 1];
    }
};
```

---

<a id="lc-473"></a>
## 18. LC 473 — Matchsticks to Square (Medium)

[Official problem](https://leetcode.com/problems/matchsticks-to-square) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0473.Matchsticks%20to%20Square/README_EN.md)

### Problem description

You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the `i^th` matchstick. You want to use **all the matchsticks** to make one square. You **should not break** any stick, but you can link them up, and each matchstick must be used **exactly one time**.

Return `true` if you can make this square and `false` otherwise.

### Constraints

- `1 <= matchsticks.length <= 15`

- `1 <= matchsticks[i] <= 10^8`

### Approach and complexity

Sort sticks descending and backtrack over four side totals, accepting only totals no larger than the target side length. Skip symmetric choices with identical current totals.

Conservative time O(4^n+n log n); auxiliary space O(n), including recursion and sorting.

### C++20 solution

```cpp
class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int s = 0, mx = 0;
        for (int& v : matchsticks) {
            s += v;
            mx = max(mx, v);
        }
        int x = s / 4, mod = s % 4;
        if (mod != 0 || x < mx) return false;
        ranges::sort(matchsticks, greater<int>());
        vector<int> edges(4);
        return dfs(0, x, matchsticks, edges);
    }

    bool dfs(int u, int x, vector<int>& matchsticks, vector<int>& edges) {
        if (u == matchsticks.size()) return true;
        for (int i = 0; i < 4; ++i) {
            if (i > 0 && edges[i - 1] == edges[i]) continue;
            edges[i] += matchsticks[u];
            if (edges[i] <= x && dfs(u + 1, x, matchsticks, edges)) return true;
            edges[i] -= matchsticks[u];
        }
        return false;
    }
};
```

---

<a id="lc-526"></a>
## 19. LC 526 — Beautiful Arrangement (Medium)

[Official problem](https://leetcode.com/problems/beautiful-arrangement) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0526.Beautiful%20Arrangement/README_EN.md)

### Problem description

Suppose you have `n` integers labeled `1` through `n`. A permutation of those `n` integers `perm` (**1-indexed**) is considered a **beautiful arrangement** if for every `i` (`1 <= i <= n`), **either** of the following is true:

- `perm[i]` is divisible by `i`.

- `i` is divisible by `perm[i]`.

Given an integer `n`, return the **number** of the **beautiful arrangements** that you can construct.

### Constraints

- `1 <= n <= 15`

### Approach and complexity

A mask describes numbers already assigned. Its popcount determines the next position. Add every unused number satisfying the divisibility condition and accumulate ways into the new mask. Each assignment order corresponds to exactly one arrangement.

Time O(n·2^n); auxiliary space O(2^n), n≤15.

### C++20 solution

```cpp
class Solution {
public:
    int countArrangement(int n) {
        vector<int> dp(1 << n);
        dp[0] = 1;
        for (unsigned mask = 0; mask < dp.size(); ++mask) {
            int position = popcount(mask) + 1;
            for (int value = 1; value <= n; ++value)
                if (!(mask & (1U << (value - 1))) && (value % position == 0 || position % value == 0))
                    dp[mask | (1U << (value - 1))] += dp[mask];
        }
        return dp.back();
    }
};
```

---

<a id="lc-1079"></a>
## 20. LC 1079 — Letter Tile Possibilities (Medium)

[Official problem](https://leetcode.com/problems/letter-tile-possibilities) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1079.Letter%20Tile%20Possibilities/README_EN.md)

### Problem description

You have `n` `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those `tiles`.

### Constraints

- `1 <= tiles.length <= 7`

- `tiles` consists of uppercase English letters.

### Approach and complexity

Count remaining occurrences of each letter. At each recursion choose any letter with positive count, count the new nonempty sequence, decrement, recurse, and restore. Counts avoid permuting indistinguishable copies.

Time O(A·R), with R distinct possible nonempty sequences and A≤26; auxiliary space O(n+A), excluding enumeration output because only a count is returned.

### C++20 solution

```cpp
class Solution {
public:
    int numTilePossibilities(string tiles) {
        int cnt[26]{};
        for (char c : tiles) {
            ++cnt[c - 'A'];
        }
        function<int(int* cnt)> dfs = [&](int* cnt) -> int {
            int res = 0;
            for (int i = 0; i < 26; ++i) {
                if (cnt[i] > 0) {
                    ++res;
                    --cnt[i];
                    res += dfs(cnt);
                    ++cnt[i];
                }
            }
            return res;
        };
        return dfs(cnt);
    }
};
```

---

<a id="lc-1239"></a>
## 21. LC 1239 — Maximum Length of a Concatenated String with Unique Characters (Medium)

[Official problem](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1239.Maximum%20Length%20of%20a%20Concatenated%20String%20with%20Unique%20Characters/README_EN.md)

### Problem description

You are given an array of strings `arr`. A string `s` is formed by the **concatenation** of a **subsequence** of `arr` that has **unique characters**.

Return the **maximum** possible length of `s`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

### Constraints

- `1 <= arr.length <= 16`

- `1 <= arr[i].length <= 26`

- `arr[i]` contains only lowercase English letters.

### Approach and complexity

Since the problem requires that the characters in the subsequence must not be repeated and all characters are lowercase letters, we can use a binary integer of length $26$ to represent a subsequence. The $i$-th bit being $1$ indicates that the subsequence contains the $i$-th character, and $0$ indicates that it does not contain the $i$-th character.

We can use an array $s$ to store the states of all subsequences that meet the conditions. Initially, $s$ contains only one element $0$.

Then we traverse the array $\textit{arr}$. For each string $t$, we use an integer $x$ to represent the state of $t$. Then we traverse the array $s$. For each state $y$, if $x$ and $y$ have no common characters, we add the union of $x$ and $y$ to $s$ and update the answer.

Finally, we return the answer.

The time complexity is $O(2^n + L)$, and the space complexity is $O(2^n)$, where $n$ is the length of the string array, and $L$ is the sum of the lengths of all strings in the array.

### C++20 solution

```cpp
class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<int> s = {0};
        int ans = 0;
        for (const string& t : arr) {
            int x = 0;
            for (char c : t) {
                int b = c - 'a';
                if ((x >> b & 1) == 1) {
                    x = 0;
                    break;
                }
                x |= 1 << b;
            }
            if (x > 0) {
                for (int i = s.size() - 1; i >= 0; --i) {
                    int y = s[i];
                    if ((x & y) == 0) {
                        s.push_back(x | y);
                        ans = max(ans, popcount(static_cast<unsigned int>(x | y)));
                    }
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1415"></a>
## 22. LC 1415 — The k-th Lexicographical String of All Happy Strings of Length n (Medium)

[Official problem](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1400-1499/1415.The%20k-th%20Lexicographical%20String%20of%20All%20Happy%20Strings%20of%20Length%20n/README_EN.md)

### Problem description

A **happy string** is a string that:

- consists only of letters of the set `['a', 'b', 'c']`.

- `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).

For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return the kth string of this list or return an **empty string** if there are less than `k` happy strings of length `n`.

### Constraints

- `1 <= n <= 10`

- `1 <= k <= 100`

### Approach and complexity

We can directly calculate what the $k$-th happy string is, without generating all happy strings.

Starting from the first happy string of length $n$, we can determine what each character position should be.

For a happy string of length $n$, the first character has $3$ choices, the second character has $2$ choices (cannot be the same as the first), the third character also has $2$ choices (cannot be the same as the second), and so on, until the $n$-th character also has $2$ choices (cannot be the same as the $(n-1)$-th). Therefore, the total number of happy strings of length $n$ is $3 \times 2^{n-1}$.

If $k$ is greater than the total number of happy strings of length $n$, we return an empty string directly.

Otherwise, we start from the first character and determine each character's position one by one. For the $i$-th character, we enumerate the character set $\{a, b, c\}$. If the last character of the current string is not equal to $c$, we calculate the number of remaining happy strings. If $k$ is less than or equal to that count, we append character $c$ to the current string and move on to the next position; otherwise, we subtract that count from $k$ and continue enumerating the next character.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string.

### C++20 solution

```cpp
class Solution {
public:
    string getHappyString(int n, int k) {
        if (k > 3 * (1 << (n - 1))) {
            return "";
        }
        string cs = "abc";
        string ans;
        for (int i = 0; i < n; ++i) {
            int remain = 1 << (n - i - 1);
            for (char c : cs) {
                if (!ans.empty() && ans.back() == c) {
                    continue;
                }
                if (k <= remain) {
                    ans.push_back(c);
                    break;
                }
                k -= remain;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1593"></a>
## 23. LC 1593 — Split a String Into the Max Number of Unique Substrings (Medium)

[Official problem](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1500-1599/1593.Split%20a%20String%20Into%20the%20Max%20Number%20of%20Unique%20Substrings/README_EN.md)

### Problem description

Given a string `s`, return the maximum number of unique substrings that the given string can be split into.

You can split string `s` into any list of **non-empty substrings**, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are **unique**.

A **substring** is a contiguous sequence of characters within a string.

### Constraints

- 
`1 <= s.length <= 16`

- 
`s` contains only lower case English letters.

### Approach and complexity

We define a hash table $st$ to store the currently split substrings. Then we use a depth-first search approach to try to split the string $s$ into several unique substrings.

Specifically, we design a function $\textit{dfs}(i)$, which means we are considering splitting $s[i:]$.

In the function $\textit{dfs}(i)$, we first check if the number of substrings already split plus the remaining characters is less than or equal to the current answer. If so, there is no need to continue splitting, and we return directly. If $i \geq n$, it means we have completed the splitting of the entire string, and we update the answer to the maximum of the current number of substrings and the answer. Otherwise, we enumerate the end position $j$ (exclusive) of the current substring and check if $s[i..j)$ has already been split. If not, we add it to the hash table $st$ and continue to recursively consider splitting the remaining part. After the recursive call, we need to remove $s[i..j)$ from the hash table $st$.

Finally, we return the answer.

The time complexity is $O(n^2 2^n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> st;
        int n = s.size();
        int ans = 0;
        auto dfs = [&](auto&& dfs, int i) -> void {
            if (st.size() + n - i <= ans) {
                return;
            }
            if (i >= n) {
                ans = max(ans, (int) st.size());
                return;
            }
            for (int j = i + 1; j <= n; ++j) {
                string t = s.substr(i, j - i);
                if (!st.contains(t)) {
                    st.insert(t);
                    dfs(dfs, j);
                    st.erase(t);
                }
            }
        };
        dfs(dfs, 0);
        return ans;
    }
};
```

---

<a id="lc-1863"></a>
## 24. LC 1863 — Sum of All Subset XOR Totals (Easy)

[Official problem](https://leetcode.com/problems/sum-of-all-subset-xor-totals) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1863.Sum%20of%20All%20Subset%20XOR%20Totals/README_EN.md)

### Problem description

The **XOR total** of an array is defined as the bitwise `XOR` of** all its elements**, or `0` if the array is** empty**.

- For example, the **XOR total** of the array `[2,5,6]` is `2 XOR 5 XOR 6 = 1`.

Given an array `nums`, return the **sum** of all **XOR totals** for every **subset** of `nums`. 

**Note:** Subsets with the **same** elements should be counted **multiple** times.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

### Constraints

- `1 <= nums.length <= 12`

- `1 <= nums[i] <= 20`

### Approach and complexity

For any bit present in at least one element, exactly half of all subsets have that XOR bit set: pairing subsets by toggling one element containing that bit flips its parity. Therefore the answer is OR(nums)·2ⁿ⁻¹.

Time O(n); auxiliary space O(1). The specified n and value bounds keep the result within int.

### C++20 solution

```cpp
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        unsigned bits = 0;
        for (int x : nums) bits |= static_cast<unsigned>(x);
        return static_cast<int>(bits << (nums.size() - 1));
    }
};
```

---

<a id="lc-2044"></a>
## 25. LC 2044 — Count Number of Maximum Bitwise-OR Subsets (Medium)

[Official problem](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2000-2099/2044.Count%20Number%20of%20Maximum%20Bitwise-OR%20Subsets/README_EN.md)

### Problem description

Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a subset of `nums` and return the **number of different non-empty subsets** with the maximum bitwise OR.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`. Two subsets are considered **different** if the indices of the elements chosen are different.

The bitwise OR of an array `a` is equal to `a[0] **OR** a[1] **OR** ... **OR** a[a.length - 1]` (**0-indexed**).

### Constraints

- `1 <= nums.length <= 16`

- `1 <= nums[i] <= 10^5`

### Approach and complexity

The maximum bitwise OR value $mx$ in the array $\textit{nums}$ can be obtained by performing bitwise OR on all elements in the array.

Then we can use depth-first search to enumerate all subsets and count the number of subsets whose bitwise OR equals $mx$. We design a function $\textit{dfs}(i, t)$, which represents the number of subsets starting from index $i$ with the current bitwise OR value being $t$. Initially, $i = 0$ and $t = 0$.

In the function $\textit{dfs}(i, t)$, if $i$ equals the array length, it means we have enumerated all elements. At this point, if $t$ equals $mx$, we increment the answer by one. Otherwise, we can choose to either exclude the current element $\textit{nums}[i]$ or include the current element $\textit{nums}[i]$, so we can recursively call $\textit{dfs}(i + 1, t)$ and $\textit{dfs}(i + 1, t | \textit{nums}[i])$.

Finally, we return the answer.

The time complexity is $O(2^n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int ans = 0;
        int mx = accumulate(nums.begin(), nums.end(), 0, bit_or<int>());
        auto dfs = [&](auto&& dfs, int i, int t) {
            if (i == nums.size()) {
                if (t == mx) {
                    ans++;
                }
                return;
            }
            dfs(dfs, i + 1, t);
            dfs(dfs, i + 1, t | nums[i]);
        };
        dfs(dfs, 0, 0);
        return ans;
    }
};
```

---

<a id="lc-2305"></a>
## 26. LC 2305 — Fair Distribution of Cookies (Medium)

[Official problem](https://leetcode.com/problems/fair-distribution-of-cookies) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2305.Fair%20Distribution%20of%20Cookies/README_EN.md)

### Problem description

You are given an integer array `cookies`, where `cookies[i]` denotes the number of cookies in the `i^th` bag. You are also given an integer `k` that denotes the number of children to distribute **all** the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The **unfairness** of a distribution is defined as the **maximum** **total** cookies obtained by a single child in the distribution.

Return the **minimum** unfairness of all distributions.

### Constraints

- `2 <= cookies.length <= 8`

- `1 <= cookies[i] <= 10^5`

- `2 <= k <= cookies.length`

### Approach and complexity

Assign larger bags first, prune any assignment whose maximum cannot beat the incumbent, and skip symmetric equal child totals.

Conservative time O(k^n·k+n log n); auxiliary space O(n+k).

### C++20 solution

```cpp
class Solution {
public:
    int distributeCookies(vector<int>& cookies, int k) {
        sort(cookies.rbegin(), cookies.rend());
        vector<int> cnt = vector<int>(k, 0);
        int n = cookies.size();
        int ans = 1 << 30;
        function<void(int)> dfs = [&](int i) {
            if (i >= n) {
                ans = *max_element(cnt.begin(), cnt.end());
                return;
            }
            for (int j = 0; j < k; ++j) {
                if (cnt[j] + cookies[i] >= ans || (j && cnt[j] == cnt[j - 1])) {
                    continue;
                }
                cnt[j] += cookies[i];
                dfs(i + 1);
                cnt[j] -= cookies[i];
            }
        };
        dfs(0);
        return ans;
    }
};
```

---

<a id="lc-2597"></a>
## 27. LC 2597 — The Number of Beautiful Subsets (Medium)

[Official problem](https://leetcode.com/problems/the-number-of-beautiful-subsets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2500-2599/2597.The%20Number%20of%20Beautiful%20Subsets/README_EN.md)

### Problem description

You are given an array `nums` of positive integers and a **positive** integer `k`.

A subset of `nums` is **beautiful** if it does not contain two integers with an absolute difference equal to `k`.

Return the number of **non-empty beautiful **subsets of the array `nums`.

A **subset** of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

### Constraints

- `1 <= nums.length <= 18`

- `1 <= nums[i], k <= 1000`

### Approach and complexity

Only values differing by k conflict, so group by residue modulo k and process values ascending within each group. A value appearing c times can be selected in 2^c−1 nonempty ways. Track skip/take counts; a gap larger than k permits either previous state, while a gap exactly k permits taking only after skipping. Multiply independent group totals and remove the empty subset.

Time O(n log n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        map<int, map<int, int>> groups;
        for (int x : nums) ++groups[x % k][x];
        long long result = 1;
        for (const auto& [remainder, counts] : groups) {
            long long skip = 1, take = 0;
            int previous = INT_MIN;
            for (const auto& [value, count] : counts) {
                long long choices = (1LL << count) - 1;
                long long nextTake = choices * (previous != INT_MIN && value - previous == k ? skip : skip + take);
                skip += take; take = nextTake; previous = value;
            }
            result *= skip + take;
        }
        return static_cast<int>(result - 1);
    }
};
```

---

<a id="lc-2698"></a>
## 28. LC 2698 — Find the Punishment Number of an Integer (Medium)

[Official problem](https://leetcode.com/problems/find-the-punishment-number-of-an-integer) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2600-2699/2698.Find%20the%20Punishment%20Number%20of%20an%20Integer/README_EN.md)

### Problem description

Given a positive integer `n`, return the **punishment number** of `n`.

The **punishment number** of `n` is defined as the sum of the squares of all integers `i` such that:

- `1 <= i <= n`

- The decimal representation of `i * i` can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals `i`.

### Constraints

- `1 <= n <= 1000`

### Approach and complexity

We enumerate $i$, where $1 \leq i \leq n$. For each $i$, we split the decimal representation string of $x = i^2$, and then check whether it meets the requirements of the problem. If it does, we add $x$ to the answer.

After the enumeration ends, we return the answer.

The time complexity is $O(n^{1 + 2 \log_{10}^2})$, and the space complexity is $O(\log n)$, where $n$ is the given positive integer.

### C++20 solution

```cpp
class Solution {
public:
    int punishmentNumber(int n) {
        int ans = 0;
        for (int i = 1; i <= n; ++i) {
            int x = i * i;
            string s = to_string(x);
            if (check(s, 0, i)) {
                ans += x;
            }
        }
        return ans;
    }

    bool check(const string& s, int i, int x) {
        int m = s.size();
        if (i >= m) {
            return x == 0;
        }
        int y = 0;
        for (int j = i; j < m; ++j) {
            y = y * 10 + s[j] - '0';
            if (y > x) {
                break;
            }
            if (check(s, j + 1, x - y)) {
                return true;
            }
        }
        return false;
    }
};
```

---

<a id="lc-1980"></a>
## 29. LC 1980 — Find Unique Binary String (Medium)

[Official problem](https://leetcode.com/problems/find-unique-binary-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1900-1999/1980.Find%20Unique%20Binary%20String/README_EN.md)

### Problem description

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return a binary string of length `n` that **does not appear** in `nums`. If there are multiple answers, you may return **any** of them.

### Constraints

- `n == nums.length`

- `1 <= n <= 16`

- `nums[i].length == n`

- `nums[i] `is either `'0'` or `'1'`.

- All the strings of `nums` are **unique**.

### Approach and complexity

We can construct a binary string $\textit{ans}$ of length $n$, where the $i$-th bit of $\textit{ans}$ differs from the $i$-th bit of $\textit{nums}[i]$. Since all strings in $\textit{nums}$ are distinct, $\textit{ans}$ will not appear in $\textit{nums}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the strings in $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();
        string ans(n, '0');
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i][i] == '0' ? '1' : '0';
        }
        return ans;
    }
};
```

---

<a id="lc-282"></a>
## 30. LC 282 — Expression Add Operators (Hard)

[Official problem](https://leetcode.com/problems/expression-add-operators) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0282.Expression%20Add%20Operators/README_EN.md)

### Problem description

Given a string `num` that contains only digits and an integer `target`, return **all possibilities** to insert the binary operators `'+'`, `'-'`, and/or `'*'` between the digits of `num` so that the resultant expression evaluates to the `target` value.

Note that operands in the returned expressions **should not** contain leading zeros.

**Note** that a number can contain multiple digits.

### Constraints

- `1 <= num.length <= 10`

- `num` consists of only digits.

- `-2^31 <= target <= 2^31 - 1`

### Approach and complexity

Enumerate each next numeric token and operator. Track the current value and the last signed term. For multiplication, replace that last term with its product, thereby implementing precedence without reparsing. Reject multi-digit tokens with a leading zero; use 64-bit arithmetic.

Time O(n·4ⁿ) as a conservative bound including output construction; auxiliary space O(n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> result;
        string expression;
        int n = num.size();
        auto dfs = [&](auto&& self, int pos, long long value, long long last) -> void {
            if (pos == n) {
                if (value == target) result.push_back(expression);
                return;
            }
            long long x = 0;
            auto oldSize = expression.size();
            for (int end = pos; end < n; ++end) {
                if (end > pos && num[pos] == '0') break;
                x = 10 * x + num[end] - '0';
                string token = num.substr(pos, end - pos + 1);
                if (pos == 0) {
                    expression += token;
                    self(self, end + 1, x, x);
                    expression.resize(oldSize);
                } else {
                    for (char op : string_view("+-*")) {
                        expression += op;
                        expression += token;
                        if (op == '+') self(self, end + 1, value + x, x);
                        if (op == '-') self(self, end + 1, value - x, -x);
                        if (op == '*') self(self, end + 1, value - last + last * x, last * x);
                        expression.resize(oldSize);
                    }
                }
            }
        };
        dfs(dfs, 0, 0, 0);
        return result;
    }
};
```

---

<a id="lc-301"></a>
## 31. LC 301 — Remove Invalid Parentheses (Hard)

[Official problem](https://leetcode.com/problems/remove-invalid-parentheses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0301.Remove%20Invalid%20Parentheses/README_EN.md)

### Problem description

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of **unique strings** that are valid with the minimum number of removals. You may return the answer in **any order**.

### Constraints

- `1 <= s.length <= 25`

- `s` consists of lowercase English letters and parentheses `'('` and `')'`.

- There will be at most `20` parentheses in `s`.

### Approach and complexity

Count the minimum unmatched left/right parentheses to delete. Backtrack over removals, preserving other characters, and accept only balanced strings after using exactly the required deletions. Deduplicate equivalent results.

Conservative time O(n·2^n), auxiliary space O(n) plus deduplication storage proportional to retained result characters.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        unordered_set<string> ans;
        int l = 0, r = 0, n = s.size();
        for (char& c : s) {
            if (c == '(') {
                ++l;
            } else if (c == ')') {
                if (l) {
                    --l;
                } else {
                    ++r;
                }
            }
        }
        function<void(int, int, int, int, int, string)> dfs;
        dfs = [&](int i, int l, int r, int lcnt, int rcnt, string t) {
            if (i == n) {
                if (l == 0 && r == 0) {
                    ans.insert(t);
                }
                return;
            }
            if (n - i < l + r || lcnt < rcnt) {
                return;
            }
            if (s[i] == '(' && l) {
                dfs(i + 1, l - 1, r, lcnt, rcnt, t);
            }
            if (s[i] == ')' && r) {
                dfs(i + 1, l, r - 1, lcnt, rcnt, t);
            }
            int x = s[i] == '(' ? 1 : 0;
            int y = s[i] == ')' ? 1 : 0;
            dfs(i + 1, l, r, lcnt + x, rcnt + y, t + s[i]);
        };

        dfs(0, l, r, 0, 0, "");
        return vector<string>(ans.begin(), ans.end());
    }
};
```

---

<a id="lc-140"></a>
## 32. LC 140 — Word Break II (Hard)

[Official problem](https://leetcode.com/problems/word-break-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0140.Word%20Break%20II/README_EN.md)

### Problem description

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in **any order**.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

### Constraints

- `1 <= s.length <= 20`

- `1 <= wordDict.length <= 1000`

- `1 <= wordDict[i].length <= 10`

- `s` and `wordDict[i]` consist of only lowercase English letters.

- All the strings of `wordDict` are **unique**.

- Input is generated in a way that the length of the answer doesn't exceed 10^5.

### Approach and complexity

For each starting position, enumerate dictionary words that match the next substring and append every sentence for the remaining suffix. Cache suffix results so repeated suffixes are solved once. The end position contributes one empty suffix to terminate concatenation.

Let n be the string length and W the number of characters in stored/output sentences. Time O(n³+W·n) is a conservative bound with substring creation and copying; space O(n²+W), including cached sentences and O(n) recursion depth. Output can be exponential.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> words(wordDict.begin(), wordDict.end());
        int n = s.size();
        vector<optional<vector<string>>> memo(n + 1);
        memo[n] = vector<string>{""};
        auto dfs = [&](auto&& self, int start) -> const vector<string>& {
            if (memo[start]) return *memo[start];
            vector<string> result;
            for (int end = start + 1; end <= n; ++end) {
                string word = s.substr(start, end - start);
                if (!words.contains(word)) continue;
                for (const string& tail : self(self, end))
                    result.push_back(word + (tail.empty() ? "" : " " + tail));
            }
            memo[start] = move(result);
            return *memo[start];
        };
        return dfs(dfs, 0);
    }
};
```

---

<a id="lc-212"></a>
## 33. LC 212 — Word Search II (Hard)

[Official problem](https://leetcode.com/problems/word-search-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0212.Word%20Search%20II/README_EN.md)

### Problem description

Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

### Constraints

- `m == board.length`

- `n == board[i].length`

- `1 <= m, n <= 12`

- `board[i][j]` is a lowercase English letter.

- `1 <= words.length <= 3 * 10^4`

- `1 <= words[i].length <= 10`

- `words[i]` consists of lowercase English letters.

- All the strings of `words` are unique.

### Approach and complexity

A trie shares dictionary prefixes. Search from each board cell, following only existing trie edges and marking cells during the current path. Clear terminal words after reporting them to avoid duplicate output.

Let S be total dictionary characters, B board cells, and L maximum word length. Conservative time O(S+B·4·3^(L−1)·L), including word/path copies; auxiliary space O(S+L), excluding output. Trie pruning reduces actual work.

### C++20 solution

```cpp
class Trie {
public:
    vector<Trie*> children;
    int ref;

    Trie()
        : children(26, nullptr)
        , ref(-1) {}

    void insert(const string& w, int ref) {
        Trie* node = this;
        for (char c : w) {
            c -= 'a';
            if (!node->children[c]) {
                node->children[c] = new Trie();
            }
            node = node->children[c];
        }
        node->ref = ref;
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie* tree = new Trie();
        for (int i = 0; i < words.size(); ++i) {
            tree->insert(words[i], i);
        }
        vector<string> ans;
        int m = board.size(), n = board[0].size();

        function<void(Trie*, int, int)> dfs = [&](Trie* node, int i, int j) {
            int idx = board[i][j] - 'a';
            if (!node->children[idx]) {
                return;
            }
            node = node->children[idx];
            if (node->ref != -1) {
                ans.emplace_back(words[node->ref]);
                node->ref = -1;
            }
            int dirs[5] = {-1, 0, 1, 0, -1};
            char c = board[i][j];
            board[i][j] = '#';
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] != '#') {
                    dfs(node, x, y);
                }
            }
            board[i][j] = c;
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                dfs(tree, i, j);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-126"></a>
## 34. LC 126 — Word Ladder II (Hard)

[Official problem](https://leetcode.com/problems/word-ladder-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0126.Word%20Ladder%20II/README_EN.md)

### Problem description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:

- Every adjacent pair of words differs by a single letter.

- Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.

- `s_k == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return all the **shortest transformation sequences** from `beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words `[beginWord, s_1, s_2, ..., s_k]`.

### Constraints

- `1 <= beginWord.length <= 5`

- `endWord.length == beginWord.length`

- `1 <= wordList.length <= 500`

- `wordList[i].length == beginWord.length`

- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.

- `beginWord != endWord`

- All the words in `wordList` are **unique**.

- The **sum** of all shortest transformation sequences does not exceed `10^5`.

### Approach and complexity

BFS records every shortest-path predecessor, including multiple parents discovered at the same depth. Backtracking through this predecessor DAG emits all and only shortest ladders.

For N words of length L, expected search time O(N·26·L²) with string hashing/copying, plus O(P·D·L) to materialize P ladders of D words. Space includes words, predecessor edges, BFS state, recursion depth O(D), and returned paths.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string>> ans;
        unordered_set<string> words(wordList.begin(), wordList.end());
        if (!words.count(endWord)) {
            return ans;
        }
        words.erase(beginWord);
        unordered_map<string, int> dist{{beginWord, 0}};
        unordered_map<string, unordered_set<string>> prev;
        queue<string> q{{beginWord}};
        bool found = false;
        int step = 0;
        while (!q.empty() && !found) {
            ++step;
            for (int i = q.size(); i > 0; --i) {
                string p = q.front();
                q.pop();
                string t = p;
                for (int j = 0; j < t.size(); ++j) {
                    char ch = t[j];
                    for (char k = 'a'; k <= 'z'; ++k) {
                        t[j] = k;
                        if (dist.count(t) && dist[t] == step) {
                            prev[t].insert(p);
                        }
                        if (!words.count(t)) {
                            continue;
                        }
                        prev[t].insert(p);
                        words.erase(t);
                        q.push(t);
                        dist[t] = step;
                        if (t == endWord) {
                            found = true;
                        }
                    }
                    t[j] = ch;
                }
            }
        }
        function<void(vector<string>&, const string&)> dfs = [&](vector<string>& path, const string& cur) {
            if (cur == beginWord) {
                ans.emplace_back(path.rbegin(), path.rend());
                return;
            }
            for (const string& precursor : prev[cur]) {
                path.push_back(precursor);
                dfs(path, precursor);
                path.pop_back();
            }
        };
        if (found) {
            vector<string> path{endWord};
            dfs(path, endWord);
        }
        return ans;
    }
};
```

---

<a id="lc-332"></a>
## 35. LC 332 — Reconstruct Itinerary (Hard)

[Official problem](https://leetcode.com/problems/reconstruct-itinerary) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0332.Reconstruct%20Itinerary/README_EN.md)

### Problem description

You are given a list of airline `tickets` where `tickets[i] = [from_i, to_i]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

### Constraints

- `1 <= tickets.length <= 300`

- `tickets[i].length == 2`

- `from_i.length == 3`

- `to_i.length == 3`

- `from_i` and `to_i` consist of uppercase English letters.

- `from_i != to_i`

### Approach and complexity

The problem is essentially about finding a path that starts from a specified starting point, passes through all the edges exactly once, and has the smallest lexicographical order among all such paths, given $n$ vertices and $m$ edges. This is a classic Eulerian path problem.

Since the problem guarantees that there is at least one feasible itinerary, we can directly use the Hierholzer algorithm to output the Eulerian path starting from the starting point.

The time complexity is $O(m \log m)$, and the space complexity is $O(m)$, where $m$ is the number of edges.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        sort(tickets.rbegin(), tickets.rend());
        unordered_map<string, vector<string>> g;
        for (const auto& ticket : tickets) {
            g[ticket[0]].push_back(ticket[1]);
        }
        vector<string> ans;
        auto dfs = [&](auto&& dfs, string& f) -> void {
            while (!g[f].empty()) {
                string t = g[f].back();
                g[f].pop_back();
                dfs(dfs, t);
            }
            ans.emplace_back(f);
        };
        string f = "JFK";
        dfs(dfs, f);
        ranges::reverse(ans);
        return ans;
    }
};
```

---

<a id="lc-491"></a>
## 36. LC 491 — Non-decreasing Subsequences (Medium)

[Official problem](https://leetcode.com/problems/non-decreasing-subsequences) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0491.Non-decreasing%20Subsequences/README_EN.md)

### Problem description

Given an integer array `nums`, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in **any order**.

### Constraints

- `1 <= nums.length <= 15`

- `-100 <= nums[i] <= 100`

### Approach and complexity

Backtrack with the last selected value. Take the current value only when it preserves nondecreasing order. Skip it only when it differs from the last selected value; this selects one representative path among duplicate subsequences.

Time O(n·2^n) including output copies; auxiliary space O(n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> t;
        dfs(0, -1000, t, nums, ans);
        return ans;
    }

    void dfs(int u, int last, vector<int>& t, vector<int>& nums, vector<vector<int>>& ans) {
        if (u == nums.size()) {
            if (t.size() > 1) ans.push_back(t);
            return;
        }
        if (nums[u] >= last) {
            t.push_back(nums[u]);
            dfs(u + 1, nums[u], t, nums, ans);
            t.pop_back();
        }
        if (nums[u] != last) dfs(u + 1, last, t, nums, ans);
    }
};
```

---

<a id="lc-842"></a>
## 37. LC 842 — Split Array into Fibonacci Sequence (Medium)

[Official problem](https://leetcode.com/problems/split-array-into-fibonacci-sequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0842.Split%20Array%20into%20Fibonacci%20Sequence/README_EN.md)

### Problem description

You are given a string of digits `num`, such as `"123456579"`. We can split it into a Fibonacci-like sequence `[123, 456, 579]`.

Formally, a **Fibonacci-like** sequence is a list `f` of non-negative integers such that:

- `0 <= f[i] < 2^31`, (that is, each integer fits in a **32-bit** signed integer type),

- `f.length >= 3`, and

- `f[i] + f[i + 1] == f[i + 2]` for all `0 <= i < f.length - 2`.

Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number `0` itself.

Return any Fibonacci-like sequence split from `num`, or return `[]` if it cannot be done.

### Constraints

- `1 <= num.length <= 200`

- `num` contains only digits.

### Approach and complexity

Backtrack over numeric prefixes, enforcing the sum of the last two chosen numbers, the signed 32-bit limit, and no leading zeros except the single digit zero. Once two numbers exist, only one continuation can fit.

Conservative time O(n³), auxiliary space O(n), including result and recursion.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> splitIntoFibonacci(string num) {
        int n = num.size();
        vector<int> ans;
        function<bool(int)> dfs = [&](int i) -> bool {
            if (i == n) {
                return ans.size() > 2;
            }
            long long x = 0;
            for (int j = i; j < n; ++j) {
                if (j > i && num[i] == '0') {
                    break;
                }
                x = x * 10 + num[j] - '0';
                if (x > INT_MAX || (ans.size() > 1 && x > (long long) ans[ans.size() - 1] + ans[ans.size() - 2])) {
                    break;
                }
                if (ans.size() < 2 || x == (long long) ans[ans.size() - 1] + ans[ans.size() - 2]) {
                    ans.push_back(x);
                    if (dfs(j + 1)) {
                        return true;
                    }
                    ans.pop_back();
                }
            }
            return false;
        };
        dfs(0);
        return ans;
    }
};
```

---

<a id="lc-797"></a>
## 38. LC 797 — All Paths From Source to Target (Medium)

[Official problem](https://leetcode.com/problems/all-paths-from-source-to-target) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0797.All%20Paths%20From%20Source%20to%20Target/README_EN.md)

### Problem description

Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

### Constraints

- `n == graph.length`

- `2 <= n <= 15`

- `0 <= graph[i][j] < n`

- `graph[i][j] != i` (i.e., there will be no self-loops).

- All the elements of `graph[i]` are **unique**.

- The input graph is **guaranteed** to be a **DAG**.

### Approach and complexity

Maintain the current source path, append each neighbor during descent, and pop on return. Emit the path only at the target. The DAG condition makes a path-local visited set unnecessary.

Time O(n·2^n) as a conservative bound, including output copies; auxiliary space O(n) excluding returned paths.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> result;
        vector<int> path{0};
        auto dfs = [&](auto&& self, int u) -> void {
            if (u == static_cast<int>(graph.size()) - 1) { result.push_back(path); return; }
            for (int v : graph[u]) {
                path.push_back(v); self(self, v); path.pop_back();
            }
        };
        dfs(dfs, 0);
        return result;
    }
};
```

---

<a id="lc-980"></a>
## 39. LC 980 — Unique Paths III (Hard)

[Official problem](https://leetcode.com/problems/unique-paths-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0980.Unique%20Paths%20III/README_EN.md)

### Problem description

You are given an `m x n` integer array `grid` where `grid[i][j]` could be:

- `1` representing the starting square. There is exactly one starting square.

- `2` representing the ending square. There is exactly one ending square.

- `0` representing empty squares we can walk over.

- `-1` representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

### Constraints

- `m == grid.length`

- `n == grid[i].length`

- `1 <= m, n <= 20`

- `1 <= m * n <= 20`

- `-1 <= grid[i][j] <= 2`

- There is exactly one starting cell and one ending cell.

### Approach and complexity

We can first traverse the entire grid, find the starting point $(x, y)$, and count the number of blank spaces $\textit{cnt}$.

Next, we can start searching from the starting point to get all the path numbers. We design a function $\textit{dfs}(i, j, k)$ to indicate that the path number is $k$ and the starting point is $(i, j)$.

In the function, we first determine whether the current cell is the end point. If it is, we determine whether $k$ is equal to $\textit{cnt} + 1$. If it is, the current path is a valid path, and $1$ is returned, otherwise $0$ is returned.

If the current cell is not the end point, we enumerate the four adjacent cells of the current cell. If the adjacent cell has not been visited, we mark the adjacent cell as visited, and then continue to search the path number from the adjacent cell. After the search is completed, we mark the adjacent cell as unvisited. After the search is completed, we return the sum of the path numbers of all adjacent cells.

Finally, we return the path number from the starting point, that is, $\textit{dfs}(x, y, 1)$.

The time complexity is $O(3^{mn})$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns of the grid, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int cnt = 0;
        for (auto& row : grid) {
            for (auto& x : row) {
                cnt += x == 0;
            }
        }
        int dirs[5] = {-1, 0, 1, 0, -1};
        vector<vector<char>> vis = vector<vector<char>>(m, vector<char>(n, 0));
        function<int(int, int, int)> dfs = [&](int i, int j, int k) -> int {
            if (grid[i][j] == 2) {
                return k == cnt + 1 ? 1 : 0;
            }
            int ans = 0;
            for (int h = 0; h < 4; ++h) {
                int x = i + dirs[h], y = j + dirs[h + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && !vis[x][y] && grid[x][y] != -1) {
                    vis[x][y] = true;
                    ans += dfs(x, y, k + 1);
                    vis[x][y] = false;
                }
            }
            return ans;
        };
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    vis[i][j] = true;
                    return dfs(i, j, 0);
                }
            }
        }
        return 0;
    }
};
```

---

<a id="lc-1219"></a>
## 40. LC 1219 — Path with Maximum Gold (Medium)

[Official problem](https://leetcode.com/problems/path-with-maximum-gold) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1219.Path%20with%20Maximum%20Gold/README_EN.md)

### Problem description

In a gold mine `grid` of size `m x n`, each cell in this mine has an integer representing the amount of gold in that cell, `0` if it is empty.

Return the maximum amount of gold you can collect under the conditions:

- Every time you are located in a cell you will collect all the gold in that cell.

- From your position, you can walk one step to the left, right, up, or down.

- You can't visit the same cell more than once.

- Never visit a cell with `0` gold.

- You can start and stop collecting gold from **any **position in the grid that has some gold.

### Constraints

- `m == grid.length`

- `n == grid[i].length`

- `1 <= m, n <= 15`

- `0 <= grid[i][j] <= 100`

- There are at most **25 **cells containing gold.

### Approach and complexity

We can enumerate each cell as the starting point, and then start a depth-first search from the starting point. During the search process, whenever we encounter a non-zero cell, we turn it into zero and continue the search. When we can no longer continue the search, we calculate the total amount of gold in the current path, then turn the current cell back into a non-zero cell, thus performing backtracking.

The time complexity is $O(mn 3^k)$, and the space complexity is $O(mn)$, where $k$ is the maximum length of each path. Since each cell can only be visited once at most, the time complexity will not exceed $O(mn 3^k)$.

### C++20 solution

```cpp
class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        function<int(int, int)> dfs = [&](int i, int j) {
            if (i < 0 || i >= m || j < 0 || j >= n || !grid[i][j]) {
                return 0;
            }
            int v = grid[i][j];
            grid[i][j] = 0;
            int ans = v + max({dfs(i - 1, j), dfs(i + 1, j), dfs(i, j - 1), dfs(i, j + 1)});
            grid[i][j] = v;
            return ans;
        };
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans = max(ans, dfs(i, j));
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1255"></a>
## 41. LC 1255 — Maximum Score Words Formed by Letters (Hard)

[Official problem](https://leetcode.com/problems/maximum-score-words-formed-by-letters) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1255.Maximum%20Score%20Words%20Formed%20by%20Letters/README_EN.md)

### Problem description

Given a list of `words`, list of single `letters` (might be repeating) and `score` of every character.

Return the maximum score of **any** valid set of words formed by using the given letters (`words[i]` cannot be used two or more times).

It is not necessary to use all characters in `letters` and each letter can only be used once. Score of letters `'a'`, `'b'`, `'c'`, ... ,`'z'` is given by `score[0]`, `score[1]`, ... , `score[25]` respectively.

### Constraints

- `1 <= words.length <= 14`

- `1 <= words[i].length <= 15`

- `1 <= letters.length <= 100`

- `letters[i].length == 1`

- `score.length == 26`

- `0 <= score[i] <= 10`

- `words[i]`, `letters[i]` contains only lower case English letters.

### Approach and complexity

Given the small data range in the problem, we can use binary enumeration to enumerate all word combinations for the given word list. Then, we check whether each word combination meets the requirements of the problem. If it does, we calculate its score and finally take the word combination with the highest score.

First, we use a hash table or array $\textit{cnt}$ to record the number of occurrences of each letter in the alphabet $\textit{letters}$.

Next, we use binary enumeration to enumerate all word combinations. Each bit in the binary represents whether each word in the word list is selected. If the $i$th bit is $1$, it means the $i$th word is selected; otherwise, the $i$th word is not selected.

Then, we count the number of occurrences of each letter in the current word combination and record it in the hash table or array $\textit{cur}$. If the number of occurrences of each letter in $\textit{cur}$ is not greater than the corresponding letter in $\textit{cnt}$, it means the current word combination meets the requirements of the problem. We calculate the score of the current word combination and take the word combination with the highest score.

The time complexity is $O(2^n n \times M)$, and the space complexity is $O(C)$, where $n$ and $M$ are the number of words in the word set and the maximum length of the word, respectively; and $C$ is the number of letters in the alphabet, in this problem, $C=26$.

### C++20 solution

```cpp
class Solution {
public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        int cnt[26]{};
        for (char& c : letters) {
            cnt[c - 'a']++;
        }
        int n = words.size();
        int ans = 0;
        for (int i = 0; i < 1 << n; ++i) {
            int cur[26]{};
            for (int j = 0; j < n; ++j) {
                if (i >> j & 1) {
                    for (char& c : words[j]) {
                        cur[c - 'a']++;
                    }
                }
            }
            bool ok = true;
            int t = 0;
            for (int j = 0; j < 26; ++j) {
                if (cur[j] > cnt[j]) {
                    ok = false;
                    break;
                }
                t += cur[j] * score[j];
            }
            if (ok && ans < t) {
                ans = t;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1601"></a>
## 42. LC 1601 — Maximum Number of Achievable Transfer Requests (Hard)

[Official problem](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1601.Maximum%20Number%20of%20Achievable%20Transfer%20Requests/README_EN.md)

### Problem description

We have `n` buildings numbered from `0` to `n - 1`. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array `requests` where `requests[i] = [from_i, to_i]` represents an employee's request to transfer from building `from_i` to building `to_i`.

**All buildings are full**, so a list of requests is achievable only if for each building, the **net change in employee transfers is zero**. This means the number of employees **leaving** is **equal** to the number of employees **moving in**. For example if `n = 3` and two employees are leaving building `0`, one is leaving building `1`, and one is leaving building `2`, there should be two employees moving to building `0`, one employee moving to building `1`, and one employee moving to building `2`.

Return the maximum number of achievable requests.

### Constraints

- `1 <= n <= 20`

- `1 <= requests.length <= 16`

- `requests[i].length == 2`

- `0 <= from_i, to_i < n`

### Approach and complexity

We note that the length of the room change request list does not exceed $16$. Therefore, we can use the method of binary enumeration to enumerate all room change request lists. Specifically, we can use a binary number of length $16$ to represent a room change request list, where the $i$-th bit being $1$ means the $i$-th room change request is selected, and $0$ means the $i$-th room change request is not selected.

We enumerate all binary numbers in the range of $[1, 2^{m})$, for each binary number $\textit{mask}$, we first calculate how many $1$s are in its binary representation, denoted as $\textit{cnt}$. If $\textit{cnt}$ is larger than the current answer $\textit{ans}$, then we judge whether $\textit{mask}$ is a feasible room change request list. If it is, then we update the answer $\textit{ans}$ with $\textit{cnt}$. To judge whether $\textit{mask}$ is a feasible room change request list, we only need to check whether the net inflow of each room is $0$.

The time complexity is $O(2^m(m + n))$, and the space complexity is $O(n)$, where $m$ and $n$ are the lengths of the room change request list and the number of rooms, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int maximumRequests(int n, vector<vector<int>>& requests) {
        int m = requests.size();
        int ans = 0;
        auto check = [&](int mask) -> bool {
            vector<int> cnt = vector<int>(n, 0);
            for (int i = 0; i < m; ++i) {
                if (mask >> i & 1) {
                    int f = requests[i][0], t = requests[i][1];
                    --cnt[f];
                    ++cnt[t];
                }
            }
            for (int v : cnt) {
                if (v) {
                    return false;
                }
            }
            return true;
        };
        for (int mask = 0; mask < 1 << m; ++mask) {
            int cnt = popcount(static_cast<unsigned int>(mask));
            if (ans < cnt && check(mask)) {
                ans = cnt;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1718"></a>
## 43. LC 1718 — Construct the Lexicographically Largest Valid Sequence (Medium)

[Official problem](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1718.Construct%20the%20Lexicographically%20Largest%20Valid%20Sequence/README_EN.md)

### Problem description

Given an integer `n`, find a sequence with elements in the range `[1, n]` that satisfies all of the following:

- The integer `1` occurs once in the sequence.

- Each integer between `2` and `n` occurs twice in the sequence.

- For every integer `i` between `2` and `n`, the **distance** between the two occurrences of `i` is exactly `i`.

The **distance** between two numbers on the sequence, `a[i]` and `a[j]`, is the absolute difference of their indices, `|j - i|`.

Return the **lexicographically largest** sequence. It is guaranteed that under the given constraints, there is always a solution. 

A sequence `a` is lexicographically larger than a sequence `b` (of the same length) if in the first position where `a` and `b` differ, sequence `a` has a number greater than the corresponding number in `b`. For example, `[0,1,9,0]` is lexicographically larger than `[0,1,5,6]` because the first position they differ is at the third number, and `9` is greater than `5`.

### Constraints

- `1 <= n <= 20`

### Approach and complexity

Fill the first unoccupied position with unused candidates from largest to smallest. Place both copies at distance equal to the value (one has a single copy), and undo on failure. The first completed sequence is lexicographically largest.

Conservative time O(n·n!), auxiliary space O(n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    int n;
    vector<int> cnt, path;

    vector<int> constructDistancedSequence(int _n) {
        n = _n;
        cnt.resize(n * 2, 2);
        path.resize(n * 2);
        cnt[1] = 1;
        dfs(1);
        vector<int> ans;
        for (int i = 1; i < n * 2; ++i) ans.push_back(path[i]);
        return ans;
    }

    bool dfs(int u) {
        if (u == n * 2) return 1;
        if (path[u]) return dfs(u + 1);
        for (int i = n; i > 1; --i) {
            if (cnt[i] && u + i < n * 2 && !path[u + i]) {
                path[u] = path[u + i] = i;
                cnt[i] = 0;
                if (dfs(u + 1)) return 1;
                cnt[i] = 2;
                path[u] = path[u + i] = 0;
            }
        }
        if (cnt[1]) {
            path[u] = 1;
            cnt[1] = 0;
            if (dfs(u + 1)) return 1;
            cnt[1] = 1;
            path[u] = 0;
        }
        return 0;
    }
};
```

---

<a id="lc-1849"></a>
## 44. LC 1849 — Splitting a String Into Descending Consecutive Values (Medium)

[Official problem](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1849.Splitting%20a%20String%20Into%20Descending%20Consecutive%20Values/README_EN.md)

### Problem description

You are given a string `s` that consists of only digits.

Check if we can split `s` into **two or more non-empty substrings** such that the **numerical values** of the substrings are in **descending order** and the **difference** between numerical values of every two **adjacent** **substrings** is equal to `1`.

- For example, the string `s = "0090089"` can be split into `["0090", "089"]` with numerical values `[90,89]`. The values are in descending order and adjacent values differ by `1`, so this way is valid.

- Another example, the string `s = "001"` can be split into `["0", "01"]`, `["00", "1"]`, or `["0", "0", "1"]`. However all the ways are invalid because they have numerical values `[0,1]`, `[0,1]`, and `[0,0,1]` respectively, all of which are not in descending order.

Return `true` if it is possible to split `s`​​​​​​ as described above, or `false` otherwise.

A **substring** is a contiguous sequence of characters in a string.

### Constraints

- `1 <= s.length <= 20`

- `s` only consists of digits.

### Approach and complexity

We can start from the first character of the string and try to split it into one or more substrings, then recursively process the remaining part.

Specifically, we design a function $\textit{dfs}(i, x)$, where $i$ represents the current position being processed, and $x$ represents the last split value. Initially, $x = -1$, indicating that we have not split out any value yet.

In $\textit{dfs}(i, x)$, we first calculate the current split value $y$. If $x = -1$, or $x - y = 1$, then we can try to use $y$ as the next value and continue to recursively process the remaining part. If the result of the recursion is $\textit{true}$, we have found a valid split method and return $\textit{true}$.

After traversing all possible split methods, if no valid split method is found, we return $\textit{false}$.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the length of the string.

### C++20 solution

```cpp
class Solution {
public:
    bool splitString(string s) {
        auto dfs = [&](auto&& dfs, int i, long long x) -> bool {
            if (i >= s.size()) {
                return true;
            }
            long long y = 0;
            int r = x < 0 ? s.size() - 1 : s.size();
            for (int j = i; j < r; ++j) {
                y = y * 10 + s[j] - '0';
                if (y > 1e10) {
                    break;
                }
                if ((x < 0 || x - y == 1) && dfs(dfs, j + 1, y)) {
                    return true;
                }
            }
            return false;
        };
        return dfs(dfs, 0, -1);
    }
};
```

---

<a id="lc-2375"></a>
## 45. LC 2375 — Construct Smallest Number From DI String (Medium)

[Official problem](https://leetcode.com/problems/construct-smallest-number-from-di-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2375.Construct%20Smallest%20Number%20From%20DI%20String/README_EN.md)

### Problem description

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

- `num` consists of the digits `'1'` to `'9'`, where each digit is used **at most** once.

- If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.

- If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

Return the lexicographically **smallest** possible string `num` that meets the conditions.

### Constraints

- `1 <= pattern.length <= 8`

- `pattern` consists of only the letters `'I'` and `'D'`.

### Approach and complexity

Push the next smallest unused digit. At an I boundary, or at the end, pop the whole stack into the answer. This reverses exactly the D runs. Using the smallest available consecutive digits for each run yields the lexicographically smallest valid number.

Time O(n); auxiliary space O(n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    string smallestNumber(string pattern) {
        string result, pending;
        for (int i = 0; i <= static_cast<int>(pattern.size()); ++i) {
            pending += static_cast<char>('1' + i);
            if (i == static_cast<int>(pattern.size()) || pattern[i] == 'I') {
                while (!pending.empty()) { result += pending.back(); pending.pop_back(); }
            }
        }
        return result;
    }
};
```

---

<a id="lc-967"></a>
## 46. LC 967 — Numbers With Same Consecutive Differences (Medium)

[Official problem](https://leetcode.com/problems/numbers-with-same-consecutive-differences) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0967.Numbers%20With%20Same%20Consecutive%20Differences/README_EN.md)

### Problem description

Given two integers n and k, return an array of all the integers of length `n` where the difference between every two consecutive digits is `k`. You may return the answer in **any order**.

Note that the integers should not have leading zeros. Integers as `02` and `043` are not allowed.

### Constraints

- `2 <= n <= 9`

- `0 <= k <= 9`

### Approach and complexity

We can enumerate the first digit of all numbers of length $n$, and then use the depth-first search method to recursively construct all numbers that meet the conditions.

Specifically, we first define a boundary value $\textit{boundary} = 10^{n-1}$, which represents the minimum value of the number we need to construct. Then, we enumerate the first digit from $1$ to $9$. For each digit $i$, we recursively construct the number of length $n$ with $i$ as the first digit.

The time complexity is $O(n 2^n|\Sigma|)$, and the space complexity is $O(2^n)$, where $|\Sigma|$ represents the set of digits, and in this problem $|\Sigma| = 9$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> ans;
        int boundary = pow(10, n - 1);
        auto dfs = [&](auto&& dfs, int x) {
            if (x >= boundary) {
                ans.push_back(x);
                return;
            }
            int last = x % 10;
            if (last + k < 10) {
                dfs(dfs, x * 10 + last + k);
            }
            if (k != 0 && last - k >= 0) {
                dfs(dfs, x * 10 + last - k);
            }
        };
        for (int i = 1; i < 10; ++i) {
            dfs(dfs, i);
        }
        return ans;
    }
};
```

---

<a id="lc-306"></a>
## 47. LC 306 — Additive Number (Medium)

[Official problem](https://leetcode.com/problems/additive-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0306.Additive%20Number/README_EN.md)

### Problem description

An **additive number** is a string whose digits can form an **additive sequence**.

A valid **additive sequence** should contain **at least** three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return `true` if it is an **additive number** or `false` otherwise.

**Note:** Numbers in the additive sequence **cannot** have leading zeros, so sequence `1, 2, 03` or `1, 02, 3` is invalid.

### Constraints

- `1 <= num.length <= 35`

- `num` consists only of digits.

**Follow up:** How would you handle overflow for very large input integers?

### Approach and complexity

Enumerate the first two terms, rejecting leading zeros. Each following term must equal their decimal-string sum. Compare the sum at the current offset and advance; string addition supports all 35 input digits without integer overflow.

Conservative time O(n³); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
    string add(const string& a, const string& b) {
        string sum;
        int i = static_cast<int>(a.size()) - 1, j = static_cast<int>(b.size()) - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry) {
            if (i >= 0) carry += a[i--] - '0';
            if (j >= 0) carry += b[j--] - '0';
            sum += static_cast<char>('0' + carry % 10);
            carry /= 10;
        }
        ranges::reverse(sum);
        return sum;
    }
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        for (int first = 1; first < n - 1; ++first) {
            if (first > 1 && num[0] == '0') break;
            for (int second = first + 1; second < n; ++second) {
                if (second > first + 1 && num[first] == '0') break;
                string a = num.substr(0, first), b = num.substr(first, second - first);
                int pos = second;
                while (pos < n) {
                    string next = add(a, b);
                    if (num.compare(pos, next.size(), next) != 0) break;
                    pos += next.size();
                    a = move(b); b = move(next);
                }
                if (pos == n) return true;
            }
        }
        return false;
    }
};
```

---

<a id="lc-60"></a>
## 48. LC 60 — Permutation Sequence (Hard)

[Official problem](https://leetcode.com/problems/permutation-sequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0060.Permutation%20Sequence/README_EN.md)

### Problem description

The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

- `"123"`

- `"132"`

- `"213"`

- `"231"`

- `"312"`

- `"321"`

Given `n` and `k`, return the `k^th` permutation sequence.

### Constraints

- `1 <= n <= 9`

- `1 <= k <= n!`

### Approach and complexity

We know that the set $[1,2,..n]$ has a total of $n!$ permutations. If we determine the first digit, the number of permutations that the remaining digits can form is $(n-1)!$.

Therefore, we enumerate each digit $i$. If $k$ is greater than the number of permutations after the current position is determined, then we can directly subtract this number; otherwise, it means that we have found the number at the current position.

For each digit $i$, where $0 \leq i < n$, the number of permutations that the remaining digits can form is $(n-i-1)!$, which we denote as $\textit{fact}$. The numbers used in the process are recorded in $\textit{vis}$.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$.

### C++20 solution

```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        string ans;
        bitset<10> vis;
        for (int i = 0; i < n; ++i) {
            int fact = 1;
            for (int j = 1; j < n - i; ++j) fact *= j;
            for (int j = 1; j <= n; ++j) {
                if (vis[j]) continue;
                if (k > fact)
                    k -= fact;
                else {
                    ans += to_string(j);
                    vis[j] = 1;
                    break;
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-89"></a>
## 49. LC 89 — Gray Code (Medium)

[Official problem](https://leetcode.com/problems/gray-code) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0089.Gray%20Code/README_EN.md)

### Problem description

An **n-bit gray code sequence** is a sequence of `2^n` integers where:

- Every integer is in the **inclusive** range `[0, 2^n - 1]`,

- The first integer is `0`,

- An integer appears **no more than once** in the sequence,

- The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and

- The binary representation of the **first** and **last** integers differs by **exactly one bit**.

Given an integer `n`, return any valid **n-bit gray code sequence**.

### Constraints

- `1 <= n <= 16`

### Approach and complexity

Gray code is a type of encoding method that we often encounter in engineering. Its basic feature is that only one bit of binary number is different between any two adjacent codes.

The rule for converting binary code to binary Gray code is to keep the highest bit of the binary code as the highest bit of the Gray code, and the second highest bit of the Gray code is the XOR of the highest bit and the second highest bit of the binary code. The calculation of the remaining bits of the Gray code is similar to the second highest bit.

Assume that a binary number is represented as $B_{n-1}B_{n-2}...B_2B_1B_0$, and its Gray code is represented as $G_{n-1}G_{n-2}...G_2G_1G_0$. The highest bit is retained, so $G_{n-1} = B_{n-1}$; and the other bits $G_i = B_{i+1} \oplus B_{i}$, where $i=0,1,2..,n-2$.

Therefore, for an integer $x$, we can use the function $\textit{gray}(x)$ to get its Gray code:

```java
int gray(x) {
    return x ^ (x >> 1);
}
```

We directly map the integers $[0,..2^n - 1]$ to the corresponding Gray codes to get the answer array.

The time complexity is $O(2^n)$, and the space complexity is $O(1)$, where $n$ is the integer given in the problem.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> ans;
        for (int i = 0; i < 1 << n; ++i) {
            ans.push_back(i ^ (i >> 1));
        }
        return ans;
    }
};
```

---

<a id="lc-95"></a>
## 50. LC 95 — Unique Binary Search Trees II (Medium)

[Official problem](https://leetcode.com/problems/unique-binary-search-trees-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0095.Unique%20Binary%20Search%20Trees%20II/README_EN.md)

### Problem description

Given an integer `n`, return all the structurally unique **BST'**s (binary search trees), which has exactly `n` nodes of unique values from `1` to `n`. Return the answer in **any order**.

### Constraints

- `1 <= n <= 8`

### Approach and complexity

We design a function $\textit{dfs}(i, j)$ that returns all feasible binary search trees composed of $[i, j]$, so the answer is $\textit{dfs}(1, n)$.

The execution steps of the function $\textit{dfs}(i, j)$ are as follows:

1. If $i > j$, it means that there are no numbers to form a binary search tree at this time, so return a list consisting of a null node.
2. If $i \leq j$, we enumerate the numbers $v$ in $[i, j]$ as the root node. The left subtree of the root node $v$ is composed of $[i, v - 1]$, and the right subtree is composed of $[v + 1, j]$. Finally, we take the Cartesian product of all combinations of the left and right subtrees, i.e., $\textit{left} \times \textit{right}$, add the root node $v$, and get all binary search trees with $v$ as the root node.

The time complexity is $O(n \times G(n))$, and the space complexity is $O(n \times G(n))$, where $G(n)$ is the Catalan number.

### C++20 solution

```cpp
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        function<vector<TreeNode*>(int, int)> dfs = [&](int i, int j) {
            if (i > j) {
                return vector<TreeNode*>{nullptr};
            }
            vector<TreeNode*> ans;
            for (int v = i; v <= j; ++v) {
                auto left = dfs(i, v - 1);
                auto right = dfs(v + 1, j);
                for (auto l : left) {
                    for (auto r : right) {
                        ans.push_back(new TreeNode(v, l, r));
                    }
                }
            }
            return ans;
        };
        return dfs(1, n);
    }
};
```
