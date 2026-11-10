# 10. Greedy Algorithms — C++20 solutions

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

1. [LC 55 — Jump Game](#lc-55)
2. [LC 45 — Jump Game II](#lc-45)
3. [LC 121 — Best Time to Buy and Sell Stock](#lc-121)
4. [LC 122 — Best Time to Buy and Sell Stock II](#lc-122)
5. [LC 134 — Gas Station](#lc-134)
6. [LC 56 — Merge Intervals](#lc-56)
7. [LC 435 — Non-overlapping Intervals](#lc-435)
8. [LC 452 — Minimum Number of Arrows to Burst Balloons](#lc-452)
9. [LC 763 — Partition Labels](#lc-763)
10. [LC 53 — Maximum Subarray](#lc-53)
11. [LC 406 — Queue Reconstruction by Height](#lc-406)
12. [LC 135 — Candy](#lc-135)
13. [LC 455 — Assign Cookies](#lc-455)
14. [LC 860 — Lemonade Change](#lc-860)
15. [LC 605 — Can Place Flowers](#lc-605)
16. [LC 665 — Non-decreasing Array](#lc-665)
17. [LC 376 — Wiggle Subsequence](#lc-376)
18. [LC 738 — Monotone Increasing Digits](#lc-738)
19. [LC 621 — Task Scheduler](#lc-621)
20. [LC 1029 — Two City Scheduling](#lc-1029)
21. [LC 646 — Maximum Length of Pair Chain](#lc-646)
22. [LC 881 — Boats to Save People](#lc-881)
23. [LC 948 — Bag of Tokens](#lc-948)
24. [LC 846 — Hand of Straights](#lc-846)
25. [LC 659 — Split Array into Consecutive Subsequences](#lc-659)
26. [LC 767 — Reorganize String](#lc-767)
27. [LC 678 — Valid Parenthesis String](#lc-678)
28. [LC 921 — Minimum Add to Make Parentheses Valid](#lc-921)
29. [LC 1249 — Minimum Remove to Make Valid Parentheses](#lc-1249)
30. [LC 402 — Remove K Digits](#lc-402)
31. [LC 316 — Remove Duplicate Letters](#lc-316)
32. [LC 1710 — Maximum Units on a Truck](#lc-1710)
33. [LC 1833 — Maximum Ice Cream Bars](#lc-1833)
34. [LC 1877 — Minimize Maximum Pair Sum in Array](#lc-1877)
35. [LC 1963 — Minimum Number of Swaps to Make the String Balanced](#lc-1963)
36. [LC 2038 — Remove Colored Pieces if Both Neighbors are the Same Color](#lc-2038)
37. [LC 2160 — Minimum Sum of Four Digit Number After Splitting Digits](#lc-2160)
38. [LC 2279 — Maximum Bags With Full Capacity of Rocks](#lc-2279)
39. [LC 2335 — Minimum Amount of Time to Fill Cups](#lc-2335)
40. [LC 2366 — Minimum Replacements to Sort the Array](#lc-2366)
41. [LC 2405 — Optimal Partition of String](#lc-2405)
42. [LC 2410 — Maximum Matching of Players With Trainers](#lc-2410)
43. [LC 2491 — Divide Players Into Teams of Equal Skill](#lc-2491)
44. [LC 2578 — Split With Minimum Sum](#lc-2578)
45. [LC 2587 — Rearrange Array to Maximize Prefix Score](#lc-2587)
46. [LC 2616 — Minimize the Maximum Difference of Pairs](#lc-2616)
47. [LC 3075 — Maximize Happiness of Selected Children](#lc-3075)
48. [LC 502 — IPO](#lc-502)
49. [LC 630 — Course Schedule III](#lc-630)
50. [LC 1642 — Furthest Building You Can Reach](#lc-1642)

---

<a id="lc-55"></a>
## 1. LC 55 — Jump Game (Medium)

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
## 2. LC 45 — Jump Game II (Medium)

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

<a id="lc-121"></a>
## 3. LC 121 — Best Time to Buy and Sell Stock (Easy)

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
## 4. LC 122 — Best Time to Buy and Sell Stock II (Medium)

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

<a id="lc-134"></a>
## 5. LC 134 — Gas Station (Medium)

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

<a id="lc-56"></a>
## 6. LC 56 — Merge Intervals (Medium)

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

<a id="lc-435"></a>
## 7. LC 435 — Non-overlapping Intervals (Medium)

[Official problem](https://leetcode.com/problems/non-overlapping-intervals) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0435.Non-overlapping%20Intervals/README_EN.md)

### Problem description

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Note** that intervals which only touch at a point are **non-overlapping**. For example, `[1, 2]` and `[2, 3]` are non-overlapping.

### Constraints

- `1 <= intervals.length <= 10^5`

- `intervals[i].length == 2`

- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

### Approach and complexity

We first sort the intervals in ascending order by their right boundary. We use a variable $\textit{pre}$ to record the right boundary of the previous interval and a variable $\textit{ans}$ to record the number of intervals that need to be removed. Initially, $\textit{ans} = \textit{intervals}.\textit{length}$.

Then we iterate through the intervals. For each interval:

- If the left boundary of the current interval is greater than or equal to $\textit{pre}$, it means that this interval does not need to be removed. We directly update $\textit{pre}$ to the right boundary of the current interval and decrement $\textit{ans}$ by one;
- Otherwise, it means that this interval needs to be removed, and we do not need to update $\textit{pre}$ and $\textit{ans}$.

Finally, we return $\textit{ans}$.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of intervals.

### C++20 solution

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        ranges::sort(intervals, [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int ans = intervals.size();
        int pre = INT_MIN;
        for (const auto& e : intervals) {
            int l = e[0], r = e[1];
            if (pre <= l) {
                --ans;
                pre = r;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-452"></a>
## 8. LC 452 — Minimum Number of Arrows to Burst Balloons (Medium)

[Official problem](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0452.Minimum%20Number%20of%20Arrows%20to%20Burst%20Balloons/README_EN.md)

### Problem description

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [x_start, x_end]` denotes a balloon whose **horizontal diameter** stretches between `x_start` and `x_end`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `x_start` and `x_end` is **burst** by an arrow shot at `x` if `x_start <= x <= x_end`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return the **minimum** number of arrows that must be shot to burst all balloons.

### Constraints

- `1 <= points.length <= 10^5`

- `points[i].length == 2`

- `-2^31 <= x_start < x_end <= 2^31 - 1`

### Approach and complexity

Sort by interval end. Shoot at the earliest remaining end, which intersects every overlapping balloon while leaving maximum room for later groups. A new arrow is needed only when the next interval starts after that point.

Time O(n log n); auxiliary space O(log n) for sorting.

### C++20 solution

```cpp
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        ranges::sort(points, [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        int ans = 0;
        long long last = -(1LL << 60);
        for (auto& p : points) {
            int a = p[0], b = p[1];
            if (a > last) {
                ++ans;
                last = b;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-763"></a>
## 9. LC 763 — Partition Labels (Medium)

[Official problem](https://leetcode.com/problems/partition-labels) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0763.Partition%20Labels/README_EN.md)

### Problem description

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return a list of integers representing the size of these parts.

### Constraints

- `1 <= s.length <= 500`

- `s` consists of lowercase English letters.

### Approach and complexity

We first use an array or hash table $\textit{last}$ to record the last occurrence of each letter in the string $s$.

Next, we use a greedy approach to partition the string into as many segments as possible.

Traverse the string $s$ from left to right, while maintaining the start index $j$ and end index $i$ of the current segment, both initially set to $0$.

For each letter $c$ visited, get the last occurrence position $\textit{last}[c]$. Since the end index of the current segment must not be less than $\textit{last}[c]$, let $mx = \max(mx, \textit{last}[c])$.

When visiting the index $mx$, it means the current segment ends. The index range of the current segment is $[j,.. i]$, and the length is $i - j + 1$. We add this length to the result array. Then set $j = i + 1$ and continue to find the next segment.

Repeat the above process until the string traversal is complete to get the lengths of all segments.

The time complexity is $O(n)$, and the space complexity is $O(|\Sigma|)$, where $n$ is the length of the string $s$, and $|\Sigma|$ is the size of the character set. In this problem, $|\Sigma| = 26$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        int last[26] = {0};
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            last[s[i] - 'a'] = i;
        }
        vector<int> ans;
        int mx = 0, j = 0;
        for (int i = 0; i < n; ++i) {
            mx = max(mx, last[s[i] - 'a']);
            if (mx == i) {
                ans.push_back(i - j + 1);
                j = i + 1;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-53"></a>
## 10. LC 53 — Maximum Subarray (Medium)

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

<a id="lc-406"></a>
## 11. LC 406 — Queue Reconstruction by Height (Medium)

[Official problem](https://leetcode.com/problems/queue-reconstruction-by-height) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0406.Queue%20Reconstruction%20by%20Height/README_EN.md)

### Problem description

You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [h_i, k_i]` represents the `i^th` person of height `h_i` with **exactly** `k_i` other people in front who have a height greater than or equal to `h_i`.

Reconstruct and return the queue that is represented by the input array `people`. The returned queue should be formatted as an array `queue`, where `queue[j] = [h_j, k_j]` is the attributes of the `j^th` person in the queue (`queue[0]` is the person at the front of the queue).

### Constraints

- `1 <= people.length <= 2000`

- `0 <= h_i <= 10^6`

- `0 <= k_i < people.length`

- It is guaranteed that the queue can be reconstructed.

### Approach and complexity

Sort heights ascending and k descending for equal heights. At placement time all empty positions will be filled by people at least as tall. Put the current person in the (k+1)th empty position. Descending k for equal heights preserves the required number of peers before each person. A Fenwick tree locates the kth empty position in logarithmic time.

Time O(n log n); auxiliary space O(n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        ranges::sort(people, [](const auto& a, const auto& b) {
            return a[0] != b[0] ? a[0] < b[0] : a[1] > b[1];
        });
        int n = people.size();
        vector<int> tree(n + 1);
        for (int i = 1; i <= n; ++i) tree[i] = i & -i; // Initially every slot is empty.
        vector<vector<int>> result(n);
        for (const auto& person : people) {
            int rank = person[1] + 1, index = 0;
            for (unsigned step = bit_floor(static_cast<unsigned>(n)); step; step >>= 1) {
                int candidate = index + static_cast<int>(step);
                if (candidate <= n && tree[candidate] < rank) {
                    index = candidate; rank -= tree[candidate];
                }
            }
            result[index] = person;
            for (int i = index + 1; i <= n; i += i & -i) --tree[i];
        }
        return result;
    }
};
```

---

<a id="lc-135"></a>
## 12. LC 135 — Candy (Hard)

[Official problem](https://leetcode.com/problems/candy) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0135.Candy/README_EN.md)

### Problem description

There are `n` children standing in a line.

Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have **at least** one candy.

- Children with a **higher** rating get more candies than their neighbors.

Return the **minimum** number of candies you need to have to distribute the candies to the children.

### Constraints

- `1 <= n == ratings.length <= 5 * 10^4`

- `0 <= ratings[i] <= 5 * 10^4`

### Approach and complexity

We initialize two arrays $\textit{left}$ and $\textit{right}$, where $\textit{left}[i]$ represents the minimum number of candies the current child should get when the current child's score is higher than the left child's score, and $\textit{right}[i]$ represents the minimum number of candies the current child should get when the current child's score is higher than the right child's score. Initially, $\textit{left}[i]=1$, $\textit{right}[i]=1$.

We traverse the array from left to right once, and if the current child's score is higher than the left child's score, then $\textit{left}[i]=\textit{left}[i-1]+1$; similarly, we traverse the array from right to left once, and if the current child's score is higher than the right child's score, then $\textit{right}[i]=\textit{right}[i+1]+1$.

Finally, we traverse the array of scores once, and the minimum number of candies each child should get is the maximum of $\textit{left}[i]$ and $\textit{right}[i]$, and we add them up to get the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array of scores.

### C++20 solution

```cpp
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> left(n, 1);
        vector<int> right(n, 1);
        for (int i = 1; i < n; ++i) {
            if (ratings[i] > ratings[i - 1]) {
                left[i] = left[i - 1] + 1;
            }
        }
        for (int i = n - 2; ~i; --i) {
            if (ratings[i] > ratings[i + 1]) {
                right[i] = right[i + 1] + 1;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += max(left[i], right[i]);
        }
        return ans;
    }
};
```

---

<a id="lc-455"></a>
## 13. LC 455 — Assign Cookies (Easy)

[Official problem](https://leetcode.com/problems/assign-cookies) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0455.Assign%20Cookies/README_EN.md)

### Problem description

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

### Constraints

- `1 <= g.length <= 3 * 10^4`

- `0 <= s.length <= 3 * 10^4`

- `1 <= g[i], s[j] <= 2^31 - 1`

**Note:** This question is the same as 2410: Maximum Matching of Players With Trainers.

### Approach and complexity

According to the problem description, we should prioritize giving cookies to children with smaller appetites, so as to satisfy as many children as possible.

Therefore, we first sort the two arrays, and then use two pointers $i$ and $j$ to point to the head of arrays $g$ and $s$ respectively. Each time we compare the size of $g[i]$ and $s[j]$:

- If $s[j] < g[i]$, it means that the current cookie $s[j]$ cannot satisfy the current child $g[i]$. We should allocate a larger cookie to the current child, so $j$ should move to the right by one. If $j$ goes out of bounds, it means that the current child cannot be satisfied. At this time, the number of successfully allocated children is $i$, and we can return directly.
- If $s[j] \ge g[i]$, it means that the current cookie $s[j]$ can satisfy the current child $g[i]$. We allocate the current cookie to the current child, so both $i$ and $j$ should move to the right by one.

If we have traversed the array $g$, it means that all children have been allocated cookies, and we can return the total number of children.

The time complexity is $O(m \log m + n \log n)$, and the space complexity is $O(\log m + \log n)$, where $m$ and $n$ are the lengths of arrays $g$ and $s$ respectively.

### C++20 solution

```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        ranges::sort(g);
        ranges::sort(s);
        int m = g.size(), n = s.size();
        for (int i = 0, j = 0; i < m; ++i) {
            while (j < n && s[j] < g[i]) {
                ++j;
            }
            if (j++ >= n) {
                return i;
            }
        }
        return m;
    }
};
```

---

<a id="lc-860"></a>
## 14. LC 860 — Lemonade Change (Easy)

[Official problem](https://leetcode.com/problems/lemonade-change) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0860.Lemonade%20Change/README_EN.md)

### Problem description

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `i^th` customer pays, return `true` if you can provide every customer with the correct change, or `false` otherwise.

### Constraints

- `1 <= bills.length <= 10^5`

- `bills[i]` is either `5`, `10`, or `20`.

### Approach and complexity

Track five- and ten-dollar bills. For twenty dollars prefer returning ten plus five, preserving five-dollar bills that are the only way to change a ten. Fail as soon as exact change is impossible.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0;
        for (int v : bills) {
            if (v == 5) {
                ++five;
            } else if (v == 10) {
                ++ten;
                --five;
            } else {
                if (ten) {
                    --ten;
                    --five;
                } else {
                    five -= 3;
                }
            }
            if (five < 0) {
                return false;
            }
        }
        return true;
    }
};
```

---

<a id="lc-605"></a>
## 15. LC 605 — Can Place Flowers (Easy)

[Official problem](https://leetcode.com/problems/can-place-flowers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0605.Can%20Place%20Flowers/README_EN.md)

### Problem description

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the `flowerbed` without violating the no-adjacent-flowers rule and `false` otherwise.

### Constraints

- `1 <= flowerbed.length <= 2 * 10^4`

- `flowerbed[i]` is `0` or `1`.

- There are no two adjacent flowers in `flowerbed`.

- `0 <= n <= flowerbed.length`

### Approach and complexity

We directly traverse the array $\textit{flowerbed}$. For each position $i$, if $\textit{flowerbed}[i]=0$ and its adjacent positions on the left and right are also $0$, then we can plant a flower at this position. Otherwise, we cannot. Finally, we count the number of flowers that can be planted. If it is not less than $n$, we return $\textit{true}$, otherwise we return $\textit{false}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{flowerbed}$.

### C++20 solution

```cpp
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int m = flowerbed.size();
        for (int i = 0; i < m; ++i) {
            int l = i == 0 ? 0 : flowerbed[i - 1];
            int r = i == m - 1 ? 0 : flowerbed[i + 1];
            if (l + flowerbed[i] + r == 0) {
                flowerbed[i] = 1;
                --n;
            }
        }
        return n <= 0;
    }
};
```

---

<a id="lc-665"></a>
## 16. LC 665 — Non-decreasing Array (Medium)

[Official problem](https://leetcode.com/problems/non-decreasing-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0665.Non-decreasing%20Array/README_EN.md)

### Problem description

Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

We define an array is non-decreasing if `nums[i] <= nums[i + 1]` holds for every `i` (**0-based**) such that (`0 <= i <= n - 2`).

### Constraints

- `n == nums.length`

- `1 <= n <= 10^4`

- `-10^5 <= nums[i] <= 10^5`

### Approach and complexity

At the first descending adjacent pair, lower the left value if it does not break the preceding boundary; otherwise raise the right value. A second inversion makes one modification insufficient.

Time O(n); auxiliary space O(1). May modify input.

### C++20 solution

```cpp
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            int a = nums[i], b = nums[i + 1];
            if (a > b) {
                nums[i] = b;
                if (is_sorted(nums.begin(), nums.end())) {
                    return true;
                }
                nums[i] = a;
                nums[i + 1] = a;
                return is_sorted(nums.begin(), nums.end());
            }
        }
        return true;
    }
};
```

---

<a id="lc-376"></a>
## 17. LC 376 — Wiggle Subsequence (Medium)

[Official problem](https://leetcode.com/problems/wiggle-subsequence) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0376.Wiggle%20Subsequence/README_EN.md)

### Problem description

A **wiggle sequence** is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

- For example, `[1, 7, 4, 9, 2, 5]` is a **wiggle sequence** because the differences `(6, -3, 5, -7, 3)` alternate between positive and negative.

- In contrast, `[1, 4, 7, 2, 5]` and `[1, 7, 4, 5, 5]` are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.

A **subsequence** is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array `nums`, return the length of the longest **wiggle subsequence** of `nums`.

### Constraints

- `1 <= nums.length <= 1000`

- `0 <= nums[i] <= 1000`

**Follow up:** Could you solve this in `O(n)` time?

### Approach and complexity

We define $f[i]$ as the length of the wiggle sequence ending at the $i$th element with an upward trend, and $g[i]$ as the length of the wiggle sequence ending at the $i$th element with a downward trend. Initially, $f[0] = g[0] = 1$ because when there is only one element, the length of the wiggle sequence is $1$. Initialize the answer as $1$.

For $f[i]$, where $i \geq 1$, we enumerate $j$ in the range $[0, i)$, if $\textit{nums}[j] < \textit{nums}[i]$, it means that $i$ can be appended after $j$ to form an upward wiggle sequence, then $f[i] = \max(f[i], g[j] + 1)$; if $\textit{nums}[j] > \textit{nums}[i]$, it means that $i$ can be appended after $j$ to form a downward wiggle sequence, then $g[i] = \max(g[i], f[j] + 1)$. Then we update the answer to $\max(f[i], g[i])$.

Finally, we return the answer.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        int ans = 1;
        vector<int> f(n, 1);
        vector<int> g(n, 1);
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    f[i] = max(f[i], g[j] + 1);
                } else if (nums[j] > nums[i]) {
                    g[i] = max(g[i], f[j] + 1);
                }
            }
            ans = max({ans, f[i], g[i]});
        }
        return ans;
    }
};
```

---

<a id="lc-738"></a>
## 18. LC 738 — Monotone Increasing Digits (Medium)

[Official problem](https://leetcode.com/problems/monotone-increasing-digits) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0738.Monotone%20Increasing%20Digits/README_EN.md)

### Problem description

An integer has **monotone increasing digits** if and only if each pair of adjacent digits `x` and `y` satisfy `x <= y`.

Given an integer `n`, return the largest number that is less than or equal to `n` with **monotone increasing digits**.

### Constraints

- `0 <= n <= 10^9`

### Approach and complexity

Scan digits right to left. Whenever a left digit exceeds its right neighbor, decrement it and remember to set all following digits to nine. Repeated propagation handles equal-digit cascades.

Time O(d); auxiliary space O(d) for d decimal digits.

### C++20 solution

```cpp
class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string s = to_string(n);
        int i = 1;
        for (; i < s.size() && s[i - 1] <= s[i]; ++i)
            ;
        if (i < s.size()) {
            for (; i > 0 && s[i - 1] > s[i]; --i) {
                --s[i - 1];
            }
            ++i;
            for (; i < s.size(); ++i) {
                s[i] = '9';
            }
        }
        return stoi(s);
    }
};
```

---

<a id="lc-621"></a>
## 19. LC 621 — Task Scheduler (Medium)

[Official problem](https://leetcode.com/problems/task-scheduler) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0621.Task%20Scheduler/README_EN.md)

### Problem description

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.

Return the **minimum** number of CPU intervals required to complete all tasks.

### Constraints

- `1 <= tasks.length <= 10^4`

- `tasks[i]` is an uppercase English letter.

- `0 <= n <= 100`

### Approach and complexity

The most frequent tasks create f−1 full cooldown gaps. With c tasks tied at that frequency, the lower bound is (f−1)(cooldown+1)+c; enough other tasks can fill these gaps, so take the maximum of that bound and total task count.

Time O(N+A), auxiliary space O(A), A=26.

### C++20 solution

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> cnt(26);
        int x = 0;
        for (char c : tasks) {
            c -= 'A';
            ++cnt[c];
            x = max(x, cnt[c]);
        }
        int s = 0;
        for (int v : cnt) {
            s += v == x;
        }
        return max((int) tasks.size(), (x - 1) * (n + 1) + s);
    }
};
```

---

<a id="lc-1029"></a>
## 20. LC 1029 — Two City Scheduling (Medium)

[Official problem](https://leetcode.com/problems/two-city-scheduling) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1029.Two%20City%20Scheduling/README_EN.md)

### Problem description

A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCost_i, bCost_i]`, the cost of flying the `i^th` person to city `a` is `aCost_i`, and the cost of flying the `i^th` person to city `b` is `bCost_i`.

Return the minimum cost to fly every person to a city such that exactly `n` people arrive in each city.

### Constraints

- `2 * n == costs.length`

- `2 <= costs.length <= 100`

- `costs.length` is even.

- `1 <= aCost_i, bCost_i <= 1000`

### Approach and complexity

Sort by cost(A)−cost(B), send the first half to A and the rest to B. An exchange argument shows every inversion in these cost differences can only increase the total.

Time O(n log n); auxiliary space O(log n) for sorting.

### C++20 solution

```cpp
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        ranges::sort(costs, [](const vector<int>& a, const vector<int>& b) {
            return a[0] - a[1] < b[0] - b[1];
        });
        int n = costs.size() / 2;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += costs[i][0] + costs[i + n][1];
        }
        return ans;
    }
};
```

---

<a id="lc-646"></a>
## 21. LC 646 — Maximum Length of Pair Chain (Medium)

[Official problem](https://leetcode.com/problems/maximum-length-of-pair-chain) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0646.Maximum%20Length%20of%20Pair%20Chain/README_EN.md)

### Problem description

You are given an array of `n` pairs `pairs` where `pairs[i] = [left_i, right_i]` and `left_i < right_i`.

A pair `p2 = [c, d]` **follows** a pair `p1 = [a, b]` if `b < c`. A **chain** of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

### Constraints

- `n == pairs.length`

- `1 <= n <= 1000`

- `-1000 <= left_i < right_i <= 1000`

### Approach and complexity

We sort all pairs in ascending order by the second number, and use a variable $\textit{pre}$ to maintain the maximum value of the second number of the selected pairs.

We traverse the sorted pairs. If the first number of the current pair is greater than $\textit{pre}$, we can greedily select the current pair, increment the answer by one, and update $\textit{pre}$ to the second number of the current pair.

After the traversal, we return the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of pairs.

### C++20 solution

```cpp
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        ranges::sort(pairs, {}, [](const auto& p) { return p[1]; });
        int ans = 0, pre = INT_MIN;
        for (const auto& p : pairs) {
            if (pre < p[0]) {
                pre = p[1];
                ++ans;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-881"></a>
## 22. LC 881 — Boats to Save People (Medium)

[Official problem](https://leetcode.com/problems/boats-to-save-people) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0881.Boats%20to%20Save%20People/README_EN.md)

### Problem description

You are given an array `people` where `people[i]` is the weight of the `i^th` person, and an **infinite number of boats** where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return the minimum number of boats to carry every given person.

### Constraints

- `1 <= people.length <= 5 * 10^4`

- `1 <= people[i] <= limit <= 3 * 10^4`

### Approach and complexity

After sorting, use two pointers to point to the beginning and end of the array respectively. Each time, compare the sum of the elements pointed to by the two pointers with $\textit{limit}$. If it is less than or equal to $\textit{limit}$, then both pointers move one step towards the middle. Otherwise, only the right pointer moves. Accumulate the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{people}$.

### C++20 solution

```cpp
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        ranges::sort(people);
        int ans = 0;
        for (int i = 0, j = people.size() - 1; i <= j; --j) {
            if (people[i] + people[j] <= limit) {
                ++i;
            }
            ++ans;
        }
        return ans;
    }
};
```

---

<a id="lc-948"></a>
## 23. LC 948 — Bag of Tokens (Medium)

[Official problem](https://leetcode.com/problems/bag-of-tokens) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0948.Bag%20of%20Tokens/README_EN.md)

### Problem description

You start with an initial **power** of `power`, an initial **score** of `0`, and a bag of tokens given as an integer array `tokens`, where each `tokens[i]` denotes the value of token_i.

Your goal is to **maximize** the total **score** by strategically playing these tokens. In one move, you can play an **unplayed** token in one of the two ways (but not both for the same token):

- **Face-up**: If your current power is **at least** `tokens[i]`, you may play token_i, losing `tokens[i]` power and gaining `1` score.

- **Face-down**: If your current score is **at least** `1`, you may play token_i, gaining `tokens[i]` power and losing `1` score.

Return the **maximum** possible score you can achieve after playing **any** number of tokens.

### Constraints

- `0 <= tokens.length <= 1000`

- `0 <= tokens[i], power < 10^4`

### Approach and complexity

There are two ways to use tokens: one is to consume energy to gain points, and the other is to consume points to gain energy. Obviously, we should consume as little energy as possible to gain as many points as possible.

Therefore, we can sort the tokens by the amount of energy they consume, and then use two pointers: one moving from left to right and the other from right to left. In each iteration, we try to consume energy to gain points as much as possible, and then update the maximum score. If the current energy is not enough to consume the current token, we try to consume the current token using points. If the points are not enough to consume the current token, we stop the iteration.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of tokens.

### C++20 solution

```cpp
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        ranges::sort(tokens);
        int ans = 0, score = 0;
        for (int i = 0, j = tokens.size() - 1; i <= j;) {
            if (power >= tokens[i]) {
                power -= tokens[i++];
                ans = max(ans, ++score);
            } else if (score > 0) {
                power += tokens[j--];
                --score;
            } else {
                break;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-846"></a>
## 24. LC 846 — Hand of Straights (Medium)

[Official problem](https://leetcode.com/problems/hand-of-straights) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0846.Hand%20of%20Straights/README_EN.md)

### Problem description

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `i^th` card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

### Constraints

- `1 <= hand.length <= 10^4`

- `0 <= hand[i] <= 10^9`

- `1 <= groupSize <= hand.length`

**Note:** This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

### Approach and complexity

We first check whether the length of the array $\textit{hand}$ is divisible by $\textit{groupSize}$. If it is not, this means that the array cannot be partitioned into multiple subarrays of length $\textit{groupSize}$, so we return $\textit{false}$.

Next, we use a hash table $\textit{cnt}$ to count the occurrences of each number in the array $\textit{hand}$, and then we sort the array $\textit{hand}$.

After that, we iterate over the sorted array $\textit{hand}$. For each number $x$, if $\textit{cnt}[x] \neq 0$, we enumerate every number $y$ from $x$ to $x + \textit{groupSize} - 1$. If $\textit{cnt}[y] = 0$, it means that we cannot partition the array into multiple subarrays of length $\textit{groupSize}$, so we return $\textit{false}$. Otherwise, we decrement $\textit{cnt}[y]$ by $1$.

If the iteration completes successfully, it means that the array can be partitioned into multiple valid subarrays, so we return $\textit{true}$.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{hand}$.

### C++20 solution

```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize) {
            return false;
        }
        ranges::sort(hand);
        unordered_map<int, int> cnt;
        for (int x : hand) {
            ++cnt[x];
        }
        for (int x : hand) {
            if (cnt.contains(x)) {
                for (int y = x; y < x + groupSize; ++y) {
                    if (!cnt.contains(y)) {
                        return false;
                    }
                    if (--cnt[y] == 0) {
                        cnt.erase(y);
                    }
                }
            }
        }
        return true;
    }
};
```

---

<a id="lc-659"></a>
## 25. LC 659 — Split Array into Consecutive Subsequences (Medium)

[Official problem](https://leetcode.com/problems/split-array-into-consecutive-subsequences) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0659.Split%20Array%20into%20Consecutive%20Subsequences/README_EN.md)

### Problem description

You are given an integer array `nums` that is **sorted in non-decreasing order**.

Determine if it is possible to split `nums` into **one or more subsequences** such that **both** of the following conditions are true:

- Each subsequence is a **consecutive increasing sequence** (i.e. each integer is **exactly one** more than the previous integer).

- All subsequences have a length of `3`** or more**.

Return `true` if you can split `nums` according to the above conditions, or `false` otherwise.

A **subsequence** of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., `[1,3,5]` is a subsequence of `[1,2,3,4,5]` while `[1,3,2]` is not).

### Constraints

- `1 <= nums.length <= 10^4`

- `-1000 <= nums[i] <= 1000`

- `nums` is sorted in **non-decreasing** order.

### Approach and complexity

Process values in sorted order, first extending a subsequence that needs the current value. Only if none exists start a length-three subsequence by consuming the next two values. Extending first avoids stranding existing chains.

Expected time O(n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, priority_queue<int, vector<int>, greater<int>>> d;
        for (int v : nums) {
            if (d.count(v - 1)) {
                auto& q = d[v - 1];
                d[v].push(q.top() + 1);
                q.pop();
                if (q.empty()) {
                    d.erase(v - 1);
                }
            } else {
                d[v].push(1);
            }
        }
        for (auto& [_, v] : d) {
            if (v.top() < 3) {
                return false;
            }
        }
        return true;
    }
};
```

---

<a id="lc-767"></a>
## 26. LC 767 — Reorganize String (Medium)

[Official problem](https://leetcode.com/problems/reorganize-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0767.Reorganize%20String/README_EN.md)

### Problem description

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return any possible rearrangement of `s` or return `""` if not possible.

### Constraints

- `1 <= s.length <= 500`

- `s` consists of lowercase English letters.

### Approach and complexity

Count letters, reject a count greater than ceil(n/2), and place characters in frequency order at alternating even then odd positions. Spacing the most frequent letters first prevents equal neighbors.

Time O(n+A log A); auxiliary space O(A) beyond output, A=26.

### C++20 solution

```cpp
class Solution {
public:
    string reorganizeString(string s) {
        vector<int> cnt(26);
        for (char& c : s) ++cnt[c - 'a'];
        int mx = *max_element(cnt.begin(), cnt.end());
        int n = s.size();
        if (mx > (n + 1) / 2) return "";
        vector<vector<int>> m;
        for (int i = 0; i < 26; ++i) {
            if (cnt[i]) m.push_back({cnt[i], i});
        }
        ranges::sort(m);
        ranges::reverse(m);
        string ans = s;
        int k = 0;
        for (auto& e : m) {
            int v = e[0], i = e[1];
            while (v--) {
                ans[k] = 'a' + i;
                k += 2;
                if (k >= n) k = 1;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-678"></a>
## 27. LC 678 — Valid Parenthesis String (Medium)

[Official problem](https://leetcode.com/problems/valid-parenthesis-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0678.Valid%20Parenthesis%20String/README_EN.md)

### Problem description

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is **valid**.

The following rules define a **valid** string:

- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.

- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.

- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.

- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

### Constraints

- `1 <= s.length <= 100`

- `s[i]` is `'('`, `')'` or `'*'`.

### Approach and complexity

Scan twice, first from left to right to make sure that each of the closing brackets is matched successfully, and second from right to left to make sure that each of the opening brackets is matched successfully.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    bool checkValidString(string s) {
        int x = 0, n = s.size();
        for (int i = 0; i < n; ++i) {
            if (s[i] != ')') {
                ++x;
            } else if (x) {
                --x;
            } else {
                return false;
            }
        }
        x = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] != '(') {
                ++x;
            } else if (x) {
                --x;
            } else {
                return false;
            }
        }
        return true;
    }
};
```

---

<a id="lc-921"></a>
## 28. LC 921 — Minimum Add to Make Parentheses Valid (Medium)

[Official problem](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0921.Minimum%20Add%20to%20Make%20Parentheses%20Valid/README_EN.md)

### Problem description

A parentheses string is valid if and only if:

- It is the empty string,

- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or

- It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

- For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(**(**)))"` or a closing parenthesis to be `"())**)**)"`.

Return the minimum number of moves required to make `s` valid.

### Constraints

- `1 <= s.length <= 1000`

- `s[i]` is either `'('` or `')'`.

### Approach and complexity

Solution 1 uses a stack to implement parenthesis matching, but we can also directly implement it through counting.

Define a variable $\textit{cnt}$ to represent the current number of left parentheses to be matched, and a variable $\textit{ans}$ to record the answer. Initially, both variables are set to $0$.

Iterate through each character $c$ in the string $s$:

- If $c$ is a left parenthesis, increase the value of $\textit{cnt}$ by $1$;
- If $c$ is a right parenthesis, at this point if $\textit{cnt} > 0$, it means that there are left parentheses that can be matched, so decrease the value of $\textit{cnt}$ by $1$; otherwise, it means that the current right parenthesis cannot be matched, so increase the value of $\textit{ans}$ by $1$.

After the iteration ends, add the value of $\textit{cnt}$ to $\textit{ans}$, which is the answer.

The Rust version uses `fold` over the bytes with $(\textit{ans}, \textit{cnt})$ as the state, so no explicit loop is needed; the greedy counting strategy is the same as above.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int ans = 0, cnt = 0;
        for (char c : s) {
            if (c == '(')
                ++cnt;
            else if (cnt)
                --cnt;
            else
                ++ans;
        }
        ans += cnt;
        return ans;
    }
};
```

---

<a id="lc-1249"></a>
## 29. LC 1249 — Minimum Remove to Make Valid Parentheses (Medium)

[Official problem](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1249.Minimum%20Remove%20to%20Make%20Valid%20Parentheses/README_EN.md)

### Problem description

Given a string s of `'('` , `')'` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return **any** valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or

- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or

- It can be written as `(A)`, where `A` is a valid string.

### Constraints

- `1 <= s.length <= 10^5`

- `s[i]` is either `'('` , `')'`, or lowercase English letter.

### Approach and complexity

First, we scan from left to right and remove the extra right parentheses. Then, we scan from right to left and remove the extra left parentheses.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

Similar problems:

- [678. Valid Parenthesis String](https://github.com/doocs/leetcode/blob/main/solution/0600-0699/0678.Valid%20Parenthesis%20String/README_EN.md)
- [2116. Check if a Parentheses String Can Be Valid](https://github.com/doocs/leetcode/blob/main/solution/2100-2199/2116.Check%20if%20a%20Parentheses%20String%20Can%20Be%20Valid/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        string stk;
        int x = 0;
        for (char& c : s) {
            if (c == ')' && x == 0) continue;
            if (c == '(')
                ++x;
            else if (c == ')')
                --x;
            stk.push_back(c);
        }
        string ans;
        x = 0;
        while (stk.size()) {
            char c = stk.back();
            stk.pop_back();
            if (c == '(' && x == 0) continue;
            if (c == ')')
                ++x;
            else if (c == '(')
                --x;
            ans.push_back(c);
        }
        ranges::reverse(ans);
        return ans;
    }
};
```

---

<a id="lc-402"></a>
## 30. LC 402 — Remove K Digits (Medium)

[Official problem](https://leetcode.com/problems/remove-k-digits) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0402.Remove%20K%20Digits/README_EN.md)

### Problem description

Given string num representing a non-negative integer `num`, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

### Constraints

- `1 <= k <= num.length <= 10^5`

- `num` consists of only digits.

- `num` does not have any leading zeros except for the zero itself.

### Approach and complexity

Maintain an increasing digit stack, removing larger preceding digits while deletions remain. Delete any remaining digits from the end, then remove leading zeros. Each earliest smaller digit improves the number lexicographically.

Time O(n); auxiliary space O(n) for the digit buffer.

### C++20 solution

```cpp
class Solution {
public:
    string removeKdigits(string num, int k) {
        string stk;
        for (char& c : num) {
            while (k && stk.size() && stk.back() > c) {
                stk.pop_back();
                --k;
            }
            stk += c;
        }
        while (k--) {
            stk.pop_back();
        }
        int i = 0;
        for (; i < stk.size() && stk[i] == '0'; ++i) {
        }
        string ans = stk.substr(i);
        return ans == "" ? "0" : ans;
    }
};
```

---

<a id="lc-316"></a>
## 31. LC 316 — Remove Duplicate Letters (Hard)

[Official problem](https://leetcode.com/problems/remove-duplicate-letters) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0316.Remove%20Duplicate%20Letters/README_EN.md)

### Problem description

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

### Constraints

- `1 <= s.length <= 10^4`

- `s` consists of lowercase English letters.

**Note:** This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

### Approach and complexity

We use an array `last` to record the last occurrence of each character, a stack to save the result string, and an array `vis` or an integer variable `mask` to record whether the current character is in the stack.

Traverse the string $s$, for each character $c$, if $c$ is not in the stack, we need to check whether the top element of the stack is greater than $c$. If it is greater than $c$ and the top element of the stack will appear later, we pop the top element of the stack and push $c$ into the stack.

Finally, concatenate the elements in the stack into a string and return it as the result.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    string removeDuplicateLetters(string s) {
        int n = s.size();
        int last[26] = {0};
        for (int i = 0; i < n; ++i) {
            last[s[i] - 'a'] = i;
        }
        string ans;
        int mask = 0;
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            if ((mask >> (c - 'a')) & 1) {
                continue;
            }
            while (!ans.empty() && ans.back() > c && last[ans.back() - 'a'] > i) {
                mask ^= 1 << (ans.back() - 'a');
                ans.pop_back();
            }
            ans.push_back(c);
            mask |= 1 << (c - 'a');
        }
        return ans;
    }
};
```

---

<a id="lc-1710"></a>
## 32. LC 1710 — Maximum Units on a Truck (Easy)

[Official problem](https://leetcode.com/problems/maximum-units-on-a-truck) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1710.Maximum%20Units%20on%20a%20Truck/README_EN.md)

### Problem description

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]`:

- `numberOfBoxes_i` is the number of boxes of type `i`.

- `numberOfUnitsPerBox_i`_ is the number of units in each box of the type `i`.

You are also given an integer `truckSize`, which is the **maximum** number of **boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return the **maximum** total number of **units** that can be put on the truck.

### Constraints

- `1 <= boxTypes.length <= 1000`

- `1 <= numberOfBoxes_i, numberOfUnitsPerBox_i <= 1000`

- `1 <= truckSize <= 10^6`

### Approach and complexity

We can also use the idea of counting sort, create an array $\textit{cnt}$ of length $1001$, where $\textit{cnt}[b]$ represents the number of boxes with $b$ units.

Then starting from the box with the maximum number of units, choose up to `truckSize` boxes, and accumulate the number of units.

The time complexity is $O(M)$, where $M$ is the maximum number of units. In this problem, $M=1000$.

### C++20 solution

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        int cnt[1001] = {0};
        for (auto& e : boxTypes) {
            int a = e[0], b = e[1];
            cnt[b] += a;
        }
        int ans = 0;
        for (int b = 1000; b > 0 && truckSize > 0; --b) {
            int a = cnt[b];
            if (a) {
                ans += b * min(truckSize, a);
                truckSize -= a;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1833"></a>
## 33. LC 1833 — Maximum Ice Cream Bars (Medium)

[Official problem](https://leetcode.com/problems/maximum-ice-cream-bars) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1833.Maximum%20Ice%20Cream%20Bars/README_EN.md)

### Problem description

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the price of the `i^th` ice cream bar in coins. The boy initially has `coins` coins to spend, and he wants to buy as many ice cream bars as possible. 

**Note:** The boy can buy the ice cream bars in any order.

Return the **maximum** number of ice cream bars the boy can buy with `coins` coins.

You must solve the problem by counting sort.

### Constraints

- `costs.length == n`

- `1 <= n <= 10^5`

- `1 <= costs[i] <= 10^5`

- `1 <= coins <= 10^8`

### Approach and complexity

To buy as many ice creams as possible, and they can be purchased in any order, we should prioritize choosing ice creams with lower prices.

Sort the $\textit{costs}$ array, and then start buying from the ice cream with the lowest price, one by one, until it is no longer possible to buy, and return the number of ice creams that can be bought.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the $\textit{costs}$ array.

### C++20 solution

```cpp
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        ranges::sort(costs);
        int n = costs.size();
        for (int i = 0; i < n; ++i) {
            if (coins < costs[i]) return i;
            coins -= costs[i];
        }
        return n;
    }
};
```

---

<a id="lc-1877"></a>
## 34. LC 1877 — Minimize Maximum Pair Sum in Array (Medium)

[Official problem](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1877.Minimize%20Maximum%20Pair%20Sum%20in%20Array/README_EN.md)

### Problem description

The **pair sum** of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is the largest **pair sum** in a list of pairs.

- For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the **maximum pair sum** would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.

Given an array `nums` of **even** length `n`, pair up the elements of `nums` into `n / 2` pairs such that:

- Each element of `nums` is in **exactly one** pair, and

- The **maximum pair sum **is **minimized**.

Return the minimized **maximum pair sum** after optimally pairing up the elements.

### Constraints

- `n == nums.length`

- `2 <= n <= 10^5`

- `n` is **even**.

- `1 <= nums[i] <= 10^5`

### Approach and complexity

To minimize the maximum pair sum in the array, we can pair the smallest number with the largest number, the second smallest with the second largest, and so on.

Therefore, we can first sort the array, then use two pointers to point to the two ends of the array. Calculate the sum of the numbers pointed to by the two pointers, update the maximum pair sum, then move the left pointer one step to the right and the right pointer one step to the left. Continue this process until the two pointers meet, and we will get the minimum maximum pair sum.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        ranges::sort(nums);
        int ans = 0, n = nums.size();
        for (int i = 0; i < n >> 1; ++i) {
            ans = max(ans, nums[i] + nums[n - i - 1]);
        }
        return ans;
    }
};
```

---

<a id="lc-1963"></a>
## 35. LC 1963 — Minimum Number of Swaps to Make the String Balanced (Medium)

[Official problem](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1900-1999/1963.Minimum%20Number%20of%20Swaps%20to%20Make%20the%20String%20Balanced/README_EN.md)

### Problem description

You are given a **0-indexed** string `s` of **even** length `n`. The string consists of **exactly** `n / 2` opening brackets `'['` and `n / 2` closing brackets `']'`.

A string is called **balanced** if and only if:

- It is the empty string, or

- It can be written as `AB`, where both `A` and `B` are **balanced** strings, or

- It can be written as `[C]`, where `C` is a **balanced** string.

You may swap the brackets at **any** two indices **any** number of times.

Return the **minimum** number of swaps to make `s` **balanced**.

### Constraints

- `n == s.length`

- `2 <= n <= 10^6`

- `n` is even.

- `s[i]` is either `'[' `or `']'`.

- The number of opening brackets `'['` equals `n / 2`, and the number of closing brackets `']'` equals `n / 2`.

### Approach and complexity

We use a variable $x$ to record the current number of unmatched left brackets. We traverse the string $s$, for each character $c$:

- If $c$ is a left bracket, then we increment $x$ by one;
- If $c$ is a right bracket, then we need to check whether $x$ is greater than zero. If it is, we match the current right bracket with the nearest unmatched left bracket on the left, i.e., decrement $x$ by one.

After the traversal, we will definitely get a string of the form `"]]]...[[[..."`. We then greedily swap the brackets at both ends each time, which can eliminate $2$ unmatched left brackets at a time. Therefore, the total number of swaps needed is $\left\lfloor \frac{x + 1}{2} \right\rfloor$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    int minSwaps(string s) {
        int x = 0;
        for (char& c : s) {
            if (c == '[') {
                ++x;
            } else if (x) {
                --x;
            }
        }
        return (x + 1) / 2;
    }
};
```

---

<a id="lc-2038"></a>
## 36. LC 2038 — Remove Colored Pieces if Both Neighbors are the Same Color (Medium)

[Official problem](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2000-2099/2038.Remove%20Colored%20Pieces%20if%20Both%20Neighbors%20are%20the%20Same%20Color/README_EN.md)

### Problem description

There are `n` pieces arranged in a line, and each piece is colored either by `'A'` or by `'B'`. You are given a string `colors` of length `n` where `colors[i]` is the color of the `i^th` piece.

Alice and Bob are playing a game where they take **alternating turns** removing pieces from the line. In this game, Alice moves** first**.

- Alice is only allowed to remove a piece colored `'A'` if **both its neighbors** are also colored `'A'`. She is **not allowed** to remove pieces that are colored `'B'`.

- Bob is only allowed to remove a piece colored `'B'` if **both its neighbors** are also colored `'B'`. He is **not allowed** to remove pieces that are colored `'A'`.

- Alice and Bob **cannot** remove pieces from the edge of the line.

- If a player cannot make a move on their turn, that player **loses** and the other player **wins**.

Assuming Alice and Bob play optimally, return `true` if Alice wins, or return `false` if Bob wins.

### Constraints

- `1 <= colors.length <= 10^5`

- `colors` consists of only the letters `'A'` and `'B'`

### Approach and complexity

We count the number of times that the string `colors` contains three consecutive `'A'`s or three consecutive `'B'`s, denoted as $a$ and $b$, respectively.

Finally, we check whether $a$ is greater than $b$. If it is, we return `true`. Otherwise, we return `false`.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $\textit{colors}$.

### C++20 solution

```cpp
class Solution {
public:
    bool winnerOfGame(string colors) {
        int n = colors.size();
        int a = 0, b = 0;
        for (int i = 0, j = 0; i < n; i = j) {
            while (j < n && colors[j] == colors[i]) {
                ++j;
            }
            int m = j - i - 2;
            if (m > 0) {
                if (colors[i] == 'A') {
                    a += m;
                } else {
                    b += m;
                }
            }
        }
        return a > b;
    }
};
```

---

<a id="lc-2160"></a>
## 37. LC 2160 — Minimum Sum of Four Digit Number After Splitting Digits (Easy)

[Official problem](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2100-2199/2160.Minimum%20Sum%20of%20Four%20Digit%20Number%20After%20Splitting%20Digits/README_EN.md)

### Problem description

You are given a **positive** integer `num` consisting of exactly four digits. Split `num` into two new integers `new1` and `new2` by using the **digits** found in `num`. **Leading zeros** are allowed in `new1` and `new2`, and **all** the digits found in `num` must be used.

- For example, given `num = 2932`, you have the following digits: two `2`'s, one `9` and one `3`. Some of the possible pairs `[new1, new2]` are `[22, 93]`, `[23, 92]`, `[223, 9]` and `[2, 329]`.

Return the **minimum** possible sum of `new1` and `new2`.

### Constraints

- `1000 <= num <= 9999`

### Approach and complexity

Sort the four digits and place the two smallest in the tens positions, the two largest in the units positions. Minimizing higher place values dominates lower positions.

Time O(1); auxiliary space O(1) for exactly four digits.

### C++20 solution

```cpp
class Solution {
public:
    int minimumSum(int num) {
        vector<int> nums;
        while (num) {
            nums.push_back(num % 10);
            num /= 10;
        }
        ranges::sort(nums);
        return 10 * (nums[0] + nums[1]) + nums[2] + nums[3];
    }
};
```

---

<a id="lc-2279"></a>
## 38. LC 2279 — Maximum Bags With Full Capacity of Rocks (Medium)

[Official problem](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2200-2299/2279.Maximum%20Bags%20With%20Full%20Capacity%20of%20Rocks/README_EN.md)

### Problem description

You have `n` bags numbered from `0` to `n - 1`. You are given two **0-indexed** integer arrays `capacity` and `rocks`. The `i^th` bag can hold a maximum of `capacity[i]` rocks and currently contains `rocks[i]` rocks. You are also given an integer `additionalRocks`, the number of additional rocks you can place in **any** of the bags.

Return the **maximum** number of bags that could have full capacity after placing the additional rocks in some bags.

### Constraints

- `n == capacity.length == rocks.length`

- `1 <= n <= 5 * 10^4`

- `1 <= capacity[i] <= 10^9`

- `0 <= rocks[i] <= capacity[i]`

- `1 <= additionalRocks <= 10^9`

### Approach and complexity

First, we calculate the remaining capacity of each bag, then sort the remaining capacities. Next, we traverse the remaining capacities from smallest to largest, putting the extra stones into the bags until the extra stones are used up or the remaining capacities of the bags are exhausted. Finally, we return the number of bags at this point.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of bags.

### C++20 solution

```cpp
class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        int n = rocks.size();
        for (int i = 0; i < n; ++i) {
            capacity[i] -= rocks[i];
        }
        ranges::sort(capacity);
        for (int i = 0; i < n; ++i) {
            additionalRocks -= capacity[i];
            if (additionalRocks < 0) {
                return i;
            }
        }
        return n;
    }
};
```

---

<a id="lc-2335"></a>
## 39. LC 2335 — Minimum Amount of Time to Fill Cups (Easy)

[Official problem](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2335.Minimum%20Amount%20of%20Time%20to%20Fill%20Cups/README_EN.md)

### Problem description

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up `2` cups with **different** types of water, or `1` cup of any type of water.

You are given a **0-indexed** integer array `amount` of length `3` where `amount[0]`, `amount[1]`, and `amount[2]` denote the number of cold, warm, and hot water cups you need to fill respectively. Return the **minimum** number of seconds needed to fill up all the cups.

### Constraints

- `amount.length == 3`

- `0 <= amount[i] <= 100`

### Approach and complexity

At least max(amount) seconds are needed for the largest type, and at least ceil(sum/2) for total throughput. Pairing cups of different types reaches the larger of those bounds.

Time O(1); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int fillCups(vector<int>& amount) {
        ranges::sort(amount);
        if (amount[0] + amount[1] <= amount[2]) {
            return amount[2];
        }
        return (amount[0] + amount[1] + amount[2] + 1) / 2;
    }
};
```

---

<a id="lc-2366"></a>
## 40. LC 2366 — Minimum Replacements to Sort the Array (Hard)

[Official problem](https://leetcode.com/problems/minimum-replacements-to-sort-the-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2366.Minimum%20Replacements%20to%20Sort%20the%20Array/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `nums`. In one operation you can replace any element of the array with **any two** elements that **sum** to it.

- For example, consider `nums = [5,6,7]`. In one operation, we can replace `nums[1]` with `2` and `4` and convert `nums` to `[5,2,4,7]`.

Return the minimum number of operations to make an array that is sorted in **non-decreasing** order.

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^9`

### Approach and complexity

We observe that to make the array $\textit{nums}$ non-decreasing or monotonically increasing, the elements towards the end of the array should be as large as possible. Therefore, it is unnecessary to replace the last element $\textit{nums}[n-1]$ of the array $\textit{nums}$ with multiple smaller numbers.

In other words, we can traverse the array $\textit{nums}$ from the end to the beginning, maintaining the current maximum value $mx$, initially $mx = \textit{nums}[n-1]$.

- If the current element $\textit{nums}[i] \leq mx$, there is no need to replace $\textit{nums}[i]$. We simply update $mx = \textit{nums}[i]$.
- Otherwise, we need to replace $\textit{nums}[i]$ with multiple numbers that sum to $\textit{nums}[i]$. The maximum of these numbers is $mx$, and the total number of replacements is $k=\left \lceil \frac{\textit{nums}[i]}{mx} \right \rceil$. Therefore, we need to perform $k-1$ operations, which are added to the answer. Among these $k$ numbers, the smallest number is $\left \lfloor \frac{\textit{nums}[i]}{k} \right \rfloor$. Therefore, we update $mx = \left \lfloor \frac{\textit{nums}[i]}{k} \right \rfloor$.

After the traversal, we return the total number of operations.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        long long ans = 0;
        int n = nums.size();
        int mx = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] <= mx) {
                mx = nums[i];
                continue;
            }
            int k = (nums[i] + mx - 1) / mx;
            ans += k - 1;
            mx = nums[i] / k;
        }
        return ans;
    }
};
```

---

<a id="lc-2405"></a>
## 41. LC 2405 — Optimal Partition of String (Medium)

[Official problem](https://leetcode.com/problems/optimal-partition-of-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2400-2499/2405.Optimal%20Partition%20of%20String/README_EN.md)

### Problem description

Given a string `s`, partition the string into one or more **substrings** such that the characters in each substring are **unique**. That is, no letter appears in a single substring more than **once**.

Return the **minimum** number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

### Constraints

- `1 <= s.length <= 10^5`

- `s` consists of only English lowercase letters.

### Approach and complexity

According to the problem description, each substring should be as long as possible and contain unique characters. Therefore, we can greedily partition the string.

We define a binary integer $\textit{mask}$ to record the characters that have appeared in the current substring. The $i$-th bit of $\textit{mask}$ being $1$ indicates that the $i$-th letter has already appeared, and $0$ indicates that it has not appeared. Additionally, we need a variable $\textit{ans}$ to record the number of substrings, initially $\textit{ans} = 1$.

Traverse each character in the string $s$. For each character $c$, convert it to an integer $x$ between $0$ and $25$, then check if the $x$-th bit of $\textit{mask}$ is $1$. If it is $1$, it means the current character $c$ is a duplicate in the current substring. In this case, increment $\textit{ans}$ by $1$ and reset $\textit{mask}$ to $0$. Otherwise, set the $x$-th bit of $\textit{mask}$ to $1$. Then, update $\textit{mask}$ to the bitwise OR result of $\textit{mask}$ and $2^x$.

Finally, return $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    int partitionString(string s) {
        int ans = 1, mask = 0;
        for (char& c : s) {
            int x = c - 'a';
            if (mask >> x & 1) {
                ++ans;
                mask = 0;
            }
            mask |= 1 << x;
        }
        return ans;
    }
};
```

---

<a id="lc-2410"></a>
## 42. LC 2410 — Maximum Matching of Players With Trainers (Medium)

[Official problem](https://leetcode.com/problems/maximum-matching-of-players-with-trainers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2400-2499/2410.Maximum%20Matching%20of%20Players%20With%20Trainers/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `players`, where `players[i]` represents the **ability** of the `i^th` player. You are also given a **0-indexed** integer array `trainers`, where `trainers[j]` represents the **training capacity **of the `j^th` trainer.

The `i^th` player can **match** with the `j^th` trainer if the player's ability is **less than or equal to** the trainer's training capacity. Additionally, the `i^th` player can be matched with at most one trainer, and the `j^th` trainer can be matched with at most one player.

Return the **maximum** number of matchings between `players` and `trainers` that satisfy these conditions.

### Constraints

- `1 <= players.length, trainers.length <= 10^5`

- `1 <= players[i], trainers[j] <= 10^9`

**Note:** This question is the same as 445: Assign Cookies.

### Approach and complexity

Sort players and trainers by ability in non-decreasing order. Pointers $i$ and $j$ mark the player and the trainer under consideration.

Start from the weakest player. While the trainer's capacity is below the player's ability, move $j$ right until a trainer is strong enough or none remain. If the trainers run out, every later player is at least as strong, so matching stops and the answer is $i$, the number already matched. Otherwise this pair matches and both pointers move forward by one. If every player is matched, return the number of players.

The time complexity is $O(m \log m + n \log n)$, and the space complexity is $O(\max(\log m, \log n))$, where $m$ and $n$ are the numbers of players and trainers, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        ranges::sort(players);
        ranges::sort(trainers);
        int m = players.size(), n = trainers.size();
        for (int i = 0, j = 0; i < m; ++i, ++j) {
            while (j < n && trainers[j] < players[i]) {
                ++j;
            }
            if (j == n) {
                return i;
            }
        }
        return m;
    }
};
```

---

<a id="lc-2491"></a>
## 43. LC 2491 — Divide Players Into Teams of Equal Skill (Medium)

[Official problem](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2400-2499/2491.Divide%20Players%20Into%20Teams%20of%20Equal%20Skill/README_EN.md)

### Problem description

You are given a positive integer array `skill` of **even** length `n` where `skill[i]` denotes the skill of the `i^th` player. Divide the players into `n / 2` teams of size `2` such that the total skill of each team is **equal**.

The **chemistry** of a team is equal to the **product** of the skills of the players on that team.

Return the sum of the **chemistry** of all the teams, or return `-1` if there is no way to divide the players into teams such that the total skill of each team is equal.

### Constraints

- `2 <= skill.length <= 10^5`

- `skill.length` is even.

- `1 <= skill[i] <= 1000`

### Approach and complexity

Every team must have target=sum/(n/2). For each player, consume an available complement or store that player for a later match. Reject complements outside the allowed value domain before indexing; count matched teams to detect leftovers.

Time O(n+U); auxiliary space O(U), U=1001.

### C++20 solution

```cpp
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int teams = skill.size() / 2;
        int sum = accumulate(skill.begin(), skill.end(), 0);
        if (sum % teams) return -1;
        int target = sum / teams;
        array<int, 1001> waiting{};
        long long chemistry = 0;
        int matched = 0;
        for (int x : skill) {
            int y = target - x;
            if (y < 1 || y > 1000) return -1;
            if (waiting[y]) { --waiting[y]; ++matched; chemistry += 1LL * x * y; }
            else ++waiting[x];
        }
        return matched == teams ? chemistry : -1;
    }
};
```

---

<a id="lc-2578"></a>
## 44. LC 2578 — Split With Minimum Sum (Easy)

[Official problem](https://leetcode.com/problems/split-with-minimum-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2500-2599/2578.Split%20With%20Minimum%20Sum/README_EN.md)

### Problem description

Given a positive integer `num`, split it into two non-negative integers `num1` and `num2` such that:

- The concatenation of `num1` and `num2` is a permutation of `num`.

- In other words, the sum of the number of occurrences of each digit in `num1` and `num2` is equal to the number of occurrences of that digit in `num`.

- `num1` and `num2` can contain leading zeros.

Return the **minimum** possible sum of `num1` and `num2`.

**Notes:**

- It is guaranteed that `num` does not contain any leading zeros.

- The order of occurrence of the digits in `num1` and `num2` may differ from the order of occurrence of `num`.

### Constraints

- `10 <= num <= 10^9`

### Approach and complexity

First, we use a hash table or array $\textit{cnt}$ to count the occurrences of each digit in $\textit{num}$, and use a variable $n$ to record the number of digits in $\textit{num}$.

Next, we enumerate all the digits $i$ in $\textit{nums}$, and alternately allocate the digits in $\textit{cnt}$ to $\textit{num1}$ and $\textit{num2}$ in ascending order, recording them in an array $\textit{ans}$ of length $2$. Finally, we return the sum of the two numbers in $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(C)$, where $n$ is the number of digits in $\textit{num}$; and $C$ is the number of different digits in $\textit{num}$, in this problem, $C \leq 10$.

### C++20 solution

```cpp
class Solution {
public:
    int splitNum(int num) {
        int cnt[10]{};
        int n = 0;
        for (; num; num /= 10) {
            ++cnt[num % 10];
            ++n;
        }
        int ans[2]{};
        for (int i = 0, j = 0; i < n; ++i) {
            while (cnt[j] == 0) {
                ++j;
            }
            --cnt[j];
            ans[i & 1] = ans[i & 1] * 10 + j;
        }
        return ans[0] + ans[1];
    }
};
```

---

<a id="lc-2587"></a>
## 45. LC 2587 — Rearrange Array to Maximize Prefix Score (Medium)

[Official problem](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2500-2599/2587.Rearrange%20Array%20to%20Maximize%20Prefix%20Score/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `nums`. You can rearrange the elements of `nums` to **any order** (including the given order).

Let `prefix` be the array containing the prefix sums of `nums` after rearranging it. In other words, `prefix[i]` is the sum of the elements from `0` to `i` in `nums` after rearranging it. The **score** of `nums` is the number of positive integers in the array `prefix`.

Return the maximum score you can achieve.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^6 <= nums[i] <= 10^6`

### Approach and complexity

To maximize the number of positive integers in the prefix sum array, we need to make the elements in the prefix sum array as large as possible, that is, to add as many positive integers as possible. Therefore, we can sort the array $\textit{nums}$ in descending order, then traverse the array, maintaining the prefix sum $s$. If $s \leq 0$, it means that there can be no more positive integers in the current position and the positions after it, so we can directly return the current position.

Otherwise, after the traversal, we return the length of the array.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int maxScore(vector<int>& nums) {
        sort(nums.rbegin(), nums.rend());
        long long s = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            s += nums[i];
            if (s <= 0) {
                return i;
            }
        }
        return n;
    }
};
```

---

<a id="lc-2616"></a>
## 46. LC 2616 — Minimize the Maximum Difference of Pairs (Medium)

[Official problem](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2600-2699/2616.Minimize%20the%20Maximum%20Difference%20of%20Pairs/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `nums` and an integer `p`. Find `p` pairs of indices of `nums` such that the **maximum** difference amongst all the pairs is **minimized**. Also, ensure no index appears more than once amongst the `p` pairs.

Note that for a pair of elements at the index `i` and `j`, the difference of this pair is `|nums[i] - nums[j]|`, where `|x|` represents the **absolute** **value** of `x`.

Return the **minimum** **maximum** difference among all `p` pairs. We define the maximum of an empty set to be zero.

### Constraints

- `1 <= nums.length <= 10^5`

- `0 <= nums[i] <= 10^9`

- `0 <= p <= (nums.length)/2`

### Approach and complexity

We notice that the maximum difference has monotonicity: if a maximum difference $x$ is feasible, then $x-1$ is also feasible. Therefore, we can use binary search to find the minimal feasible maximum difference.

First, sort the array $\textit{nums}$. Then, for a given maximum difference $x$, check whether it is possible to form $p$ pairs of indices such that the maximum difference in each pair does not exceed $x$. If possible, we can try a smaller $x$; otherwise, we need to increase $x$.

To check whether $p$ such pairs exist with maximum difference at most $x$, we can use a greedy approach. Traverse the sorted array $\textit{nums}$ from left to right. For the current index $i$, if the difference between $\textit{nums}[i+1]$ and $\textit{nums}[i]$ does not exceed $x$, we can form a pair with $i$ and $i+1$, increment the pair count $\textit{cnt}$, and increase $i$ by $2$. Otherwise, increase $i$ by $1$. After traversing, if $\textit{cnt} \geq p$, then such $p$ pairs exist; otherwise, they do not.

The time complexity is $O(n(\log n + \log m))$, and the space complexity is $O(1)$, where $n$ is the length of $\textit{nums}$ and $m$ is the difference between the maximum and minimum values in $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        ranges::sort(nums);
        int n = nums.size();
        int l = 0, r = nums[n - 1] - nums[0] + 1;
        auto check = [&](int diff) -> bool {
            int cnt = 0;
            for (int i = 0; i < n - 1; ++i) {
                if (nums[i + 1] - nums[i] <= diff) {
                    ++cnt;
                    ++i;
                }
            }
            return cnt >= p;
        };
        while (l < r) {
            int mid = (l + r) >> 1;
            if (check(mid)) {
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

<a id="lc-3075"></a>
## 47. LC 3075 — Maximize Happiness of Selected Children (Medium)

[Official problem](https://leetcode.com/problems/maximize-happiness-of-selected-children) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/3000-3099/3075.Maximize%20Happiness%20of%20Selected%20Children/README_EN.md)

### Problem description

You are given an array `happiness` of length `n`, and a **positive** integer `k`.

There are `n` children standing in a queue, where the `i^th` child has **happiness value** `happiness[i]`. You want to select `k` children from these `n` children in `k` turns.

In each turn, when you select a child, the **happiness value** of all the children that have **not** been selected till now decreases by `1`. Note that the happiness value **cannot** become negative and gets decremented **only** if it is positive.

Return the **maximum** sum of the happiness values of the selected children you can achieve by selecting `k` children.

### Constraints

- `1 <= n == happiness.length <= 2 * 10^5`

- `1 <= happiness[i] <= 10^8`

- `1 <= k <= n`

### Approach and complexity

To maximize the sum of happiness values, we should prioritize selecting children with higher happiness values. Therefore, we can sort the children in descending order by happiness value, and then select $k$ children in sequence. For the current $i$-th child, the happiness value obtained is $\max(\textit{happiness}[i] - i, 0)$. Finally, return the sum of happiness values of these $k$ children.

The time complexity is $O(n \log n + k)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{happiness}$.

### C++20 solution

```cpp
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.rbegin(), happiness.rend());
        long long ans = 0;
        for (int i = 0, n = happiness.size(); i < k; ++i) {
            int x = happiness[i] - i;
            ans += max(x, 0);
        }
        return ans;
    }
};
```

---

<a id="lc-502"></a>
## 48. LC 502 — IPO (Hard)

[Official problem](https://leetcode.com/problems/ipo) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0502.IPO/README_EN.md)

### Problem description

Suppose LeetCode will start its **IPO** soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the **IPO**. Since it has limited resources, it can only finish at most `k` distinct projects before the **IPO**. Help LeetCode design the best way to maximize its total capital after finishing at most `k` distinct projects.

You are given `n` projects where the `i^th` project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it.

Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of **at most** `k` distinct projects from given projects to **maximize your final capital**, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

### Constraints

- `1 <= k <= 10^5`

- `0 <= w <= 10^9`

- `n == profits.length`

- `n == capital.length`

- `1 <= n <= 10^5`

- `0 <= profits[i] <= 10^4`

- `0 <= capital[i] <= 10^9`

### Approach and complexity

Sort projects by capital requirement. Add newly affordable profits to a max heap, then select the highest available profit. This maximizes capital after each choice and never reduces future eligibility.

Time O(n log n+k log n); auxiliary space O(n).

### C++20 solution

```cpp
using pii = pair<int, int>;

class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        priority_queue<pii, vector<pii>, greater<pii>> q1;
        int n = profits.size();
        for (int i = 0; i < n; ++i) {
            q1.push({capital[i], profits[i]});
        }
        priority_queue<int> q2;
        while (k--) {
            while (!q1.empty() && q1.top().first <= w) {
                q2.push(q1.top().second);
                q1.pop();
            }
            if (q2.empty()) {
                break;
            }
            w += q2.top();
            q2.pop();
        }
        return w;
    }
};
```

---

<a id="lc-630"></a>
## 49. LC 630 — Course Schedule III (Hard)

[Official problem](https://leetcode.com/problems/course-schedule-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0630.Course%20Schedule%20III/README_EN.md)

### Problem description

There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [duration_i, lastDay_i]` indicate that the `i^th` course should be taken continuously for `duration_i` days and must be finished before or on `lastDay_i`.

You will start on the `1^st` day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

### Constraints

- `1 <= courses.length <= 10^4`

- `1 <= duration_i, lastDay_i <= 10^4`

### Approach and complexity

We can sort the courses in ascending order by their end time, and each time select the course with the earliest deadline to take.

If the total time $s$ of the selected courses exceeds the end time $\textit{last}$ of the current course, we remove the course with the longest duration from the previously selected courses, until the constraint of the current course's end time is satisfied. Here we use a priority queue (max-heap) $pq$ to maintain the durations of the currently selected courses, and each time we pop the course with the longest duration from the priority queue to remove it.

Finally, the number of elements in the priority queue is the maximum number of courses we can take.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of courses.

### C++20 solution

```cpp
class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        ranges::sort(courses, [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        priority_queue<int> pq;
        int s = 0;
        for (auto& e : courses) {
            int duration = e[0], last = e[1];
            pq.push(duration);
            s += duration;
            while (s > last) {
                s -= pq.top();
                pq.pop();
            }
        }
        return pq.size();
    }
};
```

---

<a id="lc-1642"></a>
## 50. LC 1642 — Furthest Building You Can Reach (Medium)

[Official problem](https://leetcode.com/problems/furthest-building-you-can-reach) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1642.Furthest%20Building%20You%20Can%20Reach/README_EN.md)

### Problem description

You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`.

You start your journey from building `0` and move to the next building by possibly using bricks or ladders.

While moving from building `i` to building `i+1` (**0-indexed**),

- If the current building's height is **greater than or equal** to the next building's height, you do **not** need a ladder or bricks.

- If the current building's height is less than the next building's height, you can either use **one ladder** or `(h[i+1] - h[i])` **bricks**.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

### Constraints

- `1 <= heights.length <= 10^5`

- `1 <= heights[i] <= 10^6`

- `0 <= bricks <= 10^9`

- `0 <= ladders <= heights.length`

### Approach and complexity

Push every positive climb into a min heap representing climbs assigned ladders. If there are too many, pay bricks for the smallest, reserving ladders for the largest climbs encountered.

Time O(n log(ladders+2)); auxiliary space O(min(n,ladders+1)).

### C++20 solution

```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int, vector<int>, greater<int>> q;
        int n = heights.size();
        for (int i = 0; i < n - 1; ++i) {
            int a = heights[i], b = heights[i + 1];
            int d = b - a;
            if (d > 0) {
                q.push(d);
                if (q.size() > ladders) {
                    bricks -= q.top();
                    q.pop();
                    if (bricks < 0) {
                        return i;
                    }
                }
            }
        }
        return n - 1;
    }
};
```
