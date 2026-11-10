# 11. Heap / Priority Queue — C++20 solutions

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

1. [LC 215 — Kth Largest Element in an Array](#lc-215)
2. [LC 347 — Top K Frequent Elements](#lc-347)
3. [LC 23 — Merge k Sorted Lists](#lc-23)
4. [LC 295 — Find Median from Data Stream](#lc-295)
5. [LC 703 — Kth Largest Element in a Stream](#lc-703)
6. [LC 973 — K Closest Points to Origin](#lc-973)
7. [LC 692 — Top K Frequent Words](#lc-692)
8. [LC 1046 — Last Stone Weight](#lc-1046)
9. [LC 373 — Find K Pairs with Smallest Sums](#lc-373)
10. [LC 378 — Kth Smallest Element in a Sorted Matrix](#lc-378)
11. [LC 767 — Reorganize String](#lc-767)
12. [LC 621 — Task Scheduler](#lc-621)
13. [LC 502 — IPO](#lc-502)
14. [LC 630 — Course Schedule III](#lc-630)
15. [LC 1642 — Furthest Building You Can Reach](#lc-1642)
16. [LC 253 — Meeting Rooms II](#lc-253)
17. [LC 2402 — Meeting Rooms III](#lc-2402)
18. [LC 1834 — Single-Threaded CPU](#lc-1834)
19. [LC 1882 — Process Tasks Using Servers](#lc-1882)
20. [LC 2462 — Total Cost to Hire K Workers](#lc-2462)
21. [LC 2542 — Maximum Subsequence Score](#lc-2542)
22. [LC 857 — Minimum Cost to Hire K Workers](#lc-857)
23. [LC 871 — Minimum Number of Refueling Stops](#lc-871)
24. [LC 1353 — Maximum Number of Events That Can Be Attended](#lc-1353)
25. [LC 1851 — Minimum Interval to Include Each Query](#lc-1851)
26. [LC 1942 — The Number of the Smallest Unoccupied Chair](#lc-1942)
27. [LC 1962 — Remove Stones to Minimize the Total](#lc-1962)
28. [LC 2208 — Minimum Operations to Halve Array Sum](#lc-2208)
29. [LC 2336 — Smallest Number in Infinite Set](#lc-2336)
30. [LC 2353 — Design a Food Rating System](#lc-2353)
31. [LC 264 — Ugly Number II](#lc-264)
32. [LC 313 — Super Ugly Number](#lc-313)
33. [LC 2642 — Design Graph With Shortest Path Calculator](#lc-2642)
34. [LC 743 — Network Delay Time](#lc-743)
35. [LC 1514 — Path with Maximum Probability](#lc-1514)
36. [LC 1631 — Path With Minimum Effort](#lc-1631)
37. [LC 778 — Swim in Rising Water](#lc-778)
38. [LC 407 — Trapping Rain Water II](#lc-407)
39. [LC 632 — Smallest Range Covering Elements from K Lists](#lc-632)
40. [LC 480 — Sliding Window Median](#lc-480)
41. [LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](#lc-1438)
42. [LC 239 — Sliding Window Maximum](#lc-239)
43. [LC 451 — Sort Characters By Frequency](#lc-451)
44. [LC 659 — Split Array into Consecutive Subsequences](#lc-659)
45. [LC 846 — Hand of Straights](#lc-846)
46. [LC 1167 — Minimum Cost to Connect Sticks](#lc-1167)
47. [LC 1792 — Maximum Average Pass Ratio](#lc-1792)
48. [LC 2233 — Maximum Product After K Increments](#lc-2233)
49. [LC 2558 — Take Gifts From the Richest Pile](#lc-2558)
50. [LC 3066 — Minimum Operations to Exceed Threshold Value II](#lc-3066)

---

<a id="lc-215"></a>
## 1. LC 215 — Kth Largest Element in an Array (Medium)

[Official problem](https://leetcode.com/problems/kth-largest-element-in-an-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0215.Kth%20Largest%20Element%20in%20an%20Array/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `k`, return the `k^th` largest element in the array.

Note that it is the `k^th` largest element in the sorted order, not the `k^th` distinct element.

Can you solve it without sorting?

### Constraints

- `1 <= k <= nums.length <= 10^5`

- `-10^4 <= nums[i] <= 10^4`

### Approach and complexity

The official values lie in [−10⁴,10⁴]. Count each value with an offset, then scan downward until k elements have been accounted for. This gives a deterministic bound and avoids quickselect’s quadratic worst case.

Time O(n+U); auxiliary space O(U), where U=20001. For unbounded values, nth_element gives average O(n) time.

### C++20 solution

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        array<int, 20001> count{};
        for (int x : nums) ++count[x + 10000];
        for (int i = 20000; i >= 0; --i) {
            k -= count[i];
            if (k <= 0) return i - 10000;
        }
        return 0;
    }
};
```

---

<a id="lc-347"></a>
## 2. LC 347 — Top K Frequent Elements (Medium)

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

<a id="lc-23"></a>
## 3. LC 23 — Merge k Sorted Lists (Hard)

[Official problem](https://leetcode.com/problems/merge-k-sorted-lists) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0023.Merge%20k%20Sorted%20Lists/README_EN.md)

### Problem description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Constraints

- `k == lists.length`

- `0 <= k <= 10^4`

- `0 <= lists[i].length <= 500`

- `-10^4 <= lists[i][j] <= 10^4`

- `lists[i]` is sorted in **ascending order**.

- The sum of `lists[i].length` will not exceed `10^4`.

### Approach and complexity

We can create a min heap $pq$ to maintain the head nodes of all linked lists. Each time, we take out the node with the smallest value from the min heap, add it to the end of the result linked list, and then add the next node of this node to the heap. Repeat the above steps until the heap is empty.

The time complexity is $O(n \log k)$, and the space complexity is $O(k)$, where $n$ is the total number of all linked list nodes, and $k$ is the number of linked lists given in the problem.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq;
        for (auto head : lists) {
            if (head) {
                pq.push(head);
            }
        }
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            if (node->next) {
                pq.push(node->next);
            }
            cur->next = node;
            cur = cur->next;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-295"></a>
## 4. LC 295 — Find Median from Data Stream (Hard)

[Official problem](https://leetcode.com/problems/find-median-from-data-stream) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0295.Find%20Median%20from%20Data%20Stream/README_EN.md)

### Problem description

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.

- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.

- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.

- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

### Constraints

- `-10^5 <= num <= 10^5`

- There will be at least one element in the data structure before calling `findMedian`.

- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

**Follow up:**

- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

### Approach and complexity

We can use two heaps to maintain all the elements, a min heap $\textit{minQ}$ and a max heap $\textit{maxQ}$, where the min heap $\textit{minQ}$ stores the larger half, and the max heap $\textit{maxQ}$ stores the smaller half.

When calling the $\textit{addNum}$ method, we first add the element to the max heap $\textit{maxQ}$, then pop the top element of $\textit{maxQ}$ and add it to the min heap $\textit{minQ}$. If at this time the size difference between $\textit{minQ}$ and $\textit{maxQ}$ is greater than $1$, we pop the top element of $\textit{minQ}$ and add it to $\textit{maxQ}$. The time complexity is $O(\log n)$.

When calling the $\textit{findMedian}$ method, if the size of $\textit{minQ}$ is equal to the size of $\textit{maxQ}$, it means the total number of elements is even, and we can return the average value of the top elements of $\textit{minQ}$ and $\textit{maxQ}$; otherwise, we return the top element of $\textit{minQ}$. The time complexity is $O(1)$.

The space complexity is $O(n)$, where $n$ is the number of elements.

### C++20 solution

```cpp
class MedianFinder {
public:
    MedianFinder() {
    }

    void addNum(int num) {
        maxQ.push(num);
        minQ.push(maxQ.top());
        maxQ.pop();

        if (minQ.size() > maxQ.size() + 1) {
            maxQ.push(minQ.top());
            minQ.pop();
        }
    }

    double findMedian() {
        return minQ.size() == maxQ.size() ? (minQ.top() + maxQ.top()) / 2.0 : minQ.top();
    }

private:
    priority_queue<int> maxQ;
    priority_queue<int, vector<int>, greater<int>> minQ;
};
```

---

<a id="lc-703"></a>
## 5. LC 703 — Kth Largest Element in a Stream (Easy)

[Official problem](https://leetcode.com/problems/kth-largest-element-in-a-stream) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0703.Kth%20Largest%20Element%20in%20a%20Stream/README_EN.md)

### Problem description

You are part of a university admissions office and need to keep track of the `kth` highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer `k`, maintains a stream of test scores and continuously returns the `k`th highest test score **after** a new score has been submitted. More specifically, we are looking for the `k`th highest score in the sorted list of all scores.

Implement the `KthLargest` class:

- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of test scores `nums`.

- `int add(int val)` Adds a new test score `val` to the stream and returns the element representing the `k^th` largest element in the pool of test scores so far.

### Constraints

- `0 <= nums.length <= 10^4`

- `1 <= k <= nums.length + 1`

- `-10^4 <= nums[i] <= 10^4`

- `-10^4 <= val <= 10^4`

- At most `10^4` calls will be made to `add`.

### Approach and complexity

We maintain a priority queue (min heap) $\textit{minQ}$.

Initially, we add the elements of the array $\textit{nums}$ to $\textit{minQ}$ one by one, ensuring that the size of $\textit{minQ}$ does not exceed $k$. The time complexity is $O(n \log k)$.

Each time a new element is added, if the size of $\textit{minQ}$ exceeds $k$, we pop the top element of the heap to ensure that the size of $\textit{minQ}$ is $k$. The time complexity is $O(\log k)$.

In this way, the elements in $\textit{minQ}$ are the largest $k$ elements in the array $\textit{nums}$, and the top element of the heap is the $k^{th}$ largest element.

The space complexity is $O(k)$.

### C++20 solution

```cpp
class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int x : nums) {
            add(x);
        }
    }

    int add(int val) {
        minQ.push(val);
        if (minQ.size() > k) {
            minQ.pop();
        }
        return minQ.top();
    }

private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minQ;
};
```

---

<a id="lc-973"></a>
## 6. LC 973 — K Closest Points to Origin (Medium)

[Official problem](https://leetcode.com/problems/k-closest-points-to-origin) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0973.K%20Closest%20Points%20to%20Origin/README_EN.md)

### Problem description

Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `√(x_1 - x_2)^2 + (y_1 - y_2)^2`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

### Constraints

- `1 <= k <= points.length <= 10^4`

- `-10^4 <= x_i, y_i <= 10^4`

### Approach and complexity

Partition points with nth_element so the first k have the k smallest squared distances. Their relative order is irrelevant. Integer squared distances avoid square roots and floating-point comparisons.

Average time O(n), plus O(k) output copying. Standard nth_element does not promise worst-case linear time or a fixed auxiliary-space bound; typical introspective implementations use O(log n) stack. A bounded max heap offers O(n log k) worst-case time and O(k) space.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto distance = [](const vector<int>& p) { return 1LL * p[0] * p[0] + 1LL * p[1] * p[1]; };
        if (k < static_cast<int>(points.size()))
            ranges::nth_element(points, points.begin() + k, {}, distance);
        return {points.begin(), points.begin() + k};
    }
};
```

---

<a id="lc-692"></a>
## 7. LC 692 — Top K Frequent Words (Medium)

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

<a id="lc-1046"></a>
## 8. LC 1046 — Last Stone Weight (Easy)

[Official problem](https://leetcode.com/problems/last-stone-weight) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1046.Last%20Stone%20Weight/README_EN.md)

### Problem description

You are given an array of integers `stones` where `stones[i]` is the weight of the `i^th` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and

- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return the weight of the last remaining stone. If there are no stones left, return `0`.

### Constraints

- `1 <= stones.length <= 30`

- `1 <= stones[i] <= 1000`

### Approach and complexity

A max heap extracts the two largest stones. Return their positive difference to the heap and repeat until at most one remains.

Time O(n log n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for (int x : stones) {
            pq.push(x);
        }
        while (pq.size() > 1) {
            int y = pq.top();
            pq.pop();
            int x = pq.top();
            pq.pop();
            if (x != y) {
                pq.push(y - x);
            }
        }
        return pq.empty() ? 0 : pq.top();
    }
};
```

---

<a id="lc-373"></a>
## 9. LC 373 — Find K Pairs with Smallest Sums (Medium)

[Official problem](https://leetcode.com/problems/find-k-pairs-with-smallest-sums) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0373.Find%20K%20Pairs%20with%20Smallest%20Sums/README_EN.md)

### Problem description

You are given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order** and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return the `k` pairs `(u_1, v_1), (u_2, v_2), ..., (u_k, v_k)` with the smallest sums.

### Constraints

- `1 <= nums1.length, nums2.length <= 10^5`

- `-10^9 <= nums1[i], nums2[i] <= 10^9`

- `nums1` and `nums2` both are sorted in **non-decreasing order**.

- `1 <= k <= 10^4`

- `k <= nums1.length * nums2.length`

### Approach and complexity

Each fixed first-array index generates a sorted row of pair sums. Seed the heap with the first pair of each relevant row, pop the smallest, and advance only that row.

Time O(min(k,m) log(min(k,m)+1)+k log(min(k,m)+1)); auxiliary space O(min(k,m)), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        auto cmp = [&nums1, &nums2](const pair<int, int>& a, const pair<int, int>& b) {
            return nums1[a.first] + nums2[a.second] > nums1[b.first] + nums2[b.second];
        };

        int m = nums1.size();
        int n = nums2.size();
        vector<vector<int>> ans;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        for (int i = 0; i < min(k, m); i++)
            pq.emplace(i, 0);
        while (k-- && !pq.empty()) {
            auto [x, y] = pq.top();
            pq.pop();
            ans.emplace_back(initializer_list<int>{nums1[x], nums2[y]});
            if (y + 1 < n)
                pq.emplace(x, y + 1);
        }

        return ans;
    }
};
```

---

<a id="lc-378"></a>
## 10. LC 378 — Kth Smallest Element in a Sorted Matrix (Medium)

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

<a id="lc-767"></a>
## 11. LC 767 — Reorganize String (Medium)

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

<a id="lc-621"></a>
## 12. LC 621 — Task Scheduler (Medium)

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

<a id="lc-502"></a>
## 13. LC 502 — IPO (Hard)

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
## 14. LC 630 — Course Schedule III (Hard)

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
## 15. LC 1642 — Furthest Building You Can Reach (Medium)

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

---

<a id="lc-253"></a>
## 16. LC 253 — Meeting Rooms II (Hard)

[Official problem](https://leetcode.com/problems/meeting-rooms-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0253.Meeting%20Rooms%20II/README_EN.md)

### Problem description

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

### Constraints

- `1 <= intervals.length <= 10^4`

- `0 <= start_i < end_i <= 10^6`

### Approach and complexity

If the meeting times span a large range, we can use a hash map instead of a difference array.

First, we create a hash map $d$, where we add to the corresponding positions for each meeting's start time and end time: $d[l] = d[l] + 1$ for the start time, and $d[r] = d[r] - 1$ for the end time.

Then, we sort the hash map by its keys, calculate the prefix sum of the hash map, and find the maximum value of the prefix sum, which represents the minimum number of meeting rooms required.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of meetings.

### C++20 solution

```cpp
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> d;
        for (const auto& e : intervals) {
            d[e[0]]++;
            d[e[1]]--;
        }
        int ans = 0, s = 0;
        for (auto& [_, v] : d) {
            s += v;
            ans = max(ans, s);
        }
        return ans;
    }
};
```

---

<a id="lc-2402"></a>
## 17. LC 2402 — Meeting Rooms III (Hard)

[Official problem](https://leetcode.com/problems/meeting-rooms-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2400-2499/2402.Meeting%20Rooms%20III/README_EN.md)

### Problem description

You are given an integer `n`. There are `n` rooms numbered from `0` to `n - 1`.

You are given a 2D integer array `meetings` where `meetings[i] = [start_i, end_i]` means that a meeting will be held during the **half-closed** time interval `[start_i, end_i)`. All the values of `start_i` are **unique**.

Meetings are allocated to rooms in the following manner:

- Each meeting will take place in the unused room with the **lowest** number.

- If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the **same** duration as the original meeting.

- When a room becomes unused, meetings that have an earlier original **start** time should be given the room.

Return the **number** of the room that held the most meetings. If there are multiple rooms, return the room with the **lowest** number.

A **half-closed interval** `[a, b)` is the interval between `a` and `b` **including** `a` and **not including** `b`.

### Constraints

- `1 <= n <= 100`

- `1 <= meetings.length <= 10^5`

- `meetings[i].length == 2`

- `0 <= start_i < end_i <= 5 * 10^5`

- All the values of `start_i` are **unique**.

### Approach and complexity

We define two priority queues to represent idle meeting rooms and busy meeting rooms respectively. The idle meeting rooms $\textit{idle}$ are sorted by **index**; the busy meeting rooms $\textit{busy}$ are sorted by **end time and index**.

First, sort the meetings by start time, then iterate through the meetings. For each meeting:

- If there are busy meeting rooms with end time less than or equal to the current meeting's start time, add them to the idle meeting rooms queue $\textit{idle}$;
- If there are idle meeting rooms available, take the room with the smallest index from the idle queue $\textit{idle}$ and add it to the busy queue $\textit{busy}$;
- If there are no idle meeting rooms, find the room with the earliest end time and smallest index from the busy queue $\textit{busy}$, and add it back to the busy queue $\textit{busy}$.

The time complexity is $O(m (\log m + \log n))$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the number of meeting rooms and meetings respectively.

Similar problems:

- [1882. Process Tasks Using Servers](https://github.com/doocs/leetcode/blob/main/solution/1800-1899/1882.Process%20Tasks%20Using%20Servers/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        ranges::sort(meetings);
        using pli = pair<long long, int>;
        priority_queue<pli, vector<pli>, greater<pli>> busy;
        priority_queue<int, vector<int>, greater<int>> idle;
        for (int i = 0; i < n; ++i) {
            idle.push(i);
        }
        vector<int> cnt(n);
        for (auto& v : meetings) {
            int s = v[0], e = v[1];
            while (!busy.empty() && busy.top().first <= s) {
                idle.push(busy.top().second);
                busy.pop();
            }
            int i = 0;
            if (!idle.empty()) {
                i = idle.top();
                idle.pop();
                busy.push({e, i});
            } else {
                auto x = busy.top();
                busy.pop();
                i = x.second;
                busy.push({x.first + e - s, i});
            }
            ++cnt[i];
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (cnt[ans] < cnt[i]) {
                ans = i;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1834"></a>
## 18. LC 1834 — Single-Threaded CPU (Medium)

[Official problem](https://leetcode.com/problems/single-threaded-cpu) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1834.Single-Threaded%20CPU/README_EN.md)

### Problem description

You are given `n`​​​​​​ tasks labeled from `0` to `n - 1` represented by a 2D integer array `tasks`, where `tasks[i] = [enqueueTime_i, processingTime_i]` means that the `i^​​​​​​th`​​​​ task will be available to process at `enqueueTime_i` and will take `processingTime_i`_ to finish processing.

You have a single-threaded CPU that can process **at most one** task at a time and will act in the following way:

- If the CPU is idle and there are no available tasks to process, the CPU remains idle.

- If the CPU is idle and there are available tasks, the CPU will choose the one with the **shortest processing time**. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.

- Once a task is started, the CPU will **process the entire task** without stopping.

- The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

### Constraints

​​​​​​​

- `1 <= tasks.length <= 10^5`

- `tasks[i] = [enqueueTime_i, processingTime_i]`

- `1 <= enqueueTime_i, processingTime_i <= 10^9`

### Approach and complexity

First, we sort the tasks by `enqueueTime` in ascending order. Next, we use a priority queue (min heap) to maintain the currently executable tasks. The elements in the queue are `(processingTime, index)`, which represent the execution time and the index of the task. We also use a variable $t$ to represent the current time, initially set to $0$.

Next, we simulate the execution process of the tasks.

If the current queue is empty, it means there are no executable tasks at the moment. We update $t$ to the larger value between the `enqueueTime` of the next task and the current time $t$. Then, we add all tasks with `enqueueTime` less than or equal to $t$ to the queue.

Then, we take out a task from the queue, add its index to the answer array, and update $t$ to the sum of the current time $t$ and the execution time of the current task.

We repeat the above process until the queue is empty and all tasks have been added to the queue.

The time complexity is $O(n \log n)$, where $n$ is the number of tasks.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = 0;
        for (auto& task : tasks) task.push_back(n++);
        ranges::sort(tasks);
        using pii = pair<int, int>;
        priority_queue<pii, vector<pii>, greater<pii>> q;
        int i = 0;
        long long t = 0;
        vector<int> ans;
        while (!q.empty() || i < n) {
            if (q.empty()) t = max(t, (long long) tasks[i][0]);
            while (i < n && tasks[i][0] <= t) {
                q.push({tasks[i][1], tasks[i][2]});
                ++i;
            }
            auto [pt, j] = q.top();
            q.pop();
            ans.push_back(j);
            t += pt;
        }
        return ans;
    }
};
```

---

<a id="lc-1882"></a>
## 19. LC 1882 — Process Tasks Using Servers (Medium)

[Official problem](https://leetcode.com/problems/process-tasks-using-servers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1882.Process%20Tasks%20Using%20Servers/README_EN.md)

### Problem description

You are given two **0-indexed** integer arrays `servers` and `tasks` of lengths `n`​​​​​​ and `m`​​​​​​ respectively. `servers[i]` is the **weight** of the `i^​​​​​​th`​​​​ server, and `tasks[j]` is the **time needed** to process the `j^​​​​​​th`​​​​ task **in seconds**.

Tasks are assigned to the servers using a **task queue**. Initially, all servers are free, and the queue is **empty**.

At second `j`, the `j^th` task is **inserted** into the queue (starting with the `0^th` task being inserted at second `0`). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the **smallest weight**, and in case of a tie, it is assigned to a free server with the **smallest index**.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned **in order of insertion** following the weight and index priorities above.

A server that is assigned task `j` at second `t` will be free again at second `t + tasks[j]`.

Build an array `ans`​​​​ of length `m`, where `ans[j]` is the **index** of the server the `j^​​​​​​th` task will be assigned to.

Return the array `ans`​​​​.

### Constraints

- `servers.length == n`

- `tasks.length == m`

- `1 <= n, m <= 2 * 10^5`

- `1 <= servers[i], tasks[j] <= 2 * 10^5`

### Approach and complexity

We use a min-heap $\textit{idle}$ to maintain all idle servers, where each element is a tuple $(x, i)$ representing the $i$-th server with weight $x$. We use another min-heap $\textit{busy}$ to maintain all busy servers, where each element is a tuple $(w, s, i)$ representing the $i$-th server that will be idle at time $w$ with weight $s$. Initially, we add all servers to $\textit{idle}$.

Next, we iterate through all tasks. For the $j$-th task, we first remove all servers from $\textit{busy}$ that will be idle at or before time $j$ and add them to $\textit{idle}$. Then we take the server with the smallest weight from $\textit{idle}$, add it to $\textit{busy}$, and assign it to the $j$-th task. If $\textit{idle}$ is empty, we take the server with the earliest idle time from $\textit{busy}$, add it to $\textit{busy}$, and assign it to the $j$-th task.

After iterating through all tasks, we obtain the answer array $\textit{ans}$.

The Rust version uses `BinaryHeap` with `Reverse` to emulate the min-heaps: the idle heap holds $(\textit{weight}, \textit{index})$ pairs and the busy heap holds $(\textit{free\_time}, \textit{weight}, \textit{index})$ triples, so the pop order matches the description above.

The time complexity is $O((n + m) \log n)$, and the space complexity is $O(n)$, where $n$ is the number of servers and $m$ is the number of tasks, and $n$ and $m$ are the number of servers and tasks, respectively.

Similar problems:

- [2402. Meeting Rooms III](https://github.com/doocs/leetcode/blob/main/solution/2400-2499/2402.Meeting%20Rooms%20III/README_EN.md)

### C++20 solution

```cpp
class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        using pii = pair<int, int>;
        using arr3 = array<long long, 3>;
        priority_queue<pii, vector<pii>, greater<pii>> idle;
        priority_queue<arr3, vector<arr3>, greater<arr3>> busy;
        for (int i = 0; i < servers.size(); ++i) {
            idle.push({servers[i], i});
        }
        int m = tasks.size();
        vector<int> ans(m);
        for (int j = 0; j < m; ++j) {
            int t = tasks[j];
            while (!busy.empty() && busy.top()[0] <= j) {
                auto [_, s, i] = busy.top();
                busy.pop();
                idle.push({(int) s, (int) i});
            }

            if (!idle.empty()) {
                auto [s, i] = idle.top();
                idle.pop();
                ans[j] = i;
                busy.push({(long long) j + t, s, i});
            } else {
                auto [w, s, i] = busy.top();
                busy.pop();
                ans[j] = (int) i;
                busy.push({w + t, s, i});
            }
        }
        return ans;
    }
};
```

---

<a id="lc-2462"></a>
## 20. LC 2462 — Total Cost to Hire K Workers (Medium)

[Official problem](https://leetcode.com/problems/total-cost-to-hire-k-workers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2400-2499/2462.Total%20Cost%20to%20Hire%20K%20Workers/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `costs` where `costs[i]` is the cost of hiring the `i^th` worker.

You are also given two integers `k` and `candidates`. We want to hire exactly `k` workers according to the following rules:

- You will run `k` sessions and hire exactly one worker in each session.

- In each hiring session, choose the worker with the lowest cost from either the first `candidates` workers or the last `candidates` workers. Break the tie by the smallest index.

- For example, if `costs = [3,2,7,7,1,2]` and `candidates = 2`, then in the first hiring session, we will choose the `4^th` worker because they have the lowest cost `[3,2,7,7,**1**,2]`.

- In the second hiring session, we will choose `1^st` worker because they have the same lowest cost as `4^th` worker but they have the smallest index `[3,**2**,7,7,2]`. Please note that the indexing may be changed in the process.

- If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.

- A worker can only be chosen once.

Return the total cost to hire exactly `k` workers.

### Constraints

- `1 <= costs.length <= 10^5 `

- `1 <= costs[i] <= 10^5`

- `1 <= k, candidates <= costs.length`

### Approach and complexity

A min heap of (cost,index) pairs contains only the eligible windows. Replenish from the same side as the selected worker, stopping when the two windows meet. Pair ordering gives the required smallest-index tie break. Update pointers in separate statements to avoid unspecified argument evaluation order.

Time O((c+k) log(c+1)) and auxiliary space O(c) for candidate-window size c, unless the windows cover the whole array; that branch sorts in O(n log n) time and O(log n) auxiliary space.

### C++20 solution

```cpp
class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        int n = costs.size();
        if (candidates * 2 > n) {
            ranges::sort(costs);
            return accumulate(costs.begin(), costs.begin() + k, 0LL);
        }
        using pii = pair<int, int>;
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        for (int i = 0; i < candidates; ++i) {
            pq.emplace(costs[i], i);
            pq.emplace(costs[n - i - 1], n - i - 1);
        }
        long long ans = 0;
        int l = candidates, r = n - candidates - 1;
        while (k--) {
            auto [cost, i] = pq.top();
            pq.pop();
            ans += cost;
            if (l > r) {
                continue;
            }
            if (i < l) {
                pq.emplace(costs[l], l);
                ++l;
            } else {
                pq.emplace(costs[r], r);
                --r;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-2542"></a>
## 21. LC 2542 — Maximum Subsequence Score (Medium)

[Official problem](https://leetcode.com/problems/maximum-subsequence-score) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2500-2599/2542.Maximum%20Subsequence%20Score/README_EN.md)

### Problem description

You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length `n` and a positive integer `k`. You must choose a **subsequence** of indices from `nums1` of length `k`.

For chosen indices `i_0`, `i_1`, ..., `i_k - 1`, your **score** is defined as:

- The sum of the selected elements from `nums1` multiplied with the **minimum** of the selected elements from `nums2`.

- It can defined simply as: `(nums1[i_0] + nums1[i_1] +...+ nums1[i_k - 1]) * min(nums2[i_0] , nums2[i_1], ... ,nums2[i_k - 1])`.

Return the **maximum** possible score.

A **subsequence** of indices of an array is a set that can be derived from the set `{0, 1, ..., n-1}` by deleting some or no elements.

### Constraints

- `n == nums1.length == nums2.length`

- `1 <= n <= 10^5`

- `0 <= nums1[i], nums2[j] <= 10^5`

- `1 <= k <= n`

### Approach and complexity

Sort nums2 and nums1 in descending order according to nums2, then traverse from front to back, maintaining a min heap. The heap stores elements from nums1, and the number of elements in the heap does not exceed $k$. At the same time, maintain a variable $s$ representing the sum of the elements in the heap, and continuously update the answer during the traversal process.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array nums1.

### C++20 solution

```cpp
class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<pair<int, int>> nums(n);
        for (int i = 0; i < n; ++i) {
            nums[i] = {-nums2[i], nums1[i]};
        }
        ranges::sort(nums);
        priority_queue<int, vector<int>, greater<int>> q;
        long long ans = 0, s = 0;
        for (auto& [a, b] : nums) {
            s += b;
            q.push(b);
            if (q.size() == k) {
                ans = max(ans, s * -a);
                s -= q.top();
                q.pop();
            }
        }
        return ans;
    }
};
```

---

<a id="lc-857"></a>
## 22. LC 857 — Minimum Cost to Hire K Workers (Hard)

[Official problem](https://leetcode.com/problems/minimum-cost-to-hire-k-workers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0857.Minimum%20Cost%20to%20Hire%20K%20Workers/README_EN.md)

### Problem description

There are `n` workers. You are given two integer arrays `quality` and `wage` where `quality[i]` is the quality of the `i^th` worker and `wage[i]` is the minimum wage expectation for the `i^th` worker.

We want to hire exactly `k` workers to form a **paid group**. To hire a group of `k` workers, we must pay them according to the following rules:

- Every worker in the paid group must be paid at least their minimum wage expectation.

- In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.

Given the integer `k`, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within `10^-5` of the actual answer will be accepted.

### Constraints

- `n == quality.length == wage.length`

- `1 <= k <= n <= 10^4`

- `1 <= quality[i], wage[i] <= 10^4`

### Approach and complexity

Sort workers by required wage/quality ratio. Treat each ratio as the highest selected ratio, keep the k smallest qualities in a max heap, and minimize ratio times total selected quality.

Time O(n log n+n log k); auxiliary space O(n+k).

### C++20 solution

```cpp
class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        int n = quality.size();
        vector<pair<double, int>> t(n);
        for (int i = 0; i < n; ++i) {
            t[i] = {(double) wage[i] / quality[i], quality[i]};
        }
        ranges::sort(t);
        priority_queue<int> pq;
        double ans = 1e18;
        int tot = 0;
        for (auto& [x, q] : t) {
            tot += q;
            pq.push(q);
            if (pq.size() == k) {
                ans = min(ans, tot * x);
                tot -= pq.top();
                pq.pop();
            }
        }
        return ans;
    }
};
```

---

<a id="lc-871"></a>
## 23. LC 871 — Minimum Number of Refueling Stops (Hard)

[Official problem](https://leetcode.com/problems/minimum-number-of-refueling-stops) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0871.Minimum%20Number%20of%20Refueling%20Stops/README_EN.md)

### Problem description

A car travels from a starting position to a destination which is `target` miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array `stations` where `stations[i] = [position_i, fuel_i]` indicates that the `i^th` gas station is `position_i` miles east of the starting position and has `fuel_i` liters of gas.

The car starts with an infinite tank of gas, which initially has `startFuel` liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return `-1`.

Note that if the car reaches a gas station with `0` fuel left, the car can still refuel there. If the car reaches the destination with `0` fuel left, it is still considered to have arrived.

### Constraints

- `1 <= target, startFuel <= 10^9`

- `0 <= stations.length <= 500`

- `1 <= position_i < position_i+1 < target`

- `1 <= fuel_i < 10^9`

### Approach and complexity

We can use a priority queue (max-heap) $pq$ to record the fuel amounts of all the gas stations we have passed. Each time the fuel is insufficient, we greedily take out the maximum fuel amount, which is the top element of $pq$, and accumulate the number of refuels $\textit{ans}$. If $pq$ is empty and the current fuel is still insufficient, it means we cannot reach the destination, and we return $-1$.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ represents the number of gas stations.

### C++20 solution

```cpp
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        priority_queue<int> pq;
        stations.push_back({target, 0});
        int ans = 0, pre = 0;
        for (const auto& station : stations) {
            int pos = station[0], fuel = station[1];
            int dist = pos - pre;
            startFuel -= dist;
            while (startFuel < 0 && !pq.empty()) {
                startFuel += pq.top();
                pq.pop();
                ++ans;
            }
            if (startFuel < 0) {
                return -1;
            }
            pq.push(fuel);
            pre = pos;
        }
        return ans;
    }
};
```

---

<a id="lc-1353"></a>
## 24. LC 1353 — Maximum Number of Events That Can Be Attended (Medium)

[Official problem](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1353.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended/README_EN.md)

### Problem description

You are given an array of `events` where `events[i] = [startDay_i, endDay_i]`. Every event `i` starts at `startDay_i`_ and ends at `endDay_i`.

You can attend an event `i` at any day `d` where `startDay_i <= d <= endDay_i`. You can only attend one event at any time `d`.

Return the maximum number of events you can attend.

### Constraints

- `1 <= events.length <= 10^5`

- `events[i].length == 2`

- `1 <= startDay_i <= endDay_i <= 10^5`

### Approach and complexity

We use a hash table $g$ to record the start and end times of each event. The key is the start time of the event, and the value is a list containing the end times of all events that start at that time. Two variables, $l$ and $r$, are used to record the minimum start time and the maximum end time among all events.

For each time point $s$ from $l$ to $r$ in increasing order, we perform the following steps:

1. Remove from the priority queue all events whose end time is less than the current time $s$.
2. Add the end times of all events that start at the current time $s$ to the priority queue.
3. If the priority queue is not empty, take out the event with the earliest end time, increment the answer count, and remove this event from the priority queue.

In this way, we ensure that at each time point $s$, we always attend the event that ends the earliest, thus maximizing the number of events attended.

The time complexity is $O(M \log n)$, and the space complexity is $O(n)$, where $M$ is the maximum end time and $n$ is the number of events.

### C++20 solution

```cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        unordered_map<int, vector<int>> g;
        int l = INT_MAX, r = 0;
        for (auto& event : events) {
            int s = event[0], e = event[1];
            g[s].push_back(e);
            l = min(l, s);
            r = max(r, e);
        }
        priority_queue<int, vector<int>, greater<int>> pq;
        int ans = 0;
        for (int s = l; s <= r; ++s) {
            while (!pq.empty() && pq.top() < s) {
                pq.pop();
            }
            for (int e : g[s]) {
                pq.push(e);
            }
            if (!pq.empty()) {
                pq.pop();
                ++ans;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1851"></a>
## 25. LC 1851 — Minimum Interval to Include Each Query (Hard)

[Official problem](https://leetcode.com/problems/minimum-interval-to-include-each-query) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1851.Minimum%20Interval%20to%20Include%20Each%20Query/README_EN.md)

### Problem description

You are given a 2D integer array `intervals`, where `intervals[i] = [left_i, right_i]` describes the `i^th` interval starting at `left_i` and ending at `right_i` **(inclusive)**. The **size** of an interval is defined as the number of integers it contains, or more formally `right_i - left_i + 1`.

You are also given an integer array `queries`. The answer to the `j^th` query is the **size of the smallest interval** `i` such that `left_i <= queries[j] <= right_i`. If no such interval exists, the answer is `-1`.

Return an array containing the answers to the queries.

### Constraints

- `1 <= intervals.length <= 10^5`

- `1 <= queries.length <= 10^5`

- `intervals[i].length == 2`

- `1 <= left_i <= right_i <= 10^7`

- `1 <= queries[j] <= 10^7`

### Approach and complexity

We notice that the order of queries does not affect the answer, and the intervals involved do not change. Therefore, we consider sorting all queries in ascending order, and sorting all intervals in ascending order of the left endpoint.

We use a priority queue (min heap) $pq$ to maintain all current intervals. Each element in the queue is a pair $(v, r)$, representing an interval with length $v$ and right endpoint $r$. Initially, the priority queue is empty. In addition, we define a pointer $i$ that points to the current interval being traversed, and initially $i=0$.

We traverse each query $(x, j)$ in ascending order and perform the following operations:

- If the pointer $i$ has not traversed all intervals, and the left endpoint of the current interval $[a, b]$ is less than or equal to $x$, then we add this interval to the priority queue and move the pointer $i$ one step forward. Repeat this process.
- If the priority queue is not empty, and the right endpoint of the heap top element is less than $x$, then we pop the heap top element. Repeat this process.
- At this point, if the priority queue is not empty, then the heap top element is the smallest interval containing $x$. We add its length $v$ to the answer array $\textit{ans}$.

After the above process is over, we return the answer array $\textit{ans}$.

The time complexity is $O(n \log n + m \log m)$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the lengths of the arrays $\textit{intervals}$ and $\textit{queries}$ respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size(), m = queries.size();
        ranges::sort(intervals);
        using pii = pair<int, int>;
        vector<pii> qs;
        for (int i = 0; i < m; ++i) {
            qs.emplace_back(queries[i], i);
        }
        ranges::sort(qs);
        vector<int> ans(m, -1);
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        int i = 0;
        for (auto& [x, j] : qs) {
            while (i < n && intervals[i][0] <= x) {
                int a = intervals[i][0], b = intervals[i][1];
                pq.emplace(b - a + 1, b);
                ++i;
            }
            while (!pq.empty() && pq.top().second < x) {
                pq.pop();
            }
            if (!pq.empty()) {
                ans[j] = pq.top().first;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1942"></a>
## 26. LC 1942 — The Number of the Smallest Unoccupied Chair (Medium)

[Official problem](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1900-1999/1942.The%20Number%20of%20the%20Smallest%20Unoccupied%20Chair/README_EN.md)

### Problem description

There is a party where `n` friends numbered from `0` to `n - 1` are attending. There is an **infinite** number of chairs in this party that are numbered from `0` to `infinity`. When a friend arrives at the party, they sit on the unoccupied chair with the **smallest number**.

- For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they will sit on chair number `2`.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a **0-indexed** 2D integer array `times` where `times[i] = [arrival_i, leaving_i]`, indicating the arrival and leaving times of the `i^th` friend respectively, and an integer `targetFriend`. All arrival times are **distinct**.

Return the **chair number** that the friend numbered `targetFriend` will sit on.

### Constraints

- `n == times.length`

- `2 <= n <= 10^4`

- `times[i].length == 2`

- `1 <= arrival_i < leaving_i <= 10^5`

- `0 <= targetFriend <= n - 1`

- Each `arrival_i` time is **distinct**.

### Approach and complexity

First, we create a tuple for each friend consisting of their arrival time, leaving time, and index, then sort these tuples by arrival time.

We use a min-heap $\textit{idle}$ to store the currently available chair numbers. Initially, we add $0, 1, \ldots, n-1$ to $\textit{idle}$. We also use a min-heap $\textit{busy}$ to store tuples $(\textit{leaving}, \textit{chair})$, where $\textit{leaving}$ represents the leaving time and $\textit{chair}$ represents the chair number.

We iterate through each friend's arrival time, leaving time, and index. For each friend, we first remove all friends from $\textit{busy}$ whose leaving time is less than or equal to the current friend's arrival time, and add their chair numbers back to $\textit{idle}$. Then we pop a chair number from $\textit{idle}$, assign it to the current friend, and add $(\textit{leaving}, \textit{chair})$ to $\textit{busy}$. If the current friend's index is equal to $\textit{targetFriend}$, we return the assigned chair number.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of friends.

### C++20 solution

```cpp
class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        using pii = pair<int, int>;
        priority_queue<pii, vector<pii>, greater<pii>> busy;
        priority_queue<int, vector<int>, greater<int>> idle;
        int n = times.size();
        for (int i = 0; i < n; ++i) {
            times[i].push_back(i);
            idle.push(i);
        }
        ranges::sort(times);
        for (const auto& e : times) {
            int arrival = e[0], leaving = e[1], i = e[2];
            while (!busy.empty() && busy.top().first <= arrival) {
                idle.push(busy.top().second);
                busy.pop();
            }
            int j = idle.top();
            if (i == targetFriend) {
                return j;
            }
            idle.pop();
            busy.emplace(leaving, j);
        }
        return -1;
    }
};
```

---

<a id="lc-1962"></a>
## 27. LC 1962 — Remove Stones to Minimize the Total (Medium)

[Official problem](https://leetcode.com/problems/remove-stones-to-minimize-the-total) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1900-1999/1962.Remove%20Stones%20to%20Minimize%20the%20Total/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `piles`, where `piles[i]` represents the number of stones in the `i^th` pile, and an integer `k`. You should apply the following operation **exactly** `k` times:

- Choose any `piles[i]` and **remove** `floor(piles[i] / 2)` stones from it.

**Notice** that you can apply the operation on the **same** pile more than once.

Return the **minimum** possible total number of stones remaining after applying the `k` operations.

`floor(x)` is the **largest** integer that is **smaller** than or **equal** to `x` (i.e., rounds `x` down).

### Constraints

- `1 <= piles.length <= 10^5`

- `1 <= piles[i] <= 10^4`

- `1 <= k <= 10^5`

### Approach and complexity

According to the problem description, in order to minimize the total number of remaining stones, we need to remove as many stones as possible from the stone piles. Therefore, we should always choose the pile with the most stones for removal.

We create a priority queue (max heap) $pq$ to store the number of stones in each pile. Initially, we add the number of stones in all piles to the priority queue.

Next, we perform $k$ operations. In each operation, we take out the top element $x$ of the priority queue, halve $x$, and then add it back to the priority queue.

After performing $k$ operations, the sum of all elements in the priority queue is the answer.

The time complexity is $O(n + k \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{piles}$.

### C++20 solution

```cpp
class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> pq;
        for (int x : piles) {
            pq.push(x);
        }
        while (k--) {
            int x = pq.top();
            pq.pop();
            pq.push(x - x / 2);
        }
        int ans = 0;
        while (!pq.empty()) {
            ans += pq.top();
            pq.pop();
        }
        return ans;
    }
};
```

---

<a id="lc-2208"></a>
## 28. LC 2208 — Minimum Operations to Halve Array Sum (Medium)

[Official problem](https://leetcode.com/problems/minimum-operations-to-halve-array-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2200-2299/2208.Minimum%20Operations%20to%20Halve%20Array%20Sum/README_EN.md)

### Problem description

You are given an array `nums` of positive integers. In one operation, you can choose **any** number from `nums` and reduce it to **exactly** half the number. (Note that you may choose this reduced number in future operations.)

Return the **minimum** number of operations to reduce the sum of `nums` by **at least** half.

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^7`

### Approach and complexity

According to the problem description, each operation will halve a number in the array. To minimize the number of operations that reduce the array sum by at least half, each operation should halve the current maximum value in the array.

Therefore, we first calculate the total sum $s$ that the array needs to reduce, and then use a priority queue (max heap) to maintain all the numbers in the array. Each time we take the maximum value $t$ from the priority queue, halve it, and then put the halved number back into the priority queue, while updating $s$, until $s \le 0$. The number of operations at this time is the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int halveArray(vector<int>& nums) {
        priority_queue<double> pq;
        double s = 0;
        for (int x : nums) {
            s += x;
            pq.push((double) x);
        }
        s /= 2.0;
        int ans = 0;
        while (s > 0) {
            double t = pq.top() / 2.0;
            pq.pop();
            s -= t;
            pq.push(t);
            ++ans;
        }
        return ans;
    }
};
```

---

<a id="lc-2336"></a>
## 29. LC 2336 — Smallest Number in Infinite Set (Medium)

[Official problem](https://leetcode.com/problems/smallest-number-in-infinite-set) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2336.Smallest%20Number%20in%20Infinite%20Set/README_EN.md)

### Problem description

You have a set which contains all positive integers `[1, 2, 3, 4, 5, ...]`.

Implement the `SmallestInfiniteSet` class:

- `SmallestInfiniteSet()` Initializes the **SmallestInfiniteSet** object to contain **all** positive integers.

- `int popSmallest()` **Removes** and returns the smallest integer contained in the infinite set.

- `void addBack(int num)` **Adds** a positive integer `num` back into the infinite set, if it is **not** already in the infinite set.

### Constraints

- `1 <= num <= 1000`

- At most `1000` calls will be made **in total** to `popSmallest` and `addBack`.

### Approach and complexity

We note that the range of elements in the set given by the problem is $[1, 1000]$, and the operations we need to support are:

- `popSmallest`: Pop the smallest element from the set
- `addBack`: Add an element back to the set

Therefore, we can use an ordered set to simulate this. Let's denote the ordered set as $s$, and the elements in the set as $s_1, s_2, \cdots, s_n$, where $n$ is the number of elements in the ordered set. In this problem, $n \le 1000$.

During initialization, we add all elements in $[1, 1000]$ to the ordered set. The time complexity is $O(n \log n)$.

In the $\textit{popSmallest}$ operation, we just need to pop the first element from the ordered set. The time complexity for a single operation is $O(\log n)$.

In the $\textit{addBack}$ operation, we just need to add the element back to the ordered set. The time complexity for a single operation is $O(\log n)$.

The space complexity is $O(n)$.

### C++20 solution

```cpp
class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() {
        for (int i = 1; i <= 1000; ++i) {
            s.insert(i);
        }
    }

    int popSmallest() {
        int x = *s.begin();
        s.erase(s.begin());
        return x;
    }

    void addBack(int num) {
        s.insert(num);
    }

private:
    set<int> s;
};
```

---

<a id="lc-2353"></a>
## 30. LC 2353 — Design a Food Rating System (Medium)

[Official problem](https://leetcode.com/problems/design-a-food-rating-system) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2353.Design%20a%20Food%20Rating%20System/README_EN.md)

### Problem description

Design a food rating system that can do the following:

- **Modify** the rating of a food item listed in the system.

- Return the highest-rated food item for a type of cuisine in the system.

Implement the `FoodRatings` class:

- `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines` and `ratings`, all of which have a length of `n`.

- `foods[i]` is the name of the `i^th` food,

- `cuisines[i]` is the type of cuisine of the `i^th` food, and

- `ratings[i]` is the initial rating of the `i^th` food.

- `void changeRating(String food, int newRating)` Changes the rating of the food item with the name `food`.

- `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of `cuisine`. If there is a tie, return the item with the **lexicographically smaller** name.

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

### Constraints

- `1 <= n <= 2 * 10^4`

- `n == foods.length == cuisines.length == ratings.length`

- `1 <= foods[i].length, cuisines[i].length <= 10`

- `foods[i]`, `cuisines[i]` consist of lowercase English letters.

- `1 <= ratings[i] <= 10^8`

- All the strings in `foods` are **distinct**.

- `food` will be the name of a food item in the system across all calls to `changeRating`.

- `cuisine` will be a type of cuisine of **at least one** food item in the system across all calls to `highestRated`.

- At most `2 * 10^4` calls **in total** will be made to `changeRating` and `highestRated`.

### Approach and complexity

We can use a hash table $d$ to store the foods for each cuisine, where the key is the cuisine and the value is an ordered set. Each element in the ordered set is a tuple $(\textit{rating}, \textit{food})$, sorted by rating in descending order, and if the ratings are the same, sorted by food name in lexicographical order.

We can also use a hash table $g$ to store the rating and cuisine for each food. That is, $g[\textit{food}] = (\textit{rating}, \textit{cuisine})$.

In the constructor, we iterate through $\textit{foods}$, $\textit{cuisines}$, and $\textit{ratings}$, storing the rating and cuisine for each food in $d$ and $g$.

In the $\textit{changeRating}$ function, we first get the original rating $\textit{oldRating}$ and cuisine $\textit{cuisine}$ of the food $\textit{food}$, then update the rating of $g[\textit{food}]$ to $\textit{newRating}$, remove $(\textit{oldRating}, \textit{food})$ from $d[\textit{cuisine}]$, and add $(\textit{newRating}, \textit{food})$ to $d[\textit{cuisine}]$.

In the $\textit{highestRated}$ function, we directly return the food name of the first element in $d[\textit{cuisine}]$.

In terms of time complexity, the constructor has a time complexity of $O(n \log n)$, where $n$ is the number of foods. The other operations have a time complexity of $O(\log n)$. The space complexity is $O(n)$.

### C++20 solution

```cpp
class FoodRatings {
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i = 0; i < foods.size(); ++i) {
            string food = foods[i], cuisine = cuisines[i];
            int rating = ratings[i];
            d[cuisine].insert({-rating, food});
            g[food] = {rating, cuisine};
        }
    }

    void changeRating(string food, int newRating) {
        auto [oldRating, cuisine] = g[food];
        g[food] = {newRating, cuisine};
        d[cuisine].erase({-oldRating, food});
        d[cuisine].insert({-newRating, food});
    }

    string highestRated(string cuisine) {
        return d[cuisine].begin()->second;
    }

private:
    unordered_map<string, set<pair<int, string>>> d;
    unordered_map<string, pair<int, string>> g;
};
```

---

<a id="lc-264"></a>
## 31. LC 264 — Ugly Number II (Medium)

[Official problem](https://leetcode.com/problems/ugly-number-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0264.Ugly%20Number%20II/README_EN.md)

### Problem description

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

Given an integer `n`, return the `n^th` **ugly number**.

### Constraints

- `1 <= n <= 1690`

### Approach and complexity

Three advancing indices merge multiples of 2, 3, and 5; advance all tied candidates to avoid duplicates. Use 64-bit candidate products even though the selected answer fits int.

Time O(n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n);
        dp[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0;
        for (int i = 1; i < n; ++i) {
            long long next2 = 2LL * dp[p2], next3 = 3LL * dp[p3], next5 = 5LL * dp[p5];
            dp[i] = min(next2, min(next3, next5));
            if (dp[i] == next2) ++p2;
            if (dp[i] == next3) ++p3;
            if (dp[i] == next5) ++p5;
        }
        return dp[n - 1];
    }
};
```

---

<a id="lc-313"></a>
## 32. LC 313 — Super Ugly Number (Medium)

[Official problem](https://leetcode.com/problems/super-ugly-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0313.Super%20Ugly%20Number/README_EN.md)

### Problem description

A **super ugly number** is a positive integer whose prime factors are in the array `primes`.

Given an integer `n` and an array of integers `primes`, return the `n^th` **super ugly number**.

The `n^th` **super ugly number** is **guaranteed** to fit in a **32-bit** signed integer.

### Constraints

- `1 <= n <= 10^5`

- `1 <= primes.length <= 100`

- `2 <= primes[i] <= 1000`

- `primes[i]` is **guaranteed** to be a prime number.

- All the values of `primes` are **unique** and sorted in **ascending order**.

### Approach and complexity

We use a priority queue (min heap) to maintain all possible super ugly numbers, initially putting $1$ into the queue.

Each time we take the smallest super ugly number $x$ from the queue, multiply $x$ by each number in the array `primes`, and put the product into the queue. Repeat the above operation $n$ times to get the $n$th super ugly number.

Since the problem guarantees that the $n$th super ugly number is within the range of a 32-bit signed integer, before we put the product into the queue, we can first check whether the product exceeds $2^{31} - 1$. If it does, there is no need to put the product into the queue. In addition, the Euler sieve can be used for optimization.

The time complexity is $O(nm \log (nm))$, and the space complexity is $O(nm)$, where $m$ and $n$ are the length of the array $\textit{primes}$ and the given integer $n$ respectively.

### C++20 solution

```cpp
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        priority_queue<int, vector<int>, greater<int>> q;
        q.push(1);
        int x = 0;
        while (n--) {
            x = q.top();
            q.pop();
            for (int& k : primes) {
                if (x <= INT_MAX / k) {
                    q.push(k * x);
                }
                if (x % k == 0) {
                    break;
                }
            }
        }
        return x;
    }
};
```

---

<a id="lc-2642"></a>
## 33. LC 2642 — Design Graph With Shortest Path Calculator (Medium)

[Official problem](https://leetcode.com/problems/design-graph-with-shortest-path-calculator) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2600-2699/2642.Design%20Graph%20With%20Shortest%20Path%20Calculator/README_EN.md)

### Problem description

There is a **directed weighted** graph that consists of `n` nodes numbered from `0` to `n - 1`. The edges of the graph are initially represented by the given array `edges` where `edges[i] = [from_i, to_i, edgeCost_i]` meaning that there is an edge from `from_i` to `to_i` with the cost `edgeCost_i`.

Implement the `Graph` class:

- `Graph(int n, int[][] edges)` initializes the object with `n` nodes and the given edges.

- `addEdge(int[] edge)` adds an edge to the list of edges where `edge = [from, to, edgeCost]`. It is guaranteed that there is no edge between the two nodes before adding this one.

- `int shortestPath(int node1, int node2)` returns the **minimum** cost of a path from `node1` to `node2`. If no path exists, return `-1`. The cost of a path is the sum of the costs of the edges in the path.

### Constraints

- `1 <= n <= 100`

- `0 <= edges.length <= n * (n - 1)`

- `edges[i].length == edge.length == 3`

- `0 <= from_i, to_i, from, to, node1, node2 <= n - 1`

- `1 <= edgeCost_i, edgeCost <= 10^6`

- There are no repeated edges and no self-loops in the graph at any point.

- At most `100` calls will be made for `addEdge`.

- At most `100` calls will be made for `shortestPath`.

### Approach and complexity

In the initialization function, we first use the adjacency matrix $g$ to store the edge weights of the graph, where $g_{ij}$ represents the edge weight from node $i$ to node $j$. If there is no edge between $i$ and $j$, the value of $g_{ij}$ is $\infty$.

In the `addEdge` function, we update the value of $g_{ij}$ to $\textit{edge}[2]$.

In the `shortestPath` function, we use Dijkstra's algorithm to find the shortest path from node $\textit{node1}$ to node $\textit{node2}$. Here, $\textit{dist}[i]$ represents the shortest path from node $\textit{node1}$ to node $i$, and $\textit{vis}[i]$ indicates whether node $i$ has been visited. We initialize $\textit{dist}[\textit{node1}]$ to $0$, and the rest of $\textit{dist}[i]$ are all $\infty$. Then we iterate $n$ times, each time finding the current unvisited node $t$ such that $\textit{dist}[t]$ is the smallest. Then we mark node $t$ as visited, and then update the value of $\textit{dist}[i]$ to $\min(\textit{dist}[i], \textit{dist}[t] + g_{ti})$. Finally, we return $\textit{dist}[\textit{node2}]$. If $\textit{dist}[\textit{node2}]$ is $\infty$, it means that there is no path from node $\textit{node1}$ to node $\textit{node2}$, so we return $-1$.

The time complexity is $O(n^2q)$, and the space complexity is $O(n^2)$, where $n$ is the number of nodes, and $q$ is the number of calls to the $\textit{shortestPath}$ function.

### C++20 solution

```cpp
class Graph {
public:
    Graph(int n, vector<vector<int>>& edges) {
        this->n = n;
        g = vector<vector<int>>(n, vector<int>(n, inf));
        for (auto& e : edges) {
            int f = e[0], t = e[1], c = e[2];
            g[f][t] = c;
        }
    }

    void addEdge(vector<int> edge) {
        int f = edge[0], t = edge[1], c = edge[2];
        g[f][t] = c;
    }

    int shortestPath(int node1, int node2) {
        vector<bool> vis(n);
        vector<int> dist(n, inf);
        dist[node1] = 0;
        for (int i = 0; i < n; ++i) {
            int t = -1;
            for (int j = 0; j < n; ++j) {
                if (!vis[j] && (t == -1 || dist[t] > dist[j])) {
                    t = j;
                }
            }
            vis[t] = true;
            for (int j = 0; j < n; ++j) {
                dist[j] = min(dist[j], dist[t] + g[t][j]);
            }
        }
        return dist[node2] >= inf ? -1 : dist[node2];
    }

private:
    vector<vector<int>> g;
    int n;
    const int inf = 1 << 29;
};
```

---

<a id="lc-743"></a>
## 34. LC 743 — Network Delay Time (Medium)

[Official problem](https://leetcode.com/problems/network-delay-time) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0743.Network%20Delay%20Time/README_EN.md)

### Problem description

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`, where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the **minimum** time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

### Constraints

- `1 <= k <= n <= 100`

- `1 <= times.length <= 6000`

- `times[i].length == 3`

- `1 <= u_i, v_i <= n`

- `u_i != v_i`

- `0 <= w_i <= 100`

- All the pairs `(u_i, v_i)` are **unique**. (i.e., no multiple edges.)

### Approach and complexity

We can use a priority queue (heap) to optimize the naive Dijkstra algorithm.

We define $g[u]$ to represent all adjacent edges of node $u$, and $\textit{dist}[u]$ to represent the shortest path length from node $k$ to node $u$. Initially, we set all $\textit{dist}[u]$ to $+\infty$, except for $\textit{dist}[k - 1] = 0$.

We define a priority queue $pq$, where each element is $(d, u)$, representing the distance $d$ from node $u$ to node $k$. Each time, we take out the node $(d, u)$ with the smallest distance from $pq$. If $d > \textit{dist}[u]$, we skip this node. Otherwise, we traverse all adjacent edges of node $u$. For each adjacent edge $(v, w)$, if $\textit{dist}[v] > \textit{dist}[u] + w$, we update $\textit{dist}[v] = \textit{dist}[u] + w$, and add $(\textit{dist}[v], v)$ to $\textit{pq}$.

Finally, we return the maximum value in $\textit{dist}$ as the answer. If the answer is $+\infty$, it means there are unreachable nodes, and we return $-1$.

The time complexity is $O(m \log m + n)$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the number of nodes and edges, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        const int inf = 1 << 29;
        using pii = pair<int, int>;
        vector<vector<pii>> g(n);
        for (auto& edge : times) {
            g[edge[0] - 1].emplace_back(edge[1] - 1, edge[2]);
        }

        vector<int> dist(n, inf);
        dist[k - 1] = 0;
        priority_queue<pii, vector<pii>, greater<>> pq;
        pq.emplace(0, k - 1);

        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) {
                continue;
            }
            for (auto& [v, w] : g[u]) {
                if (dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                    pq.emplace(dist[v], v);
                }
            }
        }

        int ans = ranges::max(dist);
        return ans == inf ? -1 : ans;
    }
};
```

---

<a id="lc-1514"></a>
## 35. LC 1514 — Path with Maximum Probability (Medium)

[Official problem](https://leetcode.com/problems/path-with-maximum-probability) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1500-1599/1514.Path%20with%20Maximum%20Probability/README_EN.md)

### Problem description

You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability.

If there is no path from `start` to `end`, **return 0**. Your answer will be accepted if it differs from the correct answer by at most **1e-5**.

### Constraints

- `2 <= n <= 10^4`

- `0 <= start, end < n`

- `start != end`

- `0 <= a, b < n`

- `a != b`

- `0 <= succProb.length == edges.length <= 2*10^4`

- `0 <= succProb[i] <= 1`

- There is at most one edge between every two nodes.

### Approach and complexity

We can use Dijkstra's algorithm to find the shortest path, but here we modify it slightly to find the path with the maximum probability.

We use a priority queue (max-heap) $pq$ to store the probability from the starting point to each node and the node's identifier. Initially, we set the probability of the starting point to $1$ and the probabilities of the other nodes to $0$, then add the starting point to $pq$.

In each iteration, we take out the node $a$ with the highest probability from $pq$ and its probability $w$. If the probability of node $a$ is already greater than $w$, we can skip this node. Otherwise, we traverse all adjacent edges $(a, b)$ of $a$. If the probability of $b$ is less than the probability of $a$ multiplied by the probability of $(a, b)$, we update the probability of $b$ and add $b$ to $pq$.

Finally, we obtain the maximum probability from the starting point to the endpoint.

The time complexity is $O(m \log m)$, and the space complexity is $O(m)$, where $m$ is the number of edges.

### C++20 solution

```cpp
class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        using pdi = pair<double, int>;
        vector<vector<pdi>> g = vector<vector<pdi>>(n, vector<pdi>{});
        for (int i = 0; i < edges.size(); ++i) {
            int a = edges[i][0], b = edges[i][1];
            double p = succProb[i];
            g[a].emplace_back(p, b);
            g[b].emplace_back(p, a);
        }
        vector<double> dist(n);
        dist[start_node] = 1;
        priority_queue<pdi> pq;
        pq.emplace(1, start_node);
        while (!pq.empty()) {
            auto [w, a] = pq.top();
            pq.pop();
            if (dist[a] > w) {
                continue;
            }
            for (auto [p, b] : g[a]) {
                auto nw = w * p;
                if (nw > dist[b]) {
                    dist[b] = nw;
                    pq.emplace(nw, b);
                }
            }
        }
        return dist[end_node];
    }
};
```

---

<a id="lc-1631"></a>
## 36. LC 1631 — Path With Minimum Effort (Medium)

[Official problem](https://leetcode.com/problems/path-with-minimum-effort) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1631.Path%20With%20Minimum%20Effort/README_EN.md)

### Problem description

You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)` (i.e., **0-indexed**). You can move **up**, **down**, **left**, or **right**, and you wish to find a route that requires the minimum **effort**.

A route's **effort** is the **maximum absolute difference**** **in heights between two consecutive cells of the route.

Return the minimum **effort** required to travel from the top-left cell to the bottom-right cell.

### Constraints

- `rows == heights.length`

- `columns == heights[i].length`

- `1 <= rows, columns <= 100`

- `1 <= heights[i][j] <= 10^6`

### Approach and complexity

We can treat each cell as a node in a graph, and the absolute difference in height between two adjacent cells as the weight of the edge. Therefore, this problem is to solve the shortest path problem from the top-left node to the bottom-right node.

We can use the Dijkstra algorithm to solve the shortest path problem, and use a priority queue (heap) to optimize the time complexity. Specifically, we maintain a two-dimensional array $\textit{dist}$ of size $m \times n$, where $\textit{dist}[i][j]$ represents the maximum weight of the shortest path from the top-left corner to the node $(i,j)$. Initially, $\textit{dist}[0][0]=0$, and all other elements are positive infinity.

We use a priority queue (heap) to store nodes, and each time we take out the node with the smallest weight from the priority queue (heap), then update the weights of its adjacent nodes. If the weight of an adjacent node changes, then we add this node to the priority queue (heap). When the priority queue (heap) is empty, it means that we have found the shortest path.

The time complexity is $O(mn \log(mn))$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns in the two-dimensional array, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<int>> dist = vector<vector<int>>(m, vector<int>(n, 0x3f3f3f3f));
        dist[0][0] = 0;
        int dirs[5] = {0, 1, 0, -1, 0};
        using T = tuple<int, int, int>;
        priority_queue<T, vector<T>, greater<T>> pq;
        pq.emplace(0, 0, 0);
        while (!pq.empty()) {
            auto [t, i, j] = pq.top();
            pq.pop();
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x < 0 || x >= m || y < 0 || y >= n) {
                    continue;
                }
                int d = max(t, abs(heights[x][y] - heights[i][j]));
                if (d < dist[x][y]) {
                    dist[x][y] = d;
                    pq.emplace(d, x, y);
                }
            }
        }
        return dist[m - 1][n - 1];
    }
};
```

---

<a id="lc-778"></a>
## 37. LC 778 — Swim in Rising Water (Hard)

[Official problem](https://leetcode.com/problems/swim-in-rising-water) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0778.Swim%20in%20Rising%20Water/README_EN.md)

### Problem description

You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

It starts raining, and water gradually rises over time. At time `t`, the water level is `t`, meaning **any** cell with elevation less than equal to `t` is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square `(n - 1, n - 1)` if you start at the top left square `(0, 0)`.

### Constraints

- `n == grid.length`

- `n == grid[i].length`

- `1 <= n <= 50`

- `0 <= grid[i][j] < n^2`

- Each value `grid[i][j]` is **unique**.

### Approach and complexity

We can map each position $(i, j)$ to an ID $id = i \times n + j$, and use a union-find data structure to maintain connected components.

First, we use a one-dimensional array $hi$ to record the position ID corresponding to each height, i.e., $hi[h]$ represents the position ID with height $h$.

Then we traverse from height $0$ to height $n^2 - 1$. For each height $t$, we merge position $hi[t]$ with its four adjacent positions that have heights not exceeding $t$. If after merging, position $0$ and position $n^2 - 1$ are connected, then we have found the minimum time $t$, and we return $t$.

The time complexity is $O(n^2 \log n)$, and the space complexity is $O(n^2)$, where $n$ is the side length of the matrix.

### C++20 solution

```cpp
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = n * n;
        vector<int> p(m);
        iota(p.begin(), p.end(), 0);

        auto find = [&](auto&& find, int x) -> int {
            if (p[x] != x) {
                p[x] = find(find, p[x]);
            }
            return p[x];
        };

        vector<int> hi(m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                hi[grid[i][j]] = i * n + j;
            }
        }

        array<int, 5> dirs{-1, 0, 1, 0, -1};

        for (int t = 0; t < m; ++t) {
            int id = hi[t];
            int x = id / n, y = id % n;
            for (int k = 0; k < 4; ++k) {
                int nx = x + dirs[k], ny = y + dirs[k + 1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] <= t) {
                    int a = find(find, x * n + y);
                    int b = find(find, nx * n + ny);
                    p[a] = b;
                }
            }
            if (find(find, 0) == find(find, m - 1)) {
                return t;
            }
        }
        return 0;
    }
};
```

---

<a id="lc-407"></a>
## 38. LC 407 — Trapping Rain Water II (Hard)

[Official problem](https://leetcode.com/problems/trapping-rain-water-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0407.Trapping%20Rain%20Water%20II/README_EN.md)

### Problem description

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

### Constraints

- `m == heightMap.length`

- `n == heightMap[i].length`

- `1 <= m, n <= 200`

- `0 <= heightMap[i][j] <= 2 * 10^4`

### Approach and complexity

This is a variant of the trapping rain water problem. Since the heights on the matrix boundaries are fixed, we can add these boundary heights to a priority queue. Then, we repeatedly take out the minimum height from the priority queue and compare it with the heights of its four adjacent cells. If an adjacent cell's height is less than the current height, we can trap water there. The volume of trapped water is the difference between the current height and the adjacent height. We then add the larger height back to the priority queue and repeat this process until the priority queue is empty.

The time complexity is $O(mn \log (mn))$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns in the matrix, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        using tii = tuple<int, int, int>;
        priority_queue<tii, vector<tii>, greater<tii>> pq;
        int m = heightMap.size(), n = heightMap[0].size();
        vector<vector<char>> vis = vector<vector<char>>(m, vector<char>(n, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                    pq.emplace(heightMap[i][j], i, j);
                    vis[i][j] = true;
                }
            }
        }
        int ans = 0;
        int dirs[5] = {-1, 0, 1, 0, -1};
        while (!pq.empty()) {
            auto [h, i, j] = pq.top();
            pq.pop();
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && !vis[x][y]) {
                    ans += max(0, h - heightMap[x][y]);
                    vis[x][y] = true;
                    pq.emplace(max(heightMap[x][y], h), x, y);
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-632"></a>
## 39. LC 632 — Smallest Range Covering Elements from K Lists (Hard)

[Official problem](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0632.Smallest%20Range%20Covering%20Elements%20from%20K%20Lists/README_EN.md)

### Problem description

You have `k` lists of sorted integers in **non-decreasing order**. Find the smallest range that includes at least one number from each of the `k` lists.

We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c` **or** `a < c` if `b - a == d - c`.

### Constraints

- `nums.length == k`

- `1 <= k <= 3500`

- `1 <= nums[i].length <= 50`

- `-10^5 <= nums[i][j] <= 10^5`

- `nums[i]` is sorted in **non-decreasing** order.

### Approach and complexity

We construct a data item $(x, i)$ for each number $x$ and its group $i$, and store these items in a new array $t$. Then, we sort $t$ by the value of the numbers (similar to merging multiple sorted arrays into a new sorted array).

Next, we traverse each data item in $t$, focusing on the group to which each number belongs. We use a hash table to record the groups of numbers within the sliding window. If the number of groups is $k$, it means the current window meets the problem's requirements. At this point, we calculate the start and end positions of the window and update the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the total number of numbers in all arrays.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        int n = 0;
        for (auto& v : nums) n += v.size();
        vector<pair<int, int>> t(n);
        int k = nums.size();
        for (int i = 0, j = 0; i < k; ++i) {
            for (int v : nums[i]) {
                t[j++] = {v, i};
            }
        }
        ranges::sort(t);
        int j = 0;
        unordered_map<int, int> cnt;
        vector<int> ans = {-1000000, 1000000};
        for (int i = 0; i < n; ++i) {
            int b = t[i].first;
            int v = t[i].second;
            ++cnt[v];
            while (cnt.size() == k) {
                int a = t[j].first;
                int w = t[j].second;
                int x = b - a - (ans[1] - ans[0]);
                if (x < 0 || (x == 0 && a < ans[0])) {
                    ans[0] = a;
                    ans[1] = b;
                }
                if (--cnt[w] == 0) {
                    cnt.erase(w);
                }
                ++j;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-480"></a>
## 40. LC 480 — Sliding Window Median (Hard)

[Official problem](https://leetcode.com/problems/sliding-window-median) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0480.Sliding%20Window%20Median/README_EN.md)

### Problem description

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

- For examples, if `arr = [2,3,4]`, the median is `3`.

- For examples, if `arr = [1,2,3,4]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within `10^-5` of the actual value will be accepted.

### Constraints

- `1 <= k <= nums.length <= 10^5`

- `-2^31 <= nums[i] <= 2^31 - 1`

### Approach and complexity

We can use two ordered sets to maintain the elements in the current window. The ordered set $l$ stores the smaller half of the elements in the current window, and the ordered set $r$ stores the larger half of the elements.

We traverse the array $\textit{nums}$. For each element $x$, we add it to the ordered set $r$, then move the smallest element in the ordered set $r$ to the ordered set $l$. If the size of the ordered set $l$ is greater than the size of the ordered set $r$ by more than $1$, we move the largest element in the ordered set $l$ to the ordered set $r$.

If the total number of elements in the current window is $k$ and the size is odd, the maximum value in the ordered set $l$ is the median. If the size of the current window is even, the average of the maximum value in the ordered set $l$ and the minimum value in the ordered set $r$ is the median. Then, we remove the leftmost element of the window and continue traversing the array.

The time complexity is $O(n \log k)$, and the space complexity is $O(k)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> l, r;
        int n = nums.size();
        vector<double> ans;
        for (int i = 0; i < n; ++i) {
            r.insert(nums[i]);
            l.insert(*r.begin());
            r.erase(r.begin());
            while (l.size() - r.size() > 1) {
                r.insert(*l.rbegin());
                l.erase(prev(l.end()));
            }
            int j = i - k + 1;
            if (j >= 0) {
                ans.push_back(k % 2 ? *l.rbegin() : ((double) *l.rbegin() + *r.begin()) / 2);
                auto it = l.find(nums[j]);
                if (it != l.end()) {
                    l.erase(it);
                } else {
                    r.erase(r.find(nums[j]));
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1438"></a>
## 41. LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (Medium)

[Official problem](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1400-1499/1438.Longest%20Continuous%20Subarray%20With%20Absolute%20Diff%20Less%20Than%20or%20Equal%20to%20Limit/README_EN.md)

### Problem description

You are given an array of integers `nums` and an integer `limit`.

Return the size of the **longest non-empty subarray** such that the **absolute** difference between **every pair of elements** in this **subarray** is **less than or equal** to `limit`.

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^9`

- `0 <= limit <= 10^9`

### Approach and complexity

We can use a deque to maintain the maximum and minimum values within the window. We maintain two deques, one for storing the indices of the maximum values and the other for the minimum values within the window. Define two pointers $l$ and $r$ to point to the left and right boundaries of the window, respectively.

Each time we move the right boundary $r$ to the right, we check if the element corresponding to the tail index of the maximum value deque is less than the current element. If it is, we dequeue the tail element until the element corresponding to the tail of the maximum value deque is not less than the current element. Similarly, we check if the element corresponding to the tail index of the minimum value deque is greater than the current element. If it is, we dequeue the tail element until the element corresponding to the tail of the minimum value deque is not greater than the current element. Then, we enqueue the current element's index.

If the difference between the elements at the front of the maximum value deque and the minimum value deque is greater than $\textit{limit}$, then we move the left boundary $l$ to the right. If the element at the front of the maximum value deque is less than $l$, we dequeue the front element of the maximum value deque. Similarly, if the element at the front of the minimum value deque is less than $l$, we dequeue the front element of the minimum value deque.

The answer is $n - l$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> max_q;
        deque<int> min_q;
        int n = nums.size();
        int l = 0;

        for (int r = 0; r < n; ++r) {
            while (!max_q.empty() && nums[max_q.back()] < nums[r]) {
                max_q.pop_back();
            }
            while (!min_q.empty() && nums[min_q.back()] > nums[r]) {
                min_q.pop_back();
            }
            max_q.push_back(r);
            min_q.push_back(r);

            if (nums[max_q.front()] - nums[min_q.front()] > limit) {
                ++l;
                if (max_q.front() < l) {
                    max_q.pop_front();
                }
                if (min_q.front() < l) {
                    min_q.pop_front();
                }
            }
        }
        return n - l;
    }
};
```

---

<a id="lc-239"></a>
## 42. LC 239 — Sliding Window Maximum (Hard)

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

<a id="lc-451"></a>
## 43. LC 451 — Sort Characters By Frequency (Medium)

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

<a id="lc-659"></a>
## 44. LC 659 — Split Array into Consecutive Subsequences (Medium)

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

<a id="lc-846"></a>
## 45. LC 846 — Hand of Straights (Medium)

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

<a id="lc-1167"></a>
## 46. LC 1167 — Minimum Cost to Connect Sticks (Medium)

[Official problem](https://leetcode.com/problems/minimum-cost-to-connect-sticks) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1100-1199/1167.Minimum%20Cost%20to%20Connect%20Sticks/README_EN.md)

### Problem description

You have some number of sticks with positive integer lengths. These lengths are given as an array `sticks`, where `sticks[i]` is the length of the `i^th` stick.

You can connect any two sticks of lengths `x` and `y` into one stick by paying a cost of `x + y`. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

### Constraints

- `1 <= sticks.length <= 10^4`

- `1 <= sticks[i] <= 10^4`

### Approach and complexity

We can use a greedy approach, each time choosing the shortest two sticks to connect, which ensures the minimum cost of connection.

Therefore, we can use a priority queue (min heap) to maintain the current stick lengths. Each time, we take out two sticks from the priority queue to connect, then put the connected stick back into the priority queue, until there is only one stick left in the priority queue.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{sticks}$.

### C++20 solution

```cpp
class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (auto& x : sticks) {
            pq.push(x);
        }
        int ans = 0;
        while (pq.size() > 1) {
            int x = pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();
            int z = x + y;
            ans += z;
            pq.push(z);
        }
        return ans;
    }
};
```

---

<a id="lc-1792"></a>
## 47. LC 1792 — Maximum Average Pass Ratio (Medium)

[Official problem](https://leetcode.com/problems/maximum-average-pass-ratio) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1792.Maximum%20Average%20Pass%20Ratio/README_EN.md)

### Problem description

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `classes`, where `classes[i] = [pass_i, total_i]`. You know beforehand that in the `i^th` class, there are `total_i` total students, but only `pass_i` number of students will pass the exam.

You are also given an integer `extraStudents`. There are another `extraStudents` brilliant students that are **guaranteed** to pass the exam of any class they are assigned to. You want to assign each of the `extraStudents` students to a class in a way that **maximizes** the **average** pass ratio across **all** the classes.

The **pass ratio** of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The **average pass ratio** is the sum of pass ratios of all the classes divided by the number of the classes.

Return the **maximum** possible average pass ratio after assigning the `extraStudents` students. Answers within `10^-5` of the actual answer will be accepted.

### Constraints

- `1 <= classes.length <= 10^5`

- `classes[i].length == 2`

- `1 <= pass_i <= total_i <= 10^5`

- `1 <= extraStudents <= 10^5`

### Approach and complexity

Suppose a class currently has a pass rate of $\frac{a}{b}$. If we arrange a smart student into this class, then the pass rate of the class will become $\frac{a+1}{b+1}$. We can find that the increment of the pass rate is $\frac{a+1}{b+1} - \frac{a}{b}$.

We maintain a max-heap, which stores the increment of the pass rate for each class.

Perform `extraStudents` operations, each time taking a class from the top of the heap, adding $1$ to both the number of students and the number of passes in this class, then recalculating the increment of the pass rate of this class and putting it back into the heap. Repeat this process until all students are allocated.

Finally, we sum up the pass rates of all classes, and then divide by the number of classes to get the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of classes.

### C++20 solution

```cpp
class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        priority_queue<tuple<double, int, int>> pq;
        for (auto& e : classes) {
            int a = e[0], b = e[1];
            double x = (double) (a + 1) / (b + 1) - (double) a / b;
            pq.push({x, a, b});
        }
        while (extraStudents--) {
            auto [_, a, b] = pq.top();
            pq.pop();
            a++;
            b++;
            double x = (double) (a + 1) / (b + 1) - (double) a / b;
            pq.push({x, a, b});
        }
        double ans = 0;
        while (pq.size()) {
            auto [_, a, b] = pq.top();
            pq.pop();
            ans += (double) a / b;
        }
        return ans / classes.size();
    }
};
```

---

<a id="lc-2233"></a>
## 48. LC 2233 — Maximum Product After K Increments (Medium)

[Official problem](https://leetcode.com/problems/maximum-product-after-k-increments) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2200-2299/2233.Maximum%20Product%20After%20K%20Increments/README_EN.md)

### Problem description

You are given an array of non-negative integers `nums` and an integer `k`. In one operation, you may choose **any** element from `nums` and **increment** it by `1`.

Return the **maximum** **product** of `nums` after **at most** `k` operations. Since the answer may be very large, return it modulo `10^9 + 7`. Note that you should maximize the product before taking the modulo.

### Constraints

- `1 <= nums.length, k <= 10^5`

- `0 <= nums[i] <= 10^6`

### Approach and complexity

An increment is best spent on a currently smallest value: for x≤y, (x+1)y≥x(y+1). Sort and raise the smallest prefix to each next level in bulk. When k cannot reach the next level, distribute it as evenly as possible across that prefix. This avoids simulating every increment.

Time O(n log n); auxiliary space O(log n) for sorting. Use 64-bit arithmetic for leveling costs and modular products.

### C++20 solution

```cpp
class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        ranges::sort(nums);
        int n = nums.size(), count = 1;
        long long remaining = k, level = nums[0];
        while (count < n) {
            long long cost = (nums[count] - level) * count;
            if (cost > remaining) break;
            remaining -= cost;
            level = nums[count++];
        }
        level += remaining / count;
        int extra = remaining % count;
        constexpr long long mod = 1'000'000'007;
        long long answer = 1;
        for (int i = 0; i < n; ++i) {
            long long value = i < count ? level + (i < extra) : nums[i];
            answer = answer * value % mod;
        }
        return static_cast<int>(answer);
    }
};
```

---

<a id="lc-2558"></a>
## 49. LC 2558 — Take Gifts From the Richest Pile (Easy)

[Official problem](https://leetcode.com/problems/take-gifts-from-the-richest-pile) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2500-2599/2558.Take%20Gifts%20From%20the%20Richest%20Pile/README_EN.md)

### Problem description

You are given an integer array `gifts` denoting the number of gifts in various piles. Every second, you do the following:

- Choose the pile with the maximum number of gifts.

- If there is more than one pile with the maximum number of gifts, choose any.

- Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.

Return the number of gifts remaining after `k` seconds.

### Constraints

- `1 <= gifts.length <= 10^3`

- `1 <= gifts[i] <= 10^9`

- `1 <= k <= 10^3`

### Approach and complexity

We can store the array $\textit{gifts}$ in a max heap, and then loop $k$ times, each time taking out the top element of the heap, taking the square root of it, and putting the result back into the heap.

Finally, we add up all the elements in the heap as the answer.

The time complexity is $O(n + k \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{gifts}$.

### C++20 solution

```cpp
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        make_heap(gifts.begin(), gifts.end());
        while (k--) {
            pop_heap(gifts.begin(), gifts.end());
            gifts.back() = sqrt(gifts.back());
            push_heap(gifts.begin(), gifts.end());
        }
        return accumulate(gifts.begin(), gifts.end(), 0LL);
    }
};
```

---

<a id="lc-3066"></a>
## 50. LC 3066 — Minimum Operations to Exceed Threshold Value II (Medium)

[Official problem](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/3000-3099/3066.Minimum%20Operations%20to%20Exceed%20Threshold%20Value%20II/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `nums`, and an integer `k`.

You are allowed to perform some operations on `nums`, where in a single operation, you can:

- Select the two **smallest** integers `x` and `y` from `nums`.

- Remove `x` and `y` from `nums`.

- Insert `(min(x, y) * 2 + max(x, y))` at any position in the array.

**Note** that you can only apply the described operation if `nums` contains **at least** two elements.

Return the **minimum** number of operations needed so that all elements of the array are **greater than or equal to** `k`.

### Constraints

- `2 <= nums.length <= 2 * 10^5`

- `1 <= nums[i] <= 10^9`

- `1 <= k <= 10^9`

- The input is generated such that an answer always exists. That is, after performing some number of operations, all elements of the array are greater than or equal to `k`.

### Approach and complexity

We can use a priority queue (min heap) to simulate this process.

Specifically, we first add the elements in the array to the priority queue `pq`. Then we continuously take out the two smallest elements `x` and `y` from the priority queue, and put `min(x, y) * 2 + max(x, y)` back into the priority queue. After each operation, we increase the operation count by one. We stop the operation when the number of elements in the queue is less than 2 or the smallest element in the queue is greater than or equal to `k`.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        using ll = long long;
        priority_queue<ll, vector<ll>, greater<ll>> pq;
        for (int x : nums) {
            pq.push(x);
        }
        int ans = 0;
        for (; pq.size() > 1 && pq.top() < k; ++ans) {
            ll x = pq.top();
            pq.pop();
            ll y = pq.top();
            pq.pop();
            pq.push(x * 2 + y);
        }
        return ans;
    }
};
```
