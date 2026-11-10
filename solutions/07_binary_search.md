# 7. Binary Search — C++20 solutions

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

1. [LC 704 — Binary Search](#lc-704)
2. [LC 35 — Search Insert Position](#lc-35)
3. [LC 34 — Find First and Last Position of Element in Sorted Array](#lc-34)
4. [LC 33 — Search in Rotated Sorted Array](#lc-33)
5. [LC 153 — Find Minimum in Rotated Sorted Array](#lc-153)
6. [LC 154 — Find Minimum in Rotated Sorted Array II](#lc-154)
7. [LC 81 — Search in Rotated Sorted Array II](#lc-81)
8. [LC 74 — Search a 2D Matrix](#lc-74)
9. [LC 240 — Search a 2D Matrix II](#lc-240)
10. [LC 278 — First Bad Version](#lc-278)
11. [LC 69 — Sqrt(x)](#lc-69)
12. [LC 367 — Valid Perfect Square](#lc-367)
13. [LC 875 — Koko Eating Bananas](#lc-875)
14. [LC 1011 — Capacity To Ship Packages Within D Days](#lc-1011)
15. [LC 410 — Split Array Largest Sum](#lc-410)
16. [LC 1482 — Minimum Number of Days to Make m Bouquets](#lc-1482)
17. [LC 1552 — Magnetic Force Between Two Balls](#lc-1552)
18. [LC 1760 — Minimum Limit of Balls in a Bag](#lc-1760)
19. [LC 2187 — Minimum Time to Complete Trips](#lc-2187)
20. [LC 2226 — Maximum Candies Allocated to K Children](#lc-2226)
21. [LC 4 — Median of Two Sorted Arrays](#lc-4)
22. [LC 162 — Find Peak Element](#lc-162)
23. [LC 852 — Peak Index in a Mountain Array](#lc-852)
24. [LC 1095 — Find in Mountain Array](#lc-1095)
25. [LC 540 — Single Element in a Sorted Array](#lc-540)
26. [LC 658 — Find K Closest Elements](#lc-658)
27. [LC 378 — Kth Smallest Element in a Sorted Matrix](#lc-378)
28. [LC 719 — Find K-th Smallest Pair Distance](#lc-719)
29. [LC 668 — Kth Smallest Number in Multiplication Table](#lc-668)
30. [LC 786 — K-th Smallest Prime Fraction](#lc-786)
31. [LC 300 — Longest Increasing Subsequence](#lc-300)
32. [LC 354 — Russian Doll Envelopes](#lc-354)
33. [LC 436 — Find Right Interval](#lc-436)
34. [LC 475 — Heaters](#lc-475)
35. [LC 611 — Valid Triangle Number](#lc-611)
36. [LC 167 — Two Sum II - Input Array Is Sorted](#lc-167)
37. [LC 209 — Minimum Size Subarray Sum](#lc-209)
38. [LC 2300 — Successful Pairs of Spells and Potions](#lc-2300)
39. [LC 2563 — Count the Number of Fair Pairs](#lc-2563)
40. [LC 981 — Time Based Key-Value Store](#lc-981)
41. [LC 1146 — Snapshot Array](#lc-1146)
42. [LC 911 — Online Election](#lc-911)
43. [LC 528 — Random Pick with Weight](#lc-528)
44. [LC 729 — My Calendar I](#lc-729)
45. [LC 1235 — Maximum Profit in Job Scheduling](#lc-1235)
46. [LC 2070 — Most Beautiful Item for Each Query](#lc-2070)
47. [LC 2080 — Range Frequency Queries](#lc-2080)
48. [LC 1838 — Frequency of the Most Frequent Element](#lc-1838)
49. [LC 1870 — Minimum Speed to Arrive on Time](#lc-1870)
50. [LC 2141 — Maximum Running Time of N Computers](#lc-2141)

---

<a id="lc-704"></a>
## 1. LC 704 — Binary Search (Easy)

[Official problem](https://leetcode.com/problems/binary-search) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0704.Binary%20Search/README_EN.md)

### Problem description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

### Constraints

- `1 <= nums.length <= 10^4`

- `-10^4 < nums[i], target < 10^4`

- All the integers in `nums` are **unique**.

- `nums` is sorted in ascending order.

### Approach and complexity

We define the left boundary $l=0$ and the right boundary $r=n-1$ for binary search.

In each iteration, we calculate the middle position $\textit{mid}=(l+r)/2$, then compare the size of $\textit{nums}[\textit{mid}]$ and $\textit{target}$.

- If $\textit{nums}[\textit{mid}] \geq \textit{target}$, it means $\textit{target}$ is in the left half, so we move the right boundary $r$ to $\textit{mid}$;
- Otherwise, it means $\textit{target}$ is in the right half, so we move the left boundary $l$ to $\textit{mid}+1$.

The loop ends when $l<r$, at this point $\textit{nums}[l]$ is the target value we are looking for. If $\textit{nums}[l]=\textit{target}$, return $l$; otherwise, return $-1$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return nums[l] == target ? l : -1;
    }
};
```

---

<a id="lc-35"></a>
## 2. LC 35 — Search Insert Position (Easy)

[Official problem](https://leetcode.com/problems/search-insert-position) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0035.Search%20Insert%20Position/README_EN.md)

### Problem description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Constraints

- `1 <= nums.length <= 10^4`

- `-10^4 <= nums[i] <= 10^4`

- `nums` contains **distinct** values sorted in **ascending** order.

- `-10^4 <= target <= 10^4`

### Approach and complexity

We can also directly use the built-in function for binary search.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    }
};
```

---

<a id="lc-34"></a>
## 3. LC 34 — Find First and Last Position of Element in Sorted Array (Medium)

[Official problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0034.Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/README_EN.md)

### Problem description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

### Constraints

- `0 <= nums.length <= 10^5`

- `-10^9 <= nums[i] <= 10^9`

- `nums` is a non-decreasing array.

- `-10^9 <= target <= 10^9`

### Approach and complexity

We can perform two binary searches to find the left boundary and the right boundary.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        int r = lower_bound(nums.begin(), nums.end(), target + 1) - nums.begin();
        if (l == r) {
            return {-1, -1};
        }
        return {l, r - 1};
    }
};
```

---

<a id="lc-33"></a>
## 4. LC 33 — Search in Rotated Sorted Array (Medium)

[Official problem](https://leetcode.com/problems/search-in-rotated-sorted-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0033.Search%20in%20Rotated%20Sorted%20Array/README_EN.md)

### Problem description

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

### Constraints

- `1 <= nums.length <= 5000`

- `-10^4 <= nums[i] <= 10^4`

- All values of `nums` are **unique**.

- `nums` is an ascending array that is possibly rotated.

- `-10^4 <= target <= 10^4`

### Approach and complexity

We use binary search to divide the array into two parts, $[left,.. mid]$ and $[mid + 1,.. right]$. At this point, we can find that one part must be sorted.

Therefore, we can determine whether $\textit{target}$ is in this part based on the sorted part:

- If the elements in the range $[0,.. mid]$ form a sorted array:
    - If $\textit{nums}[0] \leq \textit{target} \leq \textit{nums}[\textit{mid}]$, then our search range can be narrowed down to $[left,.. mid]$;
    - Otherwise, search in $[mid + 1,.. right]$;
- If the elements in the range $[\textit{mid} + 1, n - 1]$ form a sorted array:
    - If $\textit{nums}[\textit{mid}] \lt \textit{target} \leq \textit{nums}[n - 1]$, then our search range can be narrowed down to $[mid + 1,.. right]$;
    - Otherwise, search in $[left,.. mid]$.

The termination condition for binary search is $\textit{left} \geq \textit{right}$. If at the end we find that $\textit{nums}[\textit{left}]$ is not equal to $\textit{target}$, it means that there is no element with a value of $\textit{target}$ in the array, and we return $-1$. Otherwise, we return the index $\textit{left}$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0, right = n - 1;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (nums[0] <= nums[mid]) {
                if (nums[0] <= target && target <= nums[mid])
                    right = mid;
                else
                    left = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[n - 1])
                    left = mid + 1;
                else
                    right = mid;
            }
        }
        return nums[left] == target ? left : -1;
    }
};
```

---

<a id="lc-153"></a>
## 5. LC 153 — Find Minimum in Rotated Sorted Array (Medium)

[Official problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0153.Find%20Minimum%20in%20Rotated%20Sorted%20Array/README_EN.md)

### Problem description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.

- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n) time`.

### Constraints

- `n == nums.length`

- `1 <= n <= 5000`

- `-5000 <= nums[i] <= 5000`

- All the integers of `nums` are **unique**.

- `nums` is sorted and rotated between `1` and `n` times.

### Approach and complexity

We can use binary search to solve this problem.

First, we define two pointers $l$ and $r$ pointing to the start and end of the array respectively. Then we enter a loop until $l$ is no longer less than $r$.

In each iteration, we calculate the middle position $\textit{mid}$ and compare $\textit{nums}[\textit{mid}]$ with $\textit{nums}[n-1]$. If $\textit{nums}[\textit{mid}]$ is greater than $\textit{nums}[n-1]$, the minimum value is to the right of $\textit{mid}$, so we update $l$ to $\textit{mid} + 1$. Otherwise, the minimum value is at $\textit{mid}$ or to its left, so we update $r$ to $\textit{mid}$. When the loop ends, pointer $l$ will point to the minimum value, and we return $\textit{nums}[l]$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the length of array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] > nums.back()) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return nums[l];
    }
};
```

---

<a id="lc-154"></a>
## 6. LC 154 — Find Minimum in Rotated Sorted Array II (Hard)

[Official problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0154.Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II/README_EN.md)

### Problem description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,4,4,5,6,7]` might become:

- `[4,5,6,7,0,1,4]` if it was rotated `4` times.

- `[0,1,4,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` that may contain **duplicates**, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

### Constraints

- `n == nums.length`

- `1 <= n <= 5000`

- `-5000 <= nums[i] <= 5000`

- `nums` is sorted and rotated between `1` and `n` times.

**Follow up:** This problem is similar to Find Minimum in Rotated Sorted Array, but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

### Approach and complexity

We define the left boundary $l = 0$ and right boundary $r = n - 1$ for binary search. Each iteration, we calculate the middle position $\textit{mid} = (l + r) \gg 1$ and compare the relationship between $\textit{nums}[\textit{mid}]$ and $\textit{nums}[r]$:

- If $\textit{nums}[\textit{mid}] > \textit{nums}[r]$, the minimum value is to the right of $\textit{mid}$, so we update $l$ to $\textit{mid} + 1$.
- If $\textit{nums}[\textit{mid}] = \textit{nums}[r]$, we cannot determine the position of the minimum value, but we can move $r$ to the left by one position, i.e., $r = r - 1$, to narrow down the search range.
- If $\textit{nums}[\textit{mid}] < \textit{nums}[r]$, the minimum value is to the left of $\textit{mid}$ or at $\textit{mid}$ itself, so we update $r$ to $\textit{mid}$.

When $l$ and $r$ meet, the pointer $l$ points to the position of the minimum value, and we return $\textit{nums}[l]$.

The time complexity is $O(n)$, as in the worst case where all elements in the array are the same, we need to traverse the entire array. The space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else if (nums[mid] == nums[r]) {
                r--;
            } else {
                r = mid;
            }
        }
        return nums[l];
    }
};
```

---

<a id="lc-81"></a>
## 7. LC 81 — Search in Rotated Sorted Array II (Medium)

[Official problem](https://leetcode.com/problems/search-in-rotated-sorted-array-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0081.Search%20in%20Rotated%20Sorted%20Array%20II/README_EN.md)

### Problem description

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` if `target` is in `nums`, or `false` if it is not in `nums`.

You must decrease the overall operation steps as much as possible.

### Constraints

- `1 <= nums.length <= 5000`

- `-10^4 <= nums[i] <= 10^4`

- `nums` is guaranteed to be rotated at some pivot.

- `-10^4 <= target <= 10^4`

**Follow up:** This problem is similar to Search in Rotated Sorted Array, but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

### Approach and complexity

We define the left boundary of the binary search as $l = 0$ and the right boundary as $r = n - 1$, where $n$ is the length of the array.

Each time during the binary search, we get the current midpoint $\textit{mid} = (l + r) / 2$.

- If $\textit{nums}[\textit{mid}] > \textit{nums}[r]$, it means $[l, \textit{mid}]$ is ordered. If $\textit{nums}[l] \le \textit{target} \le \textit{nums}[\textit{mid}]$, it means $\textit{target}$ is in $[l, \textit{mid}]$. Otherwise, $\textit{target}$ is in $[\textit{mid} + 1, r]$.
- If $\textit{nums}[\textit{mid}] < \textit{nums}[r]$, it means $[\textit{mid} + 1, r]$ is ordered. If $\textit{nums}[\textit{mid}] < \textit{target} \le \textit{nums}[r]$, it means $\textit{target}$ is in $[\textit{mid} + 1, r]$. Otherwise, $\textit{target}$ is in $[l, \textit{mid}]$.
- If $\textit{nums}[\textit{mid}] = \textit{nums}[r]$, it means the elements $\textit{nums}[\textit{mid}]$ and $\textit{nums}[r]$ are equal. In this case, we cannot determine which interval $\textit{target}$ is in, so we can only decrease $r$ by $1$.

After the binary search, if $\textit{nums}[l] = \textit{target}$, it means the target value $\textit{target}$ exists in the array. Otherwise, it does not exist.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] > nums[r]) {
                if (nums[l] <= target && target <= nums[mid]) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            } else if (nums[mid] < nums[r]) {
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            } else {
                --r;
            }
        }
        return nums[l] == target;
    }
};
```

---

<a id="lc-74"></a>
## 8. LC 74 — Search a 2D Matrix (Medium)

[Official problem](https://leetcode.com/problems/search-a-2d-matrix) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0074.Search%20a%202D%20Matrix/README_EN.md)

### Problem description

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.

- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

### Constraints

- `m == matrix.length`

- `n == matrix[i].length`

- `1 <= m, n <= 100`

- `-10^4 <= matrix[i][j], target <= 10^4`

### Approach and complexity

We can logically unfold the two-dimensional matrix and then perform binary search.

The time complexity is $O(\log(mn))$, and the space complexity is $O(1)$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively.

### C++20 solution

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int left = 0, right = m * n - 1;
        while (left < right) {
            int mid = left + right >> 1;
            int x = mid / n, y = mid % n;
            if (matrix[x][y] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return matrix[left / n][left % n] == target;
    }
};
```

---

<a id="lc-240"></a>
## 9. LC 240 — Search a 2D Matrix II (Medium)

[Official problem](https://leetcode.com/problems/search-a-2d-matrix-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0240.Search%20a%202D%20Matrix%20II/README_EN.md)

### Problem description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.

- Integers in each column are sorted in ascending from top to bottom.

### Constraints

- `m == matrix.length`

- `n == matrix[i].length`

- `1 <= n, m <= 300`

- `-10^9 <= matrix[i][j] <= 10^9`

- All the integers in each row are **sorted** in ascending order.

- All the integers in each column are **sorted** in ascending order.

- `-10^9 <= target <= 10^9`

### Approach and complexity

We start the search from the bottom-left or top-right corner and move towards the top-right or bottom-left direction. Compare the current element $\textit{matrix}[i][j]$ with $\textit{target}$:

- If $\textit{matrix}[i][j] = \textit{target}$, it means the target value is found, and we return $\textit{true}$.
- If $\textit{matrix}[i][j] > \textit{target}$, it means all elements in this column from the current position upwards are greater than $\textit{target}$, so we move the $i$ pointer upwards, i.e., $i \leftarrow i - 1$.
- If $\textit{matrix}[i][j] < \textit{target}$, it means all elements in this row from the current position to the right are less than $\textit{target}$, so we move the $j$ pointer to the right, i.e., $j \leftarrow j + 1$.

If the search ends and the $\textit{target}$ is not found, return $\textit{false}$.

The time complexity is $O(m + n)$, and the space complexity is $O(1)$, where $m$ and $n$ are the number of rows and columns of the matrix, respectively.

### C++20 solution

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int i = m - 1, j = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] == target) {
                return true;
            }
            if (matrix[i][j] > target) {
                --i;
            } else {
                ++j;
            }
        }
        return false;
    }
};
```

---

<a id="lc-278"></a>
## 10. LC 278 — First Bad Version (Easy)

[Official problem](https://leetcode.com/problems/first-bad-version) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0278.First%20Bad%20Version/README_EN.md)

### Problem description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

### Constraints

- `1 <= bad <= n <= 2^31 - 1`

### Approach and complexity

We define the left boundary of the binary search as $l = 1$ and the right boundary as $r = n$.

While $l < r$, we calculate the middle position $\textit{mid} = \left\lfloor \frac{l + r}{2} \right\rfloor$, then call the `isBadVersion(mid)` API. If it returns $\textit{true}$, it means the first bad version is between $[l, \textit{mid}]$, so we set $r = \textit{mid}$; otherwise, the first bad version is between $[\textit{mid} + 1, r]$, so we set $l = \textit{mid} + 1$.

Finally, we return $l$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (isBadVersion(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};
```

---

<a id="lc-69"></a>
## 11. LC 69 — Sqrt(x) (Easy)

[Official problem](https://leetcode.com/problems/sqrtx) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0069.Sqrt%28x%29/README_EN.md)

### Problem description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

### Constraints

- `0 <= x <= 2^31 - 1`

### Approach and complexity

We define the left boundary of the binary search as $l = 0$ and the right boundary as $r = x$, then we search for the square root within the range $[l, r]$.

In each step of the search, we find the middle value $\textit{mid} = (l + r + 1) / 2$. If $\textit{mid} > x / \textit{mid}$, it means the square root is within the range $[l, \textit{mid} - 1]$, so we set $r = \textit{mid} - 1$. Otherwise, it means the square root is within the range $[\textit{mid}, r]$, so we set $l = \textit{mid}$.

After the search ends, we return $l$.

The time complexity is $O(\log x)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int mySqrt(int x) {
        int l = 0, r = x;
        while (l < r) {
            int mid = (l + r + 1ll) >> 1;
            if (mid > x / mid) {
                r = mid - 1;
            } else {
                l = mid;
            }
        }
        return l;
    }
};
```

---

<a id="lc-367"></a>
## 12. LC 367 — Valid Perfect Square (Easy)

[Official problem](https://leetcode.com/problems/valid-perfect-square) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0367.Valid%20Perfect%20Square/README_EN.md)

### Problem description

Given a positive integer num, return `true` if `num` is a perfect square or `false` otherwise.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

### Constraints

- `1 <= num <= 2^31 - 1`

### Approach and complexity

We can use binary search to solve this problem. Define the left boundary $l = 1$ and the right boundary $r = \textit{num}$ of the binary search, then find the smallest integer $x$ that satisfies $x^2 \geq \textit{num}$ in the range $[l, r]$. Finally, if $x^2 = \textit{num}$, then $\textit{num}$ is a perfect square.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the given number.

### C++20 solution

```cpp
class Solution {
public:
    bool isPerfectSquare(int num) {
        int l = 1, r = num;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (1LL * mid * mid >= num) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return 1LL * l * l == num;
    }
};
```

---

<a id="lc-875"></a>
## 13. LC 875 — Koko Eating Bananas (Medium)

[Official problem](https://leetcode.com/problems/koko-eating-bananas) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0875.Koko%20Eating%20Bananas/README_EN.md)

### Problem description

Koko loves to eat bananas. There are `n` piles of bananas, the `i^th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

### Constraints

- `1 <= piles.length <= 10^4`

- `piles.length <= h <= 10^9`

- `1 <= piles[i] <= 10^9`

### Approach and complexity

We notice that if Koko can eat all the bananas at a speed of $k$ within $h$ hours, then she can also eat all the bananas at a speed of $k' > k$ within $h$ hours. This shows monotonicity, so we can use binary search to find the smallest $k$ that satisfies the condition.

We define the left boundary of the binary search as $l = 1$, and the right boundary as $r = \max(\textit{piles})$. For each binary search, we take the middle value $\textit{mid} = \frac{l + r}{2}$, and then calculate the time $s$ required to eat bananas at a speed of $\textit{mid}$. If $s \leq h$, it means that the speed of $\textit{mid}$ can meet the condition, and we update the right boundary $r$ to $\textit{mid}$; otherwise, we update the left boundary $l$ to $\textit{mid} + 1$. Finally, when $l = r$, we find the smallest $k$ that satisfies the condition.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $n$ and $M$ are the length and maximum value of the array $\textit{piles}$ respectively.

### C++20 solution

```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = ranges::max(piles);
        while (l < r) {
            int mid = (l + r) >> 1;
            int s = 0;
            for (int x : piles) {
                s += (x + mid - 1) / mid;
            }
            if (s <= h) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};
```

---

<a id="lc-1011"></a>
## 14. LC 1011 — Capacity To Ship Packages Within D Days (Medium)

[Official problem](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1011.Capacity%20To%20Ship%20Packages%20Within%20D%20Days/README_EN.md)

### Problem description

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `i^th` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

### Constraints

- `1 <= days <= weights.length <= 5 * 10^4`

- `1 <= weights[i] <= 500`

### Approach and complexity

Binary-search capacity from the heaviest package to total weight. Greedily pack each day in order; a capacity is feasible iff this uses at most days days. Feasibility is monotone.

Time O(n log S); auxiliary space O(1), S=sum(weights).

### C++20 solution

```cpp
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int left = 0, right = 0;
        for (auto& w : weights) {
            left = max(left, w);
            right += w;
        }
        auto check = [&](int mx) {
            int ws = 0, cnt = 1;
            for (auto& w : weights) {
                ws += w;
                if (ws > mx) {
                    ws = w;
                    ++cnt;
                }
            }
            return cnt <= days;
        };
        while (left < right) {
            int mid = (left + right) >> 1;
            if (check(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

---

<a id="lc-410"></a>
## 15. LC 410 — Split Array Largest Sum (Hard)

[Official problem](https://leetcode.com/problems/split-array-largest-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0410.Split%20Array%20Largest%20Sum/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is **minimized**.

Return the minimized largest sum of the split.

A **subarray** is a contiguous part of the array.

### Constraints

- `1 <= nums.length <= 1000`

- `0 <= nums[i] <= 10^6`

- `1 <= k <= min(50, nums.length)`

### Approach and complexity

We notice that the larger the maximum sum of the subarrays, the fewer the number of subarrays. When there is a maximum sum of the subarrays that meets the condition, then a larger maximum sum of the subarrays will definitely meet the condition. This means that we can perform a binary search for the maximum sum of the subarrays to find the smallest value that meets the condition.

We define the left boundary of the binary search as $\textit{left} = \max(\textit{nums})$, and the right boundary as $\textit{right} = \textit{sum}(\textit{nums})$. Then for each step of the binary search, we take the middle value $\textit{mid} = \lfloor \frac{\textit{left} + \textit{right}}{2} \rfloor$, and then determine whether there is a way to split the array so that the maximum sum of the subarrays does not exceed $\textit{mid}$. If there is, it means that $\textit{mid}$ might be the smallest value that meets the condition, so we adjust the right boundary to $\textit{mid}$. Otherwise, we adjust the left boundary to $\textit{mid} + 1$.

How do we determine whether there is a way to split the array so that the maximum sum of the subarrays does not exceed $\textit{mid}$? We can use a greedy method, traverse the array from left to right, and add the elements of the array to the subarray one by one. If the current sum of the subarray is greater than $\textit{mid}$, then we add the current element to the next subarray. If we can split the array into no more than $k$ subarrays, and the maximum sum of each subarray does not exceed $\textit{mid}$, then $\textit{mid}$ is the smallest value that meets the condition. Otherwise, $\textit{mid}$ does not meet the condition.

The time complexity is $O(n \log m)$, and the space complexity is $O(1)$, where $n$ and $m$ are the length of the array and the sum of all elements in the array, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int left = 0, right = 0;
        for (int& x : nums) {
            left = max(left, x);
            right += x;
        }
        auto check = [&](int mx) {
            int s = 1 << 30, cnt = 0;
            for (int& x : nums) {
                s += x;
                if (s > mx) {
                    s = x;
                    ++cnt;
                }
            }
            return cnt <= k;
        };
        while (left < right) {
            int mid = (left + right) >> 1;
            if (check(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

---

<a id="lc-1482"></a>
## 16. LC 1482 — Minimum Number of Days to Make m Bouquets (Medium)

[Official problem](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1400-1499/1482.Minimum%20Number%20of%20Days%20to%20Make%20m%20Bouquets/README_EN.md)

### Problem description

You are given an integer array `bloomDay`, an integer `m` and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent flowers** from the garden.

The garden consists of `n` flowers, the `i^th` flower will bloom in the `bloomDay[i]` and then can be used in **exactly one** bouquet.

Return the **minimum** number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

### Constraints

- `bloomDay.length == n`

- `1 <= n <= 10^5`

- `1 <= bloomDay[i] <= 10^9`

- `1 <= m <= 10^6`

- `1 <= k <= n`

### Approach and complexity

According to the problem description, if a day $t$ can satisfy making $m$ bouquets, then for any $t' > t$, it can also satisfy making $m$ bouquets. Therefore, we can use binary search to find the minimum day that satisfies making $m$ bouquets.

Let $mx$ be the maximum blooming day in the garden. Next, we define the left boundary of the binary search as $l = 1$ and the right boundary as $r = mx + 1$.

Then, we perform binary search. For each middle value $\textit{mid} = \frac{l + r}{2}$, we check if it is possible to make $m$ bouquets. If it is possible, we update the right boundary $r$ to $\textit{mid}$; otherwise, we update the left boundary $l$ to $\textit{mid} + 1$.

Finally, when $l = r$, the binary search ends. At this point, if $l > mx$, it means it is not possible to make $m$ bouquets, and we return $-1$; otherwise, we return $l$.

Therefore, the problem is reduced to checking if a day $\textit{days}$ can make $m$ bouquets.

We can use a function $\textit{check}(\textit{days})$ to determine if it is possible to make $m$ bouquets. Specifically, we traverse each flower in the garden from left to right. If the blooming day of the current flower is less than or equal to $\textit{days}$, we add the current flower to the current bouquet; otherwise, we clear the current bouquet. When the number of flowers in the current bouquet equals $k$, we increment the bouquet count and clear the current bouquet. Finally, we check if the bouquet count is greater than or equal to $m$. If it is, it means it is possible to make $m$ bouquets; otherwise, it is not possible.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $n$ and $M$ are the number of flowers in the garden and the maximum blooming day, respectively. In this problem, $M \leq 10^9$.

### C++20 solution

```cpp
class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int mx = ranges::max(bloomDay);
        int l = 1, r = mx + 1;
        auto check = [&](int days) {
            int cnt = 0, cur = 0;
            for (int x : bloomDay) {
                cur = x <= days ? cur + 1 : 0;
                if (cur == k) {
                    cnt++;
                    cur = 0;
                }
            }
            return cnt >= m;
        };
        while (l < r) {
            int mid = (l + r) >> 1;
            if (check(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l > mx ? -1 : l;
    }
};
```

---

<a id="lc-1552"></a>
## 17. LC 1552 — Magnetic Force Between Two Balls (Medium)

[Official problem](https://leetcode.com/problems/magnetic-force-between-two-balls) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1500-1599/1552.Magnetic%20Force%20Between%20Two%20Balls/README_EN.md)

### Problem description

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has `n` empty baskets, the `i^th` basket is at `position[i]`, Morty has `m` balls and needs to distribute the balls into the baskets such that the **minimum magnetic force** between any two balls is **maximum**.

Rick stated that magnetic force between two different balls at positions `x` and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`. Return the required force.

### Constraints

- `n == position.length`

- `2 <= n <= 10^5`

- `1 <= position[i] <= 10^9`

- All integers in `position` are **distinct**.

- `2 <= m <= position.length`

### Approach and complexity

We notice that the greater the minimum magnetic force between any two balls, the fewer balls can be placed, which exhibits monotonicity. We can use binary search to find the maximum minimum magnetic force that allows the number of balls not less than $m$ to be placed.

First, we sort the positions of the baskets, and then use binary search with the left boundary $l = 1$ and the right boundary $r = \textit{position}[n - 1]$, where $n$ is the number of baskets. In each binary search iteration, we calculate the midpoint $m = (l + r + 1) / 2$, and then determine if there is a way to place the balls such that the number of balls placed is not less than $m$.

The problem is transformed into determining whether a given minimum magnetic force $f$ can place $m$ balls. We can traverse the positions of the baskets from left to right, and if the distance between the position of the last ball and the current basket's position is greater than or equal to $f$, it indicates that a ball can be placed in the current basket. Finally, we check if the number of balls placed is not less than $m$.

The time complexity is $O(n \log n + n \log M)$, and the space complexity is $O(\log n)$, where $n$ and $M$ respectively represent the number of baskets and the maximum value of the basket positions.

### C++20 solution

```cpp
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        ranges::sort(position);
        int l = 1, r = position.back();
        auto count = [&](int f) {
            int prev = position[0];
            int cnt = 1;
            for (int& curr : position) {
                if (curr - prev >= f) {
                    prev = curr;
                    cnt++;
                }
            }
            return cnt;
        };
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (count(mid) >= m) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }
};
```

---

<a id="lc-1760"></a>
## 18. LC 1760 — Minimum Limit of Balls in a Bag (Medium)

[Official problem](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1760.Minimum%20Limit%20of%20Balls%20in%20a%20Bag/README_EN.md)

### Problem description

You are given an integer array `nums` where the `i^th` bag contains `nums[i]` balls. You are also given an integer `maxOperations`.

You can perform the following operation at most `maxOperations` times:

- Take any bag of balls and divide it into two new bags with a **positive **number of balls.

- For example, a bag of `5` balls can become two new bags of `1` and `4` balls, or two new bags of `2` and `3` balls.

Your penalty is the **maximum** number of balls in a bag. You want to **minimize** your penalty after the operations.

Return the minimum possible penalty after performing the operations.

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= maxOperations, nums[i] <= 10^9`

### Approach and complexity

This problem requires us to minimize the cost, which is the maximum number of balls in a single bag. As the maximum value increases, the number of operations decreases, making it easier to meet the condition.

Therefore, we can use binary search to enumerate the maximum number of balls in a single bag and determine if it can be achieved within $\textit{maxOperations}$ operations.

Specifically, we define the left boundary of the binary search as $l = 1$ and the right boundary as $r = \max(\textit{nums})$. Then we continuously perform binary search on the middle value $\textit{mid} = \frac{l + r}{2}$. For each $\textit{mid}$, we calculate the number of operations needed. If the number of operations is less than or equal to $\textit{maxOperations}$, it means $\textit{mid}$ meets the condition, and we update the right boundary $r$ to $\textit{mid}$. Otherwise, we update the left boundary $l$ to $\textit{mid} + 1$.

Finally, we return the left boundary $l$.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $n$ and $M$ are the length and the maximum value of the array $\textit{nums}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int l = 1, r = ranges::max(nums);
        while (l < r) {
            int mid = (l + r) >> 1;
            long long s = 0;
            for (int x : nums) {
                s += (x - 1) / mid;
            }
            if (s <= maxOperations) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};
```

---

<a id="lc-2187"></a>
## 19. LC 2187 — Minimum Time to Complete Trips (Medium)

[Official problem](https://leetcode.com/problems/minimum-time-to-complete-trips) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2100-2199/2187.Minimum%20Time%20to%20Complete%20Trips/README_EN.md)

### Problem description

You are given an array `time` where `time[i]` denotes the time taken by the `i^th` bus to complete **one trip**.

Each bus can make multiple trips **successively**; that is, the next trip can start **immediately after** completing the current trip. Also, each bus operates **independently**; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer `totalTrips`, which denotes the number of trips all buses should make **in total**. Return the **minimum time** required for all buses to complete **at least** `totalTrips` trips.

### Constraints

- `1 <= time.length <= 10^5`

- `1 <= time[i], totalTrips <= 10^7`

### Approach and complexity

We notice that if we can complete at least $\textit{totalTrips}$ trips in $t$ time, then we can also complete at least $\textit{totalTrips}$ trips in $t' > t$ time. Therefore, we can use the method of binary search to find the smallest $t$.

We define the left boundary of the binary search as $l = 1$, and the right boundary as $r = \min(\textit{time}) \times \textit{totalTrips}$. For each binary search, we calculate the middle value $\textit{mid} = \frac{l + r}{2}$, and then calculate the number of trips that can be completed in $\textit{mid}$ time. If this number is greater than or equal to $\textit{totalTrips}$, then we reduce the right boundary to $\textit{mid}$, otherwise we increase the left boundary to $\textit{mid} + 1$.

Finally, return the left boundary.

The time complexity is $O(n \log(mk))$, and the space complexity is $O(1)$, where $n$ and $k$ are the length of the array $\textit{time}$ and $\textit{totalTrips}$ respectively, and $m$ is the minimum value in the array $\textit{time}$.

### C++20 solution

```cpp
class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        int mi = *min_element(time.begin(), time.end());
        long long left = 1, right = 1LL * mi * totalTrips;
        while (left < right) {
            long long cnt = 0;
            long long mid = (left + right) >> 1;
            for (int v : time) {
                cnt += mid / v;
            }
            if (cnt >= totalTrips) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

---

<a id="lc-2226"></a>
## 20. LC 2226 — Maximum Candies Allocated to K Children (Medium)

[Official problem](https://leetcode.com/problems/maximum-candies-allocated-to-k-children) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2200-2299/2226.Maximum%20Candies%20Allocated%20to%20K%20Children/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `candies`. Each element in the array denotes a pile of candies of size `candies[i]`. You can divide each pile into any number of **sub piles**, but you **cannot** merge two piles together.

You are also given an integer `k`. You should allocate piles of candies to `k` children such that each child gets the **same** number of candies. Each child can be allocated candies from **only one** pile of candies and some piles of candies may go unused.

Return the **maximum number of candies** each child can get.

### Constraints

- `1 <= candies.length <= 10^5`

- `1 <= candies[i] <= 10^7`

- `1 <= k <= 10^12`

### Approach and complexity

We notice that if each child can receive $v$ candies, then for any $v' \lt v$, each child can also receive $v'$ candies. Therefore, we can use binary search to find the maximum $v$ such that each child can receive $v$ candies.

We define the left boundary of the binary search as $l = 0$ and the right boundary as $r = \max(\textit{candies})$, where $\max(\textit{candies})$ represents the maximum value in the array $\textit{candies}$. During the binary search, we take the middle value $v = \left\lfloor \frac{l + r + 1}{2} \right\rfloor$ each time, and then calculate the total number of candies each child can receive. If the total is greater than or equal to $k$, it means each child can receive $v$ candies, so we update the left boundary $l = v$. Otherwise, we update the right boundary $r = v - 1$. Finally, when $l = r$, we have found the maximum $v$.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{candies}$, and $M$ is the maximum value in the array $\textit{candies}$.

### C++20 solution

```cpp
class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        int l = 0, r = ranges::max(candies);
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            long long cnt = 0;
            for (int x : candies) {
                cnt += x / mid;
            }
            if (cnt >= k) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }
};
```

---

<a id="lc-4"></a>
## 21. LC 4 — Median of Two Sorted Arrays (Hard)

[Official problem](https://leetcode.com/problems/median-of-two-sorted-arrays) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0004.Median%20of%20Two%20Sorted%20Arrays/README_EN.md)

### Problem description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

### Constraints

- `nums1.length == m`

- `nums2.length == n`

- `0 <= m <= 1000`

- `0 <= n <= 1000`

- `1 <= m + n <= 2000`

- `-10^6 <= nums1[i], nums2[i] <= 10^6`

### Approach and complexity

Partition the shorter array and derive the matching partition in the longer array. Move the partition until both left maxima are at most the opposite right minima. Then the two middle values are at the partition boundaries. Sentinels handle empty sides.

Time O(log(min(m,n)+1)); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& a, vector<int>& b) {
        if (a.size() > b.size()) return findMedianSortedArrays(b, a);
        int m = a.size(), n = b.size(), lo = 0, hi = m;
        while (lo <= hi) {
            int i = std::midpoint(lo, hi), j = (m + n + 1) / 2 - i;
            int al = i ? a[i - 1] : INT_MIN;
            int ar = i < m ? a[i] : INT_MAX;
            int bl = j ? b[j - 1] : INT_MIN;
            int br = j < n ? b[j] : INT_MAX;
            if (al <= br && bl <= ar) {
                if ((m + n) % 2) return max(al, bl);
                return (static_cast<double>(max(al, bl)) + min(ar, br)) / 2;
            }
            if (al > br) hi = i - 1;
            else lo = i + 1;
        }
        return 0; // Unreachable for the specified sorted, nonempty combined input.
    }
};
```

---

<a id="lc-162"></a>
## 22. LC 162 — Find Peak Element (Medium)

[Official problem](https://leetcode.com/problems/find-peak-element) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0162.Find%20Peak%20Element/README_EN.md)

### Problem description

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

### Constraints

- `1 <= nums.length <= 1000`

- `-2^31 <= nums[i] <= 2^31 - 1`

- `nums[i] != nums[i + 1]` for all valid `i`.

### Approach and complexity

We define the left boundary of binary search as $\textit{left}=0$ and the right boundary as $\textit{right}=n-1$, where $n$ is the length of the array. In each step of binary search, we find the middle element $\textit{mid}$ of the current interval, and compare the values of $\textit{mid}$ and its right neighbor $\textit{mid}+1$:

- If the value of $\textit{mid}$ is greater than the value of $\textit{mid}+1$, there exists a peak element on the left side, and we update the right boundary $\textit{right}$ to $\textit{mid}$.
- Otherwise, there exists a peak element on the right side, and we update the left boundary $\textit{left}$ to $\textit{mid}+1$.
- Finally, when the left boundary $\textit{left}$ is equal to the right boundary $\textit{right}$, we have found the peak element of the array.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$. Each step of binary search can reduce the search interval by half, so the time complexity is $O(\log n)$.

### C++20 solution

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + right >> 1;
            if (nums[mid] > nums[mid + 1]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

---

<a id="lc-852"></a>
## 23. LC 852 — Peak Index in a Mountain Array (Medium)

[Official problem](https://leetcode.com/problems/peak-index-in-a-mountain-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0852.Peak%20Index%20in%20a%20Mountain%20Array/README_EN.md)

### Problem description

You are given an integer **mountain** array `arr` of length `n` where the values increase to a **peak element** and then decrease.

Return the index of the peak element.

Your task is to solve it in `O(log(n))` time complexity.

### Constraints

- `3 <= arr.length <= 10^5`

- `0 <= arr[i] <= 10^6`

- `arr` is **guaranteed** to be a mountain array.

### Approach and complexity

On the rising slope, the peak lies to the right; on the falling slope, it lies at or to the left of midpoint. Binary search preserves an interval containing the peak.

Time O(log n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int left = 1, right = arr.size() - 2;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (arr[mid] > arr[mid + 1])
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
```

---

<a id="lc-1095"></a>
## 24. LC 1095 — Find in Mountain Array (Hard)

[Official problem](https://leetcode.com/problems/find-in-mountain-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1095.Find%20in%20Mountain%20Array/README_EN.md)

### Problem description

(This problem is an **interactive problem**.)

You may recall that an array `arr` is a **mountain array** if and only if:

- `arr.length >= 3`

- There exists some `i` with `0 < i < arr.length - 1` such that:

- `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`

- `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `mountainArr`, return the **minimum** `index` such that `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

**You cannot access the mountain array directly.** You may only access the array using a `MountainArray` interface:

- `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).

- `MountainArray.length()` returns the length of the array.

Submissions making more than `100` calls to `MountainArray.get` will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

### Constraints

- `3 <= mountainArr.length() <= 10^4`

- `0 <= target <= 10^9`

- `0 <= mountainArr.get(index) <= 10^9`

### Approach and complexity

Binary-search the peak, then search ascending and descending halves separately. Search the ascending half first to obtain the minimum valid index. Cache get calls when necessary to satisfy the API limit.

Time O(log n) MountainArray queries; auxiliary space O(1) without caching.

### C++20 solution

```cpp
class Solution {
public:
    int findInMountainArray(int target, MountainArray& mountainArr) {
        int n = mountainArr.length();
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (mountainArr.get(mid) > mountainArr.get(mid + 1)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        auto search = [&](int l, int r, int k) -> int {
            while (l < r) {
                int mid = (l + r) >> 1;
                if (k * mountainArr.get(mid) >= k * target) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            return mountainArr.get(l) == target ? l : -1;
        };
        int ans = search(0, l, 1);
        return ans == -1 ? search(l + 1, n - 1, -1) : ans;
    }
};
```

---

<a id="lc-540"></a>
## 25. LC 540 — Single Element in a Sorted Array (Medium)

[Official problem](https://leetcode.com/problems/single-element-in-a-sorted-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0540.Single%20Element%20in%20a%20Sorted%20Array/README_EN.md)

### Problem description

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in `O(log n)` time and `O(1)` space.

### Constraints

- `1 <= nums.length <= 10^5`

- `0 <= nums[i] <= 10^5`

### Approach and complexity

The given array $\textit{nums}$ is sorted, and we need to find the element that appears only once in $O(\log n)$ time. Therefore, we consider using binary search to solve this problem.

We define the left boundary of the binary search as $l = 0$ and the right boundary as $r = n - 1$, where $n$ is the length of the array.

In each step, we take the middle position $\textit{mid} = (l + r) / 2$. If the index $\textit{mid}$ is even, we should compare $\textit{nums}[\textit{mid}]$ with $\textit{nums}[\textit{mid} + 1]$. If the index $\textit{mid}$ is odd, we should compare $\textit{nums}[\textit{mid}]$ with $\textit{nums}[\textit{mid} - 1]$. Therefore, we can uniformly compare $\textit{nums}[\textit{mid}]$ with $\textit{nums}[\textit{mid} \oplus 1]$, where $\oplus$ denotes the XOR operation.

If $\textit{nums}[\textit{mid}] \neq \textit{nums}[\textit{mid} \oplus 1]$, then the answer is in $[l, \textit{mid}]$, so we set $r = \textit{mid}$. If $\textit{nums}[\textit{mid}] = \textit{nums}[\textit{mid} \oplus 1]$, then the answer is in $[\textit{mid} + 1, r]$, so we set $l = \textit{mid} + 1$. We continue the binary search until $l = r$, at which point $\textit{nums}[l]$ is the element that appears only once.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] != nums[mid ^ 1]) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return nums[l];
    }
};
```

---

<a id="lc-658"></a>
## 26. LC 658 — Find K Closest Elements (Medium)

[Official problem](https://leetcode.com/problems/find-k-closest-elements) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0658.Find%20K%20Closest%20Elements/README_EN.md)

### Problem description

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

- `|a - x| < |b - x|`, or

- `|a - x| == |b - x|` and `a < b`

### Constraints

- `1 <= k <= arr.length`

- `1 <= arr.length <= 10^4`

- `arr` is sorted in **ascending** order.

- `-10^4 <= arr[i], x <= 10^4`

### Approach and complexity

On top of method 2, binary-search the left boundary of the window of length $k$ over $[0, n - k]$. At $\textit{mid}$, move the window left when $x - \textit{arr}[\textit{mid}] \le \textit{arr}[\textit{mid} + k] - x$, and right otherwise.

The time complexity is $O(\log n)$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size() - k;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (x - arr[mid] <= arr[mid + k] - x)
                right = mid;
            else
                left = mid + 1;
        }
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};
```

---

<a id="lc-378"></a>
## 27. LC 378 — Kth Smallest Element in a Sorted Matrix (Medium)

[Official problem](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0378.Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix/README_EN.md)

### Problem description

Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return the `k^th` smallest element in the matrix.

Note that it is the `k^th` smallest element **in the sorted order**, not the `k^th` **distinct** element.

You must find a solution with a memory complexity better than `O(n^2)`.

### Constraints

- `n == matrix.length == matrix[i].length`

- `1 <= n <= 300`

- `-10^9 <= matrix[i][j] <= 10^9`

- All the rows and columns of `matrix` are **guaranteed** to be sorted in **non-decreasing order**.

- `1 <= k <= n^2`

**Follow up:**

- Could you solve the problem with a constant memory (i.e., `O(1)` memory complexity)?

- Could you solve the problem in `O(n)` time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

### Approach and complexity

Binary-search the value of the kth element. Count entries at most the midpoint with a monotone row/column staircase. The first value whose count reaches k is the answer.

Time O(n log R); auxiliary space O(1), where R=max−min+1.

### C++20 solution

```cpp
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int left = matrix[0][0], right = matrix[n - 1][n - 1];
        while (left < right) {
            int mid = left + right >> 1;
            if (check(matrix, mid, k, n)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

private:
    bool check(vector<vector<int>>& matrix, int mid, int k, int n) {
        int count = 0;
        int i = n - 1, j = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] <= mid) {
                count += (i + 1);
                ++j;
            } else {
                --i;
            }
        }
        return count >= k;
    }
};
```

---

<a id="lc-719"></a>
## 28. LC 719 — Find K-th Smallest Pair Distance (Hard)

[Official problem](https://leetcode.com/problems/find-k-th-smallest-pair-distance) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0719.Find%20K-th%20Smallest%20Pair%20Distance/README_EN.md)

### Problem description

The **distance of a pair** of integers `a` and `b` is defined as the absolute difference between `a` and `b`.

Given an integer array `nums` and an integer `k`, return the `k^th` smallest **distance among all the pairs** `nums[i]` and `nums[j]` where `0 <= i < j < nums.length`.

### Constraints

- `n == nums.length`

- `2 <= n <= 10^4`

- `0 <= nums[i] <= 10^6`

- `1 <= k <= n * (n - 1) / 2`

### Approach and complexity

Sort values and binary-search distance. A sliding left pointer counts pairs whose difference is at most a trial distance in linear time. Find the smallest distance with at least k pairs.

Time O(n log n+n log R); auxiliary space O(log n) for sorting, R=max−min+1.

### C++20 solution

```cpp
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        ranges::sort(nums);
        int left = 0, right = nums.back() - nums.front();
        while (left < right) {
            int mid = (left + right) >> 1;
            if (count(mid, k, nums) >= k)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }

    int count(int dist, int k, vector<int>& nums) {
        int cnt = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int target = nums[i] - dist;
            int j = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
            cnt += i - j;
        }
        return cnt;
    }
};
```

---

<a id="lc-668"></a>
## 29. LC 668 — Kth Smallest Number in Multiplication Table (Hard)

[Official problem](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0668.Kth%20Smallest%20Number%20in%20Multiplication%20Table/README_EN.md)

### Problem description

Nearly everyone has used the Multiplication Table. The multiplication table of size `m x n` is an integer matrix `mat` where `mat[i][j] == i * j` (**1-indexed**).

Given three integers `m`, `n`, and `k`, return the `k^th` smallest element in the `m x n` multiplication table.

### Constraints

- `1 <= m, n <= 3 * 10^4`

- `1 <= k <= m * n`

### Approach and complexity

Binary-search the answer. Row i of the multiplication table contributes min(n,floor(mid/i)) entries at most mid. The first value whose total count reaches k is the answer.

Time O(m log(mn)); auxiliary space O(1). Swapping dimensions can use min(m,n) rows.

### C++20 solution

```cpp
class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        int left = 1, right = m * n;
        while (left < right) {
            int mid = (left + right) >> 1;
            int cnt = 0;
            for (int i = 1; i <= m; ++i) cnt += min(mid / i, n);
            if (cnt >= k)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
```

---

<a id="lc-786"></a>
## 30. LC 786 — K-th Smallest Prime Fraction (Hard)

[Official problem](https://leetcode.com/problems/k-th-smallest-prime-fraction) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0786.K-th%20Smallest%20Prime%20Fraction/README_EN.md)

### Problem description

You are given a sorted integer array `arr` containing `1` and **prime** numbers, where all the integers of `arr` are unique. You are also given an integer `k`.

For every `i` and `j` where `0 <= i < j < arr.length`, we consider the fraction `arr[i] / arr[j]`.

Return the `k^th` smallest fraction considered. Return your answer as an array of integers of size `2`, where `answer[0] == arr[i]` and `answer[1] == arr[j]`.

### Constraints

- `2 <= arr.length <= 1000`

- `1 <= arr[i] <= 3 * 10^4`

- `arr[0] == 1`

- `arr[i]` is a **prime** number for `i > 0`.

- All the numbers of `arr` are **unique** and sorted in **strictly increasing** order.

- `1 <= k <= arr.length * (arr.length - 1) / 2`

**Follow up:** Can you solve the problem with better than `O(n^2)` complexity?

### Approach and complexity

Each denominator yields a sorted sequence of fractions as its numerator increases. Seed a min heap with the smallest fraction for each denominator; pop k times, advancing that sequence after each pop.

Time O((n+k) log n); auxiliary space O(n). Compare fractions by cross multiplication to avoid precision loss.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        using pii = pair<int, int>;
        int n = arr.size();
        auto cmp = [&](const pii& a, const pii& b) {
            return arr[a.first] * arr[b.second] > arr[b.first] * arr[a.second];
        };
        priority_queue<pii, vector<pii>, decltype(cmp)> pq(cmp);
        for (int i = 1; i < n; ++i) {
            pq.push({0, i});
        }
        for (int i = 1; i < k; ++i) {
            pii f = pq.top();
            pq.pop();
            if (f.first + 1 < f.second) {
                pq.push({f.first + 1, f.second});
            }
        }
        return {arr[pq.top().first], arr[pq.top().second]};
    }
};
```

---

<a id="lc-300"></a>
## 31. LC 300 — Longest Increasing Subsequence (Medium)

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

<a id="lc-354"></a>
## 32. LC 354 — Russian Doll Envelopes (Hard)

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

<a id="lc-436"></a>
## 33. LC 436 — Find Right Interval (Medium)

[Official problem](https://leetcode.com/problems/find-right-interval) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0436.Find%20Right%20Interval/README_EN.md)

### Problem description

You are given an array of `intervals`, where `intervals[i] = [start_i, end_i]` and each `start_i` is **unique**.

The **right interval** for an interval `i` is an interval `j` such that `start_j >= end_i` and `start_j` is **minimized**. Note that `i` may equal `j`.

Return an array of **right interval** indices for each interval `i`. If no **right interval** exists for interval `i`, then put `-1` at index `i`.

### Constraints

- `1 <= intervals.length <= 2 * 10^4`

- `intervals[i].length == 2`

- `-10^6 <= start_i <= end_i <= 10^6`

- The start point of each interval is **unique**.

### Approach and complexity

We can store the start point and index of each interval into an array `arr`, and sort it by the start point. Then we iterate through the interval array, for each interval `[_, ed]`, we can use binary search to find the first interval whose start point is greater than or equal to `ed`, which is its right-side interval. If found, we store its index into the answer array, otherwise, we store `-1`.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the intervals.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<pair<int, int>> arr;
        for (int i = 0; i < n; ++i) {
            arr.emplace_back(intervals[i][0], i);
        }
        ranges::sort(arr);
        vector<int> ans;
        for (auto& e : intervals) {
            int j = lower_bound(arr.begin(), arr.end(), make_pair(e[1], -1)) - arr.begin();
            ans.push_back(j == n ? -1 : arr[j].second);
        }
        return ans;
    }
};
```

---

<a id="lc-475"></a>
## 34. LC 475 — Heaters (Medium)

[Official problem](https://leetcode.com/problems/heaters) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0475.Heaters/README_EN.md)

### Problem description

Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of `houses` and `heaters` on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

**Notice** that all the `heaters` follow your radius standard, and the warm radius will be the same.

### Constraints

- `1 <= houses.length, heaters.length <= 3 * 10^4`

- `1 <= houses[i], heaters[i] <= 10^9`

### Approach and complexity

Sort heater positions. For each house, lower_bound finds its first heater on the right; compare it with the preceding heater on the left. The maximum of these nearest distances is the required radius.

Time O(h log h+n log h); auxiliary space O(log h) for sorting. Houses are left unchanged.

### C++20 solution

```cpp
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        ranges::sort(heaters);
        int radius = 0;
        for (int house : houses) {
            auto right = ranges::lower_bound(heaters, house);
            int distance = INT_MAX;
            if (right != heaters.end()) distance = *right - house;
            if (right != heaters.begin()) distance = min(distance, house - *prev(right));
            radius = max(radius, distance);
        }
        return radius;
    }
};
```

---

<a id="lc-611"></a>
## 35. LC 611 — Valid Triangle Number (Medium)

[Official problem](https://leetcode.com/problems/valid-triangle-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0611.Valid%20Triangle%20Number/README_EN.md)

### Problem description

Given an integer array `nums`, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

### Constraints

- `1 <= nums.length <= 1000`

- `0 <= nums[i] <= 1000`

### Approach and complexity

A valid triangle must satisfy: **the sum of any two sides is greater than the third side**. That is:

$$a + b \gt c \tag{1}$$

$$a + c \gt b \tag{2}$$

$$b + c \gt a \tag{3}$$

If we arrange the sides in ascending order, i.e., $a \leq b \leq c$, then obviously conditions (2) and (3) are satisfied. We only need to ensure that condition (1) is also satisfied to form a valid triangle.

We enumerate $i$ in the range $[0, n - 3]$, enumerate $j$ in the range $[i + 1, n - 2]$, and perform binary search in the range $[j + 1, n - 1]$ to find the first index $\textit{left}$ that is greater than or equal to $\textit{nums}[i] + \textit{nums}[j]$. Then, the values of $k$ in the range $[j + 1, \textit{left} - 1]$ satisfy the condition, and we add them to the result $\textit{ans}$.

The time complexity is $O(n^2 \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        ranges::sort(nums);
        int ans = 0, n = nums.size();
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                int sum = nums[i] + nums[j];
                auto it = ranges::lower_bound(nums.begin() + j + 1, nums.end(), sum);
                int k = int(it - nums.begin()) - 1;
                ans += max(0, k - j);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-167"></a>
## 36. LC 167 — Two Sum II - Input Array Is Sorted (Medium)

[Official problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0167.Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted/README_EN.md)

### Problem description

You are given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**.

Find **two** numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index_1]` and `numbers[index_2]` where `1 <= index_1 < index_2 <= numbers.length`.

Return the indices of the two numbers `index_1` and `index_2` as an integer array `[index_1, index_2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

### Constraints

- `2 <= numbers.length <= 3 * 10^4`

- `-1000 <= numbers[i] <= 1000`

- `numbers` is sorted in **non-decreasing order**.

- `-1000 <= target <= 1000`

- The tests are generated such that there is **exactly one solution**.

### Approach and complexity

Note that the array is sorted in non-decreasing order, so for each `numbers[i]`, we can find the position of `target - numbers[i]` by binary search, and return $[i + 1, j + 1]$ if it exists.

The time complexity is $O(n \log n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{numbers}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i = 0, n = numbers.size();; ++i) {
            int x = target - numbers[i];
            int j = lower_bound(numbers.begin() + i + 1, numbers.end(), x) - numbers.begin();
            if (j < n && numbers[j] == x) {
                return {i + 1, j + 1};
            }
        }
    }
};
```

---

<a id="lc-209"></a>
## 37. LC 209 — Minimum Size Subarray Sum (Medium)

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

<a id="lc-2300"></a>
## 38. LC 2300 — Successful Pairs of Spells and Potions (Medium)

[Official problem](https://leetcode.com/problems/successful-pairs-of-spells-and-potions) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2300.Successful%20Pairs%20of%20Spells%20and%20Potions/README_EN.md)

### Problem description

You are given two positive integer arrays `spells` and `potions`, of length `n` and `m` respectively, where `spells[i]` represents the strength of the `i^th` spell and `potions[j]` represents the strength of the `j^th` potion.

You are also given an integer `success`. A spell and potion pair is considered **successful** if the **product** of their strengths is **at least** `success`.

Return an integer array `pairs` of length `n` where `pairs[i]` is the number of **potions** that will form a successful pair with the `i^th` spell.

### Constraints

- `n == spells.length`

- `m == potions.length`

- `1 <= n, m <= 10^5`

- `1 <= spells[i], potions[i] <= 10^5`

- `1 <= success <= 10^10`

### Approach and complexity

We can sort the potion array, then traverse the spell array. For each spell $v$, we use binary search to find the first potion that is greater than or equal to $\frac{\textit{success}}{v}$. We mark its index as $i$. The length of the potion array minus $i$ is the number of potions that can successfully combine with this spell.

The time complexity is $O((m + n) \log m)$, and the space complexity is $O(\log n)$, where $m$ and $n$ are the lengths of the potion array and the spell array, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        ranges::sort(potions);
        const int m = potions.size();
        vector<int> ans;
        ans.reserve(spells.size());

        for (int v : spells) {
            auto it = ranges::lower_bound(potions, static_cast<double>(success) / v);
            ans.push_back(m - static_cast<int>(it - potions.begin()));
        }
        return ans;
    }
};
```

---

<a id="lc-2563"></a>
## 39. LC 2563 — Count the Number of Fair Pairs (Medium)

[Official problem](https://leetcode.com/problems/count-the-number-of-fair-pairs) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2500-2599/2563.Count%20the%20Number%20of%20Fair%20Pairs/README_EN.md)

### Problem description

Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return the number of fair pairs.

A pair `(i, j)` is fair if:

- `0 <= i < j < n`, and

- `lower <= nums[i] + nums[j] <= upper`

### Constraints

- `1 <= nums.length <= 10^5`

- `nums.length == n`

- `-10^9 <= nums[i] <= 10^9`

- `-10^9 <= lower <= upper <= 10^9`

### Approach and complexity

First, we sort the array $\textit{nums}$ in ascending order. Then, for each `nums[i]`, we use binary search to find the lower bound `j` of `nums[j]`, i.e., the first index that satisfies `nums[j] >= lower - nums[i]`. Then, we use binary search again to find the lower bound `k` of `nums[k]`, i.e., the first index that satisfies `nums[k] >= upper - nums[i] + 1`. Therefore, `[j, k)` is the index range for `nums[j]` that satisfies `lower <= nums[i] + nums[j] <= upper`. The count of these indices corresponding to `nums[j]` is `k - j`, and we can add this to the answer. Note that $j > i$.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        long long ans = 0;
        ranges::sort(nums);
        for (int i = 0; i < nums.size(); ++i) {
            auto j = lower_bound(nums.begin() + i + 1, nums.end(), lower - nums[i]);
            auto k = lower_bound(nums.begin() + i + 1, nums.end(), upper - nums[i] + 1);
            ans += k - j;
        }
        return ans;
    }
};
```

---

<a id="lc-981"></a>
## 40. LC 981 — Time Based Key-Value Store (Medium)

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

<a id="lc-1146"></a>
## 41. LC 1146 — Snapshot Array (Medium)

[Official problem](https://leetcode.com/problems/snapshot-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1100-1199/1146.Snapshot%20Array/README_EN.md)

### Problem description

Implement a SnapshotArray that supports the following interface:

- `SnapshotArray(int length)` initializes an array-like data structure with the given length. **Initially, each element equals 0**.

- `void set(index, val)` sets the element at the given `index` to be equal to `val`.

- `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.

- `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

### Constraints

- `1 <= length <= 5 * 10^4`

- `0 <= index < length`

- `0 <= val <= 10^9`

- `0 <= snap_id < `(the total number of times we call `snap()`)

- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

### Approach and complexity

We maintain an array of length `length`. Each element in the array is a list, which is used to store the value set each time and the corresponding snapshot ID.

When the $\textit{set}$ method is called, we add the value and snapshot ID to the list at the corresponding index. The time complexity is $O(1)$.

When the $\textit{snap}$ method is called, we first increment the snapshot ID, then return the snapshot ID minus one. The time complexity is $O(1)$.

When the $\textit{get}$ method is called, we use binary search to find the first snapshot ID greater than $\textit{snap\_id}$ at the corresponding position, and then return the previous value. If it cannot be found, return 0. The time complexity is $O(\log n)$.

The space complexity is $O(n)$.

### C++20 solution

```cpp
class SnapshotArray {
public:
    SnapshotArray(int length) {
        arr.resize(length);
    }

    void set(int index, int val) {
        arr[index].emplace_back(i, val);
    }

    int snap() {
        return i++;
    }

    int get(int index, int snap_id) {
        auto it = upper_bound(arr[index].begin(), arr[index].end(), make_pair(snap_id, INT_MAX));
        return it == arr[index].begin() ? 0 : prev(it)->second;
    }

private:
    vector<vector<pair<int, int>>> arr;
    int i = 0;
};
```

---

<a id="lc-911"></a>
## 42. LC 911 — Online Election (Medium)

[Official problem](https://leetcode.com/problems/online-election) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0911.Online%20Election/README_EN.md)

### Problem description

You are given two integer arrays `persons` and `times`. In an election, the `i^th` vote was cast for `persons[i]` at time `times[i]`.

For each query at a time `t`, find the person that was leading the election at time `t`. Votes cast at time `t` will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the `TopVotedCandidate` class:

- `TopVotedCandidate(int[] persons, int[] times)` Initializes the object with the `persons` and `times` arrays.

- `int q(int t)` Returns the number of the person that was leading the election at time `t` according to the mentioned rules.

### Constraints

- `1 <= persons.length <= 5000`

- `times.length == persons.length`

- `0 <= persons[i] < persons.length`

- `0 <= times[i] <= 10^9`

- `times` is sorted in a strictly increasing order.

- `times[0] <= t <= 10^9`

- At most `10^4` calls will be made to `q`.

### Approach and complexity

We can record the winner at each moment during initialization, and then use binary search to find the largest moment less than or equal to $t$ during the query, and return the winner at that moment.

During initialization, we use a counter $\textit{cnt}$ to record the votes of each candidate, and a variable $\textit{cur}$ to record the current leading candidate. Then we traverse each moment, update $\textit{cnt}$ and $\textit{cur}$, and record the winner at each moment.

During the query, we use binary search to find the largest moment less than or equal to $t$, and return the winner at that moment.

In terms of time complexity, during initialization, we need $O(n)$ time, and during the query, we need $O(\log n)$ time. The space complexity is $O(n)$.

### C++20 solution

```cpp
class TopVotedCandidate {
public:
    TopVotedCandidate(vector<int>& persons, vector<int>& times) {
        int n = persons.size();
        this->times = times;
        wins.resize(n);
        vector<int> cnt(n);
        int cur = 0;
        for (int i = 0; i < n; ++i) {
            int p = persons[i];
            ++cnt[p];
            if (cnt[cur] <= cnt[p]) {
                cur = p;
            }
            wins[i] = cur;
        }
    }

    int q(int t) {
        int i = upper_bound(times.begin(), times.end(), t) - times.begin() - 1;
        return wins[i];
    }

private:
    vector<int> times;
    vector<int> wins;
};
```

---

<a id="lc-528"></a>
## 43. LC 528 — Random Pick with Weight (Medium)

[Official problem](https://leetcode.com/problems/random-pick-with-weight) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0528.Random%20Pick%20with%20Weight/README_EN.md)

### Problem description

You are given a **0-indexed** array of positive integers `w` where `w[i]` describes the **weight** of the `i^th` index.

You need to implement the function `pickIndex()`, which **randomly** picks an index in the range `[0, w.length - 1]` (**inclusive**) and returns it. The **probability** of picking an index `i` is `w[i] / sum(w)`.

- For example, if `w = [1, 3]`, the probability of picking index `0` is `1 / (1 + 3) = 0.25` (i.e., `25%`), and the probability of picking index `1` is `3 / (1 + 3) = 0.75` (i.e., `75%`).

### Constraints

- `1 <= w.length <= 10^4`

- `1 <= w[i] <= 10^5`

- `pickIndex` will be called at most `10^4` times.

### Approach and complexity

Prefix sums partition [1,total] into weight-sized blocks. Draw uniformly with uniform_int_distribution and locate the first prefix at least the sample. Each block has exactly its weight’s number of equally likely integers.

Initialization O(n); pickIndex O(log n); persistent space O(n).

### C++20 solution

```cpp
class Solution {
    vector<long long> prefix;
    mt19937 engine{random_device{}()};
public:
    Solution(vector<int>& w) {
        long long sum = 0;
        for (int weight : w) prefix.push_back(sum += weight);
    }
    int pickIndex() {
        long long value = uniform_int_distribution<long long>(1, prefix.back())(engine);
        return ranges::lower_bound(prefix, value) - prefix.begin();
    }
};
```

---

<a id="lc-729"></a>
## 44. LC 729 — My Calendar I (Medium)

[Official problem](https://leetcode.com/problems/my-calendar-i) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0729.My%20Calendar%20I/README_EN.md)

### Problem description

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a **double booking**.

A **double booking** happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers `startTime` and `endTime` that represents a booking on the half-open interval `[startTime, endTime)`, the range of real numbers `x` such that `startTime <= x < endTime`.

Implement the `MyCalendar` class:

- `MyCalendar()` Initializes the calendar object.

- `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a **double booking**. Otherwise, return `false` and do not add the event to the calendar.

### Constraints

- `0 <= start < end <= 10^9`

- At most `1000` calls will be made to `book`.

### Approach and complexity

We can use an ordered set to store the schedule. An ordered set can perform insert, delete, and search operations in $O(\log n)$ time. The elements in the ordered set are sorted by the $\textit{endTime}$ of the schedule in ascending order.

When calling the $\textit{book}(\textit{start}, \textit{end})$ method, we search for the first schedule in the ordered set with an end time greater than $\textit{start}$. If it exists and its start time is less than $\textit{end}$, it means there is a double booking, and we return $\textit{false}$. Otherwise, we insert $\textit{end}$ as the key and $\textit{start}$ as the value into the ordered set and return $\textit{true}$.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of schedules.

### C++20 solution

```cpp
class MyCalendar {
public:
    MyCalendar() {
    }

    bool book(int startTime, int endTime) {
        auto e = m.lower_bound(startTime + 1);
        if (e != m.end() && e->second < endTime) {
            return false;
        }
        m[endTime] = startTime;
        return true;
    }

private:
    map<int, int> m;
};
```

---

<a id="lc-1235"></a>
## 45. LC 1235 — Maximum Profit in Job Scheduling (Hard)

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

<a id="lc-2070"></a>
## 46. LC 2070 — Most Beautiful Item for Each Query (Medium)

[Official problem](https://leetcode.com/problems/most-beautiful-item-for-each-query) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2000-2099/2070.Most%20Beautiful%20Item%20for%20Each%20Query/README_EN.md)

### Problem description

You are given a 2D integer array `items` where `items[i] = [price_i, beauty_i]` denotes the **price** and **beauty** of an item respectively.

You are also given a **0-indexed** integer array `queries`. For each `queries[j]`, you want to determine the **maximum beauty** of an item whose **price** is **less than or equal** to `queries[j]`. If no such item exists, then the answer to this query is `0`.

Return an array `answer` of the same length as `queries` where `answer[j]` is the answer to the `j^th` query.

### Constraints

- `1 <= items.length, queries.length <= 10^5`

- `items[i].length == 2`

- `1 <= price_i, beauty_i, queries[j] <= 10^9`

### Approach and complexity

For each query, we need to find the maximum beauty value among the items with a price less than or equal to the query price. We can use the offline query method, first sort the items by price, and then sort the queries by price.

Next, we traverse the queries from small to large. For each query, we use a pointer $i$ to point to the item array. If the price of the item is less than or equal to the query price, we update the current maximum beauty value and move the pointer $i$ to the right until the price of the item is greater than the query price. We record the current maximum beauty value, which is the answer to the current query. Continue to traverse the next query until all queries are processed.

The time complexity is $O(n \log n + m \log m)$, and the space complexity is $O(\log n + m)$, where $n$ and $m$ are the lengths of the item array and the query array, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        ranges::sort(items);
        int n = items.size();
        int m = queries.size();
        vector<int> idx(m);
        iota(idx.begin(), idx.end(), 0);
        ranges::sort(idx, [&](int i, int j) {
            return queries[i] < queries[j];
        });
        int mx = 0, i = 0;
        vector<int> ans(m);
        for (int j : idx) {
            while (i < n && items[i][0] <= queries[j]) {
                mx = max(mx, items[i][1]);
                ++i;
            }
            ans[j] = mx;
        }
        return ans;
    }
};
```

---

<a id="lc-2080"></a>
## 47. LC 2080 — Range Frequency Queries (Medium)

[Official problem](https://leetcode.com/problems/range-frequency-queries) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2000-2099/2080.Range%20Frequency%20Queries/README_EN.md)

### Problem description

Design a data structure to find the **frequency** of a given value in a given subarray.

The **frequency** of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the `RangeFreqQuery` class:

- `RangeFreqQuery(int[] arr)` Constructs an instance of the class with the given **0-indexed** integer array `arr`.

- `int query(int left, int right, int value)` Returns the **frequency** of `value` in the subarray `arr[left...right]`.

A **subarray** is a contiguous sequence of elements within an array. `arr[left...right]` denotes the subarray that contains the elements of `nums` between indices `left` and `right` (**inclusive**).

### Constraints

- `1 <= arr.length <= 10^5`

- `1 <= arr[i], value <= 10^4`

- `0 <= left <= right < arr.length`

- At most `10^5` calls will be made to `query`

### Approach and complexity

We use a hash table $g$ to store the array of indices corresponding to each value. In the constructor, we traverse the array $\textit{arr}$, adding the index corresponding to each value to the hash table.

In the query function, we first check whether the given value exists in the hash table. If it does not exist, it means that the value does not exist in the array, so we directly return $0$. Otherwise, we get the index array $\textit{idx}$ corresponding to the value. Then we use binary search to find the first index $l$ that is greater than or equal to $\textit{left}$, and the first index $r$ that is greater than $\textit{right}$. Finally, we return $r - l$.

In terms of time complexity, the time complexity of the constructor is $O(n)$, and the time complexity of the query function is $O(\log n)$. The space complexity is $O(n)$. Where $n$ is the length of the array.

### C++20 solution

```cpp
class RangeFreqQuery {
public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0; i < arr.size(); ++i) {
            g[arr[i]].push_back(i);
        }
    }

    int query(int left, int right, int value) {
        if (!g.contains(value)) {
            return 0;
        }
        auto& idx = g[value];
        auto l = lower_bound(idx.begin(), idx.end(), left);
        auto r = lower_bound(idx.begin(), idx.end(), right + 1);
        return r - l;
    }

private:
    unordered_map<int, vector<int>> g;
};
```

---

<a id="lc-1838"></a>
## 48. LC 1838 — Frequency of the Most Frequent Element (Medium)

[Official problem](https://leetcode.com/problems/frequency-of-the-most-frequent-element) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1838.Frequency%20of%20the%20Most%20Frequent%20Element/README_EN.md)

### Problem description

The **frequency** of an element is the number of times it occurs in an array.

You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

Return the **maximum possible frequency** of an element after performing **at most** `k` operations.

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^5`

- `1 <= k <= 10^5`

### Approach and complexity

We can also use two pointers to maintain a sliding window, where all elements in the window can be changed to the maximum value in the window. The number of operations for the elements in the window is $s$, and $s \leq k$.

Initially, we set the left pointer $j$ to point to the first element of the array, and the right pointer $i$ also points to the first element of the array. Next, we move the right pointer $i$ each time, changing all elements in the window to $\textit{nums}[i]$. At this time, the number of operations to be increased is $(\textit{nums}[i] - \textit{nums}[i - 1]) \times (i - j)$. If this number of operations exceeds $k$, then we need to move the left pointer $j$ until the number of operations for the elements in the window does not exceed $k$. Then, we update the answer to the maximum length of the window.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        ranges::sort(nums);
        int ans = 1;
        long long s = 0;
        for (int i = 1, j = 0; i < nums.size(); ++i) {
            s += 1LL * (nums[i] - nums[i - 1]) * (i - j);
            while (s > k) {
                s -= nums[i] - nums[j++];
            }
            ans = max(ans, i - j + 1);
        }
        return ans;
    }
};
```

---

<a id="lc-1870"></a>
## 49. LC 1870 — Minimum Speed to Arrive on Time (Medium)

[Official problem](https://leetcode.com/problems/minimum-speed-to-arrive-on-time) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1870.Minimum%20Speed%20to%20Arrive%20on%20Time/README_EN.md)

### Problem description

You are given a floating-point number `hour`, representing the amount of time you have to reach the office. To commute to the office, you must take `n` trains in sequential order. You are also given an integer array `dist` of length `n`, where `dist[i]` describes the distance (in kilometers) of the `i^th` train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

- For example, if the `1^st` train ride takes `1.5` hours, you must wait for an additional `0.5` hours before you can depart on the `2^nd` train ride at the 2 hour mark.

Return the **minimum positive integer** speed **(in kilometers per hour)** that all the trains must travel at for you to reach the office on time, or `-1` if it is impossible to be on time.

Tests are generated such that the answer will not exceed `10^7` and `hour` will have **at most two digits after the decimal point**.

### Constraints

- `n == dist.length`

- `1 <= n <= 10^5`

- `1 <= dist[i] <= 10^5`

- `1 <= hour <= 10^9`

- There will be at most two digits after the decimal point in `hour`.

### Approach and complexity

We notice that if a speed value $v$ allows us to arrive within the stipulated time, then for any $v' > v$, we can also definitely arrive within the stipulated time. This exhibits monotonicity, hence we can use binary search to find the smallest speed value that meets the condition.

Before conducting the binary search, we need to first determine if it is possible to arrive within the stipulated time. If the number of trains is greater than the ceiling of the stipulated time, then it is definitely impossible to arrive within the stipulated time, and we should directly return $-1$.

Next, we define the left and right boundaries for the binary search as $l = 1$, $r = 10^7 + 1$, and then we take the middle value $\textit{mid} = \frac{l + r}{2}$ each time to check if it meets the condition. If it does, we move the right boundary to $\textit{mid}$; otherwise, we move the left boundary to $\textit{mid} + 1$.

The problem is transformed into determining whether a speed value $v$ can allow us to arrive within the stipulated time. We can traverse each train trip, calculate the running time of each trip $t = \frac{d}{v}$, if it is the last trip, we directly add $t$; otherwise, we round up and add $t$. Finally, we check if the total time is less than or equal to the stipulated time, if so, it means the condition is met.

After the binary search ends, if the left boundary exceeds $10^7$, it means we cannot arrive within the stipulated time, and we return $-1$; otherwise, we return the left boundary.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $n$ and $M$ are the number of train trips and the upper bound of the speed, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        if (dist.size() > ceil(hour)) {
            return -1;
        }
        const int m = 1e7;
        int l = 1, r = m + 1;
        int n = dist.size();
        auto check = [&](int v) {
            double s = 0;
            for (int i = 0; i < n; ++i) {
                double t = dist[i] * 1.0 / v;
                s += i == n - 1 ? t : ceil(t);
            }
            return s <= hour;
        };
        while (l < r) {
            int mid = (l + r) >> 1;
            if (check(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l > m ? -1 : l;
    }
};
```

---

<a id="lc-2141"></a>
## 50. LC 2141 — Maximum Running Time of N Computers (Hard)

[Official problem](https://leetcode.com/problems/maximum-running-time-of-n-computers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2100-2199/2141.Maximum%20Running%20Time%20of%20N%20Computers/README_EN.md)

### Problem description

You have `n` computers. You are given the integer `n` and a **0-indexed** integer array `batteries` where the `i^th` battery can **run** a computer for `batteries[i]` minutes. You are interested in running **all** `n` computers **simultaneously** using the given batteries.

Initially, you can insert **at most one battery** into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery **any number of times**. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the **maximum** number of minutes you can run all the `n` computers simultaneously.

### Constraints

- `1 <= n <= batteries.length <= 10^5`

- `1 <= batteries[i] <= 10^9`

### Approach and complexity

We notice that if we can run $n$ computers simultaneously for $t$ minutes, then we can also run $n$ computers simultaneously for $t' \le t$ minutes, which shows monotonicity. Therefore, we can use the binary search method to find the maximum $t$.

We define the left boundary of the binary search as $l=0$ and the right boundary as $r=\sum_{i=0}^{n-1} \textit{batteries}[i]$. During each binary search iteration, we use a variable $\textit{mid}$ to represent the current middle value, i.e., $\textit{mid} = (l + r + 1) >> 1$. We check if there exists a scheme that allows $n$ computers to run simultaneously for $\textit{mid}$ minutes. If such a scheme exists, then we update $l$ to $\textit{mid}$; otherwise, we update $r$ to $\textit{mid} - 1$. Finally, we return $l$ as the answer.

The problem is transformed into how to determine if there exists a scheme that allows $n$ computers to run simultaneously for $\textit{mid}$ minutes. If a battery can run for more minutes than $\textit{mid}$, since the computers run simultaneously for $\textit{mid}$ minutes and a battery can only power one computer at a time, we can only use this battery for $\textit{mid}$ minutes. If a battery can run for minutes less than or equal to $\textit{mid}$, we can use all the power of this battery. Therefore, we calculate the total minutes $s$ that all batteries can power, and if $s \ge n \times \textit{mid}$, then we can make $n$ computers run simultaneously for $\textit{mid}$ minutes.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $M$ is the total power of all batteries.

### C++20 solution

```cpp
class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        long long l = 0, r = 0;
        for (int x : batteries) {
            r += x;
        }
        while (l < r) {
            long long mid = (l + r + 1) >> 1;
            long long s = 0;
            for (int x : batteries) {
                s += min(1LL * x, mid);
            }
            if (s >= n * mid) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }
};
```
