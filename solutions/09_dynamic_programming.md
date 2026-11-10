# 9. Dynamic Programming — C++20 solutions

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

1. [LC 70 — Climbing Stairs](#lc-70)
2. [LC 198 — House Robber](#lc-198)
3. [LC 322 — Coin Change](#lc-322)
4. [LC 300 — Longest Increasing Subsequence](#lc-300)
5. [LC 1143 — Longest Common Subsequence](#lc-1143)
6. [LC 72 — Edit Distance](#lc-72)
7. [LC 416 — Partition Equal Subset Sum](#lc-416)
8. [LC 139 — Word Break](#lc-139)
9. [LC 62 — Unique Paths](#lc-62)
10. [LC 64 — Minimum Path Sum](#lc-64)
11. [LC 53 — Maximum Subarray](#lc-53)
12. [LC 152 — Maximum Product Subarray](#lc-152)
13. [LC 91 — Decode Ways](#lc-91)
14. [LC 746 — Min Cost Climbing Stairs](#lc-746)
15. [LC 213 — House Robber II](#lc-213)
16. [LC 337 — House Robber III](#lc-337)
17. [LC 279 — Perfect Squares](#lc-279)
18. [LC 377 — Combination Sum IV](#lc-377)
19. [LC 518 — Coin Change II](#lc-518)
20. [LC 494 — Target Sum](#lc-494)
21. [LC 474 — Ones and Zeroes](#lc-474)
22. [LC 1049 — Last Stone Weight II](#lc-1049)
23. [LC 221 — Maximal Square](#lc-221)
24. [LC 120 — Triangle](#lc-120)
25. [LC 931 — Minimum Falling Path Sum](#lc-931)
26. [LC 63 — Unique Paths II](#lc-63)
27. [LC 115 — Distinct Subsequences](#lc-115)
28. [LC 97 — Interleaving String](#lc-97)
29. [LC 5 — Longest Palindromic Substring](#lc-5)
30. [LC 647 — Palindromic Substrings](#lc-647)
31. [LC 516 — Longest Palindromic Subsequence](#lc-516)
32. [LC 1312 — Minimum Insertion Steps to Make a String Palindrome](#lc-1312)
33. [LC 312 — Burst Balloons](#lc-312)
34. [LC 1547 — Minimum Cost to Cut a Stick](#lc-1547)
35. [LC 1039 — Minimum Score Triangulation of Polygon](#lc-1039)
36. [LC 309 — Best Time to Buy and Sell Stock with Cooldown](#lc-309)
37. [LC 714 — Best Time to Buy and Sell Stock with Transaction Fee](#lc-714)
38. [LC 123 — Best Time to Buy and Sell Stock III](#lc-123)
39. [LC 188 — Best Time to Buy and Sell Stock IV](#lc-188)
40. [LC 121 — Best Time to Buy and Sell Stock](#lc-121)
41. [LC 122 — Best Time to Buy and Sell Stock II](#lc-122)
42. [LC 55 — Jump Game](#lc-55)
43. [LC 45 — Jump Game II](#lc-45)
44. [LC 673 — Number of Longest Increasing Subsequence](#lc-673)
45. [LC 354 — Russian Doll Envelopes](#lc-354)
46. [LC 1235 — Maximum Profit in Job Scheduling](#lc-1235)
47. [LC 983 — Minimum Cost For Tickets](#lc-983)
48. [LC 96 — Unique Binary Search Trees](#lc-96)
49. [LC 95 — Unique Binary Search Trees II](#lc-95)
50. [LC 10 — Regular Expression Matching](#lc-10)

---

<a id="lc-70"></a>
## 1. LC 70 — Climbing Stairs (Easy)

[Official problem](https://leetcode.com/problems/climbing-stairs) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0070.Climbing%20Stairs/README_EN.md)

### Problem description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### Constraints

- `1 <= n <= 45`

### Approach and complexity

We set $\textit{Fib}(n)$ to represent a $1 \times 2$ matrix $\begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}$, where $F_n$ and $F_{n - 1}$ are the $n$-th and $(n - 1)$-th Fibonacci numbers respectively.

We hope to derive $\textit{Fib}(n)$ based on $\textit{Fib}(n-1) = \begin{bmatrix} F_{n - 1} & F_{n - 2} \end{bmatrix}$. That is to say, we need a matrix $\textit{base}$, so that $\textit{Fib}(n - 1) \times \textit{base} = \textit{Fib}(n)$, that is:

$$
\begin{bmatrix}
F_{n - 1} & F_{n - 2}
\end{bmatrix} \times \textit{base} = \begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}
$$

Since $F_n = F_{n - 1} + F_{n - 2}$, the first column of the matrix $\textit{base}$ is:

$$
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

The second column is:

$$
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

Therefore:

$$
\begin{bmatrix} F_{n - 1} & F_{n - 2} \end{bmatrix} \times \begin{bmatrix}1 & 1 \\ 1 & 0\end{bmatrix} = \begin{bmatrix} F_n & F_{n - 1} \end{bmatrix}
$$

We define the initial matrix $\textit{res} = \begin{bmatrix} 1 & 1 \end{bmatrix}$, then $F_n$ is equal to the first element of the first row of the result matrix of $\textit{res}$ multiplied by $\textit{base}^{n - 1}$. We can solve it using matrix quick power.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<vector<long long>> a = {{1, 1}, {1, 0}};
        return pow(a, n - 1)[0][0];
    }

private:
    vector<vector<long long>> mul(vector<vector<long long>>& a, vector<vector<long long>>& b) {
        int m = a.size(), n = b[0].size();
        vector<vector<long long>> res(m, vector<long long>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < a[0].size(); ++k) {
                    res[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return res;
    }

    vector<vector<long long>> pow(vector<vector<long long>>& a, int n) {
        vector<vector<long long>> res = {{1, 1}, {0, 0}};
        while (n) {
            if (n & 1) {
                res = mul(res, a);
            }
            a = mul(a, a);
            n >>= 1;
        }
        return res;
    }
};
```

---

<a id="lc-198"></a>
## 2. LC 198 — House Robber (Medium)

[Official problem](https://leetcode.com/problems/house-robber) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0198.House%20Robber/README_EN.md)

### Problem description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Constraints

- `1 <= nums.length <= 100`

- `0 <= nums[i] <= 400`

### Approach and complexity

We notice that when $i \gt 2$, $f[i]$ is only related to $f[i-1]$ and $f[i-2]$. Therefore, we can use two variables instead of an array to reduce the space complexity to $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int f = 0, g = 0;
        for (int& x : nums) {
            int ff = max(f, g);
            g = f + x;
            f = ff;
        }
        return max(f, g);
    }
};
```

---

<a id="lc-322"></a>
## 3. LC 322 — Coin Change (Medium)

[Official problem](https://leetcode.com/problems/coin-change) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0322.Coin%20Change/README_EN.md)

### Problem description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest** number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

### Constraints

- `1 <= coins.length <= 12`

- `1 <= coins[i] <= 2^31 - 1`

- `0 <= amount <= 10^4`

### Approach and complexity

We notice that $f[i][j]$ is only related to $f[i - 1][j]$ and $f[i][j - x]$. Therefore, we can optimize the two-dimensional array into a one-dimensional array, reducing the space complexity to $O(n)$. The time complexity remains $O(mn)$.

Similar problems:

- [279. Perfect Squares](https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0279.Perfect%20Squares/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = amount;
        vector<int> f = vector<int>(n + 1, 0x3f3f3f3f);
        f[0] = 0;
        for (int x : coins) {
            for (int j = x; j <= n; ++j) {
                f[j] = min(f[j], f[j - x] + 1);
            }
        }
        return f[n] > n ? -1 : f[n];
    }
};
```

---

<a id="lc-300"></a>
## 4. LC 300 — Longest Increasing Subsequence (Medium)

[Official problem](https://leetcode.com/problems/longest-increasing-subsequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0300.Longest%20Increasing%20Subsequence/README_EN.md)

### Problem description

Given an integer array `nums`, return the length of the longest **strictly increasing ****subsequence**.

### Constraints

- `1 <= nums.length <= 2500`

- `-10^4 <= nums[i] <= 10^4`

Follow up: Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

### Approach and complexity

Maintain tails[len−1], the smallest possible final value of an increasing subsequence of length len. Replace the first tail at least x; append when none exists. Smaller tails preserve all future extension opportunities. Use lower_bound rather than upper_bound for strictly increasing sequences.

Time O(n log n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails;
        for (int x : nums) {
            auto it = ranges::lower_bound(tails, x);
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
        }
        return tails.size();
    }
};
```

---

<a id="lc-1143"></a>
## 5. LC 1143 — Longest Common Subsequence (Medium)

[Official problem](https://leetcode.com/problems/longest-common-subsequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1100-1199/1143.Longest%20Common%20Subsequence/README_EN.md)

### Problem description

Given two strings `text1` and `text2`, return the length of their longest **common subsequence**. If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

### Constraints

- `1 <= text1.length, text2.length <= 1000`

- `text1` and `text2` consist of only lowercase English characters.

### Approach and complexity

Update prefix LCS lengths row by row. Equal characters extend the previous diagonal; different characters take the better of excluding either last character. Store the shorter dimension.

Time O(mn); auxiliary space O(min(m,n)).

### C++20 solution

```cpp
class Solution {
public:
    int longestCommonSubsequence(string a, string b) {
        if (a.size() < b.size()) swap(a, b);
        vector<int> dp(b.size() + 1);
        for (char x : a) {
            int diagonal = 0;
            for (int j = 1; j <= static_cast<int>(b.size()); ++j) {
                int above = dp[j];
                dp[j] = x == b[j - 1] ? diagonal + 1 : max(dp[j], dp[j - 1]);
                diagonal = above;
            }
        }
        return dp.back();
    }
};
```

---

<a id="lc-72"></a>
## 6. LC 72 — Edit Distance (Medium)

[Official problem](https://leetcode.com/problems/edit-distance) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0072.Edit%20Distance/README_EN.md)

### Problem description

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character

- Delete a character

- Replace a character

### Constraints

- `0 <= word1.length, word2.length <= 500`

- `word1` and `word2` consist of lowercase English letters.

### Approach and complexity

For each character of the first word, update the row for prefixes of the second word. Save the old diagonal before overwriting it. Matching characters inherit the diagonal; otherwise add one to the minimum of insert, delete, and replace.

Time O(mn); auxiliary space O(min(m,n)).

### C++20 solution

```cpp
class Solution {
public:
    int minDistance(string a, string b) {
        if (a.size() < b.size()) swap(a, b);
        vector<int> dp(b.size() + 1);
        iota(dp.begin(), dp.end(), 0);
        for (int i = 1; i <= static_cast<int>(a.size()); ++i) {
            int diagonal = dp[0];
            dp[0] = i;
            for (int j = 1; j <= static_cast<int>(b.size()); ++j) {
                int above = dp[j];
                dp[j] = a[i - 1] == b[j - 1] ? diagonal : 1 + min({diagonal, dp[j], dp[j - 1]});
                diagonal = above;
            }
        }
        return dp.back();
    }
};
```

---

<a id="lc-416"></a>
## 7. LC 416 — Partition Equal Subset Sum (Medium)

[Official problem](https://leetcode.com/problems/partition-equal-subset-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0416.Partition%20Equal%20Subset%20Sum/README_EN.md)

### Problem description

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

### Constraints

- `1 <= nums.length <= 200`

- `1 <= nums[i] <= 100`

### Approach and complexity

We notice that in Solution 1, $f[i][j]$ is only related to $f[i - 1][\cdot]$. Therefore, we can compress the two-dimensional array into a one-dimensional array.

The time complexity is $O(nm)$, and the space complexity is $O(m)$, where $n$ is the length of the array, and $m$ is half of the total sum of the array.

### C++20 solution

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        if (s % 2 == 1) {
            return false;
        }
        int m = s >> 1;
        vector<char> f = vector<char>(m + 1, 0);
        f[0] = true;
        for (int& x : nums) {
            for (int j = m; j >= x; --j) {
                f[j] |= f[j - x];
            }
        }
        return f[m];
    }
};
```

---

<a id="lc-139"></a>
## 8. LC 139 — Word Break (Medium)

[Official problem](https://leetcode.com/problems/word-break) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0139.Word%20Break/README_EN.md)

### Problem description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

### Constraints

- `1 <= s.length <= 300`

- `1 <= wordDict.length <= 1000`

- `1 <= wordDict[i].length <= 20`

- `s` and `wordDict[i]` consist of only lowercase English letters.

- All the strings of `wordDict` are **unique**.

### Approach and complexity

Build a trie in a vector-owned node pool. From each reachable prefix, follow matching trie edges and mark every terminal endpoint reachable. This avoids repeated substring allocation and hashing.

Let S be total dictionary characters and L the longest word. Time O(S+nL); auxiliary space O(S+n). The pool releases all trie storage automatically.

### C++20 solution

```cpp
class Solution {
    struct TrieNode { array<int, 26> next; bool terminal = false; TrieNode() { next.fill(-1); } };
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<TrieNode> trie(1);
        for (const auto& word : wordDict) {
            int node = 0;
            for (char c : word) {
                int letter = c - 'a';
                if (trie[node].next[letter] == -1) {
                    int child = trie.size();
                    trie.emplace_back();
                    trie[node].next[letter] = child;
                }
                node = trie[node].next[letter];
            }
            trie[node].terminal = true;
        }
        vector<bool> reachable(s.size() + 1);
        reachable[0] = true;
        for (int start = 0; start < static_cast<int>(s.size()); ++start) {
            if (!reachable[start]) continue;
            int node = 0;
            for (int end = start; end < static_cast<int>(s.size()); ++end) {
                node = trie[node].next[s[end] - 'a'];
                if (node == -1) break;
                if (trie[node].terminal) reachable[end + 1] = true;
            }
        }
        return reachable.back();
    }
};
```

---

<a id="lc-62"></a>
## 9. LC 62 — Unique Paths (Medium)

[Official problem](https://leetcode.com/problems/unique-paths) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0062.Unique%20Paths/README_EN.md)

### Problem description

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

### Constraints

- `1 <= m, n <= 100`

### Approach and complexity

A path consists of m−1 down moves and n−1 right moves. Choose the positions of the smaller move count using C(m+n−2,min(m−1,n−1)). Each incremental multiplication/division is exact; 64-bit intermediates are safe because the final answer fits signed int and m,n≤100.

Time O(min(m,n)); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        int k = min(m - 1, n - 1), total = m + n - 2;
        long long paths = 1;
        for (int i = 1; i <= k; ++i) paths = paths * (total - k + i) / i;
        return static_cast<int>(paths);
    }
};
```

---

<a id="lc-64"></a>
## 10. LC 64 — Minimum Path Sum (Medium)

[Official problem](https://leetcode.com/problems/minimum-path-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0064.Minimum%20Path%20Sum/README_EN.md)

### Problem description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

### Constraints

- `m == grid.length`

- `n == grid[i].length`

- `1 <= m, n <= 200`

- `0 <= grid[i][j] <= 200`

### Approach and complexity

The best path into a cell comes from above or left. A single row stores the previous row before overwrite and the current row to the left. A finite sentinel well above all valid path costs handles boundaries.

Time O(mn); auxiliary space O(n). Leaves the input unchanged.

### C++20 solution

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<int> dp(grid[0].size(), INT_MAX / 2);
        dp[0] = 0;
        for (const auto& row : grid)
            for (int j = 0; j < static_cast<int>(row.size()); ++j)
                dp[j] = row[j] + min(dp[j], j ? dp[j - 1] : INT_MAX / 2);
        return dp.back();
    }
};
```

---

<a id="lc-53"></a>
## 11. LC 53 — Maximum Subarray (Medium)

[Official problem](https://leetcode.com/problems/maximum-subarray) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0053.Maximum%20Subarray/README_EN.md)

### Problem description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^4 <= nums[i] <= 10^4`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

### Approach and complexity

We define $f[i]$ to represent the maximum sum of a contiguous subarray ending at element $\textit{nums}[i]$. Initially, $f[0] = \textit{nums}[0]$. The final answer we seek is $\max_{0 \leq i < n} f[i]$.

Consider $f[i]$ for $i \geq 1$. Its state transition equation is:

$$
f[i] = \max(f[i - 1] + \textit{nums}[i], \textit{nums}[i])
$$

That is:

$$
f[i] = \max(f[i - 1], 0) + \textit{nums}[i]
$$

Since $f[i]$ is only related to $f[i - 1]$, we can use a single variable $f$ to maintain the current value of $f[i]$ and perform the state transition. The answer is $\max_{0 \leq i < n} f$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0], f = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            f = max(f, 0) + nums[i];
            ans = max(ans, f);
        }
        return ans;
    }
};
```

---

<a id="lc-152"></a>
## 12. LC 152 — Maximum Product Subarray (Medium)

[Official problem](https://leetcode.com/problems/maximum-product-subarray) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0152.Maximum%20Product%20Subarray/README_EN.md)

### Problem description

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

### Constraints

- `1 <= nums.length <= 2 * 10^4`

- `-10 <= nums[i] <= 10`

- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

### Approach and complexity

Maintain both minimum and maximum products ending at each index: a negative value can swap their roles. Compare starting fresh with extending either product.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int f = nums[0], g = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int ff = f, gg = g;
            f = max({nums[i], ff * nums[i], gg * nums[i]});
            g = min({nums[i], ff * nums[i], gg * nums[i]});
            ans = max(ans, f);
        }
        return ans;
    }
};
```

---

<a id="lc-91"></a>
## 13. LC 91 — Decode Ways (Medium)

[Official problem](https://leetcode.com/problems/decode-ways) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0091.Decode%20Ways/README_EN.md)

### Problem description

You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

- `"AAJF"` with the grouping `(1, 1, 10, 6)`

- `"KJF"` with the grouping `(11, 10, 6)`

- The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

### Constraints

- `1 <= s.length <= 100`

- `s` contains only digits and may contain leading zero(s).

### Approach and complexity

We notice that the state $f[i]$ is only related to $f[i-1]$ and $f[i-2]$. Therefore, we can use two variables to replace these states, reducing the space complexity from $O(n)$ to $O(1)$. The time complexity remains $O(n)$.

### C++20 solution

```cpp
class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        int f = 0, g = 1;
        for (int i = 1; i <= n; ++i) {
            int h = s[i - 1] != '0' ? g : 0;
            if (i > 1 && (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6'))) {
                h += f;
            }
            f = g;
            g = h;
        }
        return g;
    }
};
```

---

<a id="lc-746"></a>
## 14. LC 746 — Min Cost Climbing Stairs (Easy)

[Official problem](https://leetcode.com/problems/min-cost-climbing-stairs) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0746.Min%20Cost%20Climbing%20Stairs/README_EN.md)

### Problem description

You are given an integer array `cost` where `cost[i]` is the cost of `i^th` step on a staircase.

Once you pay the cost, you can either climb **one** or **two** steps.

You can either start from the step with index 0, or the step with index 1.

Return the **minimum** cost to reach the top of the staircase, which is the position just past the last step (index `cost.length`).

### Constraints

- `2 <= cost.length <= 1000`

- `0 <= cost[i] <= 999`

### Approach and complexity

We notice that the state transition equation for $f[i]$ only depends on $f[i - 1]$ and $f[i - 2]$. Therefore, we can use two variables $f$ and $g$ to alternately record the values of $f[i - 2]$ and $f[i - 1]$, thus optimizing the space complexity to $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int f = 0, g = 0;
        for (int i = 2; i <= cost.size(); ++i) {
            int gg = min(f + cost[i - 2], g + cost[i - 1]);
            f = g;
            g = gg;
        }
        return g;
    }
};
```

---

<a id="lc-213"></a>
## 15. LC 213 — House Robber II (Medium)

[Official problem](https://leetcode.com/problems/house-robber-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0213.House%20Robber%20II/README_EN.md)

### Problem description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police**.

### Constraints

- `1 <= nums.length <= 100`

- `0 <= nums[i] <= 1000`

### Approach and complexity

The circular arrangement means that at most one of the first and last houses can be chosen for theft, so this circular arrangement problem can be reduced to two single-row house problems.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        return max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }

    int robRange(vector<int>& nums, int l, int r) {
        int f = 0, g = 0;
        for (; l <= r; ++l) {
            int ff = max(f, g);
            g = f + nums[l];
            f = ff;
        }
        return max(f, g);
    }
};
```

---

<a id="lc-337"></a>
## 16. LC 337 — House Robber III (Medium)

[Official problem](https://leetcode.com/problems/house-robber-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0337.House%20Robber%20III/README_EN.md)

### Problem description

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called `root`.

Besides the `root`, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if **two directly-linked houses were broken into on the same night**.

Given the `root` of the binary tree, return the maximum amount of money the thief can rob **without alerting the police**.

### Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.

- `0 <= Node.val <= 10^4`

### Approach and complexity

For each subtree return two profits: rob the root, or skip it. Robbing forces both children to be skipped; skipping permits the best choice for each child.

Time O(n); auxiliary space O(h) including the recursion stack.

### C++20 solution

```cpp
class Solution {
public:
    int rob(TreeNode* root) {
        function<pair<int, int>(TreeNode*)> dfs = [&](TreeNode* root) -> pair<int, int> {
            if (!root) {
                return make_pair(0, 0);
            }
            auto [la, lb] = dfs(root->left);
            auto [ra, rb] = dfs(root->right);
            return make_pair(root->val + lb + rb, max(la, lb) + max(ra, rb));
        };
        auto [a, b] = dfs(root);
        return max(a, b);
    }
};
```

---

<a id="lc-279"></a>
## 17. LC 279 — Perfect Squares (Medium)

[Official problem](https://leetcode.com/problems/perfect-squares) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0279.Perfect%20Squares/README_EN.md)

### Problem description

Given an integer `n`, return the least number of perfect square numbers that sum to `n`.

A **perfect square** is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16` are perfect squares while `3` and `11` are not.

### Constraints

- `1 <= n <= 10^4`

### Approach and complexity

A perfect square needs one term. Remove factors of four; a remaining value congruent to seven modulo eight requires four squares (Legendre). Otherwise test whether two squares suffice; if not, Lagrange’s four-square theorem and the exclusion above guarantee exactly three.

Time O(sqrt(n)); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
    bool square(int n) {
        int root = static_cast<int>(sqrt(n));
        return root * root == n;
    }
public:
    int numSquares(int n) {
        if (square(n)) return 1;
        int reduced = n;
        while (reduced % 4 == 0) reduced /= 4;
        if (reduced % 8 == 7) return 4;
        for (int x = 1; x * x <= n; ++x) if (square(n - x * x)) return 2;
        return 3;
    }
};
```

---

<a id="lc-377"></a>
## 18. LC 377 — Combination Sum IV (Medium)

[Official problem](https://leetcode.com/problems/combination-sum-iv) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0377.Combination%20Sum%20IV/README_EN.md)

### Problem description

Given an array of **distinct** integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

The test cases are generated so that the answer can fit in a **32-bit** integer.

### Constraints

- `1 <= nums.length <= 200`

- `1 <= nums[i] <= 1000`

- All the elements of `nums` are **unique**.

- `1 <= target <= 1000`

**Follow up:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

### Approach and complexity

dp[sum] counts ordered sequences totaling sum. Choose the final value, adding dp[sum−value]. Saturate at INT_MAX to handle large intermediate counts for sums that cannot contribute to the requested target; since the final answer fits int, saturation preserves it exactly.

Time O(target·n); auxiliary space O(target). Positive candidate values make the recurrence acyclic.

### C++20 solution

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target + 1);
        dp[0] = 1;
        for (int sum = 1; sum <= target; ++sum)
            for (int x : nums) if (x <= sum)
                dp[sum] = static_cast<int>(min<long long>(INT_MAX, 1LL * dp[sum] + dp[sum - x]));
        return dp[target];
    }
};
```

---

<a id="lc-518"></a>
## 19. LC 518 — Coin Change II (Medium)

[Official problem](https://leetcode.com/problems/coin-change-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0518.Coin%20Change%20II/README_EN.md)

### Problem description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The **final** answer is **guaranteed** to fit into a signed **32-bit** integer.

### Constraints

- `1 <= coins.length <= 300`

- `1 <= coins[i] <= 5000`

- All the values of `coins` are **unique**.

- `0 <= amount <= 5000`

### Approach and complexity

For each coin, scan amounts upward, adding combinations that use that coin to combinations using only earlier coin types. This counts unordered combinations once. Saturate unused intermediate counts at INT_MAX because only the requested answer is guaranteed to fit signed int.

Time O(amount·number_of_coins); auxiliary space O(amount).

### C++20 solution

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount + 1);
        dp[0] = 1;
        for (int coin : coins)
            for (int value = coin; value <= amount; ++value)
                dp[value] = static_cast<int>(min<long long>(INT_MAX, 1LL * dp[value] + dp[value - coin]));
        return dp[amount];
    }
};
```

---

<a id="lc-494"></a>
## 20. LC 494 — Target Sum (Medium)

[Official problem](https://leetcode.com/problems/target-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0494.Target%20Sum/README_EN.md)

### Problem description

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

### Constraints

- `1 <= nums.length <= 20`

- `0 <= nums[i] <= 1000`

- `0 <= sum(nums[i]) <= 1000`

- `-1000 <= target <= 1000`

### Approach and complexity

We can observe that in the state transition equation of Solution 1, the value of $f[i][j]$ is only related to $f[i - 1][j]$ and $f[i - 1][j - \textit{nums}[i - 1]]$. Therefore, we can eliminate the first dimension of the space and use only a one-dimensional array.

The time complexity is $O(mn)$, and the space complexity is $O(n)$.

### C++20 solution

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        if (s < target || (s - target) % 2) {
            return 0;
        }
        int n = (s - target) / 2;
        vector<int> f = vector<int>(n + 1, 0);
        f[0] = 1;
        for (int x : nums) {
            for (int j = n; j >= x; --j) {
                f[j] += f[j - x];
            }
        }
        return f[n];
    }
};
```

---

<a id="lc-474"></a>
## 21. LC 474 — Ones and Zeroes (Medium)

[Official problem](https://leetcode.com/problems/ones-and-zeroes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0474.Ones%20and%20Zeroes/README_EN.md)

### Problem description

You are given an array of binary strings `strs` and two integers `m` and `n`.

Return the size of the largest subset of `strs` such that there are **at most** `m` `0`'s and `n` `1`'s in the subset.

A set `x` is a **subset** of a set `y` if all elements of `x` are also elements of `y`.

### Constraints

- `1 <= strs.length <= 600`

- `1 <= strs[i].length <= 100`

- `strs[i]` consists only of digits `'0'` and `'1'`.

- `1 <= m, n <= 100`

### Approach and complexity

We notice that the calculation of $f[i][j][k]$ only depends on $f[i-1][j][k]$ and $f[i-1][j-a][k-b]$. Therefore, we can eliminate the first dimension and optimize the space complexity to $O(mn)$.

### C++20 solution

```cpp
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> f = vector<vector<int>>(m + 1, vector<int>(n + 1, 0));
        for (auto& s : strs) {
            auto [a, b] = count(s);
            for (int i = m; i >= a; --i) {
                for (int j = n; j >= b; --j) {
                    f[i][j] = max(f[i][j], f[i - a][j - b] + 1);
                }
            }
        }
        return f[m][n];
    }

    pair<int, int> count(string& s) {
        int a = count_if(s.begin(), s.end(), [](char c) { return c == '0'; });
        return {a, s.size() - a};
    }
};
```

---

<a id="lc-1049"></a>
## 22. LC 1049 — Last Stone Weight II (Medium)

[Official problem](https://leetcode.com/problems/last-stone-weight-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1049.Last%20Stone%20Weight%20II/README_EN.md)

### Problem description

You are given an array of integers `stones` where `stones[i]` is the weight of the `i^th` stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and

- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return `0`.

### Constraints

- `1 <= stones.length <= 30`

- `1 <= stones[i] <= 100`

### Approach and complexity

$dp[i][j]$ only depends on the previous row $dp[i - 1][\cdot]$, so we can drop the first dimension and enumerate the capacity from large to small, reducing the space complexity to $O(\textit{sum})$.

### C++20 solution

```cpp
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int s = accumulate(stones.begin(), stones.end(), 0);
        int n = s >> 1;
        vector<int> dp(n + 1);
        for (int& v : stones)
            for (int j = n; j >= v; --j)
                dp[j] = max(dp[j], dp[j - v] + v);
        return s - dp[n] * 2;
    }
};
```

---

<a id="lc-221"></a>
## 23. LC 221 — Maximal Square (Medium)

[Official problem](https://leetcode.com/problems/maximal-square) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0221.Maximal%20Square/README_EN.md)

### Problem description

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.

### Constraints

- `m == matrix.length`

- `n == matrix[i].length`

- `1 <= m, n <= 300`

- `matrix[i][j]` is `'0'` or `'1'`.

### Approach and complexity

For a one-cell, the largest square ending there extends the minimum of the above, left, and upper-left squares. Zero-cells reset to zero. Save the previous diagonal while updating a single row.

Time O(mn); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        vector<int> dp(matrix[0].size() + 1);
        int best = 0;
        for (const auto& row : matrix) {
            int diagonal = 0;
            for (int j = 1; j <= static_cast<int>(row.size()); ++j) {
                int above = dp[j];
                dp[j] = row[j - 1] == '1' ? 1 + min({dp[j], dp[j - 1], diagonal}) : 0;
                best = max(best, dp[j]); diagonal = above;
            }
        }
        return best * best;
    }
};
```

---

<a id="lc-120"></a>
## 24. LC 120 — Triangle (Medium)

[Official problem](https://leetcode.com/problems/triangle) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0120.Triangle/README_EN.md)

### Problem description

Given a `triangle` array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

### Constraints

- `1 <= triangle.length <= 200`

- `triangle[0].length == 1`

- `triangle[i].length == triangle[i - 1].length + 1`

- `-10^4 <= triangle[i][j] <= 10^4`

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

### Approach and complexity

We notice that the state $f[i][j]$ only depends on states $f[i + 1][j]$ and $f[i + 1][j + 1]$. Therefore, we can use a one-dimensional array instead of a two-dimensional array, reducing the space complexity from $O(n^2)$ to $O(n)$.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the number of rows in the triangle.

### C++20 solution

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> f(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            for (int j = 0; j <= i; ++j) {
                f[j] = min(f[j], f[j + 1]) + triangle[i][j];
            }
        }
        return f[0];
    }
};
```

---

<a id="lc-931"></a>
## 25. LC 931 — Minimum Falling Path Sum (Medium)

[Official problem](https://leetcode.com/problems/minimum-falling-path-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0931.Minimum%20Falling%20Path%20Sum/README_EN.md)

### Problem description

Given an `n x n` array of integers `matrix`, return the **minimum sum** of any **falling path** through `matrix`.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

### Constraints

- `n == matrix.length == matrix[i].length`

- `1 <= n <= 100`

- `-100 <= matrix[i][j] <= 100`

### Approach and complexity

Let $f[i][j]$ be the minimum falling path sum that ends at row $i$, column $j$:

$$
f[i][j] = \textit{matrix}[i][j] + \min \left\{ \begin{aligned} & f[i - 1][j - 1], & j > 0 \\ & f[i - 1][j], & 0 \leq j < n \\ & f[i - 1][j + 1], & j + 1 < n \end{aligned} \right.
$$

The answer is $\min_{0 \leq j < n} f[n - 1][j]$.

$f[i][j]$ depends only on the previous row, so we keep two arrays $f$ and $g$ of length $n$.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the side length of the matrix.

### C++20 solution

```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> f(n);
        for (auto& row : matrix) {
            auto g = f;
            for (int j = 0; j < n; ++j) {
                if (j) {
                    g[j] = min(g[j], f[j - 1]);
                }
                if (j + 1 < n) {
                    g[j] = min(g[j], f[j + 1]);
                }
                g[j] += row[j];
            }
            f = move(g);
        }
        return *min_element(f.begin(), f.end());
    }
};
```

---

<a id="lc-63"></a>
## 26. LC 63 — Unique Paths II (Medium)

[Official problem](https://leetcode.com/problems/unique-paths-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0063.Unique%20Paths%20II/README_EN.md)

### Problem description

You are given an `m x n` integer array `grid`. There is a robot initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

### Constraints

- `m == obstacleGrid.length`

- `n == obstacleGrid[i].length`

- `1 <= m, n <= 100`

- `obstacleGrid[i][j]` is `0` or `1`.

### Approach and complexity

Process cells row by row. A blocked cell resets its count to zero; an open cell adds the left count to the above count already stored at that column. The initial dp[0]=1 supplies the start unless it is blocked. Saturate intermediate counts at INT_MAX: the statement bounds only the final answer, and counts into a dead-end region can otherwise overflow.

Time O(mn); auxiliary space O(n). Saturation preserves an exact final answer whenever that answer fits int, as guaranteed.

### C++20 solution

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        vector<int> dp(grid[0].size());
        dp[0] = 1;
        for (const auto& row : grid) {
            for (int j = 0; j < static_cast<int>(row.size()); ++j) {
                if (row[j]) dp[j] = 0;
                else if (j) dp[j] = static_cast<int>(min<long long>(INT_MAX, 1LL * dp[j] + dp[j - 1]));
            }
        }
        return dp.back();
    }
};
```

---

<a id="lc-115"></a>
## 27. LC 115 — Distinct Subsequences (Hard)

[Official problem](https://leetcode.com/problems/distinct-subsequences) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0115.Distinct%20Subsequences/README_EN.md)

### Problem description

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

### Constraints

- `1 <= s.length, t.length <= 1000`

- `s` and `t` consist of English letters.

### Approach and complexity

dp[j] counts ways to form the first j target characters from the processed source. Update backward so each source character contributes once. Saturate counts at INT_MAX because the final answer is guaranteed to fit int, while counts of shorter target prefixes may exceed even 64 bits. Saturation cannot change a final count below the cap.

Time O(mn); auxiliary space O(n), n=target length.

### C++20 solution

```cpp
class Solution {
public:
    int numDistinct(string s, string t) {
        vector<int> dp(t.size() + 1);
        dp[0] = 1;
        for (char c : s)
            for (int j = t.size(); j >= 1; --j)
                if (c == t[j - 1]) dp[j] = static_cast<int>(min<long long>(INT_MAX, 1LL * dp[j] + dp[j - 1]));
        return dp.back();
    }
};
```

---

<a id="lc-97"></a>
## 28. LC 97 — Interleaving String (Medium)

[Official problem](https://leetcode.com/problems/interleaving-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0097.Interleaving%20String/README_EN.md)

### Problem description

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- `s = s_1 + s_2 + ... + s_n`

- `t = t_1 + t_2 + ... + t_m`

- `|n - m| <= 1`

- The **interleaving** is `s_1 + t_1 + s_2 + t_2 + s_3 + t_3 + ...` or `t_1 + s_1 + t_2 + s_2 + t_3 + s_3 + ...`

**Note:** `a + b` is the concatenation of strings `a` and `b`.

### Constraints

- `0 <= s1.length, s2.length <= 100`

- `0 <= s3.length <= 200`

- `s1`, `s2`, and `s3` consist of lowercase English letters.

**Follow up:** Could you solve it using only `O(s2.length)` additional memory space?

### Approach and complexity

We notice that $f[i][j]$ is only related to $f[i - 1][j]$ and $f[i][j - 1]$. Therefore, we can use a rolling array to reduce the space complexity to $O(n)$. The time complexity remains $O(mn)$.

### C++20 solution

```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size(), n = s2.size();
        if (m + n != s3.size()) {
            return false;
        }
        vector<char> f = vector<char>(n + 1, 0);
        f[0] = true;
        for (int i = 0; i <= m; ++i) {
            for (int j = 0; j <= n; ++j) {
                int k = i + j - 1;
                if (i) {
                    f[j] &= s1[i - 1] == s3[k];
                }
                if (j) {
                    f[j] |= (s2[j - 1] == s3[k] && f[j - 1]);
                }
            }
        }
        return f[n];
    }
};
```

---

<a id="lc-5"></a>
## 29. LC 5 — Longest Palindromic Substring (Medium)

[Official problem](https://leetcode.com/problems/longest-palindromic-substring) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0005.Longest%20Palindromic%20Substring/README_EN.md)

### Problem description

Given a string `s`, return the longest palindromic substring in `s`.

### Constraints

- `1 <= s.length <= 1000`

- `s` consist of only digits and English letters.

### Approach and complexity

Interleave virtual separators with characters and maintain the rightmost known palindrome. Mirror radii give a safe initial radius inside that palindrome; expand only beyond known bounds. Each successful new boundary expansion advances the right boundary, giving linear total work. A virtual radius equals the palindrome length in the original string.

Time O(n); auxiliary space O(n). Center expansion uses O(1) auxiliary space but O(n²) worst-case time.

### C++20 solution

```cpp
class Solution {

    vector<int> radii(const string& s) {
        // Separators occupy even indices; characters occupy odd indices.
        int m = 2 * static_cast<int>(s.size()) + 1;
        vector<int> p(m);
        auto equal = [&](int a, int b) {
            return a % 2 == b % 2 && (a % 2 == 0 || s[a / 2] == s[b / 2]);
        };
        int center = 0, right = 0;
        for (int i = 0; i < m; ++i) {
            if (i < right) p[i] = min(right - i, p[2 * center - i]);
            while (i - p[i] - 1 >= 0 && i + p[i] + 1 < m &&
                   equal(i - p[i] - 1, i + p[i] + 1)) ++p[i];
            if (i + p[i] > right) { center = i; right = i + p[i]; }
        }
        return p;
    }

public:
    string longestPalindrome(string s) {
        auto p = radii(s);
        int center = ranges::max_element(p) - p.begin();
        return s.substr((center - p[center]) / 2, p[center]);
    }
};
```

---

<a id="lc-647"></a>
## 30. LC 647 — Palindromic Substrings (Medium)

[Official problem](https://leetcode.com/problems/palindromic-substrings) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0647.Palindromic%20Substrings/README_EN.md)

### Problem description

Given a string `s`, return the number of **palindromic substrings** in it.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

### Constraints

- `1 <= s.length <= 1000`

- `s` consists of lowercase English letters.

### Approach and complexity

Compute palindrome radii around virtual character/separator centers. At each center, (radius+1)/2 is the number of nonempty palindromes centered there; adding these counts includes each substring exactly once. Mirroring and expansion make the total radius computation linear.

Time O(n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {

    vector<int> radii(const string& s) {
        // Separators occupy even indices; characters occupy odd indices.
        int m = 2 * static_cast<int>(s.size()) + 1;
        vector<int> p(m);
        auto equal = [&](int a, int b) {
            return a % 2 == b % 2 && (a % 2 == 0 || s[a / 2] == s[b / 2]);
        };
        int center = 0, right = 0;
        for (int i = 0; i < m; ++i) {
            if (i < right) p[i] = min(right - i, p[2 * center - i]);
            while (i - p[i] - 1 >= 0 && i + p[i] + 1 < m &&
                   equal(i - p[i] - 1, i + p[i] + 1)) ++p[i];
            if (i + p[i] > right) { center = i; right = i + p[i]; }
        }
        return p;
    }

public:
    int countSubstrings(string s) {
        auto p = radii(s);
        int answer = 0;
        for (int radius : p) answer += (radius + 1) / 2;
        return answer;
    }
};
```

---

<a id="lc-516"></a>
## 31. LC 516 — Longest Palindromic Subsequence (Medium)

[Official problem](https://leetcode.com/problems/longest-palindromic-subsequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0516.Longest%20Palindromic%20Subsequence/README_EN.md)

### Problem description

Given a string `s`, find the longest palindromic **subsequence**'s length in `s`.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

### Constraints

- `1 <= s.length <= 1000`

- `s` consists only of lowercase English letters.

### Approach and complexity

Process left endpoints backward and right endpoints forward. Before updating dp[j], it holds the best subsequence for [i+1,j]; dp[j−1] holds [i,j−1]; the saved diagonal holds [i+1,j−1]. Equal endpoints add two, otherwise take the maximum.

Time O(n²); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<int> dp(n);
        for (int i = n - 1; i >= 0; --i) {
            int diagonal = 0;
            dp[i] = 1;
            for (int j = i + 1; j < n; ++j) {
                int old = dp[j];
                dp[j] = s[i] == s[j] ? diagonal + 2 : max(dp[j], dp[j - 1]);
                diagonal = old;
            }
        }
        return dp.back();
    }
};
```

---

<a id="lc-1312"></a>
## 32. LC 1312 — Minimum Insertion Steps to Make a String Palindrome (Hard)

[Official problem](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1312.Minimum%20Insertion%20Steps%20to%20Make%20a%20String%20Palindrome/README_EN.md)

### Problem description

Given a string `s`. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make `s` palindrome.

A Palindrome String is one that reads the same backward as well as forward.

### Constraints

- `1 <= s.length <= 500`

- `s` consists of lowercase English letters.

### Approach and complexity

For [i,j], matching endpoints require only the inner interval’s insertions. Otherwise insert a match for one endpoint and take one plus the smaller adjacent interval. A saved diagonal permits in-place row updates.

Time O(n²); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int minInsertions(string s) {
        int n = s.size();
        vector<int> dp(n);
        for (int i = n - 2; i >= 0; --i) {
            int diagonal = 0;
            for (int j = i + 1; j < n; ++j) {
                int old = dp[j];
                dp[j] = s[i] == s[j] ? diagonal : 1 + min(dp[j], dp[j - 1]);
                diagonal = old;
            }
        }
        return dp.back();
    }
};
```

---

<a id="lc-312"></a>
## 33. LC 312 — Burst Balloons (Hard)

[Official problem](https://leetcode.com/problems/burst-balloons) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0312.Burst%20Balloons/README_EN.md)

### Problem description

You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst the `i^th` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

### Constraints

- `n == nums.length`

- `1 <= n <= 300`

- `0 <= nums[i] <= 100`

### Approach and complexity

Let's denote the length of the array `nums` as $n$. According to the problem description, we can add a $1$ to both ends of the array `nums`, denoted as $\textit{arr}$.

Then, we define $f[i][j]$ as the maximum number of coins we can get by bursting all the balloons in the interval $[i, j]$. Therefore, the answer is $f[0][n+1]$.

For $f[i][j]$, we enumerate all positions $k$ in the interval $[i, j]$. Suppose $k$ is the last balloon to burst, then we can get the following state transition equation:

$$
f[i][j] = \max(f[i][j], f[i][k] + f[k][j] + \textit{arr}[i] \times \textit{arr}[k] \times \textit{arr}[j])
$$

In implementation, since the state transition equation of $f[i][j]$ involves $f[i][k]$ and $f[k][j]$, where $i < k < j$, we need to traverse $i$ from large to small and $j$ from small to large. This ensures that when calculating $f[i][j]$, $f[i][k]$ and $f[k][j]$ have already been calculated.

Finally, we return $f[0][n+1]$.

The time complexity is $O(n^3)$, and the space complexity is $O(n^2)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr(n + 2, 1);
        for (int i = 0; i < n; ++i) {
            arr[i + 1] = nums[i];
        }

        vector<vector<int>> f(n + 2, vector<int>(n + 2, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i + 2; j <= n + 1; ++j) {
                for (int k = i + 1; k < j; ++k) {
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j]);
                }
            }
        }
        return f[0][n + 1];
    }
};
```

---

<a id="lc-1547"></a>
## 34. LC 1547 — Minimum Cost to Cut a Stick (Hard)

[Official problem](https://leetcode.com/problems/minimum-cost-to-cut-a-stick) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1500-1599/1547.Minimum%20Cost%20to%20Cut%20a%20Stick/README_EN.md)

### Problem description

Given a wooden stick of length `n` units. The stick is labelled from `0` to `n`. For example, a stick of length **6** is labelled as follows:

![Problem illustration](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1547.Minimum%20Cost%20to%20Cut%20a%20Stick/images/statement.jpg)

Given an integer array `cuts` where `cuts[i]` denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.

### Constraints

- `2 <= n <= 10^6`

- `1 <= cuts.length <= min(n - 1, 100)`

- `1 <= cuts[i] <= n - 1`

- All the integers in `cuts` array are **distinct**.

### Approach and complexity

Add endpoints 0 and n, then dp[i][j] is the minimum cost to make all cuts strictly between them. Choosing the first cut k gives dp[i][k]+dp[k][j]+position[j]−position[i]. For this nonnegative additive interval cost, Knuth’s monotonicity restricts an optimal k to [opt[i][j−1],opt[i+1][j]], reducing total transitions to quadratic. Adjacent endpoints have cost zero.

For c cuts, time O(c²+c log c); auxiliary space O(c²).

### C++20 solution

```cpp
class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        vector<int> position = cuts;
        position.push_back(0); position.push_back(n);
        ranges::sort(position);
        int size = position.size();
        vector<vector<int>> dp(size, vector<int>(size));
        vector<vector<int>> optimum(size, vector<int>(size));
        for (int i = 0; i + 1 < size; ++i) optimum[i][i + 1] = i + 1;
        for (int gap = 2; gap < size; ++gap) {
            for (int i = 0; i + gap < size; ++i) {
                int j = i + gap;
                dp[i][j] = INT_MAX;
                int lo = max(i + 1, optimum[i][j - 1]);
                int hi = min(j - 1, optimum[i + 1][j]);
                for (int k = lo; k <= hi; ++k) {
                    int value = dp[i][k] + dp[k][j] + position[j] - position[i];
                    if (value < dp[i][j]) { dp[i][j] = value; optimum[i][j] = k; }
                }
            }
        }
        return dp[0][size - 1];
    }
};
```

---

<a id="lc-1039"></a>
## 35. LC 1039 — Minimum Score Triangulation of Polygon (Medium)

[Official problem](https://leetcode.com/problems/minimum-score-triangulation-of-polygon) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1039.Minimum%20Score%20Triangulation%20of%20Polygon/README_EN.md)

### Problem description

You have a convex `n`-sided polygon where each vertex has an integer value. You are given an integer array `values` where `values[i]` is the value of the `i^th` vertex in **clockwise order**.

**Polygon** **triangulation** is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in `n - 2` triangles.

You will **triangulate** the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all `n - 2` triangles.

Return the minimum possible score that you can achieve with some **triangulation** of the polygon.

### Constraints

- `n == values.length`

- `3 <= n <= 50`

- `1 <= values[i] <= 100`

### Approach and complexity

We can convert the memoization approach in Solution 1 into a dynamic programming approach.

Define $f[i][j]$ as the minimum score after triangulating the polygon from vertex $i$ to $j$. Initially, $f[i][j] = 0$, and the answer is $f[0][n-1]$.

For $f[i][j]$ (where $i + 1 \lt j$), we first initialize $f[i][j]$ to $\infty$.

We enumerate a vertex $k$ between $i$ and $j$, i.e., $i \lt k \lt j$. Triangulating the polygon from vertex $i$ to $j$ can be divided into two subproblems: triangulating the polygon from vertex $i$ to $k$ and triangulating the polygon from vertex $k$ to $j$. The minimum scores of these two subproblems are $f[i][k]$ and $f[k][j]$, respectively. The score of the triangle formed by vertices $i$, $j$, and $k$ is $\textit{values}[i] \times \textit{values}[k] \times \textit{values}[j]$. Thus, the minimum score for this triangulation is $f[i][k] + f[k][j] + \textit{values}[i] \times \textit{values}[k] \times \textit{values}[j]$. We take the minimum value of all possibilities, which becomes the value of $f[i][j]$.

In summary, we can derive the state transition equation:

$$
f[i][j]=
\begin{cases}
0, & i+1=j \\
\infty, & i+1<j \\
\min_{i<k<j} \{f[i][k]+f[k][j]+\textit{values}[i] \times \textit{values}[k] \times \textit{values}[j]\}, & i+1<j
\end{cases}
$$

Note that when enumerating $i$ and $j$, there are two possible enumeration strategies:

1. Enumerate $i$ from large to small and $j$ from small to large. This ensures that when calculating the state $f[i][j]$, the states $f[i][k]$ and $f[k][j]$ have already been computed.
2. Enumerate the interval length $l$ from small to large, where $3 \leq l \leq n$. Then enumerate the left endpoint $i$ of the interval, and the right endpoint can be calculated as $j = i + l - 1$. This also ensures that when calculating the larger interval $f[i][j]$, the smaller intervals $f[i][k]$ and $f[k][j]$ have already been computed.

Finally, we return $f[0][n-1]$.

The time complexity is $O(n^3)$, and the space complexity is $O(n^2)$, where $n$ is the number of vertices in the polygon.

Related problems:

- [1312. Minimum Insertion Steps to Make a String Palindrome](https://github.com/doocs/leetcode/blob/main/solution/1300-1399/1312.Minimum%20Insertion%20Steps%20to%20Make%20a%20String%20Palindrome/README.md)

### C++20 solution

```cpp
class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vector<vector<int>> f(n, vector<int>(n));
        for (int i = n - 3; i >= 0; --i) {
            for (int j = i + 2; j < n; ++j) {
                f[i][j] = 1 << 30;
                for (int k = i + 1; k < j; ++k) {
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + values[i] * values[k] * values[j]);
                }
            }
        }
        return f[0][n - 1];
    }
};
```

---

<a id="lc-309"></a>
## 36. LC 309 — Best Time to Buy and Sell Stock with Cooldown (Medium)

[Official problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0309.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20with%20Cooldown/README_EN.md)

### Problem description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### Constraints

- `1 <= prices.length <= 5000`

- `0 <= prices[i] <= 1000`

### Approach and complexity

The transition only needs the previous two days, so three variables are enough and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int f = 0, f0 = 0, f1 = -prices[0];
        for (int i = 1; i < prices.size(); ++i) {
            int g0 = max(f0, f1 + prices[i]);
            f1 = max(f1, f - prices[i]);
            f = f0;
            f0 = g0;
        }
        return f0;
    }
};
```

---

<a id="lc-714"></a>
## 37. LC 714 — Best Time to Buy and Sell Stock with Transaction Fee (Medium)

[Official problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0714.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20with%20Transaction%20Fee/README_EN.md)

### Problem description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**Note:**

- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

- The transaction fee is only charged once for each stock purchase and sale.

### Constraints

- `1 <= prices.length <= 5 * 10^4`

- `1 <= prices[i] < 5 * 10^4`

- `0 <= fee < 5 * 10^4`

### Approach and complexity

The transition only needs the previous day, so two variables are enough and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int f0 = 0, f1 = -prices[0];
        for (int i = 1; i < prices.size(); ++i) {
            int g0 = max(f0, f1 + prices[i] - fee);
            f1 = max(f1, f0 - prices[i]);
            f0 = g0;
        }
        return f0;
    }
};
```

---

<a id="lc-123"></a>
## 38. LC 123 — Best Time to Buy and Sell Stock III (Hard)

[Official problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0123.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20III/README_EN.md)

### Problem description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### Constraints

- `1 <= prices.length <= 10^5`

- `0 <= prices[i] <= 10^5`

### Approach and complexity

We define the following variables:

- `f1` represents the maximum profit after the first purchase of the stock;
- `f2` represents the maximum profit after the first sale of the stock;
- `f3` represents the maximum profit after the second purchase of the stock;
- `f4` represents the maximum profit after the second sale of the stock.

During the traversal, we directly calculate `f1`, `f2`, `f3`, `f4`. We consider that buying and selling on the same day will result in a profit of $0$, which will not affect the answer.

Finally, return `f4`.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the $\textit{prices}$ array.

### C++20 solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int f1 = -prices[0], f2 = 0, f3 = -prices[0], f4 = 0;
        for (int i = 1; i < prices.size(); ++i) {
            f1 = max(f1, -prices[i]);
            f2 = max(f2, f1 + prices[i]);
            f3 = max(f3, f2 - prices[i]);
            f4 = max(f4, f3 + prices[i]);
        }
        return f4;
    }
};
```

---

<a id="lc-188"></a>
## 39. LC 188 — Best Time to Buy and Sell Stock IV (Hard)

[Official problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0188.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20IV/README_EN.md)

### Problem description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### Constraints

- `1 <= k <= 100`

- `1 <= prices.length <= 1000`

- `0 <= prices[i] <= 1000`

### Approach and complexity

$f[i][j][k]$ depends only on the previous day, so a table of size $(k+1) \times 2$ is enough. The space complexity is $O(k)$.

### C++20 solution

```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        vector<vector<int>> f = vector<vector<int>>(k + 1, vector<int>(2, 0));
        for (int j = 1; j <= k; ++j) {
            f[j][1] = -prices[0];
        }
        for (int i = 1; i < n; ++i) {
            for (int j = k; j; --j) {
                f[j][0] = max(f[j][1] + prices[i], f[j][0]);
                f[j][1] = max(f[j - 1][0] - prices[i], f[j][1]);
            }
        }
        return f[k][0];
    }
};
```

---

<a id="lc-121"></a>
## 40. LC 121 — Best Time to Buy and Sell Stock (Easy)

[Official problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0121.Best%20Time%20to%20Buy%20and%20Sell%20Stock/README_EN.md)

### Problem description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Constraints

- `1 <= prices.length <= 10^5`

- `0 <= prices[i] <= 10^4`

### Approach and complexity

We can enumerate each element of the array $\textit{nums}$ as the selling price. Then we need to find a minimum value in front of it as the purchase price to maximize the profit.

Therefore, we use a variable $mi$ to maintain the prefix minimum value of the array $\textit{nums}$. Then we traverse the array $\textit{nums}$ and for each element $v$, calculate the difference between it and the minimum value $mi$ in front of it, and update the answer to the maximum of the difference. Then update $mi = \min(mi, v)$. Continue to traverse the array $\textit{nums}$ until the traversal ends.

Finally, return the answer.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0, mi = prices[0];
        for (int& v : prices) {
            ans = max(ans, v - mi);
            mi = min(mi, v);
        }
        return ans;
    }
};
```

---

<a id="lc-122"></a>
## 41. LC 122 — Best Time to Buy and Sell Stock II (Medium)

[Official problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0122.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II/README_EN.md)

### Problem description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can sell and buy the stock multiple times on the **same day**, ensuring you never hold more than one share of the stock.

Find and return the **maximum** profit you can achieve.

### Constraints

- `1 <= prices.length <= 3 * 10^4`

- `0 <= prices[i] <= 10^4`

### Approach and complexity

Starting from the second day, if the stock price is higher than the previous day, buy on the previous day and sell on the current day to make a profit. If the stock price is lower than the previous day, do not buy or sell. In other words, buy and sell on all rising trading days, and do not trade on all falling trading days. The final profit will be the maximum.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the $\textit{prices}$ array.

### C++20 solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        for (int i = 1; i < prices.size(); ++i) ans += max(0, prices[i] - prices[i - 1]);
        return ans;
    }
};
```

---

<a id="lc-55"></a>
## 42. LC 55 — Jump Game (Medium)

[Official problem](https://leetcode.com/problems/jump-game) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0055.Jump%20Game/README_EN.md)

### Problem description

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

### Constraints

- `1 <= nums.length <= 10^4`

- `0 <= nums[i] <= 10^5`

### Approach and complexity

We use a variable $mx$ to maintain the farthest index that can currently be reached, initially $mx = 0$.

We traverse the array from left to right. For each position $i$ we traverse, if $mx < i$, it means that the current position cannot be reached, so we directly return `false`. Otherwise, the farthest position that we can reach by jumping from position $i$ is $i+\textit{nums}[i]$, we use $i+\textit{nums}[i]$ to update the value of $mx$, that is, $mx = \max(mx, i + \textit{nums}[i])$.

At the end of the traversal, we directly return `true`.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

Similar problems:

- [45. Jump Game II](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0045.Jump%20Game%20II/README_EN.md)
- [1024. Video Stitching](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1024.Video%20Stitching/README_EN.md)
- [1326. Minimum Number of Taps to Open to Water a Garden](https://github.com/doocs/leetcode/blob/main/solution/1300-1399/1326.Minimum%20Number%20of%20Taps%20to%20Open%20to%20Water%20a%20Garden/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int mx = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (mx < i) {
                return false;
            }
            mx = max(mx, i + nums[i]);
        }
        return true;
    }
};
```

---

<a id="lc-45"></a>
## 43. LC 45 — Jump Game II (Medium)

[Official problem](https://leetcode.com/problems/jump-game-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0045.Jump%20Game%20II/README_EN.md)

### Problem description

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at index 0.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at index `i`, you can jump to any index `(i + j)` where:

- `0 <= j <= nums[i]` and

- `i + j < n`

Return the minimum number of jumps to reach index `n - 1`. The test cases are generated such that you can reach index `n - 1`.

### Constraints

- `1 <= nums.length <= 10^4`

- `0 <= nums[i] <= 1000`

- It's guaranteed that you can reach `nums[n - 1]`.

### Approach and complexity

We can use a variable $mx$ to record the farthest position that can be reached from the current position, a variable $\textit{last}$ to record the position of the last jump, and a variable $\textit{ans}$ to record the number of jumps.

Next, we traverse each position $i$ in $[0,..n - 2]$. For each position $i$, we can calculate the farthest position that can be reached from the current position through $i + \textit{nums}[i]$. We use $mx$ to record this farthest position, that is, $mx = \max(mx, i + \textit{nums}[i])$. Then, we check whether the current position has reached the boundary of the last jump, that is, $i = \textit{last}$. If it has reached, then we need to make a jump, update $\textit{last}$ to $mx$, and increase the number of jumps $\textit{ans}$ by $1$.

Finally, we return the number of jumps $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

Similar problems:

- [55. Jump Game](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0055.Jump%20Game/README_EN.md)
- [1024. Video Stitching](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1024.Video%20Stitching/README_EN.md)
- [1326. Minimum Number of Taps to Open to Water a Garden](https://github.com/doocs/leetcode/blob/main/solution/1300-1399/1326.Minimum%20Number%20of%20Taps%20to%20Open%20to%20Water%20a%20Garden/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int ans = 0, mx = 0, last = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            mx = max(mx, i + nums[i]);
            if (last == i) {
                ++ans;
                last = mx;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-673"></a>
## 44. LC 673 — Number of Longest Increasing Subsequence (Medium)

[Official problem](https://leetcode.com/problems/number-of-longest-increasing-subsequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0673.Number%20of%20Longest%20Increasing%20Subsequence/README_EN.md)

### Problem description

Given an integer array `nums`, return the number of longest increasing subsequences.

**Notice** that the sequence has to be **strictly** increasing.

### Constraints

- `1 <= nums.length <= 2000`

- `-10^6 <= nums[i] <= 10^6`

- The answer is guaranteed to fit inside a 32-bit integer.

### Approach and complexity

We can use a binary indexed tree to maintain the length and count of the longest increasing subsequence in the prefix interval. We remove duplicates from the array $\textit{nums}$ and sort it to get the array $\textit{arr}$. Then we enumerate each element $x$ in $\textit{nums}$, find the position $i$ of $x$ in the array $\textit{arr}$ by binary search, then query the length and count of the longest increasing subsequence in $[1,i-1]$, denoted as $v$ and $\textit{cnt}$, then update the length and count of the longest increasing subsequence in $[i]$ to $v+1$ and $\max(\textit{cnt},1)$. Finally, we query the length and count of the longest increasing subsequence in $[1,m]$, where $m$ is the length of the array $\textit{arr}$, which is the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class BinaryIndexedTree {
private:
    int n;
    vector<int> c;
    vector<int> d;

public:
    BinaryIndexedTree(int n)
        : n(n)
        , c(n + 1, 0)
        , d(n + 1, 0) {}

    void update(int x, int v, int cnt) {
        while (x <= n) {
            if (c[x] < v) {
                c[x] = v;
                d[x] = cnt;
            } else if (c[x] == v) {
                d[x] += cnt;
            }
            x += x & -x;
        }
    }

    pair<int, int> query(int x) {
        int v = 0, cnt = 0;
        while (x > 0) {
            if (c[x] > v) {
                v = c[x];
                cnt = d[x];
            } else if (c[x] == v) {
                cnt += d[x];
            }
            x -= x & -x;
        }
        return {v, cnt};
    }
};

class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        vector<int> arr = nums;
        ranges::sort(arr);
        arr.erase(unique(arr.begin(), arr.end()), arr.end());
        int m = arr.size();
        BinaryIndexedTree tree(m);
        for (int x : nums) {
            auto it = lower_bound(arr.begin(), arr.end(), x);
            int i = distance(arr.begin(), it) + 1;
            auto [v, cnt] = tree.query(i - 1);
            tree.update(i, v + 1, max(cnt, 1));
        }
        return tree.query(m).second;
    }
};
```

---

<a id="lc-354"></a>
## 45. LC 354 — Russian Doll Envelopes (Hard)

[Official problem](https://leetcode.com/problems/russian-doll-envelopes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0354.Russian%20Doll%20Envelopes/README_EN.md)

### Problem description

You are given a 2D array of integers `envelopes` where `envelopes[i] = [w_i, h_i]` represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

**Note:** You cannot rotate an envelope.

### Constraints

- `1 <= envelopes.length <= 10^5`

- `envelopes[i].length == 2`

- `1 <= w_i, h_i <= 10^5`

### Approach and complexity

Sort widths ascending and heights descending for equal widths. A strictly increasing subsequence of heights then corresponds exactly to nestable envelopes; equal widths cannot contribute two envelopes.

Time O(n log n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        ranges::sort(envelopes, [](const auto& e1, const auto& e2) {
            return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]);
        });
        int n = envelopes.size();
        vector<int> d{envelopes[0][1]};
        for (int i = 1; i < n; ++i) {
            int x = envelopes[i][1];
            if (x > d[d.size() - 1])
                d.push_back(x);
            else {
                int idx = lower_bound(d.begin(), d.end(), x) - d.begin();
                if (idx == d.size()) idx = 0;
                d[idx] = x;
            }
        }
        return d.size();
    }
};
```

---

<a id="lc-1235"></a>
## 46. LC 1235 — Maximum Profit in Job Scheduling (Hard)

[Official problem](https://leetcode.com/problems/maximum-profit-in-job-scheduling) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1235.Maximum%20Profit%20in%20Job%20Scheduling/README_EN.md)

### Problem description

We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

You're given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time `X` you will be able to start another job that starts at time `X`.

### Constraints

- `1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4`

- `1 <= startTime[i] < endTime[i] <= 10^9`

- `1 <= profit[i] <= 10^4`

### Approach and complexity

Solution 1 sorts by start and fills a suffix table. Here we sort by end and define a prefix table.

First, sort the jobs, this time we sort by end time in ascending order, then define $dp[i]$, which represents the maximum profit that can be obtained from the first $i$ jobs. The answer is $dp[n]$. Initialize $dp[0]=0$.

For the $i$-th job, we can choose to do it or not. If we don't do it, the maximum profit is $dp[i]$; if we do it, we can use binary search to find the last job that ends before the start time of the $i$-th job, denoted as $j$, then the maximum profit is $\textit{profit}[i] + dp[j]$. We take the larger of the two. That is:

$$
dp[i+1] = \max(dp[i], \textit{profit}[i] + dp[j])
$$

Where $j$ is the largest index that satisfies $\textit{endTime}[j] \leq \textit{startTime}[i]$.

The time complexity is $O(n \log n)$, where $n$ is the number of jobs.

Similar problems:

- [2008. Maximum Earnings From Taxi](https://github.com/doocs/leetcode/blob/main/solution/2000-2099/2008.Maximum%20Earnings%20From%20Taxi/README.md)
- [1751. Maximum Number of Events That Can Be Attended II](https://github.com/doocs/leetcode/blob/main/solution/1700-1799/1751.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended%20II/README.md)

### C++20 solution

```cpp
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = profit.size();
        vector<tuple<int, int, int>> jobs(n);
        for (int i = 0; i < n; ++i) jobs[i] = {endTime[i], startTime[i], profit[i]};
        ranges::sort(jobs);
        vector<int> dp(n + 1);
        for (int i = 0; i < n; ++i) {
            auto [_, s, p] = jobs[i];
            int j = upper_bound(jobs.begin(), jobs.begin() + i, s, [&](int x, auto& job) -> bool { return x < get<0>(job); }) - jobs.begin();
            dp[i + 1] = max(dp[i], dp[j] + p);
        }
        return dp[n];
    }
};
```

---

<a id="lc-983"></a>
## 47. LC 983 — Minimum Cost For Tickets (Medium)

[Official problem](https://leetcode.com/problems/minimum-cost-for-tickets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0983.Minimum%20Cost%20For%20Tickets/README_EN.md)

### Problem description

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array `days`. Each day is an integer from `1` to `365`.

Train tickets are sold in **three different ways**:

- a **1-day** pass is sold for `costs[0]` dollars,

- a **7-day** pass is sold for `costs[1]` dollars, and

- a **30-day** pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel.

- For example, if we get a **7-day** pass on day `2`, then we can travel for `7` days: `2`, `3`, `4`, `5`, `6`, `7`, and `8`.

Return the minimum number of dollars you need to travel every day in the given list of days.

### Constraints

- `1 <= days.length <= 365`

- `1 <= days[i] <= 365`

- `days` is in strictly increasing order.

- `costs.length == 3`

- `1 <= costs[i] <= 1000`

### Approach and complexity

Let's denote the last day in the $\textit{days}$ array as $m$. We can define an array $f$ of length $m + 1$, where $f[i]$ represents the minimum cost from day $1$ to day $i$.

We can calculate the value of $f[i]$ in increasing order of the dates in the $\textit{days}$ array, starting from day $1$. If day $i$ is a travel day, we can consider three purchasing options: buying a 1-day pass, buying a 7-day pass, and buying a 30-day pass. We calculate the cost for these three purchasing methods separately and take the minimum cost among these three as the value of $f[i]$. If day $i$ is not a travel day, then $f[i] = f[i - 1]$.

The final answer is $f[m]$.

The time complexity is $O(m)$, and the space complexity is $O(m)$, where $m$ represents the last day of travel.

### C++20 solution

```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int m = days.back();
        vector<int> f = vector<int>(m + 1, 0);
        f[0] = 0;
        int valid[3] = {1, 7, 30};
        for (int i = 1, j = 0; i <= m; ++i) {
            if (i == days[j]) {
                f[i] = INT_MAX;
                for (int k = 0; k < 3; ++k) {
                    int c = costs[k], v = valid[k];
                    f[i] = min(f[i], f[max(0, i - v)] + c);
                }
                ++j;
            } else {
                f[i] = f[i - 1];
            }
        }
        return f[m];
    }
};
```

---

<a id="lc-96"></a>
## 48. LC 96 — Unique Binary Search Trees (Medium)

[Official problem](https://leetcode.com/problems/unique-binary-search-trees) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0096.Unique%20Binary%20Search%20Trees/README_EN.md)

### Problem description

Given an integer `n`, return the number of structurally unique **BST'**s (binary search trees) which has exactly `n` nodes of unique values from `1` to `n`.

### Constraints

- `1 <= n <= 19`

### Approach and complexity

The number of binary search tree shapes is the nth Catalan number. Starting with C₀=1, use Cᵢ₊₁=Cᵢ·2(2i+1)/(i+2). Division is exact at every step. A 64-bit intermediate prevents overflow for n≤19.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int numTrees(int n) {
        long long count = 1;
        for (int i = 0; i < n; ++i) count = count * 2 * (2 * i + 1) / (i + 2);
        return static_cast<int>(count);
    }
};
```

---

<a id="lc-95"></a>
## 49. LC 95 — Unique Binary Search Trees II (Medium)

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

---

<a id="lc-10"></a>
## 50. LC 10 — Regular Expression Matching (Hard)

[Official problem](https://leetcode.com/problems/regular-expression-matching) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0010.Regular%20Expression%20Matching/README_EN.md)

### Problem description

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.​​​​

- `'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

### Constraints

- `1 <= s.length <= 20`

- `1 <= p.length <= 20`

- `s` contains only lowercase English letters.

- `p` contains only lowercase English letters, `'.'`, and `'*'`.

- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

### Approach and complexity

dp[j] means the consumed string prefix matches the first j pattern characters. For x*, either consume zero copies (current row j−2), or consume a matching character and retain x* (previous row j). Non-star tokens use the previous diagonal.

Time O(mn); auxiliary space O(n), where n is pattern length. Valid patterns never begin with *.

### C++20 solution

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int n = p.size();
        vector<bool> previous(n + 1), current(n + 1);
        previous[0] = true;
        for (int j = 2; j <= n; ++j) if (p[j - 1] == '*') previous[j] = previous[j - 2];
        for (char c : s) {
            fill(current.begin(), current.end(), false);
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '*') {
                    bool matches = p[j - 2] == '.' || p[j - 2] == c;
                    current[j] = current[j - 2] || (matches && previous[j]);
                } else current[j] = previous[j - 1] && (p[j - 1] == '.' || p[j - 1] == c);
            }
            previous.swap(current);
        }
        return previous[n];
    }
};
```
