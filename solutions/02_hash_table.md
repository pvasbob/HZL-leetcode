# 2. Hash Table — C++20 solutions

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

1. [LC 1 — Two Sum](#lc-1)
2. [LC 49 — Group Anagrams](#lc-49)
3. [LC 217 — Contains Duplicate](#lc-217)
4. [LC 242 — Valid Anagram](#lc-242)
5. [LC 128 — Longest Consecutive Sequence](#lc-128)
6. [LC 347 — Top K Frequent Elements](#lc-347)
7. [LC 560 — Subarray Sum Equals K](#lc-560)
8. [LC 3 — Longest Substring Without Repeating Characters](#lc-3)
9. [LC 36 — Valid Sudoku](#lc-36)
10. [LC 205 — Isomorphic Strings](#lc-205)
11. [LC 290 — Word Pattern](#lc-290)
12. [LC 383 — Ransom Note](#lc-383)
13. [LC 387 — First Unique Character in a String](#lc-387)
14. [LC 350 — Intersection of Two Arrays II](#lc-350)
15. [LC 349 — Intersection of Two Arrays](#lc-349)
16. [LC 202 — Happy Number](#lc-202)
17. [LC 219 — Contains Duplicate II](#lc-219)
18. [LC 454 — 4Sum II](#lc-454)
19. [LC 438 — Find All Anagrams in a String](#lc-438)
20. [LC 567 — Permutation in String](#lc-567)
21. [LC 76 — Minimum Window Substring](#lc-76)
22. [LC 146 — LRU Cache](#lc-146)
23. [LC 380 — Insert Delete GetRandom O(1)](#lc-380)
24. [LC 705 — Design HashSet](#lc-705)
25. [LC 706 — Design HashMap](#lc-706)
26. [LC 981 — Time Based Key-Value Store](#lc-981)
27. [LC 1396 — Design Underground System](#lc-1396)
28. [LC 460 — LFU Cache](#lc-460)
29. [LC 692 — Top K Frequent Words](#lc-692)
30. [LC 451 — Sort Characters By Frequency](#lc-451)
31. [LC 409 — Longest Palindrome](#lc-409)
32. [LC 594 — Longest Harmonious Subsequence](#lc-594)
33. [LC 525 — Contiguous Array](#lc-525)
34. [LC 523 — Continuous Subarray Sum](#lc-523)
35. [LC 974 — Subarray Sums Divisible by K](#lc-974)
36. [LC 930 — Binary Subarrays With Sum](#lc-930)
37. [LC 1248 — Count Number of Nice Subarrays](#lc-1248)
38. [LC 532 — K-diff Pairs in an Array](#lc-532)
39. [LC 1679 — Max Number of K-Sum Pairs](#lc-1679)
40. [LC 1207 — Unique Number of Occurrences](#lc-1207)
41. [LC 1657 — Determine if Two Strings Are Close](#lc-1657)
42. [LC 2225 — Find Players With Zero or One Losses](#lc-2225)
43. [LC 2364 — Count Number of Bad Pairs](#lc-2364)
44. [LC 1487 — Making File Names Unique](#lc-1487)
45. [LC 609 — Find Duplicate File in System](#lc-609)
46. [LC 187 — Repeated DNA Sequences](#lc-187)
47. [LC 652 — Find Duplicate Subtrees](#lc-652)
48. [LC 133 — Clone Graph](#lc-133)
49. [LC 721 — Accounts Merge](#lc-721)
50. [LC 355 — Design Twitter](#lc-355)

---

<a id="lc-1"></a>
## 1. LC 1 — Two Sum (Easy)

[Official problem](https://leetcode.com/problems/two-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0001.Two%20Sum/README_EN.md)

### Problem description

You are given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Constraints

- `2 <= nums.length <= 10^4`

- `-10^9 <= nums[i] <= 10^9`

- `-10^9 <= target <= 10^9`

- **Only one valid answer exists.**

**Follow-up: **Can you come up with an algorithm that is less than `O(n^2)` time complexity?

### Approach and complexity

We can use a hash table $d$ to store each element and its corresponding index.

Traverse the array $\textit{nums}$, for the current element $\textit{nums}[i]$, we first check if $\textit{target} - \textit{nums}[i]$ is in the hash table $d$. If it is in $d$, it means the $\textit{target}$ value has been found, and we return the indices of $\textit{target} - \textit{nums}[i]$ and $i$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> d;
        for (int i = 0;; ++i) {
            int x = nums[i];
            int y = target - x;
            if (d.contains(y)) {
                return {d[y], i};
            }
            d[x] = i;
        }
    }
};
```

---

<a id="lc-49"></a>
## 2. LC 49 — Group Anagrams (Medium)

[Official problem](https://leetcode.com/problems/group-anagrams) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0049.Group%20Anagrams/README_EN.md)

### Problem description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

### Constraints

- `1 <= strs.length <= 10^4`

- `0 <= strs[i].length <= 100`

- `strs[i]` consists of lowercase English letters.

### Approach and complexity

We can also change the sorting part in Solution 1 to counting, that is, use the characters in each string $s$ and their occurrence times as `key`, and use the string $s$ as `value` to store in the hash table.

The time complexity is $O(n(k + C))$, where $n$ and $k$ are the lengths of the string array and the maximum length of the string, respectively, and $C$ is the size of the character set. In this problem, $C = 26$.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> d;
        for (auto& s : strs) {
            int cnt[26] = {0};
            for (auto& c : s) ++cnt[c - 'a'];
            string k;
            for (int i = 0; i < 26; ++i) {
                if (cnt[i]) {
                    k += 'a' + i;
                    k += to_string(cnt[i]);
                }
            }
            d[k].emplace_back(s);
        }
        vector<vector<string>> ans;
        for (auto& [_, v] : d) ans.emplace_back(v);
        return ans;
    }
};
```

---

<a id="lc-217"></a>
## 3. LC 217 — Contains Duplicate (Easy)

[Official problem](https://leetcode.com/problems/contains-duplicate) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0217.Contains%20Duplicate/README_EN.md)

### Problem description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^9 <= nums[i] <= 10^9`

### Approach and complexity

We traverse the array and record the elements that have appeared in the hash table $s$. If an element appears for the second time, it means that there are duplicate elements in the array, and we directly return `true`.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        return s.size() < nums.size();
    }
};
```

---

<a id="lc-242"></a>
## 4. LC 242 — Valid Anagram (Easy)

[Official problem](https://leetcode.com/problems/valid-anagram) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0242.Valid%20Anagram/README_EN.md)

### Problem description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Constraints

- `1 <= s.length, t.length <= 5 * 10^4`

- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

### Approach and complexity

We first determine whether the length of the two strings is equal. If they are not equal, the characters in the two strings must be different, so return `false`.

Otherwise, we use a hash table or an array of length $26$ to record the number of times each character appears in the string $s$, and then traverse the other string $t$. Each time we traverse a character, we subtract the number of times the corresponding character appears in the hash table by one. If the number of times after subtraction is less than $0$, the number of times the character appears in the two strings is different, return `false`. If after traversing the two strings, all the character counts in the hash table are $0$, it means that the characters in the two strings appear the same number of times, return `true`.

The time complexity is $O(n)$, and the space complexity is $O(C)$, where $n$ is the length of the string; and $C$ is the size of the character set, which is $C=26$ in this problem.

### C++20 solution

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        vector<int> cnt(26);
        for (int i = 0; i < s.size(); ++i) {
            ++cnt[s[i] - 'a'];
            --cnt[t[i] - 'a'];
        }
        return all_of(cnt.begin(), cnt.end(), [](int x) { return x == 0; });
    }
};
```

---

<a id="lc-128"></a>
## 5. LC 128 — Longest Consecutive Sequence (Medium)

[Official problem](https://leetcode.com/problems/longest-consecutive-sequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0128.Longest%20Consecutive%20Sequence/README_EN.md)

### Problem description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

### Constraints

- `0 <= nums.length <= 10^5`

- `-10^9 <= nums[i] <= 10^9`

### Approach and complexity

Similar to Solution 1, we use a hash table $s$ to store all the elements in the array and a variable $\textit{ans}$ to record the length of the longest consecutive sequence. However, we no longer use a hash table $d$ to record the length of the consecutive sequence each element $x$ belongs to. During the iteration, we skip elements where $x-1$ is also in the hash table $s$. If $x-1$ is in the hash table $s$, then $x$ is definitely not the start of a consecutive sequence, so we can directly skip $x$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int ans = 0;
        for (int x : s) {
            if (!s.contains(x - 1)) {
                int y = x + 1;
                while (s.contains(y)) {
                    y++;
                }
                ans = max(ans, y - x);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-347"></a>
## 6. LC 347 — Top K Frequent Elements (Medium)

[Official problem](https://leetcode.com/problems/top-k-frequent-elements) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0347.Top%20K%20Frequent%20Elements/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^4 <= nums[i] <= 10^4`

- `k` is in the range `[1, the number of unique elements in the array]`.

- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

### Approach and complexity

Count each distinct number, then put it into the bucket indexed by its frequency. Scanning buckets from highest frequency downward emits the k most frequent numbers without sorting or heap operations.

Expected time O(n); auxiliary space O(n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency;
        for (int x : nums) ++frequency[x];
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto [value, count] : frequency) buckets[count].push_back(value);
        vector<int> answer;
        for (int count = nums.size(); count > 0; --count)
            for (int value : buckets[count]) {
                answer.push_back(value);
                if (static_cast<int>(answer.size()) == k) return answer;
            }
        return answer;
    }
};
```

---

<a id="lc-560"></a>
## 7. LC 560 — Subarray Sum Equals K (Medium)

[Official problem](https://leetcode.com/problems/subarray-sum-equals-k) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0560.Subarray%20Sum%20Equals%20K/README_EN.md)

### Problem description

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

### Constraints

- `1 <= nums.length <= 2 * 10^4`

- `-1000 <= nums[i] <= 1000`

- `-10^7 <= k <= 10^7`

### Approach and complexity

We define a hash table $\textit{cnt}$ to store the number of times the prefix sum of the array `nums` appears. Initially, we set the value of `cnt[0]` to `1`, indicating that the prefix sum `0` appears once.

We traverse the array `nums`, calculate the prefix sum `s`, then add the value of `cnt[s - k]` to the answer, and increase the value of `cnt[s]` by `1`.

After the traversal, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> cnt{{0, 1}};
        int ans = 0, s = 0;
        for (int x : nums) {
            s += x;
            ans += cnt[s - k];
            ++cnt[s];
        }
        return ans;
    }
};
```

---

<a id="lc-3"></a>
## 8. LC 3 — Longest Substring Without Repeating Characters (Medium)

[Official problem](https://leetcode.com/problems/longest-substring-without-repeating-characters) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0003.Longest%20Substring%20Without%20Repeating%20Characters/README_EN.md)

### Problem description

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

### Constraints

- `0 <= s.length <= 10^5`

- `s` consists of English letters, digits, symbols and spaces.

### Approach and complexity

We can use two pointers $l$ and $r$ to maintain a sliding window that always satisfies the condition of having no repeating characters within the window. Initially, both $l$ and $r$ point to the first character of the string. We use a hash table or an array of length $128$ called $\textit{cnt}$ to record the number of occurrences of each character, where $\textit{cnt}[c]$ represents the number of occurrences of character $c$.

Next, we move the right pointer $r$ one step at a time. Each time we move it, we increment the value of $\textit{cnt}[s[r]]$ by $1$, and then check if the value of $\textit{cnt}[s[r]]$ is greater than $1$ within the current window $[l, r]$. If it is greater than $1$, it means there are repeating characters within the current window, and we need to move the left pointer $l$ until there are no repeating characters within the window. Then, we update the answer $\textit{ans} = \max(\textit{ans}, r - l + 1)$.

Finally, we return the answer $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(|\Sigma|)$, where $n$ is the length of the string, and $\Sigma$ represents the character set, and the size of $\Sigma$ is $128$.

### C++20 solution

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int cnt[128]{};
        int ans = 0, n = s.size();
        for (int l = 0, r = 0; r < n; ++r) {
            ++cnt[s[r]];
            while (cnt[s[r]] > 1) {
                --cnt[s[l++]];
            }
            ans = max(ans, r - l + 1);
        }
        return ans;
    }
};
```

---

<a id="lc-36"></a>
## 9. LC 36 — Valid Sudoku (Medium)

[Official problem](https://leetcode.com/problems/valid-sudoku) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0036.Valid%20Sudoku/README_EN.md)

### Problem description

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

- Each row must contain the digits `1-9` without repetition.

- Each column must contain the digits `1-9` without repetition.

- Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.

- Only the filled cells need to be validated according to the mentioned rules.

### Constraints

- `board.length == 9`

- `board[i].length == 9`

- `board[i][j]` is a digit `1-9` or `'.'`.

### Approach and complexity

The valid sudoku satisfies the following three conditions:

- The digits are not repeated in each row;
- The digits are not repeated in each column;
- The digits are not repeated in each $3 \times 3$ box.

Traverse the sudoku, for each digit, check whether the row, column and $3 \times 3$ box it is in have appeared the digit. If it is, return `false`. If the traversal is over, return `true`.

The time complexity is $O(C)$, and the space complexity is $O(C)$, where $C$ is the number of empty spaces in the sudoku. In this question, $C=81$.

### C++20 solution

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<bool>> row(9, vector<bool>(9, false));
        vector<vector<bool>> col(9, vector<bool>(9, false));
        vector<vector<bool>> sub(9, vector<bool>(9, false));
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char c = board[i][j];
                if (c == '.') continue;
                int num = c - '0' - 1;
                int k = i / 3 * 3 + j / 3;
                if (row[i][num] || col[j][num] || sub[k][num]) {
                    return false;
                }
                row[i][num] = true;
                col[j][num] = true;
                sub[k][num] = true;
            }
        }
        return true;
    }
};
```

---

<a id="lc-205"></a>
## 10. LC 205 — Isomorphic Strings (Easy)

[Official problem](https://leetcode.com/problems/isomorphic-strings) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0205.Isomorphic%20Strings/README_EN.md)

### Problem description

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

### Constraints

- `1 <= s.length <= 5 * 10^4`

- `t.length == s.length`

- `s` and `t` consist of any valid ascii character.

### Approach and complexity

We can use two hash tables or arrays $d_1$ and $d_2$ to record the character mapping relationship between $s$ and $t$.

Traverse $s$ and $t$, if the corresponding character mapping relationships in $d_1$ and $d_2$ are different, return `false`, otherwise update the corresponding character mapping relationships in $d_1$ and $d_2$. After the traversal is complete, it means that $s$ and $t$ are isomorphic, and return `true`.

The time complexity is $O(n)$, and the space complexity is $O(C)$, where $n$ is the length of the string $s$; and $C$ is the size of the character set, which is $C = 256$ in this problem.

### C++20 solution

```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int d1[256]{};
        int d2[256]{};
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            char a = s[i], b = t[i];
            if (d1[a] != d2[b]) {
                return false;
            }
            d1[a] = d2[b] = i + 1;
        }
        return true;
    }
};
```

---

<a id="lc-290"></a>
## 11. LC 290 — Word Pattern (Easy)

[Official problem](https://leetcode.com/problems/word-pattern) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0290.Word%20Pattern/README_EN.md)

### Problem description

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`. Specifically:

- Each letter in `pattern` maps to **exactly** one unique word in `s`.

- Each unique word in `s` maps to **exactly** one letter in `pattern`.

- No two letters map to the same word, and no two words map to the same letter.

### Constraints

- `1 <= pattern.length <= 300`

- `pattern` contains only lower-case English letters.

- `1 <= s.length <= 3000`

- `s` contains only lowercase English letters and spaces `' '`.

- `s` **does not contain** any leading or trailing spaces.

- All the words in `s` are separated by a **single space**.

### Approach and complexity

First, we split the string $s$ into a word array $ws$ with spaces. If the length of $\textit{pattern}$ and $ws$ is not equal, return `false` directly. Otherwise, we use two hash tables $d_1$ and $d_2$ to record the correspondence between each character and word in $\textit{pattern}$ and $ws$.

Then, we traverse $\textit{pattern}$ and $ws$. For each character $a$ and word $b$, if there is a mapping for $a$ in $d_1$, and the mapped word is not $b$, or there is a mapping for $b$ in $d_2$, and the mapped character is not $a$, return `false`. Otherwise, we add the mapping of $a$ and $b$ to $d_1$ and $d_2$ respectively.

After the traversal, return `true`.

The time complexity is $O(m + n)$, and the space complexity is $O(m + n)$, where $m$ and $n$ are the length of $\textit{pattern}$ and string $s$.

### C++20 solution

```cpp
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        istringstream is(s);
        vector<string> ws;
        while (is >> s) {
            ws.push_back(s);
        }
        if (pattern.size() != ws.size()) {
            return false;
        }
        unordered_map<char, string> d1;
        unordered_map<string, char> d2;
        for (int i = 0; i < ws.size(); ++i) {
            char a = pattern[i];
            string b = ws[i];
            if ((d1.count(a) && d1[a] != b) || (d2.count(b) && d2[b] != a)) {
                return false;
            }
            d1[a] = b;
            d2[b] = a;
        }
        return true;
    }
};
```

---

<a id="lc-383"></a>
## 12. LC 383 — Ransom Note (Easy)

[Official problem](https://leetcode.com/problems/ransom-note) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0383.Ransom%20Note/README_EN.md)

### Problem description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

### Constraints

- `1 <= ransomNote.length, magazine.length <= 10^5`

- `ransomNote` and `magazine` consist of lowercase English letters.

### Approach and complexity

We can use a hash table or an array $\textit{cnt}$ of length $26$ to record the number of times each character appears in the string `magazine`. Then traverse the string `ransomNote`, for each character $c$ in it, we decrease the number of $c$ by $1$ in $\textit{cnt}$. If the number of $c$ is less than $0$ after the decrease, it means that the number of $c$ in `magazine` is not enough, so it cannot be composed of `ransomNote`, just return $\textit{false}$.

Otherwise, after the traversal, it means that each character in `ransomNote` can be found in `magazine`. Therefore, return $\textit{true}$.

The time complexity is $O(m + n)$, and the space complexity is $O(C)$, where $m$ and $n$ are the lengths of the strings $\textit{ransomNote}$ and $\textit{magazine}$ respectively; and $C$ is the size of the character set, which is $26$ in this question.

### C++20 solution

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int cnt[26]{};
        for (char& c : magazine) {
            ++cnt[c - 'a'];
        }
        for (char& c : ransomNote) {
            if (--cnt[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};
```

---

<a id="lc-387"></a>
## 13. LC 387 — First Unique Character in a String (Easy)

[Official problem](https://leetcode.com/problems/first-unique-character-in-a-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0387.First%20Unique%20Character%20in%20a%20String/README_EN.md)

### Problem description

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

### Constraints

- `1 <= s.length <= 10^5`

- `s` consists of only lowercase English letters.

### Approach and complexity

We use a hash table or an array of length $26$ $\textit{cnt}$ to store the frequency of each character. Then, we traverse each character $s[i]$ from the beginning. If $\textit{cnt}[s[i]]$ is $1$, we return $i$.

If no such character is found after the traversal, we return $-1$.

The time complexity is $O(n)$, and the space complexity is $O(|\Sigma|)$, where $n$ is the length of the string, and $\Sigma$ is the character set. In this problem, the character set consists of lowercase letters, so $|\Sigma|=26$.

### C++20 solution

```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        int cnt[26]{};
        for (char& c : s) {
            ++cnt[c - 'a'];
        }
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            if (cnt[s[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
};
```

---

<a id="lc-350"></a>
## 14. LC 350 — Intersection of Two Arrays II (Easy)

[Official problem](https://leetcode.com/problems/intersection-of-two-arrays-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0350.Intersection%20of%20Two%20Arrays%20II/README_EN.md)

### Problem description

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

### Constraints

- `1 <= nums1.length, nums2.length <= 1000`

- `0 <= nums1[i], nums2[i] <= 1000`

**Follow up:**

- What if the given array is already sorted? How would you optimize your algorithm?

- What if `nums1`'s size is small compared to `nums2`'s size? Which algorithm is better?

- What if elements of `nums2` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

### Approach and complexity

We can use a hash table $\textit{cnt}$ to count the occurrences of each element in the array $\textit{nums1}$. Then, we iterate through the array $\textit{nums2}$. If an element $x$ is in $\textit{cnt}$ and the occurrence of $x$ is greater than $0$, we add $x$ to the answer and then decrement the occurrence of $x$ by one.

After the iteration is finished, we return the answer array.

The time complexity is $O(m + n)$, and the space complexity is $O(m)$, where $m$ and $n$ are the lengths of the arrays $\textit{nums1}$ and $\textit{nums2}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> cnt;
        for (int x : nums1) {
            ++cnt[x];
        }
        vector<int> ans;
        for (int x : nums2) {
            if (cnt[x]-- > 0) {
                ans.push_back(x);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-349"></a>
## 15. LC 349 — Intersection of Two Arrays (Easy)

[Official problem](https://leetcode.com/problems/intersection-of-two-arrays) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0349.Intersection%20of%20Two%20Arrays/README_EN.md)

### Problem description

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be **unique** and you may return the result in **any order**.

### Constraints

- `1 <= nums1.length, nums2.length <= 1000`

- `0 <= nums1[i], nums2[i] <= 1000`

### Approach and complexity

First, we use a hash table or an array $s$ of length $1001$ to record the elements that appear in the array $\textit{nums1}$. Then, we iterate through each element in the array $\textit{nums2}$. If an element $x$ is in $s$, we add $x$ to the answer and remove $x$ from $s$.

After the iteration is finished, we return the answer array.

The time complexity is $O(n+m)$, and the space complexity is $O(n)$, where $n$ and $m$ are the lengths of the arrays $\textit{nums1}$ and $\textit{nums2}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        bool s[1001];
        memset(s, false, sizeof(s));
        for (int x : nums1) {
            s[x] = true;
        }
        vector<int> ans;
        for (int x : nums2) {
            if (s[x]) {
                ans.push_back(x);
                s[x] = false;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-202"></a>
## 16. LC 202 — Happy Number (Easy)

[Official problem](https://leetcode.com/problems/happy-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0202.Happy%20Number/README_EN.md)

### Problem description

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.

- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.

- Those numbers for which this process **ends in 1** are happy.

Return `true` if `n` is a happy number, and `false` if not.

### Constraints

- `1 <= n <= 2^31 - 1`

### Approach and complexity

Repeatedly replace the number by the sum of its squared digits. A repeated state is a cycle; reaching one is success. Cycle detection avoids simulating forever.

O(log n) digit work to enter a fixed bounded state space, then constant bounded work for fixed-width integers; auxiliary space O(1) under the stated bounded numeric domain.

### C++20 solution

```cpp
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> vis;
        while (n != 1 && !vis.count(n)) {
            vis.insert(n);
            int x = 0;
            for (; n; n /= 10) {
                x += (n % 10) * (n % 10);
            }
            n = x;
        }
        return n == 1;
    }
};
```

---

<a id="lc-219"></a>
## 17. LC 219 — Contains Duplicate II (Easy)

[Official problem](https://leetcode.com/problems/contains-duplicate-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0219.Contains%20Duplicate%20II/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^9 <= nums[i] <= 10^9`

- `0 <= k <= 10^5`

### Approach and complexity

We use a hash table $d$ to store the recently traversed numbers and their corresponding indices.

Traverse the array $\textit{nums}$. For the current element $\textit{nums}[i]$, if it exists in the hash table and the difference between the indices is no more than $k$, return $\textit{true}$. Otherwise, add the current element to the hash table.

After traversing, return $\textit{false}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> d;
        for (int i = 0; i < nums.size(); ++i) {
            if (d.count(nums[i]) && i - d[nums[i]] <= k) {
                return true;
            }
            d[nums[i]] = i;
        }
        return false;
    }
};
```

---

<a id="lc-454"></a>
## 18. LC 454 — 4Sum II (Medium)

[Official problem](https://leetcode.com/problems/4sum-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0454.4Sum%20II/README_EN.md)

### Problem description

Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length `n`, return the number of tuples `(i, j, k, l)` such that:

- `0 <= i, j, k, l < n`

- `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`

### Constraints

- `n == nums1.length`

- `n == nums2.length`

- `n == nums3.length`

- `n == nums4.length`

- `1 <= n <= 200`

- `-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28`

### Approach and complexity

We can add the elements $a$ and $b$ in arrays $\textit{nums1}$ and $\textit{nums2}$ respectively, and store all possible sums in a hash table $\textit{cnt}$, where the key is the sum of the two numbers, and the value is the count of the sum.

Then we iterate through the elements $c$ and $d$ in arrays $\textit{nums3}$ and $\textit{nums4}$, let $c+d$ be the target value, then the answer is the cumulative sum of $\textit{cnt}[-(c+d)]$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> cnt;
        for (int a : nums1) {
            for (int b : nums2) {
                ++cnt[a + b];
            }
        }
        int ans = 0;
        for (int c : nums3) {
            for (int d : nums4) {
                ans += cnt[-(c + d)];
            }
        }
        return ans;
    }
};
```

---

<a id="lc-438"></a>
## 19. LC 438 — Find All Anagrams in a String (Medium)

[Official problem](https://leetcode.com/problems/find-all-anagrams-in-a-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0438.Find%20All%20Anagrams%20in%20a%20String/README_EN.md)

### Problem description

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in **any order**.

### Constraints

- `1 <= s.length, p.length <= 3 * 10^4`

- `s` and `p` consist of lowercase English letters.

### Approach and complexity

Maintain counts for a fixed-length sliding window and the pattern. When their 26 frequencies match, record the window start, then slide one character.

Time O(n+m) for a fixed 26-letter alphabet; auxiliary space O(1), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int m = s.size(), n = p.size();
        vector<int> ans;
        if (m < n) {
            return ans;
        }
        vector<int> cnt1(26);
        for (char& c : p) {
            ++cnt1[c - 'a'];
        }
        vector<int> cnt2(26);
        for (int i = 0; i < n - 1; ++i) {
            ++cnt2[s[i] - 'a'];
        }
        for (int i = n - 1; i < m; ++i) {
            ++cnt2[s[i] - 'a'];
            if (cnt1 == cnt2) {
                ans.push_back(i - n + 1);
            }
            --cnt2[s[i - n + 1] - 'a'];
        }
        return ans;
    }
};
```

---

<a id="lc-567"></a>
## 20. LC 567 — Permutation in String (Medium)

[Official problem](https://leetcode.com/problems/permutation-in-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0567.Permutation%20in%20String/README_EN.md)

### Problem description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

### Constraints

- `1 <= s1.length, s2.length <= 10^4`

- `s1` and `s2` consist of lowercase English letters.

### Approach and complexity

We use an array $\textit{cnt}$ to record the characters and their counts that need to be matched, and a variable $\textit{need}$ to record the number of different characters that still need to be matched. Initially, $\textit{cnt}$ contains the character counts from the string $\textit{s1}$, and $\textit{need}$ is the number of different characters in $\textit{s1}$.

Then we traverse the string $\textit{s2}$. For each character, we decrement its corresponding value in $\textit{cnt}$. If the decremented value equals $0$, it means the current character's count in $\textit{s1}$ is satisfied, and we decrement $\textit{need}$. If the current index $i$ is greater than or equal to the length of $\textit{s1}$, we need to increment the corresponding value in $\textit{cnt}$ for $\textit{s2}[i-\textit{s1}]$. If the incremented value equals $1$, it means the current character's count in $\textit{s1}$ is no longer satisfied, and we increment $\textit{need}$. During the traversal, if the value of $\textit{need}$ equals $0$, it means all character counts are satisfied, and we have found a valid substring, so we return $\textit{true}$.

Otherwise, if the traversal ends without finding a valid substring, we return $\textit{false}$.

The time complexity is $O(m + n)$, and the space complexity is $O(|\Sigma|)$, where $m$ and $n$ are the lengths of strings $\textit{s1}$ and $\textit{s2}$, respectively, and $\Sigma$ is the character set. In this problem, the character set is lowercase letters, so the space complexity is constant.

### C++20 solution

```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int need = 0;
        int cnt[26]{};
        for (char c : s1) {
            if (++cnt[c - 'a'] == 1) {
                ++need;
            }
        }
        int m = s1.size(), n = s2.size();
        for (int i = 0; i < n; ++i) {
            int c = s2[i] - 'a';
            if (--cnt[c] == 0) {
                --need;
            }
            if (i >= m) {
                c = s2[i - m] - 'a';
                if (++cnt[c] == 1) {
                    ++need;
                }
            }
            if (need == 0) {
                return true;
            }
        }
        return false;
    }
};
```

---

<a id="lc-76"></a>
## 21. LC 76 — Minimum Window Substring (Hard)

[Official problem](https://leetcode.com/problems/minimum-window-substring) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0076.Minimum%20Window%20Substring/README_EN.md)

### Problem description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window** **substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

### Constraints

- `m == s.length`

- `n == t.length`

- `1 <= m, n <= 10^5`

- `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

### Approach and complexity

We use a hash table or array $\textit{need}$ to count the occurrences of each character in string $t$, and another hash table or array $\textit{window}$ to count the occurrences of each character in the sliding window. Additionally, we define two pointers $l$ and $r$ to point to the left and right boundaries of the window, a variable $\textit{cnt}$ to represent how many characters from $t$ are already included in the window, and variables $k$ and $mi$ to represent the starting position and length of the minimum window substring.

We traverse the string $s$ from left to right. For the current character $s[r]$:

- We add it to the window, i.e., $\textit{window}[s[r]] = \textit{window}[s[r]] + 1$. If $\textit{need}[s[r]] \geq \textit{window}[s[r]]$, it means $s[r]$ is a "necessary character", and we increment $\textit{cnt}$ by one.
- If $\textit{cnt}$ equals the length of $t$, it means the window already contains all characters from $t$, and we can try to update the starting position and length of the minimum window substring. If $r - l + 1 < mi$, it means the current window represents a shorter substring, so we update $mi = r - l + 1$ and $k = l$.
- Then, we try to move the left boundary $l$. If $\textit{need}[s[l]] \geq \textit{window}[s[l]]$, it means $s[l]$ is a "necessary character", and moving the left boundary will remove $s[l]$ from the window. Therefore, we need to decrement $\textit{cnt}$ by one, update $\textit{window}[s[l]] = \textit{window}[s[l]] - 1$, and move $l$ one position to the right.
- If $\textit{cnt}$ is not equal to the length of $t$, it means the window does not yet contain all characters from $t$, so we do not need to move the left boundary. Instead, we move $r$ one position to the right and continue traversing.

After the traversal, if no minimum window substring is found, return an empty string. Otherwise, return $s[k:k+mi]$.

The time complexity is $O(m + n)$, and the space complexity is $O(|\Sigma|)$, where $m$ and $n$ are the lengths of strings $s$ and $t$, respectively; and $|\Sigma|$ is the size of the character set, which is $128$ in this problem.

### C++20 solution

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> need(128, 0);
        vector<int> window(128, 0);
        for (char c : t) {
            ++need[c];
        }

        int m = s.length(), n = t.length();
        int k = -1, mi = m + 1, cnt = 0;

        for (int l = 0, r = 0; r < m; ++r) {
            char c = s[r];
            if (++window[c] <= need[c]) {
                ++cnt;
            }

            while (cnt == n) {
                if (r - l + 1 < mi) {
                    mi = r - l + 1;
                    k = l;
                }

                c = s[l];
                if (window[c] <= need[c]) {
                    --cnt;
                }
                --window[c];
                ++l;
            }
        }

        return k < 0 ? "" : s.substr(k, mi);
    }
};
```

---

<a id="lc-146"></a>
## 22. LC 146 — LRU Cache (Medium)

[Official problem](https://leetcode.com/problems/lru-cache) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0146.LRU%20Cache/README_EN.md)

### Problem description

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.

- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.

- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

### Constraints

- `1 <= capacity <= 3000`

- `0 <= key <= 10^4`

- `0 <= value <= 10^5`

- At most `2 * 10^5` calls will be made to `get` and `put`.

### Approach and complexity

A doubly linked list owns the cache entries in most-recent-first order. The hash map stores list iterators. splice moves a hit to the front without allocating or invalidating iterators; eviction erases the least recent item from both containers.

get/put expected O(1); persistent space O(capacity). Standard containers release all cache storage automatically.

### C++20 solution

```cpp
class LRUCache {
    size_t capacity;
    list<pair<int, int>> entries;
    unordered_map<int, list<pair<int, int>>::iterator> location;
public:
    LRUCache(int capacity) : capacity(capacity) {}
    LRUCache(const LRUCache&) = delete;
    LRUCache& operator=(const LRUCache&) = delete;
    int get(int key) {
        auto it = location.find(key);
        if (it == location.end()) return -1;
        entries.splice(entries.begin(), entries, it->second);
        return it->second->second;
    }
    void put(int key, int value) {
        if (auto it = location.find(key); it != location.end()) {
            it->second->second = value;
            entries.splice(entries.begin(), entries, it->second);
            return;
        }
        if (capacity == 0) return;
        if (entries.size() == capacity) {
            location.erase(entries.back().first);
            entries.pop_back();
        }
        entries.emplace_front(key, value);
        location[key] = entries.begin();
    }
};
```

---

<a id="lc-380"></a>
## 23. LC 380 — Insert Delete GetRandom O(1) (Medium)

[Official problem](https://leetcode.com/problems/insert-delete-getrandom-o1) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0380.Insert%20Delete%20GetRandom%20O%281%29/README_EN.md)

### Problem description

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.

- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.

- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.

- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

### Constraints

- `-2^31 <= val <= 2^31 - 1`

- At most `2 * ``10^5` calls will be made to `insert`, `remove`, and `getRandom`.

- There will be **at least one** element in the data structure when `getRandom` is called.

### Approach and complexity

Append on insertion. For deletion, move the final value into the deleted slot and update its index, then pop the vector. Uniformly sample an index with uniform_int_distribution to avoid modulo bias.

insert/remove expected amortized O(1), getRandom O(1); persistent space O(n).

### C++20 solution

```cpp
class RandomizedSet {
    vector<int> values;
    unordered_map<int, size_t> position;
    mt19937 engine{random_device{}()};
public:
    RandomizedSet() = default;
    bool insert(int val) {
        if (position.contains(val)) return false;
        position[val] = values.size();
        values.push_back(val);
        return true;
    }
    bool remove(int val) {
        auto it = position.find(val);
        if (it == position.end()) return false;
        size_t index = it->second;
        values[index] = values.back();
        position[values[index]] = index;
        values.pop_back();
        position.erase(it);
        return true;
    }
    int getRandom() {
        return values[uniform_int_distribution<size_t>(0, values.size() - 1)(engine)];
    }
};
```

---

<a id="lc-705"></a>
## 24. LC 705 — Design HashSet (Easy)

[Official problem](https://leetcode.com/problems/design-hashset) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0705.Design%20HashSet/README_EN.md)

### Problem description

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:

- `void add(key)` Inserts the value `key` into the HashSet.

- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.

- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

### Constraints

- `0 <= key <= 10^6`

- At most `10^4` calls will be made to `add`, `remove`, and `contains`.

### Approach and complexity

Directly create an array of size $1000001$, initially with each element set to `false`, indicating that the element does not exist in the hash set.

When adding an element to the hash set, set the corresponding position in the array to `true`; when deleting an element, set the corresponding position in the array to `false`; when checking if an element exists, directly return the value at the corresponding position in the array.

The time complexity of the above operations is $O(1)$.

### C++20 solution

```cpp
class MyHashSet {
public:
    bool data[1000001];

    MyHashSet() {
        memset(data, false, sizeof data);
    }

    void add(int key) {
        data[key] = true;
    }

    void remove(int key) {
        data[key] = false;
    }

    bool contains(int key) {
        return data[key];
    }
};
```

---

<a id="lc-706"></a>
## 25. LC 706 — Design HashMap (Easy)

[Official problem](https://leetcode.com/problems/design-hashmap) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0706.Design%20HashMap/README_EN.md)

### Problem description

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

- `MyHashMap()` initializes the object with an empty map.

- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.

- `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.

- `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

### Constraints

- `0 <= key, value <= 10^6`

- At most `10^4` calls will be made to `put`, `get`, and `remove`.

### Approach and complexity

The key domain is bounded by 10⁶. Direct-address storage uses the key as its index, with −1 representing no mapping.

Each operation O(1); initialization and persistent storage O(U), U=1000001.

### C++20 solution

```cpp
class MyHashMap {
public:
    int data[1000001];

    MyHashMap() {
        memset(data, -1, sizeof data);
    }

    void put(int key, int value) {
        data[key] = value;
    }

    int get(int key) {
        return data[key];
    }

    void remove(int key) {
        data[key] = -1;
    }
};
```

---

<a id="lc-981"></a>
## 26. LC 981 — Time Based Key-Value Store (Medium)

[Official problem](https://leetcode.com/problems/time-based-key-value-store) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0981.Time%20Based%20Key-Value%20Store/README_EN.md)

### Problem description

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

- `TimeMap()` Initializes the object of the data structure.

- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.

- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

### Constraints

- `1 <= key.length, value.length <= 100`

- `key` and `value` consist of lowercase English letters and digits.

- `1 <= timestamp <= 10^7`

- All the timestamps `timestamp` of `set` are strictly increasing.

- At most `2 * 10^5` calls will be made to `set` and `get`.

### Approach and complexity

We can use a hash table $\textit{kvt}$ to record key-value pairs, where the key is the string $\textit{key}$ and the value is an ordered set. Each element in the set is a tuple $(\textit{timestamp}, \textit{value})$, representing the value $\textit{value}$ corresponding to the key $\textit{key}$ at the timestamp $\textit{timestamp}$.

When we need to query the value corresponding to the key $\textit{key}$ at the timestamp $\textit{timestamp}$, we can use the ordered set to find the largest timestamp $\textit{timestamp}'$ such that $\textit{timestamp}' \leq \textit{timestamp}$, and then return the corresponding value.

In terms of time complexity, for the $\textit{set}$ operation, since the insertion operation of the hash table has a time complexity of $O(1)$, the time complexity is $O(1)$. For the $\textit{get}$ operation, since the lookup operation of the hash table has a time complexity of $O(1)$ and the lookup operation of the ordered set has a time complexity of $O(\log n)$, the time complexity is $O(\log n)$. The space complexity is $O(n)$, where $n$ is the number of $\textit{set}$ operations.

### C++20 solution

```cpp
class TimeMap {
public:
    TimeMap() {
    }

    void set(string key, string value, int timestamp) {
        ktv[key].emplace_back(timestamp, value);
    }

    string get(string key, int timestamp) {
        auto& pairs = ktv[key];
        pair<int, string> p = {timestamp, string({127})};
        auto i = upper_bound(pairs.begin(), pairs.end(), p);
        return i == pairs.begin() ? "" : (i - 1)->second;
    }

private:
    unordered_map<string, vector<pair<int, string>>> ktv;
};
```

---

<a id="lc-1396"></a>
## 27. LC 1396 — Design Underground System (Medium)

[Official problem](https://leetcode.com/problems/design-underground-system) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1396.Design%20Underground%20System/README_EN.md)

### Problem description

An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the `UndergroundSystem` class:

- `void checkIn(int id, string stationName, int t)`

- A customer with a card ID equal to `id`, checks in at the station `stationName` at time `t`.

- A customer can only be checked into one place at a time.

- `void checkOut(int id, string stationName, int t)`

- A customer with a card ID equal to `id`, checks out from the station `stationName` at time `t`.

- `double getAverageTime(string startStation, string endStation)`

- Returns the average time it takes to travel from `startStation` to `endStation`.

- The average time is computed from all the previous traveling times from `startStation` to `endStation` that happened **directly**, meaning a check in at `startStation` followed by a check out from `endStation`.

- The time it takes to travel from `startStation` to `endStation` **may be different** from the time it takes to travel from `endStation` to `startStation`.

- There will be at least one customer that has traveled from `startStation` to `endStation` before `getAverageTime` is called.

You may assume all calls to the `checkIn` and `checkOut` methods are consistent. If a customer checks in at time `t_1` then checks out at time `t_2`, then `t_1 < t_2`. All events happen in chronological order.

### Constraints

- `1 <= id, t <= 10^6`

- `1 <= stationName.length, startStation.length, endStation.length <= 10`

- All strings consist of uppercase and lowercase English letters and digits.

- There will be at most `2 * 10^4` calls **in total** to `checkIn`, `checkOut`, and `getAverageTime`.

- Answers within `10^-5` of the actual value will be accepted.

### Approach and complexity

We use two hash tables to store data:

- `ts`: Stores the passenger's id, check-in time, and check-in station. The key is the passenger's id, and the value is a tuple `(t, stationName)`.
- `d`: Stores the passenger's check-in station, check-out station, travel time, and number of trips. The key is a tuple `(startStation, endStation)`, and the value is a tuple `(totalTime, count)`.

When a passenger checks in, we store the passenger's id, check-in time, and check-in station in `ts`, i.e., `ts[id] = (t, stationName)`.

When a passenger checks out, we retrieve the passenger's check-in time and station `(t0, station)` from `ts`, then calculate the passenger's travel time $t - t_0$, and store the passenger's travel time and number of trips in `d`.

When we want to calculate a passenger's average travel time, we retrieve the passenger's total travel time and number of trips `(totalTime, count)` from `d`, then calculate the average travel time as $\textit{totalTime} / \textit{count}$.

The time complexity is $O(1)$, and the space complexity is $O(n)$, where $n$ is the number of passengers.

### C++20 solution

```cpp
class UndergroundSystem {
public:
    UndergroundSystem() {
    }

    void checkIn(int id, string stationName, int t) {
        ts[id] = {stationName, t};
    }

    void checkOut(int id, string stationName, int t) {
        auto [station, t0] = ts[id];
        auto key = station + "-" + stationName;
        auto [tot, cnt] = d[key];
        d[key] = {tot + t - t0, cnt + 1};
    }

    double getAverageTime(string startStation, string endStation) {
        auto [tot, cnt] = d[startStation + "-" + endStation];
        return (double) tot / cnt;
    }

private:
    unordered_map<int, pair<string, int>> ts;
    unordered_map<string, pair<int, int>> d;
};
```

---

<a id="lc-460"></a>
## 28. LC 460 — LFU Cache (Hard)

[Official problem](https://leetcode.com/problems/lfu-cache) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0460.LFU%20Cache/README_EN.md)

### Problem description

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the `LFUCache` class:

- `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.

- `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.

- `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** `key` would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest **use counter** is the least frequently used key.

When a key is first inserted into the cache, its **use counter** is set to `1` (due to the `put` operation). The **use counter** for a key in the cache is incremented either a `get` or `put` operation is called on it.

The functions get and put must each run in `O(1)` average time complexity.

### Constraints

- `1 <= capacity <= 10^4`

- `0 <= key <= 10^5`

- `0 <= value <= 10^9`

- At most `2 * 10^5` calls will be made to `get` and `put`.

### Approach and complexity

Each frequency has a most-recent-first list of keys. A key maps to its value, frequency, and position. Access splices its key into the next frequency list. Evict the back of the minimum-frequency list, breaking frequency ties by least recent use. Erase empty lists so storage stays bounded by capacity.

get/put expected O(1); persistent space O(capacity). No manually allocated nodes or leaked frequency buckets.

### C++20 solution

```cpp
class LFUCache {
    struct Entry { int value, frequency; list<int>::iterator position; };
    int capacity, minimum = 0;
    unordered_map<int, Entry> entries;
    unordered_map<int, list<int>> buckets;
    void touch(unordered_map<int, Entry>::iterator it) {
        int key = it->first, frequency = it->second.frequency;
        // Inserting may rehash buckets, so acquire references afterwards.
        buckets.try_emplace(frequency + 1);
        auto& from = buckets.at(frequency);
        auto& to = buckets.at(frequency + 1);
        to.splice(to.begin(), from, it->second.position);
        it->second.frequency++;
        it->second.position = to.begin();
        if (from.empty()) {
            buckets.erase(frequency);
            if (minimum == frequency) ++minimum;
        }
    }
public:
    LFUCache(int capacity) : capacity(capacity) {}
    LFUCache(const LFUCache&) = delete;
    LFUCache& operator=(const LFUCache&) = delete;
    int get(int key) {
        auto it = entries.find(key);
        if (it == entries.end()) return -1;
        touch(it);
        return it->second.value;
    }
    void put(int key, int value) {
        if (!capacity) return;
        if (auto it = entries.find(key); it != entries.end()) {
            it->second.value = value;
            touch(it);
            return;
        }
        if (static_cast<int>(entries.size()) == capacity) {
            auto& least = buckets.at(minimum);
            entries.erase(least.back());
            least.pop_back();
            if (least.empty()) buckets.erase(minimum);
        }
        auto& first = buckets[1];
        first.push_front(key);
        entries.emplace(key, Entry{value, 1, first.begin()});
        minimum = 1;
    }
};
```

---

<a id="lc-692"></a>
## 29. LC 692 — Top K Frequent Words (Medium)

[Official problem](https://leetcode.com/problems/top-k-frequent-words) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0692.Top%20K%20Frequent%20Words/README_EN.md)

### Problem description

Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.

Return the answer **sorted** by **the frequency** from highest to lowest. Sort the words with the same frequency by their **lexicographical order**.

### Constraints

- `1 <= words.length <= 500`

- `1 <= words[i].length <= 10`

- `words[i]` consists of lowercase English letters.

- `k` is in the range `[1, The number of **unique** words[i]]`

**Follow-up:** Could you solve it in `O(n log(k))` time and `O(n)` extra space?

### Approach and complexity

We can use a hash table $\textit{cnt}$ to record the frequency of each word. Then, we sort the key-value pairs in the hash table by value, and if the values are the same, we sort by key.

Finally, we take the first $k$ keys.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of words.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for (const auto& w : words) {
            ++cnt[w];
        }
        vector<string> ans;
        for (const auto& [w, _] : cnt) {
            ans.push_back(w);
        }
        ranges::sort(ans, [&](const string& a, const string& b) {
            return cnt[a] > cnt[b] || (cnt[a] == cnt[b] && a < b);
        });
        ans.resize(k);
        return ans;
    }
};
```

---

<a id="lc-451"></a>
## 30. LC 451 — Sort Characters By Frequency (Medium)

[Official problem](https://leetcode.com/problems/sort-characters-by-frequency) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0451.Sort%20Characters%20By%20Frequency/README_EN.md)

### Problem description

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

### Constraints

- `1 <= s.length <= 5 * 10^5`

- `s` consists of uppercase and lowercase English letters and digits.

### Approach and complexity

We use a hash table $\textit{cnt}$ to count the occurrences of each character in the string $s$. Then, we sort the key-value pairs in $\textit{cnt}$ in descending order by the number of occurrences. Finally, we concatenate the characters according to the sorted order.

The time complexity is $O(n + k \log k)$, and the space complexity is $O(n + k)$, where $n$ is the length of the string $s$, and $k$ is the number of distinct characters.

### C++20 solution

```cpp
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> cnt;
        for (char& c : s) {
            ++cnt[c];
        }
        vector<char> cs;
        for (auto& [c, _] : cnt) {
            cs.push_back(c);
        }
        ranges::sort(cs, [&](char& a, char& b) {
            return cnt[a] > cnt[b];
        });
        string ans;
        for (char& c : cs) {
            ans += string(cnt[c], c);
        }
        return ans;
    }
};
```

---

<a id="lc-409"></a>
## 31. LC 409 — Longest Palindrome (Easy)

[Official problem](https://leetcode.com/problems/longest-palindrome) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0409.Longest%20Palindrome/README_EN.md)

### Problem description

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

### Constraints

- `1 <= s.length <= 2000`

- `s` consists of lowercase **and/or** uppercase English letters only.

### Approach and complexity

A valid palindrome string can have at most one character that appears an odd number of times, and the rest of the characters appear an even number of times.

Therefore, we can first traverse the string $s$, count the number of occurrences of each character, and record it in an array or hash table $\textit{cnt}$.

Then, we traverse $\textit{cnt}$, for each count $v$, we divide $v$ by 2, take the integer part, multiply by 2, and add it to the answer $\textit{ans}$.

Finally, if the answer is less than the length of the string $s$, we increment the answer by one and return $\textit{ans}$.

The time complexity is $O(n + |\Sigma|)$, and the space complexity is $O(|\Sigma|)$, where $n$ is the length of the string $s$, and $|\Sigma|$ is the size of the character set. In this problem, $|\Sigma| = 128$.

### C++20 solution

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        int cnt[128]{};
        for (char c : s) {
            ++cnt[c];
        }
        int ans = 0;
        for (int v : cnt) {
            ans += v / 2 * 2;
        }
        ans += ans < s.size();
        return ans;
    }
};
```

---

<a id="lc-594"></a>
## 32. LC 594 — Longest Harmonious Subsequence (Easy)

[Official problem](https://leetcode.com/problems/longest-harmonious-subsequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0594.Longest%20Harmonious%20Subsequence/README_EN.md)

### Problem description

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly `1`.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.

### Constraints

- `1 <= nums.length <= 2 * 10^4`

- `-10^9 <= nums[i] <= 10^9`

### Approach and complexity

We can use a hash table $\textit{cnt}$ to record the occurrence count of each element in the array $\textit{nums}$. Then, we iterate through each key-value pair $(x, c)$ in the hash table. If the key $x + 1$ exists in the hash table, then the sum of occurrences of elements $x$ and $x + 1$, $c + \textit{cnt}[x + 1]$, forms a harmonious subsequence. We just need to find the maximum length among all harmonious subsequences.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> cnt;
        for (int x : nums) {
            ++cnt[x];
        }
        int ans = 0;
        for (auto& [x, c] : cnt) {
            if (cnt.contains(x + 1)) {
                ans = max(ans, c + cnt[x + 1]);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-525"></a>
## 33. LC 525 — Contiguous Array (Medium)

[Official problem](https://leetcode.com/problems/contiguous-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0525.Contiguous%20Array/README_EN.md)

### Problem description

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

### Constraints

- `1 <= nums.length <= 10^5`

- `nums[i]` is either `0` or `1`.

### Approach and complexity

According to the problem description, we can treat $0$s in the array as $-1$. In this way, when encountering a $0$, the prefix sum $s$ will decrease by one, and when encountering a $1$, the prefix sum $s$ will increase by one. Therefore, suppose the prefix sum $s$ is equal at indices $j$ and $i$, where $j < i$, then the subarray from index $j + 1$ to $i$ has an equal number of $0$s and $1$s.

We use a hash table to store all prefix sums and their first occurrence indices. Initially, we map the prefix sum of $0$ to $-1$.

As we iterate through the array, we calculate the prefix sum $s$. If $s$ is already in the hash table, then we have found a subarray with a sum of $0$, and its length is $i - d[s]$, where $d[s]$ is the index where $s$ first appeared in the hash table. If $s$ is not in the hash table, we store $s$ and its index $i$ in the hash table.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> d{{0, -1}};
        int ans = 0, s = 0;
        for (int i = 0; i < nums.size(); ++i) {
            s += nums[i] ? 1 : -1;
            if (d.contains(s)) {
                ans = max(ans, i - d[s]);
            } else {
                d[s] = i;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-523"></a>
## 34. LC 523 — Continuous Subarray Sum (Medium)

[Official problem](https://leetcode.com/problems/continuous-subarray-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0523.Continuous%20Subarray%20Sum/README_EN.md)

### Problem description

Given an integer array nums and an integer k, return `true` if `nums` has a **good subarray** or `false` otherwise.

A **good subarray** is a subarray where:

- its length is **at least two**, and

- the sum of the elements of the subarray is a multiple of `k`.

**Note** that:

- A **subarray** is a contiguous part of the array.

- An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is **always** a multiple of `k`.

### Constraints

- `1 <= nums.length <= 10^5`

- `0 <= nums[i] <= 10^9`

- `0 <= sum(nums[i]) <= 2^31 - 1`

- `1 <= k <= 2^31 - 1`

### Approach and complexity

According to the problem description, if there exist two positions $i$ and $j$ ($j < i$) where the remainders of the prefix sums modulo $k$ are the same, then the sum of the subarray $\textit{nums}[j+1..i]$ is a multiple of $k$.

Therefore, we can use a hash table to store the first occurrence of each remainder of the prefix sum modulo $k$. Initially, we store a key-value pair $(0, -1)$ in the hash table, indicating that the remainder $0$ of the prefix sum $0$ appears at position $-1$.

As we iterate through the array, we calculate the current prefix sum's remainder modulo $k$. If the current prefix sum's remainder modulo $k$ has not appeared in the hash table, we store the current prefix sum's remainder modulo $k$ and its corresponding position in the hash table. Otherwise, if the current prefix sum's remainder modulo $k$ has already appeared in the hash table at position $j$, then we have found a subarray $\textit{nums}[j+1..i]$ that meets the conditions, and thus return $\textit{True}$.

After completing the iteration, if no subarray meeting the conditions is found, we return $\textit{False}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> d{{0, -1}};
        int s = 0;
        for (int i = 0; i < nums.size(); ++i) {
            s = (s + nums[i]) % k;
            if (!d.contains(s)) {
                d[s] = i;
            } else if (i - d[s] > 1) {
                return true;
            }
        }
        return false;
    }
};
```

---

<a id="lc-974"></a>
## 35. LC 974 — Subarray Sums Divisible by K (Medium)

[Official problem](https://leetcode.com/problems/subarray-sums-divisible-by-k) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0974.Subarray%20Sums%20Divisible%20by%20K/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `k`, return the number of non-empty **subarrays** that have a sum divisible by `k`.

A **subarray** is a **contiguous** part of an array.

### Constraints

- `1 <= nums.length <= 3 * 10^4`

- `-10^4 <= nums[i] <= 10^4`

- `2 <= k <= 10^4`

### Approach and complexity

Suppose there exists $i \leq j$ such that the sum of $\textit{nums}[i,..j]$ is divisible by $k$. If we let $s_i$ represent the sum of $\textit{nums}[0,..i]$ and $s_j$ represent the sum of $\textit{nums}[0,..j]$, then $s_j - s_i$ is divisible by $k$, i.e., $(s_j - s_i) \bmod k = 0$, which means $s_j \bmod k = s_i \bmod k$. Therefore, we can use a hash table to count the number of prefix sums modulo $k$, allowing us to quickly determine if there exists a subarray that meets the condition.

We use a hash table $\textit{cnt}$ to count the number of prefix sums modulo $k$, where $\textit{cnt}[i]$ represents the number of prefix sums with a modulo $k$ value of $i$. Initially, $\textit{cnt}[0] = 1$. We use a variable $s$ to represent the prefix sum, initially $s = 0$.

Next, we traverse the array $\textit{nums}$ from left to right. For each element $x$, we calculate $s = (s + x) \bmod k$, then update the answer $\textit{ans} = \textit{ans} + \textit{cnt}[s]$, where $\textit{cnt}[s]$ represents the number of prefix sums with a modulo $k$ value of $s$. Finally, we increment the value of $\textit{cnt}[s]$ by $1$ and continue to the next element.

In the end, we return the answer $\textit{ans}$.

> Note: Since the value of $s$ can be negative, we can add $k$ to the result of $s \bmod k$ and then take modulo $k$ again to ensure that the value of $s$ is non-negative.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> cnt{{0, 1}};
        int ans = 0, s = 0;
        for (int& x : nums) {
            s = ((s + x) % k + k) % k;
            ans += cnt[s]++;
        }
        return ans;
    }
};
```

---

<a id="lc-930"></a>
## 36. LC 930 — Binary Subarrays With Sum (Medium)

[Official problem](https://leetcode.com/problems/binary-subarrays-with-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0930.Binary%20Subarrays%20With%20Sum/README_EN.md)

### Problem description

Given a binary array `nums` and an integer `goal`, return the number of non-empty **subarrays** with a sum `goal`.

A **subarray** is a contiguous part of the array.

### Constraints

- `1 <= nums.length <= 3 * 10^4`

- `nums[i]` is either `0` or `1`.

- `0 <= goal <= nums.length`

### Approach and complexity

Use two sliding windows: one excludes sums greater than goal and the other excludes sums at least goal. The difference in left boundaries counts starts producing exactly goal for each right endpoint.

Time O(n); auxiliary space O(1). Nonnegative binary values are essential.

### C++20 solution

```cpp
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int i1 = 0, i2 = 0, s1 = 0, s2 = 0, j = 0, ans = 0;
        int n = nums.size();
        while (j < n) {
            s1 += nums[j];
            s2 += nums[j];
            while (i1 <= j && s1 > goal) s1 -= nums[i1++];
            while (i2 <= j && s2 >= goal) s2 -= nums[i2++];
            ans += i2 - i1;
            ++j;
        }
        return ans;
    }
};
```

---

<a id="lc-1248"></a>
## 37. LC 1248 — Count Number of Nice Subarrays (Medium)

[Official problem](https://leetcode.com/problems/count-number-of-nice-subarrays) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1248.Count%20Number%20of%20Nice%20Subarrays/README_EN.md)

### Problem description

Given an array of integers `nums` and an integer `k`. A continuous subarray is called **nice** if there are `k` odd numbers on it.

Return the number of **nice** sub-arrays.

### Constraints

- `1 <= nums.length <= 50000`

- `1 <= nums[i] <= 10^5`

- `1 <= k <= nums.length`

### Approach and complexity

The problem asks for the number of subarrays that contain exactly $k$ odd numbers. We can calculate the number of odd numbers $t$ in each prefix array and record it in an array or hash table $\textit{cnt}$. For each prefix array, we only need to find the number of prefix arrays with $t-k$ odd numbers, which is the number of subarrays ending with the current prefix array.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> cnt(n + 1);
        cnt[0] = 1;
        int ans = 0, t = 0;
        for (int& v : nums) {
            t += v & 1;
            if (t - k >= 0) {
                ans += cnt[t - k];
            }
            cnt[t]++;
        }
        return ans;
    }
};
```

---

<a id="lc-532"></a>
## 38. LC 532 — K-diff Pairs in an Array (Medium)

[Official problem](https://leetcode.com/problems/k-diff-pairs-in-an-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0532.K-diff%20Pairs%20in%20an%20Array/README_EN.md)

### Problem description

Given an array of integers `nums` and an integer `k`, return the number of unique k-diff pairs in the array.

A **k-diff** pair is an integer pair `(nums[i], nums[j])`, where the following are true:

- `0 <= i, j < nums.length`

- `i != j`

- `|nums[i] - nums[j]| == k`

**Notice** that `|val|` denotes the absolute value of `val`.

### Constraints

- `1 <= nums.length <= 10^4`

- `-10^7 <= nums[i] <= 10^7`

- `0 <= k <= 10^7`

### Approach and complexity

Since $k$ is a fixed value, we can use a hash table $\textit{ans}$ to record the smaller value of the pairs, which allows us to determine the larger value. Finally, we return the size of $\textit{ans}$ as the answer.

We traverse the array $\textit{nums}$. For the current number $x$, we use a hash table $\textit{vis}$ to record all the numbers that have been traversed. If $x-k$ is in $\textit{vis}$, we add $x-k$ to $\textit{ans}$. If $x+k$ is in $\textit{vis}$, we add $x$ to $\textit{ans}$. Then, we add $x$ to $\textit{vis}$. Continue traversing the array $\textit{nums}$ until the end.

Finally, we return the size of $\textit{ans}$ as the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_set<int> ans, vis;
        for (int x : nums) {
            if (vis.count(x - k)) {
                ans.insert(x - k);
            }
            if (vis.count(x + k)) {
                ans.insert(x);
            }
            vis.insert(x);
        }
        return ans.size();
    }
};
```

---

<a id="lc-1679"></a>
## 39. LC 1679 — Max Number of K-Sum Pairs (Medium)

[Official problem](https://leetcode.com/problems/max-number-of-k-sum-pairs) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1679.Max%20Number%20of%20K-Sum%20Pairs/README_EN.md)

### Problem description

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^9`

- `1 <= k <= 10^9`

### Approach and complexity

We use a hash table $\textit{cnt}$ to record the current remaining integers and their occurrence counts.

We iterate over $\textit{nums}$. For the current integer $x$, we check if $k - x$ is in $\textit{cnt}$. If it exists, it means that we have found two integers whose sum is $k$. We increment the answer and then decrement the occurrence count of $k - x$; otherwise, we increment the occurrence count of $x$.

After the iteration ends, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        int ans = 0;
        for (int& x : nums) {
            if (cnt[k - x]) {
                --cnt[k - x];
                ++ans;
            } else {
                ++cnt[x];
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1207"></a>
## 40. LC 1207 — Unique Number of Occurrences (Easy)

[Official problem](https://leetcode.com/problems/unique-number-of-occurrences) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1207.Unique%20Number%20of%20Occurrences/README_EN.md)

### Problem description

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique** or `false` otherwise.

### Constraints

- `1 <= arr.length <= 1000`

- `-1000 <= arr[i] <= 1000`

### Approach and complexity

We use a hash table $\textit{cnt}$ to count the frequency of each number in the array $\textit{arr}$, and then use another hash table $\textit{vis}$ to count the types of frequencies. Finally, we check whether the sizes of $\textit{cnt}$ and $\textit{vis}$ are equal.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{arr}$.

### C++20 solution

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> cnt;
        for (int& x : arr) {
            ++cnt[x];
        }
        unordered_set<int> vis;
        for (auto& [_, v] : cnt) {
            if (vis.count(v)) {
                return false;
            }
            vis.insert(v);
        }
        return true;
    }
};
```

---

<a id="lc-1657"></a>
## 41. LC 1657 — Determine if Two Strings Are Close (Medium)

[Official problem](https://leetcode.com/problems/determine-if-two-strings-are-close) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1657.Determine%20if%20Two%20Strings%20Are%20Close/README_EN.md)

### Problem description

Two strings are considered **close** if you can attain one from the other using the following operations:

- Operation 1: Swap any two **existing** characters.

- For example, `abcde -> aecdb`

- Operation 2: Transform **every** occurrence of one **existing** character into another **existing** character, and do the same with the other character.

- For example, `aacabb -> bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` if `word1` and `word2` are **close**, and `false` otherwise.

### Constraints

- `1 <= word1.length, word2.length <= 10^5`

- `word1` and `word2` contain only lowercase English letters.

### Approach and complexity

According to the problem description, two strings are close if they meet the following two conditions simultaneously:

1. The strings `word1` and `word2` must contain the same types of letters.
2. The arrays obtained by sorting the counts of all characters in `word1` and `word2` must be the same.

Therefore, we can first use an array or hash table to count the occurrences of each letter in `word1` and `word2` respectively, and then compare whether they are the same. If they are not the same, return `false` early.

Otherwise, we sort the corresponding counts, and then compare whether the counts at the corresponding positions are the same. If they are not the same, return `false`.

At the end of the traversal, return `true`.

The time complexity is $O(m + n + C \log C)$, and the space complexity is $O(C)$, where $m$ and $n$ are the lengths of the strings $\textit{word1}$ and $\textit{word2}$ respectively, and $C$ is the number of letter types. In this problem, $C=26$.

### C++20 solution

```cpp
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        int cnt1[26]{};
        int cnt2[26]{};
        for (char& c : word1) {
            ++cnt1[c - 'a'];
        }
        for (char& c : word2) {
            ++cnt2[c - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if ((cnt1[i] == 0) != (cnt2[i] == 0)) {
                return false;
            }
        }
        sort(cnt1, cnt1 + 26);
        sort(cnt2, cnt2 + 26);
        return equal(cnt1, cnt1 + 26, cnt2);
    }
};
```

---

<a id="lc-2225"></a>
## 42. LC 2225 — Find Players With Zero or One Losses (Medium)

[Official problem](https://leetcode.com/problems/find-players-with-zero-or-one-losses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2200-2299/2225.Find%20Players%20With%20Zero%20or%20One%20Losses/README_EN.md)

### Problem description

You are given an integer array `matches` where `matches[i] = [winner_i, loser_i]` indicates that the player `winner_i` defeated player `loser_i` in a match.

Return a list `answer` of size `2` where:

- `answer[0]` is a list of all players that have **not** lost any matches.

- `answer[1]` is a list of all players that have lost exactly **one** match.

The values in the two lists should be returned in **increasing** order.

**Note:**

- You should only consider the players that have played **at least one** match.

- The testcases will be generated such that **no** two matches will have the **same** outcome.

### Constraints

- `1 <= matches.length <= 10^5`

- `matches[i].length == 2`

- `1 <= winner_i, loser_i <= 10^5`

- `winner_i != loser_i`

- All `matches[i]` are **unique**.

### Approach and complexity

We use a hash table $\textit{cnt}$ to record the number of matches each player has lost.

Then we traverse the hash table, put the players who lost 0 matches into `ans[0]`, and put the players who lost 1 match into `ans[1]`.

Finally, we sort `ans[0]` and `ans[1]` in ascending order and return the result.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of matches.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int, int> cnt;
        for (auto& e : matches) {
            if (!cnt.contains(e[0])) {
                cnt[e[0]] = 0;
            }
            ++cnt[e[1]];
        }
        vector<vector<int>> ans(2);
        for (auto& [x, v] : cnt) {
            if (v < 2) {
                ans[v].push_back(x);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-2364"></a>
## 43. LC 2364 — Count Number of Bad Pairs (Medium)

[Official problem](https://leetcode.com/problems/count-number-of-bad-pairs) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2364.Count%20Number%20of%20Bad%20Pairs/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

Return the total number of **bad pairs** in `nums`.

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^9`

### Approach and complexity

According to the problem description, for any $i \lt j$, if $j - i \neq \textit{nums}[j] - \textit{nums}[i]$, then $(i, j)$ is a bad pair.

We can transform the equation into $i - \textit{nums}[i] \neq j - \textit{nums}[j]$. This suggests using a hash table $\textit{cnt}$ to count the occurrences of $i - \textit{nums}[i]$.

While iterating through the array, for the current element $\textit{nums}[i]$, we add $i - \textit{cnt}[i - \textit{nums}[i]]$ to the answer, and then increment the count of $i - \textit{nums}[i]$ by $1$.

Finally, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        unordered_map<int, int> cnt;
        long long ans = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int x = i - nums[i];
            ans += i - cnt[x]++;
        }
        return ans;
    }
};
```

---

<a id="lc-1487"></a>
## 44. LC 1487 — Making File Names Unique (Medium)

[Official problem](https://leetcode.com/problems/making-file-names-unique) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1400-1499/1487.Making%20File%20Names%20Unique/README_EN.md)

### Problem description

Given an array of strings `names` of size `n`. You will create `n` folders in your file system **such that**, at the `i^th` minute, you will create a folder with the name `names[i]`.

Since two files **cannot** have the same name, if you enter a folder name that was previously used, the system will have a suffix addition to its name in the form of `(k)`, where, `k` is the **smallest positive integer** such that the obtained name remains unique.

Return an array of strings of length `n` where `ans[i]` is the actual name the system will assign to the `i^th` folder when you create it.

### Constraints

- `1 <= names.length <= 5 * 10^4`

- `1 <= names[i].length <= 20`

- `names[i]` consists of lowercase English letters, digits, and/or round brackets.

### Approach and complexity

We can use a hash table $d$ to record the minimum available index for each folder name, where $d[\textit{name}] = k$ means the minimum available index for the folder $\textit{name}$ is $k$. Initially, $d$ is empty since there are no folders.

Next, we iterate through the folder names array. For each file name $\textit{name}$:

- If $\textit{name}$ is already in $d$, it means the folder $\textit{name}$ already exists, and we need to find a new folder name. We can keep trying $\textit{name}(k)$, where $k$ starts from $d[\textit{name}]$, until we find a folder name $\textit{name}(k)$ that does not exist in $d$. We add $\textit{name}(k)$ to $d$, update $d[\textit{name}]$ to $k + 1$, and then update $\textit{name}$ to $\textit{name}(k)$.
- If $\textit{name}$ is not in $d$, we can directly add $\textit{name}$ to $d$ and set $d[\textit{name}]$ to $1$.
- Then, we add $\textit{name}$ to the answer array and continue to the next file name.

After traversing all file names, we obtain the answer array.

> In the code implementation below, we directly modify the $\textit{names}$ array without using an extra answer array.

The time complexity is $O(L)$, and the space complexity is $O(L)$, where $L$ is the sum of the lengths of all file names in the $\textit{names}$ array.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> getFolderNames(vector<string>& names) {
        unordered_map<string, int> d;
        for (auto& name : names) {
            int k = d[name];
            if (k) {
                while (d[name + "(" + to_string(k) + ")"]) {
                    k++;
                }
                d[name] = k;
                name += "(" + to_string(k) + ")";
            }
            d[name] = 1;
        }
        return names;
    }
};
```

---

<a id="lc-609"></a>
## 45. LC 609 — Find Duplicate File in System (Medium)

[Official problem](https://leetcode.com/problems/find-duplicate-file-in-system) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0609.Find%20Duplicate%20File%20in%20System/README_EN.md)

### Problem description

Given a list `paths` of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in **any order**.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

- `"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"`

It means there are `n` files `(f1.txt, f2.txt ... fn.txt)` with content `(f1_content, f2_content ... fn_content)` respectively in the directory "`root/d1/d2/.../dm"`. Note that `n >= 1` and `m >= 0`. If `m = 0`, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

- `"directory_path/file_name.txt"`

### Constraints

- `1 <= paths.length <= 2 * 10^4`

- `1 <= paths[i].length <= 3000`

- `1 <= sum(paths[i].length) <= 5 * 10^5`

- `paths[i]` consist of English letters, digits, `'/'`, `'.'`, `'('`, `')'`, and `' '`.

- You may assume no files or directories share the same name in the same directory.

- You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.

**Follow up:**

- Imagine you are given a real file system, how will you search files? DFS or BFS?

- If the file content is very large (GB level), how will you modify your solution?

- If you can only read the file by 1kb each time, how will you modify your solution?

- What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?

- How to make sure the duplicated files you find are not false positive?

### Approach and complexity

We create a hash table $d$, where the key is the file content and the value is a list of file paths with the same content.

Next, we iterate over $\textit{paths}$. For each path, we split it into the directory path and file information. For each file entry, we extract the file name and file content, and append the file path to the corresponding list in hash table $d$.

Finally, we return all values in hash table $d$ that have more than one file path.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of $\textit{paths}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> d;
        for (auto& p : paths) {
            auto ps = split(p, ' ');
            for (int i = 1; i < ps.size(); ++i) {
                int j = ps[i].find('(');
                auto content = ps[i].substr(j + 1, ps[i].size() - j - 2);
                auto name = ps[0] + '/' + ps[i].substr(0, j);
                d[content].push_back(name);
            }
        }
        vector<vector<string>> ans;
        for (auto& [_, e] : d) {
            if (e.size() > 1) {
                ans.push_back(e);
            }
        }
        return ans;
    }

    vector<string> split(string& s, char c) {
        vector<string> res;
        stringstream ss(s);
        string t;
        while (getline(ss, t, c)) {
            res.push_back(t);
        }
        return res;
    }
};
```

---

<a id="lc-187"></a>
## 46. LC 187 — Repeated DNA Sequences (Medium)

[Official problem](https://leetcode.com/problems/repeated-dna-sequences) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0187.Repeated%20DNA%20Sequences/README_EN.md)

### Problem description

The **DNA sequence** is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'`, and `'T'`.

- For example, `"ACGAATTCCG"` is a **DNA sequence**.

When studying **DNA**, it is useful to identify repeated sequences within the DNA.

Given a string `s` that represents a **DNA sequence**, return all the **`10`-letter-long** sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in **any order**.

### Constraints

- `1 <= s.length <= 10^5`

- `s[i]` is either `'A'`, `'C'`, `'G'`, or `'T'`.

### Approach and complexity

We define a hash table $\textit{cnt}$ to store the occurrence count of all substrings of length $10$.

We iterate through all substrings of length $10$ in the string $s$. For the current substring $t$, we update its count in the hash table. If the count of $t$ is $2$, we add it to the answer.

After the iteration, we return the answer array.

The time complexity is $O(10n)$, and the space complexity is $O(10n)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> cnt;
        vector<string> ans;
        for (int i = 0, n = s.size() - 10 + 1; i < n; ++i) {
            auto t = s.substr(i, 10);
            if (++cnt[t] == 2) {
                ans.emplace_back(t);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-652"></a>
## 47. LC 652 — Find Duplicate Subtrees (Medium)

[Official problem](https://leetcode.com/problems/find-duplicate-subtrees) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0652.Find%20Duplicate%20Subtrees/README_EN.md)

### Problem description

Given the `root` of a binary tree, return all **duplicate subtrees**.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are **duplicate** if they have the **same structure** with the **same node values**.

### Constraints

- The number of the nodes in the tree will be in the range `[1, 5000]`

- `-200 <= Node.val <= 200`

### Approach and complexity

A subtree is uniquely determined by (value,left ID,right ID), with ID zero reserved for null. Hash and intern each triple; report its root only when its count becomes two. Explicit postorder traversal avoids stack overflow on a skewed tree.

Expected time O(n); auxiliary space O(n), including traversal stack and interning.

### C++20 solution

```cpp
class Solution {
    struct Key {
        int value, left, right;
        bool operator==(const Key&) const = default;
    };
    struct Hash {
        size_t operator()(const Key& key) const {
            size_t h = hash<int>{}(key.value);
            h ^= hash<int>{}(key.left) + 0x9e3779b9U + (h << 6) + (h >> 2);
            h ^= hash<int>{}(key.right) + 0x9e3779b9U + (h << 6) + (h >> 2);
            return h;
        }
    };
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<Key, int, Hash> intern;
        unordered_map<TreeNode*, int> id;
        vector<int> count(1);
        vector<TreeNode*> result;
        vector<pair<TreeNode*, bool>> stack;
        if (root) stack.emplace_back(root, false);
        while (!stack.empty()) {
            auto [node, visited] = stack.back(); stack.pop_back();
            if (!visited) {
                stack.emplace_back(node, true);
                if (node->right) stack.emplace_back(node->right, false);
                if (node->left) stack.emplace_back(node->left, false);
            } else {
                Key key{node->val, node->left ? id.at(node->left) : 0, node->right ? id.at(node->right) : 0};
                auto [it, inserted] = intern.try_emplace(key, count.size());
                if (inserted) count.push_back(0);
                id[node] = it->second;
                if (++count[it->second] == 2) result.push_back(node);
            }
        }
        return result;
    }
};
```

---

<a id="lc-133"></a>
## 48. LC 133 — Clone Graph (Medium)

[Official problem](https://leetcode.com/problems/clone-graph) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0133.Clone%20Graph/README_EN.md)

### Problem description

Given a reference of a node in a **connected** undirected graph.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

class Node {
public int val;
public List<Node> neighbors;
}

**Test case format:**

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

### Constraints

- The number of nodes in the graph is in the range `[0, 100]`.

- `1 <= Node.val <= 100`

- `Node.val` is unique for each node.

- There are no repeated edges and no self-loops in the graph.

- The Graph is connected and all nodes can be visited starting from the given node.

### Approach and complexity

We use a hash table $g$ to record the correspondence between each node in the original graph and its copy, and then perform depth-first search.

We define the function $\textit{dfs}(\textit{node})$, which returns the copy of the $\textit{node}$. The process of $\textit{dfs}(\textit{node})$ is as follows:

- If $\textit{node}$ is $\textit{null}$, then the return value of $\textit{dfs}(\textit{node})$ is $\textit{null}$.
- If $\textit{node}$ is in $g$, then the return value of $\textit{dfs}(\textit{node})$ is $g[\textit{node}]$.
- Otherwise, we create a new node $\textit{cloned}$ and set the value of $g[\textit{node}]$ to $\textit{cloned}$. Then, we traverse all the neighbor nodes $\textit{nxt}$ of $\textit{node}$ and add $\textit{dfs}(\textit{nxt})$ to the neighbor list of $\textit{cloned}$.
- Finally, return $\textit{cloned}$.

In the main function, we return $\textit{dfs}(\textit{node})$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes.

### C++20 solution

```cpp
class Solution {
public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> g;
        auto dfs = [&](auto&& dfs, Node* node) -> Node* {
            if (!node) {
                return nullptr;
            }
            if (g.contains(node)) {
                return g[node];
            }
            Node* cloned = new Node(node->val);
            g[node] = cloned;
            for (auto& nxt : node->neighbors) {
                cloned->neighbors.push_back(dfs(dfs, nxt));
            }
            return cloned;
        };
        return dfs(dfs, node);
    }
};
```

---

<a id="lc-721"></a>
## 49. LC 721 — Accounts Merge (Medium)

[Official problem](https://leetcode.com/problems/accounts-merge) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0721.Accounts%20Merge/README_EN.md)

### Problem description

Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are **emails** representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in **any order**.

### Constraints

- `1 <= accounts.length <= 1000`

- `2 <= accounts[i].length <= 10`

- `1 <= accounts[i][j].length <= 30`

- `accounts[i][0]` consists of English letters.

- `accounts[i][j] (for j > 0)` is a valid email.

### Approach and complexity

Based on the problem description, we can use a union-find data structure to merge accounts with the same email address. The specific steps are as follows:

First, we iterate through all the accounts. For the $i$th account, we iterate through all its email addresses. If an email address appears in the hash table $d$, we use the union-find to merge the account's index $i$ with the previously appeared account's index; otherwise, we map this email address to the account's index $i$.

Next, we iterate through all the accounts again. For the $i$th account, we use the union-find to find its root node, and then add all the email addresses of that account to the hash table $g$, where the key is the root node, and the value is the account's email addresses.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of accounts.

### C++20 solution

```cpp
class UnionFind {
public:
    UnionFind(int n) {
        p = vector<int>(n);
        size = vector<int>(n, 1);
        iota(p.begin(), p.end(), 0);
    }

    bool unite(int a, int b) {
        int pa = find(a), pb = find(b);
        if (pa == pb) {
            return false;
        }
        if (size[pa] > size[pb]) {
            p[pb] = pa;
            size[pa] += size[pb];
        } else {
            p[pa] = pb;
            size[pb] += size[pa];
        }
        return true;
    }

    int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }

private:
    vector<int> p, size;
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        UnionFind uf(n);
        unordered_map<string, int> d;
        for (int i = 0; i < n; ++i) {
            for (int j = 1; j < accounts[i].size(); ++j) {
                const string& email = accounts[i][j];
                if (d.find(email) != d.end()) {
                    uf.unite(i, d[email]);
                } else {
                    d[email] = i;
                }
            }
        }
        unordered_map<int, set<string>> g;
        for (int i = 0; i < n; ++i) {
            int root = uf.find(i);
            g[root].insert(accounts[i].begin() + 1, accounts[i].end());
        }
        vector<vector<string>> ans;
        for (const auto& [root, s] : g) {
            vector<string> emails(s.begin(), s.end());
            emails.insert(emails.begin(), accounts[root][0]);
            ans.push_back(emails);
        }
        return ans;
    }
};
```

---

<a id="lc-355"></a>
## 50. LC 355 — Design Twitter (Medium)

[Official problem](https://leetcode.com/problems/design-twitter) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0355.Design%20Twitter/README_EN.md)

### Problem description

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.

Implement the `Twitter` class:

- `Twitter()` Initializes your twitter object.

- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique `tweetId`.

- `List<Integer> getNewsFeed(int userId)` Retrieves the `10` most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be **ordered from most recent to least recent**.

- `void follow(int followerId, int followeeId)` The user with ID `followerId` started following the user with ID `followeeId`.

- `void unfollow(int followerId, int followeeId)` The user with ID `followerId` started unfollowing the user with ID `followeeId`.

### Constraints

- `1 <= userId, followerId, followeeId <= 500`

- `0 <= tweetId <= 10^4`

- All the tweets have **unique** IDs.

- At most `3 * 10^4` calls will be made to `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.

- A user cannot follow himself.

### Approach and complexity

Append timestamped tweets to each author’s timeline. For a feed, put the newest tweet from the user and each followed author into a max heap, then pop at most ten tweets, replenishing from the same timeline. Hash sets make follow/unfollow expected O(1).

Let F be the number of followed authors, T stored tweets, E follow edges. postTweet amortized O(1), follow/unfollow expected O(1), getNewsFeed O(F + 10 log(F+2)) with bulk heap construction; feed auxiliary space O(F). Persistent space O(T+E).

### C++20 solution

```cpp
class Twitter {
    struct Tweet { long long time; int id; };
    unordered_map<int, vector<Tweet>> tweets;
    unordered_map<int, unordered_set<int>> follows;
    long long clock = 0;
public:
    Twitter() = default;
    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({clock++, tweetId});
    }
    vector<int> getNewsFeed(int userId) {
        using Entry = tuple<long long, int, int>; // timestamp, author, timeline index
        vector<Entry> initial;
        auto add = [&](int author) {
            auto it = tweets.find(author);
            if (it != tweets.end() && !it->second.empty()) {
                int i = static_cast<int>(it->second.size()) - 1;
                initial.emplace_back(it->second[i].time, author, i);
            }
        };
        add(userId);
        if (auto it = follows.find(userId); it != follows.end())
            for (int author : it->second) if (author != userId) add(author);
        priority_queue<Entry> heap(less<Entry>{}, move(initial));
        vector<int> result;
        while (!heap.empty() && result.size() < 10) {
            auto [time, author, i] = heap.top();
            heap.pop();
            result.push_back(tweets[author][i].id);
            if (i > 0) heap.emplace(tweets[author][i - 1].time, author, i - 1);
        }
        return result;
    }
    void follow(int followerId, int followeeId) {
        if (followerId != followeeId) follows[followerId].insert(followeeId);
    }
    void unfollow(int followerId, int followeeId) {
        if (auto it = follows.find(followerId); it != follows.end()) it->second.erase(followeeId);
    }
};
```
