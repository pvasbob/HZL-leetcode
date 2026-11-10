# 1. Array & String — C++20 solutions

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
2. [LC 3 — Longest Substring Without Repeating Characters](#lc-3)
3. [LC 238 — Product of Array Except Self](#lc-238)
4. [LC 53 — Maximum Subarray](#lc-53)
5. [LC 121 — Best Time to Buy and Sell Stock](#lc-121)
6. [LC 26 — Remove Duplicates from Sorted Array](#lc-26)
7. [LC 283 — Move Zeroes](#lc-283)
8. [LC 15 — 3Sum](#lc-15)
9. [LC 11 — Container With Most Water](#lc-11)
10. [LC 42 — Trapping Rain Water](#lc-42)
11. [LC 56 — Merge Intervals](#lc-56)
12. [LC 88 — Merge Sorted Array](#lc-88)
13. [LC 189 — Rotate Array](#lc-189)
14. [LC 75 — Sort Colors](#lc-75)
15. [LC 169 — Majority Element](#lc-169)
16. [LC 217 — Contains Duplicate](#lc-217)
17. [LC 49 — Group Anagrams](#lc-49)
18. [LC 125 — Valid Palindrome](#lc-125)
19. [LC 242 — Valid Anagram](#lc-242)
20. [LC 14 — Longest Common Prefix](#lc-14)
21. [LC 28 — Find the Index of the First Occurrence in a String](#lc-28)
22. [LC 344 — Reverse String](#lc-344)
23. [LC 151 — Reverse Words in a String](#lc-151)
24. [LC 5 — Longest Palindromic Substring](#lc-5)
25. [LC 76 — Minimum Window Substring](#lc-76)
26. [LC 438 — Find All Anagrams in a String](#lc-438)
27. [LC 567 — Permutation in String](#lc-567)
28. [LC 209 — Minimum Size Subarray Sum](#lc-209)
29. [LC 239 — Sliding Window Maximum](#lc-239)
30. [LC 560 — Subarray Sum Equals K](#lc-560)
31. [LC 152 — Maximum Product Subarray](#lc-152)
32. [LC 41 — First Missing Positive](#lc-41)
33. [LC 31 — Next Permutation](#lc-31)
34. [LC 48 — Rotate Image](#lc-48)
35. [LC 54 — Spiral Matrix](#lc-54)
36. [LC 73 — Set Matrix Zeroes](#lc-73)
37. [LC 36 — Valid Sudoku](#lc-36)
38. [LC 977 — Squares of a Sorted Array](#lc-977)
39. [LC 134 — Gas Station](#lc-134)
40. [LC 55 — Jump Game](#lc-55)
41. [LC 45 — Jump Game II](#lc-45)
42. [LC 128 — Longest Consecutive Sequence](#lc-128)
43. [LC 347 — Top K Frequent Elements](#lc-347)
44. [LC 18 — 4Sum](#lc-18)
45. [LC 16 — 3Sum Closest](#lc-16)
46. [LC 27 — Remove Element](#lc-27)
47. [LC 80 — Remove Duplicates from Sorted Array II](#lc-80)
48. [LC 443 — String Compression](#lc-443)
49. [LC 394 — Decode String](#lc-394)
50. [LC 8 — String to Integer (atoi)](#lc-8)

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

<a id="lc-3"></a>
## 2. LC 3 — Longest Substring Without Repeating Characters (Medium)

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

<a id="lc-238"></a>
## 3. LC 238 — Product of Array Except Self (Medium)

[Official problem](https://leetcode.com/problems/product-of-array-except-self) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0238.Product%20of%20Array%20Except%20Self/README_EN.md)

### Problem description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

### Constraints

- `2 <= nums.length <= 10^5`

- `-30 <= nums[i] <= 30`

- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

### Approach and complexity

We define two variables $\textit{left}$ and $\textit{right}$ to represent the product of all elements to the left and right of the current element, respectively. Initially, $\textit{left} = 1$ and $\textit{right} = 1$. We define an answer array $\textit{ans}$ of length $n$.

First, we traverse the array from left to right. For the $i$-th element, we update $\textit{ans}[i]$ with $\textit{left}$, then multiply $\textit{left}$ by $\textit{nums}[i]$.

Next, we traverse the array from right to left. For the $i$-th element, we update $\textit{ans}[i]$ to $\textit{ans}[i] \times \textit{right}$, then multiply $\textit{right}$ by $\textit{nums}[i]$.

After the traversal, we return the answer array $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        for (int i = 0, left = 1; i < n; ++i) {
            ans[i] = left;
            left *= nums[i];
        }
        for (int i = n - 1, right = 1; ~i; --i) {
            ans[i] *= right;
            right *= nums[i];
        }
        return ans;
    }
};
```

---

<a id="lc-53"></a>
## 4. LC 53 — Maximum Subarray (Medium)

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

<a id="lc-121"></a>
## 5. LC 121 — Best Time to Buy and Sell Stock (Easy)

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

<a id="lc-26"></a>
## 6. LC 26 — Remove Duplicates from Sorted Array (Easy)

[Official problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0026.Remove%20Duplicates%20from%20Sorted%20Array/README_EN.md)

### Problem description

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of unique elements in `nums` to be `k**​​​​​​​**`​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

**Custom Judge:**

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be **accepted**.

### Constraints

- `1 <= nums.length <= 3 * 10^4`

- `-100 <= nums[i] <= 100`

- `nums` is sorted in **non-decreasing** order.

### Approach and complexity

We use a variable $k$ to record the current length of the processed array. Initially, $k=0$ represents an empty array.

Then we traverse the array from left to right. For each element $x$ we encounter, if $k=0$ or $x \neq \textit{nums}[k-1]$, we place $x$ in the position of $\textit{nums}[k]$, and then increment $k$ by $1$. Otherwise, $x$ is the same as $\textit{nums}[k-1]$, so we skip this element. Continue to traverse until the entire array is traversed.

In this way, when the traversal ends, the first $k$ elements in $\textit{nums}$ are the answer we are looking for, and $k$ is the length of the answer.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

Supplement:

The original problem requires that the same number appear at most once. We can extend it to keep at most $k$ identical numbers.

- Since the same number can be kept at most $k$ times, we can directly keep the first $k$ elements of the original array;
- For the following numbers, the premise of being able to keep them is: the current number $x$ is compared with the last $k$th element of the previously retained numbers. If they are different, keep them, otherwise skip them.

Similar problems:

- [80. Remove Duplicates from Sorted Array II](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0080.Remove%20Duplicates%20from%20Sorted%20Array%20II/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        for (int x : nums) {
            if (k == 0 || x != nums[k - 1]) {
                nums[k++] = x;
            }
        }
        return k;
    }
};
```

---

<a id="lc-283"></a>
## 7. LC 283 — Move Zeroes (Easy)

[Official problem](https://leetcode.com/problems/move-zeroes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0283.Move%20Zeroes/README_EN.md)

### Problem description

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

### Constraints

- `1 <= nums.length <= 10^4`

- `-2^31 <= nums[i] <= 2^31 - 1`

**Follow up:** Could you minimize the total number of operations done?

### Approach and complexity

We use a pointer $k$ to record the current position to insert, initially $k = 0$.

Then we iterate through the array $\textit{nums}$, and each time we encounter a non-zero number, we swap it with $\textit{nums}[k]$ and increment $k$ by 1.

This way, we can ensure that the first $k$ elements of $\textit{nums}$ are non-zero, and their relative order is the same as in the original array.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int k = 0, n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i]) {
                swap(nums[i], nums[k++]);
            }
        }
    }
};
```

---

<a id="lc-15"></a>
## 8. LC 15 — 3Sum (Medium)

[Official problem](https://leetcode.com/problems/3sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0015.3Sum/README_EN.md)

### Problem description

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Constraints

- `3 <= nums.length <= 3000`

- `-10^5 <= nums[i] <= 10^5`

### Approach and complexity

We notice that the problem does not require us to return the triplet in order, so we might as well sort the array first, which makes it easy to skip duplicate elements.

Next, we enumerate the first element of the triplet $\textit{nums}[i]$, where $0 \leq i \lt n - 2$. For each $i$, we can find $j$ and $k$ satisfying $\textit{nums}[i] + \textit{nums}[j] + \textit{nums}[k] = 0$ by maintaining two pointers $j = i + 1$ and $k = n - 1$. In the enumeration process, we need to skip duplicate elements to avoid duplicate triplets.

The specific judgment logic is as follows:

If $i \gt 0$ and $\textit{nums}[i] = \textit{nums}[i - 1]$, it means that the element currently enumerated is the same as the previous element, we can skip it directly, because it will not produce new results.

If $\textit{nums}[i] \gt 0$, it means that the element currently enumerated is greater than $0$, so the sum of three numbers must not be equal to $0$, and the enumeration ends.

Otherwise, we let the left pointer $j = i + 1$, and the right pointer $k = n - 1$. When $j \lt k$, the loop is executed, and the sum of three numbers $x = \textit{nums}[i] + \textit{nums}[j] + \textit{nums}[k]$ is calculated and compared with $0$:

- If $x \lt 0$, it means that $\textit{nums}[j]$ is too small, we need to move $j$ to the right.
- If $x \gt 0$, it means that $\textit{nums}[k]$ is too large, we need to move $k$ to the left.
- Otherwise, it means that we have found a valid triplet, add it to the answer, move $j$ to the right, move $k$ to the left, and skip all duplicate elements to continue looking for the next valid triplet.

After the enumeration is over, we can get the answer to the triplet.

The time complexity is $O(n^2)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        ranges::sort(nums);
        vector<vector<int>> ans;
        int n = nums.size();
        for (int i = 0; i < n - 2 && nums[i] <= 0; ++i) {
            if (i && nums[i] == nums[i - 1]) {
                continue;
            }
            int j = i + 1, k = n - 1;
            while (j < k) {
                int x = nums[i] + nums[j] + nums[k];
                if (x < 0) {
                    ++j;
                } else if (x > 0) {
                    --k;
                } else {
                    ans.push_back({nums[i], nums[j++], nums[k--]});
                    while (j < k && nums[j] == nums[j - 1]) {
                        ++j;
                    }
                    while (j < k && nums[k] == nums[k + 1]) {
                        --k;
                    }
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-11"></a>
## 9. LC 11 — Container With Most Water (Medium)

[Official problem](https://leetcode.com/problems/container-with-most-water) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0011.Container%20With%20Most%20Water/README_EN.md)

### Problem description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i^th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

### Constraints

- `n == height.length`

- `2 <= n <= 10^5`

- `0 <= height[i] <= 10^4`

### Approach and complexity

We use two pointers $l$ and $r$ to point to the left and right ends of the array, respectively, i.e., $l = 0$ and $r = n - 1$, where $n$ is the length of the array.

Next, we use a variable $\textit{ans}$ to record the maximum capacity of the container, initially set to $0$.

Then, we start a loop. In each iteration, we calculate the current capacity of the container, i.e., $\textit{min}(\textit{height}[l], \textit{height}[r]) \times (r - l)$, and compare it with $\textit{ans}$, assigning the larger value to $\textit{ans}$. Then, we compare the values of $\textit{height}[l]$ and $\textit{height}[r]$. If $\textit{height}[l] < \textit{height}[r]$, moving the $r$ pointer will not improve the result because the height of the container is determined by the shorter vertical line, so we move the $l$ pointer. Otherwise, we move the $r$ pointer.

After the iteration, we return $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{height}$.

### C++20 solution

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int ans = 0;
        while (l < r) {
            int t = min(height[l], height[r]) * (r - l);
            ans = max(ans, t);
            if (height[l] < height[r]) {
                ++l;
            } else {
                --r;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-42"></a>
## 10. LC 42 — Trapping Rain Water (Hard)

[Official problem](https://leetcode.com/problems/trapping-rain-water) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0042.Trapping%20Rain%20Water/README_EN.md)

### Problem description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### Constraints

- `n == height.length`

- `1 <= n <= 2 * 10^4`

- `0 <= height[i] <= 10^5`

### Approach and complexity

Advance the side with the smaller current boundary. That side has an opposite boundary at least as high, so its water is determined by its running maximum. Each index is finalized once.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = static_cast<int>(height.size()) - 1;
        int leftMax = 0, rightMax = 0, water = 0;
        while (left <= right) {
            if (height[left] <= height[right]) {
                leftMax = max(leftMax, height[left]);
                water += leftMax - height[left++];
            } else {
                rightMax = max(rightMax, height[right]);
                water += rightMax - height[right--];
            }
        }
        return water;
    }
};
```

---

<a id="lc-56"></a>
## 11. LC 56 — Merge Intervals (Medium)

[Official problem](https://leetcode.com/problems/merge-intervals) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0056.Merge%20Intervals/README_EN.md)

### Problem description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Constraints

- `1 <= intervals.length <= 10^4`

- `intervals[i].length == 2`

- `0 <= start_i <= end_i <= 10^4`

### Approach and complexity

We can sort the intervals in ascending order by the left endpoint, and then traverse the intervals for merging operations.

The specific merging operation is as follows.

First, we add the first interval to the answer. Then, we consider each subsequent interval in turn:

- If the right endpoint of the last interval in the answer array is less than the left endpoint of the current interval, it means that the two intervals will not overlap, so we can directly add the current interval to the end of the answer array;
- Otherwise, it means that the two intervals overlap. We need to use the right endpoint of the current interval to update the right endpoint of the last interval in the answer array, setting it to the larger of the two.

Finally, we return the answer array.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of intervals.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        ranges::sort(intervals);
        int st = intervals[0][0], ed = intervals[0][1];
        vector<vector<int>> ans;
        for (int i = 1; i < intervals.size(); ++i) {
            if (ed < intervals[i][0]) {
                ans.push_back({st, ed});
                st = intervals[i][0];
                ed = intervals[i][1];
            } else {
                ed = max(ed, intervals[i][1]);
            }
        }
        ans.push_back({st, ed});
        return ans;
    }
};
```

---

<a id="lc-88"></a>
## 12. LC 88 — Merge Sorted Array (Easy)

[Official problem](https://leetcode.com/problems/merge-sorted-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0088.Merge%20Sorted%20Array/README_EN.md)

### Problem description

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

### Constraints

- `nums1.length == m + n`

- `nums2.length == n`

- `0 <= m, n <= 200`

- `1 <= m + n <= 200`

- `-10^9 <= nums1[i], nums2[j] <= 10^9`

**Follow up: **Can you come up with an algorithm that runs in `O(m + n)` time?

### Approach and complexity

We use two pointers $i$ and $j$ pointing to the end of two arrays, and a pointer $k$ pointing to the end of the merged array.

Every time we compare the two elements at the end of the two arrays, and move the larger one to the end of the merged array. Then we move the pointer one step forward, and repeat this process until the two pointers reach the start of the arrays.

The time complexity is $O(m + n)$, and the space complexity is $O(1)$, where $m$ and $n$ are the lengths of two arrays.

### C++20 solution

```cpp
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int i = m - 1, j = n - 1, k = m + n - 1; ~j; --k) {
            nums1[k] = i >= 0 && nums1[i] > nums2[j] ? nums1[i--] : nums2[j--];
        }
    }
};
```

---

<a id="lc-189"></a>
## 13. LC 189 — Rotate Array (Medium)

[Official problem](https://leetcode.com/problems/rotate-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0189.Rotate%20Array/README_EN.md)

### Problem description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Constraints

- `1 <= nums.length <= 10^5`

- `-2^31 <= nums[i] <= 2^31 - 1`

- `0 <= k <= 10^5`

**Follow up:**

- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.

- Could you do it in-place with `O(1)` extra space?

### Approach and complexity

We can assume the length of the array is $n$ and calculate the actual number of steps needed by taking the module of $k$ and $n$, which is $k \bmod n$.

Next, let us reverse three times to get the final result:

1. Reverse the entire array.
2. Reverse the first $k$ elements.
3. Reverse the last $n - k$ elements.

For example, for the array $[1, 2, 3, 4, 5, 6, 7]$, $k = 3$, $n = 7$, $k \bmod n = 3$.

1. In the first reverse, reverse the entire array. We get $[7, 6, 5, 4, 3, 2, 1]$.
2. In the second reverse, reverse the first $k$ elements. We get $[5, 6, 7, 4, 3, 2, 1]$.
3. In the third reverse, reverse the last $n - k$ elements. We get $[5, 6, 7, 1, 2, 3, 4]$, which is the final result.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        ranges::reverse(nums);
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};
```

---

<a id="lc-75"></a>
## 14. LC 75 — Sort Colors (Medium)

[Official problem](https://leetcode.com/problems/sort-colors) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0075.Sort%20Colors/README_EN.md)

### Problem description

You are given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place **so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

### Constraints

- `n == nums.length`

- `1 <= n <= 300`

- `nums[i]` is either 0, 1, or 2.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

### Approach and complexity

We define three pointers $i$, $j$, and $k$. Pointer $i$ is used to point to the rightmost boundary of the elements with a value of $0$ in the array, and pointer $j$ is used to point to the leftmost boundary of the elements with a value of $2$ in the array. Initially, $i=-1$, $j=n$. Pointer $k$ is used to point to the current element being traversed, initially $k=0$.

When $k < j$, we perform the following operations:

- If $\textit{nums}[k] = 0$, then swap it with $\textit{nums}[i+1]$, then increment both $i$ and $k$ by $1$;
- If $\textit{nums}[k] = 2$, then swap it with $\textit{nums}[j-1]$, then decrement $j$ by $1$;
- If $\textit{nums}[k] = 1$, then increment $k$ by $1$.

After the traversal, the elements in the array are divided into three parts: $[0,i]$, $[i+1,j-1]$ and $[j,n-1]$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array. Only one traversal of the array is needed.

### C++20 solution

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i = -1, j = nums.size(), k = 0;
        while (k < j) {
            if (nums[k] == 0) {
                swap(nums[++i], nums[k++]);
            } else if (nums[k] == 2) {
                swap(nums[--j], nums[k]);
            } else {
                ++k;
            }
        }
    }
};
```

---

<a id="lc-169"></a>
## 15. LC 169 — Majority Element (Easy)

[Official problem](https://leetcode.com/problems/majority-element) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0169.Majority%20Element/README_EN.md)

### Problem description

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

### Constraints

- `n == nums.length`

- `1 <= n <= 5 * 10^4`

- `-10^9 <= nums[i] <= 10^9`

- The input is generated such that a majority element will exist in the array.

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

### Approach and complexity

The basic steps of the Moore voting algorithm are as follows:

Initialize the element $m$ and initialize the counter $\textit{cnt} = 0$. Then, for each element $x$ in the input list:

1. If $\textit{cnt} = 0$, then $m = x$ and $\textit{cnt} = 1$;
1. Otherwise, if $m = x$, then $\textit{cnt} = \textit{cnt} + 1$, otherwise $\textit{cnt} = \textit{cnt} - 1$.

In general, the Moore voting algorithm requires **two passes** over the input list. In the first pass, we generate the candidate value $m$, and if there is a majority, the candidate value is the majority value. In the second pass, we simply compute the frequency of the candidate value to confirm whether it is the majority value. Since this problem has clearly stated that there is a majority value, we can directly return $m$ after the first pass, without the need for a second pass to confirm whether it is the majority value.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt = 0, m = 0;
        for (int& x : nums) {
            if (cnt == 0) {
                m = x;
                cnt = 1;
            } else {
                cnt += m == x ? 1 : -1;
            }
        }
        return m;
    }
};
```

---

<a id="lc-217"></a>
## 16. LC 217 — Contains Duplicate (Easy)

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

<a id="lc-49"></a>
## 17. LC 49 — Group Anagrams (Medium)

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

<a id="lc-125"></a>
## 18. LC 125 — Valid Palindrome (Easy)

[Official problem](https://leetcode.com/problems/valid-palindrome) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0125.Valid%20Palindrome/README_EN.md)

### Problem description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

### Constraints

- `1 <= s.length <= 2 * 10^5`

- `s` consists only of printable ASCII characters.

### Approach and complexity

We use two pointers $i$ and $j$ to point to the two ends of the string $s$, and then loop through the following process until $i \geq j$:

1. If $s[i]$ is not a letter or a number, move the pointer $i$ one step to the right and continue to the next loop.
2. If $s[j]$ is not a letter or a number, move the pointer $j$ one step to the left and continue to the next loop.
3. If the lowercase form of $s[i]$ and $s[j]$ are not equal, return `false`.
4. Otherwise, move the pointer $i$ one step to the right and the pointer $j$ one step to the left, and continue to the next loop.

At the end of the loop, return `true`.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            if (!isalnum(s[i])) {
                ++i;
            } else if (!isalnum(s[j])) {
                --j;
            } else if (tolower(s[i]) != tolower(s[j])) {
                return false;
            } else {
                ++i;
                --j;
            }
        }
        return true;
    }
};
```

---

<a id="lc-242"></a>
## 19. LC 242 — Valid Anagram (Easy)

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

<a id="lc-14"></a>
## 20. LC 14 — Longest Common Prefix (Easy)

[Official problem](https://leetcode.com/problems/longest-common-prefix) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0014.Longest%20Common%20Prefix/README_EN.md)

### Problem description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

### Constraints

- `1 <= strs.length <= 200`

- `0 <= strs[i].length <= 200`

- `strs[i]` consists of only lowercase English letters if it is non-empty.

### Approach and complexity

We use the first string $\textit{strs}[0]$ as a benchmark, and compare whether the $i$-th character of the subsequent strings is the same as the $i$-th character of $\textit{strs}[0]$. If they are the same, we continue to compare the next character. Otherwise, we return the first $i$ characters of $\textit{strs}[0]$.

If the traversal ends, it means that the first $i$ characters of all strings are the same, and we return $\textit{strs}[0]$.

The time complexity is $O(nm)$, and the space complexity is $O(1)$, where $n$ and $m$ are the length of the string array and the minimum length of the strings, respectively.

### C++20 solution

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        for (int i = 0; i < strs[0].size(); ++i) {
            for (int j = 1; j < n; ++j) {
                if (strs[j].size() <= i || strs[j][i] != strs[0][i]) {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0];
    }
};
```

---

<a id="lc-28"></a>
## 21. LC 28 — Find the Index of the First Occurrence in a String (Easy)

[Official problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0028.Find%20the%20Index%20of%20the%20First%20Occurrence%20in%20a%20String/README_EN.md)

### Problem description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

### Constraints

- `1 <= haystack.length, needle.length <= 10^4`

- `haystack` and `needle` consist of only lowercase English characters.

### Approach and complexity

Compute the prefix function $\textit{next}$ of $\textit{needle}$, where $\textit{next}[i]$ is the longest proper border of $\textit{needle}[0..i]$. Scan $\textit{haystack}$: equal characters grow the match length, and a mismatch jumps it to $\textit{next}[j-1]$. When the match length reaches $m$, return the start index $i-m+1$.

The time complexity is $O(n+m)$, and the space complexity is $O(m)$, where $n$ and $m$ are the lengths of $\textit{haystack}$ and $\textit{needle}$.

### C++20 solution

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size(), m = needle.size();
        vector<int> nxt(m);
        for (int i = 1, j = 0; i < m; ++i) {
            while (j > 0 && needle[i] != needle[j]) {
                j = nxt[j - 1];
            }
            if (needle[i] == needle[j]) {
                ++j;
            }
            nxt[i] = j;
        }
        for (int i = 0, j = 0; i < n; ++i) {
            while (j > 0 && haystack[i] != needle[j]) {
                j = nxt[j - 1];
            }
            if (haystack[i] == needle[j]) {
                ++j;
            }
            if (j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }
};
```

---

<a id="lc-344"></a>
## 22. LC 344 — Reverse String (Easy)

[Official problem](https://leetcode.com/problems/reverse-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0344.Reverse%20String/README_EN.md)

### Problem description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

### Constraints

- `1 <= s.length <= 10^5`

- `s[i]` is a printable ascii character.

### Approach and complexity

We use two pointers $i$ and $j$, initially pointing to the start and end of the array respectively. Each time, we swap the elements at $i$ and $j$, then move $i$ forward and $j$ backward, until $i$ and $j$ meet.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        for (int i = 0, j = s.size() - 1; i < j;) {
            swap(s[i++], s[j--]);
        }
    }
};
```

---

<a id="lc-151"></a>
## 23. LC 151 — Reverse Words in a String (Medium)

[Official problem](https://leetcode.com/problems/reverse-words-in-a-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0151.Reverse%20Words%20in%20a%20String/README_EN.md)

### Problem description

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Constraints

- `1 <= s.length <= 10^4`

- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.

- There is **at least one** word in `s`.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

### Approach and complexity

We can use two pointers $i$ and $j$ to find each word, add it to the result list, then reverse the result list, and finally concatenate it into a string.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string.

### C++20 solution

```cpp
class Solution {
public:
    string reverseWords(string s) {
        int i = 0;
        int j = 0;
        int n = s.size();
        while (i < n) {
            while (i < n && s[i] == ' ') {
                ++i;
            }
            if (i < n) {
                if (j != 0) {
                    s[j++] = ' ';
                }
                int k = i;
                while (k < n && s[k] != ' ') {
                    s[j++] = s[k++];
                }
                reverse(s.begin() + j - (k - i), s.begin() + j);
                i = k;
            }
        }
        s.erase(s.begin() + j, s.end());
        ranges::reverse(s);
        return s;
    }
};
```

---

<a id="lc-5"></a>
## 24. LC 5 — Longest Palindromic Substring (Medium)

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

<a id="lc-76"></a>
## 25. LC 76 — Minimum Window Substring (Hard)

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

<a id="lc-438"></a>
## 26. LC 438 — Find All Anagrams in a String (Medium)

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
## 27. LC 567 — Permutation in String (Medium)

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

<a id="lc-209"></a>
## 28. LC 209 — Minimum Size Subarray Sum (Medium)

[Official problem](https://leetcode.com/problems/minimum-size-subarray-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0209.Minimum%20Size%20Subarray%20Sum/README_EN.md)

### Problem description

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

### Constraints

- `1 <= target <= 10^9`

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^4`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

### Approach and complexity

We can use two pointers $j$ and $i$ to maintain a window, where the sum of all elements in the window is less than $\textit{target}$. Initially, $j = 0$, and the answer $\textit{ans} = n + 1$, where $n$ is the length of the array $\textit{nums}$.

Next, the pointer $i$ starts to move to the right from $0$, moving one step each time. We add the element corresponding to the pointer $i$ to the window and update the sum of the elements in the window. If the sum of the elements in the window is greater than or equal to $\textit{target}$, it means that the current subarray satisfies the condition, and we can update the answer, i.e., $\textit{ans} = \min(\textit{ans}, i - j + 1)$. Then we continuously remove the element $\textit{nums}[j]$ from the window until the sum of the elements in the window is less than $\textit{target}$, and then repeat the above process.

Finally, if $\textit{ans} \leq n$, it means that there exists a subarray that satisfies the condition, return $\textit{ans}$, otherwise return $0$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, n = nums.size();
        long long s = 0;
        int ans = n + 1;
        for (int r = 0; r < n; ++r) {
            s += nums[r];
            while (s >= target) {
                ans = min(ans, r - l + 1);
                s -= nums[l++];
            }
        }
        return ans > n ? 0 : ans;
    }
};
```

---

<a id="lc-239"></a>
## 29. LC 239 — Sliding Window Maximum (Hard)

[Official problem](https://leetcode.com/problems/sliding-window-maximum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0239.Sliding%20Window%20Maximum/README_EN.md)

### Problem description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^4 <= nums[i] <= 10^4`

- `1 <= k <= nums.length`

### Approach and complexity

To find the maximum value in a sliding window, a common method is to use a monotonic queue.

We can maintain a queue $q$ that is monotonically decreasing from the front to the back, storing the indices of the elements. As we traverse the array $\textit{nums}$, for the current element $\textit{nums}[i]$, we first check if the front element of the queue is out of the window. If it is, we remove the front element. Then, we compare the current element $\textit{nums}[i]$ with the elements at the back of the queue. If the elements at the back are less than or equal to the current element, we remove them until the element at the back is greater than the current element or the queue is empty. Then, we add the index of the current element to the queue. At this point, the front element of the queue is the maximum value of the current sliding window. Note that we add the front element of the queue to the result array when the index $i$ is greater than or equal to $k-1$.

The time complexity is $O(n)$, and the space complexity is $O(k)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> q;
        vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            if (q.size() && i - q.front() >= k) {
                q.pop_front();
            }
            while (q.size() && nums[q.back()] <= nums[i]) {
                q.pop_back();
            }
            q.push_back(i);
            if (i >= k - 1) {
                ans.push_back(nums[q.front()]);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-560"></a>
## 30. LC 560 — Subarray Sum Equals K (Medium)

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

<a id="lc-152"></a>
## 31. LC 152 — Maximum Product Subarray (Medium)

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

<a id="lc-41"></a>
## 32. LC 41 — First Missing Positive (Hard)

[Official problem](https://leetcode.com/problems/first-missing-positive) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0041.First%20Missing%20Positive/README_EN.md)

### Problem description

Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

### Constraints

- `1 <= nums.length <= 10^5`

- `-2^31 <= nums[i] <= 2^31 - 1`

### Approach and complexity

We assume the length of the array $\textit{nums}$ is $n$, then the smallest positive integer must be in the range $[1, .., n + 1]$. We can traverse the array and swap each number $x$ to its correct position, that is, the position $x - 1$. If $x$ is not in the range $[1, n + 1]$, then we can ignore it.

After the traversal, we traverse the array again. If $i+1$ is not equal to $\textit{nums}[i]$, then $i+1$ is the smallest positive integer we are looking for.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            while (nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
                swap(nums[i], nums[nums[i] - 1]);
            }
        }
        for (int i = 0; i < n; ++i) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return n + 1;
    }
};
```

---

<a id="lc-31"></a>
## 33. LC 31 — Next Permutation (Medium)

[Official problem](https://leetcode.com/problems/next-permutation) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0031.Next%20Permutation/README_EN.md)

### Problem description

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.

- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.

- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be **in place** and use only constant extra memory.

### Constraints

- `1 <= nums.length <= 100`

- `0 <= nums[i] <= 100`

### Approach and complexity

We first traverse the array from back to front and find the first position $i$ where $\textit{nums}[i] \lt \textit{nums}[i + 1]$.

Then traverse the array from back to front again and find the first position $j$ where $\textit{nums}[j] \gt \textit{nums}[i]$. Swap $\textit{nums}[i]$ and $\textit{nums}[j]$, and then reverse the elements from $\textit{nums}[i + 1]$ to $\textit{nums}[n - 1]$, the next permutation can be obtained.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;
        while (~i && nums[i] >= nums[i + 1]) {
            --i;
        }
        if (~i) {
            for (int j = n - 1; j > i; --j) {
                if (nums[j] > nums[i]) {
                    swap(nums[i], nums[j]);
                    break;
                }
            }
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};
```

---

<a id="lc-48"></a>
## 34. LC 48 — Rotate Image (Medium)

[Official problem](https://leetcode.com/problems/rotate-image) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0048.Rotate%20Image/README_EN.md)

### Problem description

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

### Constraints

- `n == matrix.length == matrix[i].length`

- `1 <= n <= 20`

- `-1000 <= matrix[i][j] <= 1000`

### Approach and complexity

According to the problem requirements, we need to rotate $\textit{matrix}[i][j]$ to $\textit{matrix}[j][n - i - 1]$.

We can first flip the matrix upside down, i.e., swap $\textit{matrix}[i][j]$ with $\textit{matrix}[n - i - 1][j]$, and then flip the matrix along the main diagonal, i.e., swap $\textit{matrix}[i][j]$ with $\textit{matrix}[j][i]$. This way, we can rotate $\textit{matrix}[i][j]$ to $\textit{matrix}[j][n - i - 1]$.

The time complexity is $O(n^2)$, and the space complexity is $O(1)$, where $n$ is the side length of the matrix.

### C++20 solution

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n >> 1; ++i) {
            for (int j = 0; j < n; ++j) {
                swap(matrix[i][j], matrix[n - i - 1][j]);
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};
```

---

<a id="lc-54"></a>
## 35. LC 54 — Spiral Matrix (Medium)

[Official problem](https://leetcode.com/problems/spiral-matrix) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0054.Spiral%20Matrix/README_EN.md)

### Problem description

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

### Constraints

- `m == matrix.length`

- `n == matrix[i].length`

- `1 <= m, n <= 10`

- `-100 <= matrix[i][j] <= 100`

### Approach and complexity

Notice that the range of matrix element values is $[-100, 100]$. Therefore, we can add a large value, such as $300$, to the visited elements. This way, we only need to check if the visited element is greater than $100$, without needing extra space to record whether it has been visited. If we need to restore the original values of the visited elements, we can traverse the matrix again after the traversal is complete and subtract $300$ from all elements.

The time complexity is $O(mn)$, and the space complexity is $O(1)$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int dirs[5] = {0, 1, 0, -1, 0};
        int i = 0, j = 0, k = 0;
        vector<int> ans;
        for (int h = m * n; h; --h) {
            ans.push_back(matrix[i][j]);
            matrix[i][j] += 300;
            int x = i + dirs[k], y = j + dirs[k + 1];
            if (x < 0 || x >= m || y < 0 || y >= n || matrix[x][y] > 100) {
                k = (k + 1) % 4;
            }
            i += dirs[k];
            j += dirs[k + 1];
        }
        for (i = 0; i < m; ++i) {
            for (j = 0; j < n; ++j) {
                matrix[i][j] -= 300;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-73"></a>
## 36. LC 73 — Set Matrix Zeroes (Medium)

[Official problem](https://leetcode.com/problems/set-matrix-zeroes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0073.Set%20Matrix%20Zeroes/README_EN.md)

### Problem description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

### Constraints

- `m == matrix.length`

- `n == matrix[0].length`

- `1 <= m, n <= 200`

- `-2^31 <= matrix[i][j] <= 2^31 - 1`

**Follow up:**

- A straightforward solution using `O(mn)` space is probably a bad idea.

- A simple improvement uses `O(m + n)` space, but still not the best solution.

- Could you devise a constant space solution?

### Approach and complexity

In the first method, we use an additional array to mark the rows and columns to be cleared. In fact, we can also use the first row and first column of the matrix to mark them, without creating an additional array.

Since the first row and the first column are used to mark, their values ​​may change due to the mark, so we need additional variables $\textit{i0}$, $\textit{j0}$ to mark whether the first row and the first column need to be cleared.

The time complexity is $O(mn)$, and the space complexity is $O(1)$, where $m$ and $n$ are the number of rows and columns of the matrix respectively.

### C++20 solution

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool i0 = false, j0 = false;
        for (int j = 0; j < n; ++j) {
            if (matrix[0][j] == 0) {
                i0 = true;
                break;
            }
        }
        for (int i = 0; i < m; ++i) {
            if (matrix[i][0] == 0) {
                j0 = true;
                break;
            }
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (i0) {
            for (int j = 0; j < n; ++j) {
                matrix[0][j] = 0;
            }
        }
        if (j0) {
            for (int i = 0; i < m; ++i) {
                matrix[i][0] = 0;
            }
        }
    }
};
```

---

<a id="lc-36"></a>
## 37. LC 36 — Valid Sudoku (Medium)

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

<a id="lc-977"></a>
## 38. LC 977 — Squares of a Sorted Array (Easy)

[Official problem](https://leetcode.com/problems/squares-of-a-sorted-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0977.Squares%20of%20a%20Sorted%20Array/README_EN.md)

### Problem description

Given an integer array `nums` sorted in **non-decreasing** order, return an array of **the squares of each number** sorted in non-decreasing order.

### Constraints

- `1 <= nums.length <= 10^4`

- `-10^4 <= nums[i] <= 10^4`

- `nums` is sorted in **non-decreasing** order.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

### Approach and complexity

Since the array $\textit{nums}$ is already sorted in non-decreasing order, the square values of the negative numbers in the array are decreasing, and the square values of the positive numbers are increasing. We can use two pointers, each pointing to the ends of the array. Each time we compare the square values of the elements pointed to by the two pointers, we put the larger square value at the end of the result array.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        for (int i = 0, j = n - 1, k = n - 1; i <= j; --k) {
            int a = nums[i] * nums[i];
            int b = nums[j] * nums[j];
            if (a > b) {
                ans[k] = a;
                ++i;
            } else {
                ans[k] = b;
                --j;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-134"></a>
## 39. LC 134 — Gas Station (Medium)

[Official problem](https://leetcode.com/problems/gas-station) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0134.Gas%20Station/README_EN.md)

### Problem description

There are `n` gas stations along a circular route, where the amount of gas at the `i^th` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i^th` station to its next `(i + 1)^th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is **guaranteed** to be **unique**.

### Constraints

- `n == gas.length == cost.length`

- `1 <= n <= 10^5`

- `0 <= gas[i], cost[i] <= 10^4`

- The input is generated such that the answer is unique.

### Approach and complexity

Track total fuel balance and balance since the candidate start. If the latter becomes negative, no point in that failed segment can start a valid trip, so restart after it. A nonnegative total guarantees the surviving candidate works.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int i = n - 1, j = n - 1;
        int cnt = 0, s = 0;
        while (cnt < n) {
            s += gas[j] - cost[j];
            ++cnt;
            j = (j + 1) % n;
            while (s < 0 && cnt < n) {
                --i;
                s += gas[i] - cost[i];
                ++cnt;
            }
        }
        return s < 0 ? -1 : i;
    }
};
```

---

<a id="lc-55"></a>
## 40. LC 55 — Jump Game (Medium)

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
## 41. LC 45 — Jump Game II (Medium)

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

<a id="lc-128"></a>
## 42. LC 128 — Longest Consecutive Sequence (Medium)

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
## 43. LC 347 — Top K Frequent Elements (Medium)

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

<a id="lc-18"></a>
## 44. LC 18 — 4Sum (Medium)

[Official problem](https://leetcode.com/problems/4sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0018.4Sum/README_EN.md)

### Problem description

Given an array `nums` of `n` integers, return an array of all the **unique** quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`

- `a`, `b`, `c`, and `d` are **distinct**.

- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

### Constraints

- `1 <= nums.length <= 200`

- `-10^9 <= nums[i] <= 10^9`

- `-10^9 <= target <= 10^9`

### Approach and complexity

We notice that the problem requires us to find non-repeating quadruplets. Therefore, we can first sort the array, which makes it easy to skip duplicate elements.

Next, we enumerate the first two elements of the quadruplet, $\textit{nums}[i]$ and $\textit{nums}[j]$, where $i \lt j$. During the enumeration process, we skip duplicate $\textit{nums}[i]$ and $\textit{nums}[j]$. Then, we use two pointers $k$ and $l$ to point to the two ends behind $\textit{nums}[i]$ and $\textit{nums}[j]$. Let $x = \textit{nums}[i] + \textit{nums}[j] + \textit{nums}[k] + \textit{nums}[l]$, we compare $x$ with $\textit{target}$ and perform the following operations:

- If $x \lt \textit{target}$, then update $k = k + 1$ to get a larger $x$;
- If $x \gt \textit{target}$, then update $l = l - 1$ to get a smaller $x$;
- Otherwise, it means that a quadruplet $(\textit{nums}[i], \textit{nums}[j], \textit{nums}[k], \textit{nums}[l])$ is found. Add it to the answer, then we update the pointers $k$ and $l$, and skip all duplicate elements to prevent the answer from containing duplicate quadruplets, and continue to find the next quadruplet.

The time complexity is $O(n^3)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<vector<int>> ans;
        if (n < 4) {
            return ans;
        }
        ranges::sort(nums);
        for (int i = 0; i < n - 3; ++i) {
            if (i && nums[i] == nums[i - 1]) {
                continue;
            }
            for (int j = i + 1; j < n - 2; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                int k = j + 1, l = n - 1;
                while (k < l) {
                    long long x = (long long) nums[i] + nums[j] + nums[k] + nums[l];
                    if (x < target) {
                        ++k;
                    } else if (x > target) {
                        --l;
                    } else {
                        ans.push_back({nums[i], nums[j], nums[k++], nums[l--]});
                        while (k < l && nums[k] == nums[k - 1]) {
                            ++k;
                        }
                        while (k < l && nums[l] == nums[l + 1]) {
                            --l;
                        }
                    }
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-16"></a>
## 45. LC 16 — 3Sum Closest (Medium)

[Official problem](https://leetcode.com/problems/3sum-closest) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0016.3Sum%20Closest/README_EN.md)

### Problem description

You are given an integer array `nums` of length `n` and an integer `target`.

Find three integers at **distinct indices** in `nums` such that the sum is **closest** to `target`.

Return the sum of the three integers.

You may assume that each input would have **exactly** one solution.

### Constraints

- `3 <= nums.length <= 500`

- `-1000 <= nums[i] <= 1000`

- `-10^4 <= target <= 10^4`

### Approach and complexity

We sort the array first, then traverse the array. For each element $\textit{nums}[i]$, we use pointers $j$ and $k$ to point to $i+1$ and $n-1$ respectively, calculate the sum of the three numbers. If the sum of the three numbers equals $\textit{target}$, we directly return $\textit{target}$. Otherwise, we update the answer based on the difference from $\textit{target}$. If the sum of the three numbers is greater than $\textit{target}$, we move $k$ one place to the left, otherwise, we move $j$ one place to the right.

The time complexity is $O(n^2)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        ranges::sort(nums);
        int ans = 1 << 30;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int j = i + 1, k = n - 1;
            while (j < k) {
                int t = nums[i] + nums[j] + nums[k];
                if (t == target) return t;
                if (abs(t - target) < abs(ans - target)) ans = t;
                if (t > target)
                    --k;
                else
                    ++j;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-27"></a>
## 46. LC 27 — Remove Element (Easy)

[Official problem](https://leetcode.com/problems/remove-element) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0027.Remove%20Element/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.

- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
// It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be **accepted**.

### Constraints

- `0 <= nums.length <= 100`

- `0 <= nums[i] <= 50`

- `0 <= val <= 100`

### Approach and complexity

We use the variable $k$ to record the number of elements that are not equal to $\textit{val}$.

Traverse the array $\textit{nums}$, if the current element $x$ is not equal to $\textit{val}$, then assign $x$ to $\textit{nums}[k]$, and increment $k$ by $1$.

Finally, return $k$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int x : nums) {
            if (x != val) {
                nums[k++] = x;
            }
        }
        return k;
    }
};
```

---

<a id="lc-80"></a>
## 47. LC 80 — Remove Duplicates from Sorted Array II (Medium)

[Official problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0080.Remove%20Duplicates%20from%20Sorted%20Array%20II/README_EN.md)

### Problem description

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array in-place** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be **accepted**.

### Constraints

- `1 <= nums.length <= 3 * 10^4`

- `-10^4 <= nums[i] <= 10^4`

- `nums` is sorted in **non-decreasing** order.

### Approach and complexity

We use a variable $k$ to record the current length of the array that has been processed. Initially, $k=0$, representing an empty array.

Then we traverse the array from left to right. For each element $x$ we traverse, if $k < 2$ or $x \neq \textit{nums}[k-2]$, we put $x$ in the position of $\textit{nums}[k]$, and then increment $k$ by $1$. Otherwise, $x$ is the same as $\textit{nums}[k-2]$, we directly skip this element. Continue to traverse until the entire array is traversed.

In this way, when the traversal ends, the first $k$ elements in $\textit{nums}$ are the answer we want, and $k$ is the length of the answer.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

Supplement:

The original problem requires that the same number appears at most $2$ times. We can extend it to keep at most $k$ identical numbers.

- Since the same number can be kept at most $k$ times, we can directly keep the first $k$ elements of the original array;
- For the later numbers, the premise of being able to keep them is: the current number $x$ compares with the $k$th element from the end of the previously kept numbers. If they are different, keep it, otherwise skip it.

Similar problems:

- [26. Remove Duplicates from Sorted Array](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0026.Remove%20Duplicates%20from%20Sorted%20Array/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        for (int x : nums) {
            if (k < 2 || x != nums[k - 2]) {
                nums[k++] = x;
            }
        }
        return k;
    }
};
```

---

<a id="lc-443"></a>
## 48. LC 443 — String Compression (Medium)

[Official problem](https://leetcode.com/problems/string-compression) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0443.String%20Compression/README_EN.md)

### Problem description

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

- If the group's length is `1`, append the character to `s`.

- Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array `chars`**. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array,** return the new length of the array.

You must write an algorithm that uses only constant extra space.

**Note: **The characters in the array beyond the returned length do not matter and should be ignored.

### Constraints

- `1 <= chars.length <= 2000`

- `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.

### Approach and complexity

Read maximal equal-character runs and write the character plus decimal count when greater than one. The write position never passes unread input.

Time O(n); auxiliary space O(log n) for the temporary count string.

### C++20 solution

```cpp
class Solution {
public:
    int compress(vector<char>& chars) {
        int k = 0, n = chars.size();
        for (int i = 0, j = i + 1; i < n;) {
            while (j < n && chars[j] == chars[i])
                ++j;
            chars[k++] = chars[i];
            if (j - i > 1) {
                for (char c : to_string(j - i)) {
                    chars[k++] = c;
                }
            }
            i = j;
        }
        return k;
    }
};
```

---

<a id="lc-394"></a>
## 49. LC 394 — Decode String (Medium)

[Official problem](https://leetcode.com/problems/decode-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0394.Decode%20String/README_EN.md)

### Problem description

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed `10^5`.

### Constraints

- `1 <= s.length <= 30`

- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.

- `s` is guaranteed to be **a valid** input.

- All the integers in `s` are in the range `[1, 300]`.

### Approach and complexity

On an opening bracket, save the decoded prefix and its repetition count, then start a fresh fragment. On a closing bracket, append the completed fragment the saved number of times. Multi-digit counts are accumulated before opening brackets.

If d is maximum nesting depth, N encoded length, and L decoded length, time O(N+dL) is a conservative copying bound; live auxiliary storage O(N+L). Deeply nested count-one blocks may copy the same fragment repeatedly.

### C++20 solution

```cpp
class Solution {
public:
    string decodeString(string s) {
        vector<pair<string, int>> stack;
        string current;
        int count = 0;
        for (unsigned char c : s) {
            if (isdigit(c)) count = count * 10 + c - '0';
            else if (c == '[') {
                stack.emplace_back(move(current), count);
                current.clear();
                count = 0;
            } else if (c == ']') {
                auto [prefix, repeat] = move(stack.back());
                stack.pop_back();
                prefix.reserve(prefix.size() + current.size() * repeat);
                while (repeat--) prefix += current;
                current = move(prefix);
            } else current += static_cast<char>(c);
        }
        return current;
    }
};
```

---

<a id="lc-8"></a>
## 50. LC 8 — String to Integer (atoi) (Medium)

[Official problem](https://leetcode.com/problems/string-to-integer-atoi) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0008.String%20to%20Integer%20%28atoi%29/README_EN.md)

### Problem description

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

- **Whitespace**: Ignore any leading whitespace (`" "`).

- **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.

- **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.

- **Rounding**: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2^31` should be rounded to `-2^31`, and integers greater than `2^31 - 1` should be rounded to `2^31 - 1`.

Return the integer as the final result.

**Note:**​​​​​​​ You must not use any built-in library function that converts a string to a number (for example, `atoi`, `stoi`, `Integer.parseInt`, `int()`, `parseInt`, `Number()`). Perform the conversion manually.

### Constraints

- `0 <= s.length <= 200`

- `s` consists of English letters (lower-case and upper-case), digits (`0 - 9`), `' '`, `'+'`, `'-'`, and `'.'`.

### Approach and complexity

First, we determine whether the string is empty. If it is, we directly return $0$.

Otherwise, we need to traverse the string, skip the leading spaces, and determine whether the first non-space character is a positive or negative sign.

Then we traverse the following characters. If it is a digit, we judge whether adding this digit will cause integer overflow. If it does, we return the result according to the positive or negative sign. Otherwise, we add the digit to the result. We continue to traverse the following characters until we encounter a non-digit character or the traversal ends.

After the traversal ends, we return the result according to the positive or negative sign.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string. We only need to process all characters in turn.

### C++20 solution

```cpp
class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.size();
        while (i < n && s[i] == ' ')
            ++i;

        int sign = 1;
        if (i < n && (s[i] == '-' || s[i] == '+')) {
            sign = s[i] == '-' ? -1 : 1;
            ++i;
        }

        int res = 0;
        while (i < n && isdigit(s[i])) {
            int digit = s[i] - '0';
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && digit > INT_MAX % 10)) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            res = res * 10 + digit;
            ++i;
        }
        return res * sign;
    }
};
```
