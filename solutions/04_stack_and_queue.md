# 4. Stack & Queue — C++20 solutions

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

1. [LC 20 — Valid Parentheses](#lc-20)
2. [LC 155 — Min Stack](#lc-155)
3. [LC 232 — Implement Queue using Stacks](#lc-232)
4. [LC 225 — Implement Stack using Queues](#lc-225)
5. [LC 150 — Evaluate Reverse Polish Notation](#lc-150)
6. [LC 739 — Daily Temperatures](#lc-739)
7. [LC 496 — Next Greater Element I](#lc-496)
8. [LC 503 — Next Greater Element II](#lc-503)
9. [LC 84 — Largest Rectangle in Histogram](#lc-84)
10. [LC 85 — Maximal Rectangle](#lc-85)
11. [LC 42 — Trapping Rain Water](#lc-42)
12. [LC 394 — Decode String](#lc-394)
13. [LC 71 — Simplify Path](#lc-71)
14. [LC 227 — Basic Calculator II](#lc-227)
15. [LC 224 — Basic Calculator](#lc-224)
16. [LC 32 — Longest Valid Parentheses](#lc-32)
17. [LC 402 — Remove K Digits](#lc-402)
18. [LC 316 — Remove Duplicate Letters](#lc-316)
19. [LC 901 — Online Stock Span](#lc-901)
20. [LC 853 — Car Fleet](#lc-853)
21. [LC 735 — Asteroid Collision](#lc-735)
22. [LC 946 — Validate Stack Sequences](#lc-946)
23. [LC 1047 — Remove All Adjacent Duplicates In String](#lc-1047)
24. [LC 1209 — Remove All Adjacent Duplicates in String II](#lc-1209)
25. [LC 1249 — Minimum Remove to Make Valid Parentheses](#lc-1249)
26. [LC 1544 — Make The String Great](#lc-1544)
27. [LC 678 — Valid Parenthesis String](#lc-678)
28. [LC 921 — Minimum Add to Make Parentheses Valid](#lc-921)
29. [LC 856 — Score of Parentheses](#lc-856)
30. [LC 1021 — Remove Outermost Parentheses](#lc-1021)
31. [LC 933 — Number of Recent Calls](#lc-933)
32. [LC 622 — Design Circular Queue](#lc-622)
33. [LC 641 — Design Circular Deque](#lc-641)
34. [LC 239 — Sliding Window Maximum](#lc-239)
35. [LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](#lc-1438)
36. [LC 862 — Shortest Subarray with Sum at Least K](#lc-862)
37. [LC 1696 — Jump Game VI](#lc-1696)
38. [LC 2073 — Time Needed to Buy Tickets](#lc-2073)
39. [LC 649 — Dota2 Senate](#lc-649)
40. [LC 1700 — Number of Students Unable to Eat Lunch](#lc-1700)
41. [LC 1823 — Find the Winner of the Circular Game](#lc-1823)
42. [LC 950 — Reveal Cards In Increasing Order](#lc-950)
43. [LC 994 — Rotting Oranges](#lc-994)
44. [LC 102 — Binary Tree Level Order Traversal](#lc-102)
45. [LC 199 — Binary Tree Right Side View](#lc-199)
46. [LC 542 — 01 Matrix](#lc-542)
47. [LC 752 — Open the Lock](#lc-752)
48. [LC 127 — Word Ladder](#lc-127)
49. [LC 210 — Course Schedule II](#lc-210)
50. [LC 2390 — Removing Stars From a String](#lc-2390)

---

<a id="lc-20"></a>
## 1. LC 20 — Valid Parentheses (Easy)

[Official problem](https://leetcode.com/problems/valid-parentheses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0020.Valid%20Parentheses/README_EN.md)

### Problem description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.

- Open brackets must be closed in the correct order.

- Every close bracket has a corresponding open bracket of the same type.

### Constraints

- `1 <= s.length <= 10^4`

- `s` consists of parentheses only `'()[]{}'`.

### Approach and complexity

We use a hash table $d$ to map each opening bracket to its closing bracket, and a stack $\textit{stk}$ to store closers that have not been matched yet. Scan $s$ from left to right. When the current character is an opening bracket, push the corresponding closer from $d$ onto $\textit{stk}$. When it is a closing bracket, return `false` if $\textit{stk}$ is empty or the popped top is different from that character.

After the scan, return `true` if $\textit{stk}$ is empty: every pair has been closed in the right type and order. If the stack still holds a closer, some opening bracket was never matched, so return `false`.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of $s$.

### C++20 solution

```cpp
class Solution {
public:
    bool isValid(string s) {
        string stk;
        unordered_map<char, char> d{{'(', ')'}, {'[', ']'}, {'{', '}'}};
        for (char c : s) {
            if (d.contains(c)) {
                stk.push_back(d[c]);
            } else if (stk.empty() || stk.back() != c) {
                return false;
            } else {
                stk.pop_back();
            }
        }
        return stk.empty();
    }
};
```

---

<a id="lc-155"></a>
## 2. LC 155 — Min Stack (Medium)

[Official problem](https://leetcode.com/problems/min-stack) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0155.Min%20Stack/README_EN.md)

### Problem description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.

- `void push(int value)` pushes the element `value` onto the stack.

- `void pop()` removes the element on the top of the stack.

- `int top()` gets the top element of the stack.

- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

### Constraints

- `-2^31 <= val <= 2^31 - 1`

- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.

- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

### Approach and complexity

Maintain a value stack and a parallel stack of prefix minima. The minimum after each push is the smaller of the new value and the prior minimum; popping restores both states.

Each operation O(1); storage O(n).

### C++20 solution

```cpp
class MinStack {
public:
    MinStack() {
        stk2.push(INT_MAX);
    }

    void push(int val) {
        stk1.push(val);
        stk2.push(min(val, stk2.top()));
    }

    void pop() {
        stk1.pop();
        stk2.pop();
    }

    int top() {
        return stk1.top();
    }

    int getMin() {
        return stk2.top();
    }

private:
    stack<int> stk1;
    stack<int> stk2;
};
```

---

<a id="lc-232"></a>
## 3. LC 232 — Implement Queue using Stacks (Easy)

[Official problem](https://leetcode.com/problems/implement-queue-using-stacks) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0232.Implement%20Queue%20using%20Stacks/README_EN.md)

### Problem description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.

- `int pop()` Removes the element from the front of the queue and returns it.

- `int peek()` Returns the element at the front of the queue.

- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.

- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

### Constraints

- `1 <= x <= 9`

- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.

- All the calls to `pop` and `peek` are valid.

**Follow-up:** Can you implement the queue such that each operation is **amortized** `O(1)` time complexity? In other words, performing `n` operations will take overall `O(n)` time even if one of those operations may take longer.

### Approach and complexity

We use two stacks, where $\textit{stk1}$ is used for enqueue, and another stack $\textit{stk2}$ is used for dequeue.

When enqueueing, we directly push the element into $\textit{stk1}$. The time complexity is $O(1)$.

When dequeueing, we first check whether $\textit{stk2}$ is empty. If it is empty, we pop all elements from $\textit{stk1}$ and push them into $\textit{stk2}$, and then pop an element from $\textit{stk2}$. If $\textit{stk2}$ is not empty, we directly pop an element from $\textit{stk2}$. The amortized time complexity is $O(1)$.

When getting the front element, we first check whether $\textit{stk2}$ is empty. If it is empty, we pop all elements from $\textit{stk1}$ and push them into $\textit{stk2}$, and then get the top element from $\textit{stk2}$. If $\textit{stk2}$ is not empty, we directly get the top element from $\textit{stk2}$. The amortized time complexity is $O(1)$.

When checking whether the queue is empty, we only need to check whether both stacks are empty. The time complexity is $O(1)$.

### C++20 solution

```cpp
class MyQueue {
public:
    MyQueue() {
    }

    void push(int x) {
        stk1.push(x);
    }

    int pop() {
        move();
        int ans = stk2.top();
        stk2.pop();
        return ans;
    }

    int peek() {
        move();
        return stk2.top();
    }

    bool empty() {
        return stk1.empty() && stk2.empty();
    }

private:
    stack<int> stk1;
    stack<int> stk2;

    void move() {
        if (stk2.empty()) {
            while (!stk1.empty()) {
                stk2.push(stk1.top());
                stk1.pop();
            }
        }
    }
};
```

---

<a id="lc-225"></a>
## 4. LC 225 — Implement Stack using Queues (Easy)

[Official problem](https://leetcode.com/problems/implement-stack-using-queues) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0225.Implement%20Stack%20using%20Queues/README_EN.md)

### Problem description

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element x to the top of the stack.

- `int pop()` Removes the element on the top of the stack and returns it.

- `int top()` Returns the element on the top of the stack.

- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

Notes:

- You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.

- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

### Constraints

- `1 <= x <= 9`

- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.

- All the calls to `pop` and `top` are valid.

**Follow-up:** Can you implement the stack using only one queue?

### Approach and complexity

We use two queues $q_1$ and $q_2$, where $q_1$ is used to store the elements in the stack, and $q_2$ is used to assist in implementing the stack operations.

- $\textit{push}$ operation: Push the element into $q_2$, then pop the elements in $q_1$ one by one and push them into $q_2$, finally swap the references of $q_1$ and $q_2$. The time complexity is $O(n)$.
- $\textit{pop}$ operation: Directly pop the front element of $q_1$. The time complexity is $O(1)$.
- $\textit{top}$ operation: Directly return the front element of $q_1$. The time complexity is $O(1)$.
- $\textit{empty}$ operation: Check whether $q_1$ is empty. The time complexity is $O(1)$.

The space complexity is $O(n)$, where $n$ is the number of elements in the stack.

### C++20 solution

```cpp
class MyStack {
public:
    MyStack() {
    }

    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }

    int pop() {
        int x = q1.front();
        q1.pop();
        return x;
    }

    int top() {
        return q1.front();
    }

    bool empty() {
        return q1.empty();
    }

private:
    queue<int> q1;
    queue<int> q2;
};
```

---

<a id="lc-150"></a>
## 5. LC 150 — Evaluate Reverse Polish Notation (Medium)

[Official problem](https://leetcode.com/problems/evaluate-reverse-polish-notation) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0150.Evaluate%20Reverse%20Polish%20Notation/README_EN.md)

### Problem description

You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

**Note** that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.

- Each operand may be an integer or another expression.

- The division between two integers always **truncates toward zero**.

- There will not be any division by zero.

- The input represents a valid arithmetic expression in a reverse polish notation.

- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

### Constraints

- `1 <= tokens.length <= 10^4`

- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

### Approach and complexity

Use a value stack. An operator consumes the last two operands in left/right order and pushes its result. Integer division truncates toward zero.

Time O(n) in token count; auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (auto& t : tokens) {
            if (t.size() > 1 || isdigit(t[0])) {
                stk.push(stoi(t));
            } else {
                int y = stk.top();
                stk.pop();
                int x = stk.top();
                stk.pop();
                if (t[0] == '+')
                    stk.push(x + y);
                else if (t[0] == '-')
                    stk.push(x - y);
                else if (t[0] == '*')
                    stk.push(x * y);
                else
                    stk.push(x / y);
            }
        }
        return stk.top();
    }
};
```

---

<a id="lc-739"></a>
## 6. LC 739 — Daily Temperatures (Medium)

[Official problem](https://leetcode.com/problems/daily-temperatures) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0739.Daily%20Temperatures/README_EN.md)

### Problem description

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i^th` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Constraints

- `1 <= temperatures.length <= 10^5`

- `30 <= temperatures[i] <= 100`

### Approach and complexity

This problem requires us to find the position of the first element greater than each element to its right, which is a typical application scenario for a monotonic stack.

We traverse the array $\textit{temperatures}$ from right to left, maintaining a stack $\textit{stk}$ that is monotonically increasing from top to bottom in terms of temperature. The stack stores the indices of the array elements. For each element $\textit{temperatures}[i]$, we continuously compare it with the top element of the stack. If the temperature corresponding to the top element of the stack is less than or equal to $\textit{temperatures}[i]$, we pop the top element of the stack in a loop until the stack is empty or the temperature corresponding to the top element of the stack is greater than $\textit{temperatures}[i]$. At this point, the top element of the stack is the first element greater than $\textit{temperatures}[i]$ to its right, and the distance is $\textit{stk}.\textit{top}() - i$. We update the answer array accordingly. Then we push $\textit{temperatures}[i]$ onto the stack and continue traversing.

After the traversal, we return the answer array.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{temperatures}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<int> stk;
        vector<int> ans(n);
        for (int i = n - 1; ~i; --i) {
            while (!stk.empty() && temperatures[stk.top()] <= temperatures[i]) {
                stk.pop();
            }
            if (!stk.empty()) {
                ans[i] = stk.top() - i;
            }
            stk.push(i);
        }
        return ans;
    }
};
```

---

<a id="lc-496"></a>
## 7. LC 496 — Next Greater Element I (Easy)

[Official problem](https://leetcode.com/problems/next-greater-element-i) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0496.Next%20Greater%20Element%20I/README_EN.md)

### Problem description

The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the **next greater element** as described above.

### Constraints

- `1 <= nums1.length <= nums2.length <= 1000`

- `0 <= nums1[i], nums2[i] <= 10^4`

- All integers in `nums1` and `nums2` are **unique**.

- All the integers of `nums1` also appear in `nums2`.

**Follow up:** Could you find an `O(nums1.length + nums2.length)` solution?

### Approach and complexity

We can traverse the array $\textit{nums2}$ from right to left, maintaining a stack $\textit{stk}$ that is monotonically increasing from top to bottom. We use a hash table $d$ to record the next greater element for each element.

When we encounter an element $x$, if the stack is not empty and the top element of the stack is less than $x$, we keep popping the top elements until the stack is empty or the top element is greater than or equal to $x$. At this point, if the stack is not empty, the top element of the stack is the next greater element for $x$. Otherwise, $x$ has no next greater element.

Finally, we traverse the array $\textit{nums1}$ and use the hash table $d$ to get the answer.

The time complexity is $O(m + n)$, and the space complexity is $O(n)$, where $m$ and $n$ are the lengths of the arrays $\textit{nums1}$ and $\textit{nums2}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> stk;
        unordered_map<int, int> d;
        ranges::reverse(nums2);
        for (int x : nums2) {
            while (!stk.empty() && stk.top() < x) {
                stk.pop();
            }
            if (!stk.empty()) {
                d[x] = stk.top();
            }
            stk.push(x);
        }
        vector<int> ans;
        for (int x : nums1) {
            ans.push_back(d.contains(x) ? d[x] : -1);
        }
        return ans;
    }
};
```

---

<a id="lc-503"></a>
## 8. LC 503 — Next Greater Element II (Medium)

[Official problem](https://leetcode.com/problems/next-greater-element-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0503.Next%20Greater%20Element%20II/README_EN.md)

### Problem description

Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return the **next greater number** for every element in `nums`.

The **next greater number** of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

### Constraints

- `1 <= nums.length <= 10^4`

- `-10^9 <= nums[i] <= 10^9`

### Approach and complexity

The problem requires us to find the next greater element for each element. Therefore, we can traverse the array from back to front, which effectively turns the problem into finding the previous greater element. Additionally, since the array is circular, we can traverse the array twice.

Specifically, we start traversing the array from index $n \times 2 - 1$, where $n$ is the length of the array. Then, we let $j = i \bmod n$, where $\bmod$ represents the modulo operation. If the stack is not empty and the top element of the stack is less than or equal to $\textit{nums}[j]$, then we continuously pop the top element of the stack until the stack is empty or the top element of the stack is greater than $\textit{nums}[j]$. At this point, the top element of the stack is the previous greater element for $\textit{nums}[j]$, and we assign it to $\textit{ans}[j]$. Finally, we push $\textit{nums}[j]$ onto the stack. We continue to the next element.

After the traversal is complete, we can obtain the array $\textit{ans}$, which represents the next greater element for each element in the array $\textit{nums}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);
        stack<int> stk;
        for (int i = n * 2 - 1; ~i; --i) {
            int j = i % n;
            while (stk.size() && stk.top() <= nums[j]) {
                stk.pop();
            }
            if (stk.size()) {
                ans[j] = stk.top();
            }
            stk.push(nums[j]);
        }
        return ans;
    }
};
```

---

<a id="lc-84"></a>
## 9. LC 84 — Largest Rectangle in Histogram (Hard)

[Official problem](https://leetcode.com/problems/largest-rectangle-in-histogram) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0084.Largest%20Rectangle%20in%20Histogram/README_EN.md)

### Problem description

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

### Constraints

- `1 <= heights.length <= 10^5`

- `0 <= heights[i] <= 10^4`

### Approach and complexity

We can enumerate the height $h$ of each bar as the height of the rectangle. Using a monotonic stack, we find the index $\textit{left}_i$, $\textit{right}_i$ of the first bar with a height less than $h$ to the left and right. The area of the rectangle at this time is $h \times (\textit{right}_i-\textit{left}_i-1)$. We can find the maximum value.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ represents the length of $\textit{heights}$.

Common model of monotonic stack: Find the **nearest** number to the left/right of each number that is **larger/smaller** than it. Template:

```python
stk = []
for i in range(n):
    while stk and check(stk[-1], i):
        stk.pop()
    stk.append(i)
```

### C++20 solution

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0, n = heights.size();
        stack<int> stk;
        vector<int> left(n, -1);
        vector<int> right(n, n);
        for (int i = 0; i < n; ++i) {
            while (!stk.empty() && heights[stk.top()] >= heights[i]) {
                right[stk.top()] = i;
                stk.pop();
            }
            if (!stk.empty()) left[i] = stk.top();
            stk.push(i);
        }
        for (int i = 0; i < n; ++i)
            res = max(res, heights[i] * (right[i] - left[i] - 1));
        return res;
    }
};
```

---

<a id="lc-85"></a>
## 10. LC 85 — Maximal Rectangle (Hard)

[Official problem](https://leetcode.com/problems/maximal-rectangle) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0085.Maximal%20Rectangle/README_EN.md)

### Problem description

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

### Constraints

- `rows == matrix.length`

- `cols == matrix[i].length`

- `1 <= rows, cols <= 200`

- `matrix[i][j]` is `'0'` or `'1'`.

### Approach and complexity

We can treat each row as the base of a histogram and calculate the maximum area of the histogram for each row.

Specifically, we maintain an array $\textit{heights}$ with the same length as the number of columns in the matrix, where $\textit{heights}[j]$ represents the height of the column at the $j$-th position with the current row as the base. For each row, we iterate through each column:

- If the current element is '1', increment $\textit{heights}[j]$ by $1$.
- If the current element is '0', set $\textit{heights}[j]$ to $0$.

Then, we use the monotonic stack algorithm to calculate the maximum rectangle area of the current histogram and update the answer.

The specific steps of the monotonic stack are as follows:

1. Initialize an empty stack $\textit{stk}$ to store the indices of the columns.
2. Initialize two arrays $\textit{left}$ and $\textit{right}$, representing the index of the first column to the left and right of each column that is shorter than the current column.
3. Iterate through the heights array $\textit{heights}$, first calculating the index of the first column to the left of each column that is shorter than the current column, and store it in $\textit{left}$.
4. Then iterate through the heights array $\textit{heights}$ in reverse order, calculating the index of the first column to the right of each column that is shorter than the current column, and store it in $\textit{right}$.
5. Finally, calculate the maximum rectangle area for each column and update the answer.

The time complexity is $O(mn)$, where $m$ is the number of rows in $\textit{matrix}$ and $n$ is the number of columns in $\textit{matrix}$.

### C++20 solution

```cpp
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int n = matrix[0].size();
        vector<int> heights(n);
        int ans = 0;
        for (auto& row : matrix) {
            for (int j = 0; j < n; ++j) {
                if (row[j] == '1')
                    ++heights[j];
                else
                    heights[j] = 0;
            }
            ans = max(ans, largestRectangleArea(heights));
        }
        return ans;
    }

    int largestRectangleArea(vector<int>& heights) {
        int res = 0, n = heights.size();
        stack<int> stk;
        vector<int> left(n, -1);
        vector<int> right(n, n);
        for (int i = 0; i < n; ++i) {
            while (!stk.empty() && heights[stk.top()] >= heights[i]) {
                right[stk.top()] = i;
                stk.pop();
            }
            if (!stk.empty()) left[i] = stk.top();
            stk.push(i);
        }
        for (int i = 0; i < n; ++i)
            res = max(res, heights[i] * (right[i] - left[i] - 1));
        return res;
    }
};
```

---

<a id="lc-42"></a>
## 11. LC 42 — Trapping Rain Water (Hard)

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

<a id="lc-394"></a>
## 12. LC 394 — Decode String (Medium)

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

<a id="lc-71"></a>
## 13. LC 71 — Simplify Path (Medium)

[Official problem](https://leetcode.com/problems/simplify-path) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0071.Simplify%20Path/README_EN.md)

### Problem description

You are given an absolute path for a Unix-style file system, which always begins with a slash `'/'`. Your task is to transform this absolute path into its **simplified canonical path**.

The rules of a Unix-style file system are as follows:

- A single period `'.'` represents the current directory.

- A double period `'..'` represents the previous/parent directory.

- Multiple consecutive slashes such as `'//'` and `'///'` are treated as a single slash `'/'`.

- Any sequence of periods that does **not match** the rules above should be treated as a **valid directory or** **file ****name**. For example, `'...' `and `'....'` are valid directory or file names.

The simplified canonical path should follow these rules:

- The path must start with a single slash `'/'`.

- Directories within the path must be separated by exactly one slash `'/'`.

- The path must not end with a slash `'/'`, unless it is the root directory.

- The path must not have any single or double periods (`'.'` and `'..'`) used to denote current or parent directories.

Return the **simplified canonical path**.

### Constraints

- `1 <= path.length <= 3000`

- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.

- `path` is a valid absolute Unix path.

### Approach and complexity

We first split the path into a number of substrings split by `'/'`. Then, we traverse each substring and perform the following operations based on the content of the substring:

- If the substring is empty or `'.'`, no operation is performed because `'.'` represents the current directory.
- If the substring is `'..'`, the top element of the stack is popped, because `'..'` represents the parent directory.
- If the substring is other strings, the substring is pushed into the stack, because the substring represents the subdirectory of the current directory.

Finally, we concatenate all the elements in the stack from the bottom to the top of the stack to form a string, which is the simplified canonical path.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the path.

### C++20 solution

```cpp
class Solution {
public:
    string simplifyPath(string path) {
        deque<string> stk;
        stringstream ss(path);
        string t;
        while (getline(ss, t, '/')) {
            if (t == "" || t == ".") {
                continue;
            }
            if (t == "..") {
                if (!stk.empty()) {
                    stk.pop_back();
                }
            } else {
                stk.push_back(t);
            }
        }
        if (stk.empty()) {
            return "/";
        }
        string ans;
        for (auto& s : stk) {
            ans += "/" + s;
        }
        return ans;
    }
};
```

---

<a id="lc-227"></a>
## 14. LC 227 — Basic Calculator II (Medium)

[Official problem](https://leetcode.com/problems/basic-calculator-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0227.Basic%20Calculator%20II/README_EN.md)

### Problem description

Given a string `s` which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

### Constraints

- `1 <= s.length <= 3 * 10^5`

- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.

- `s` represents a valid expression.

- All the integers in the expression are non-negative integers in the range `[0, 2^31 - 1]`.

- The answer is **guaranteed** to fit in a **32-bit integer**.

### Approach and complexity

We traverse the string $s$, and use a variable $\textit{sign}$ to record the operator before each number. For the first number, its previous operator is considered as a plus sign. Each time we traverse to the end of a number, we decide the calculation method based on $\textit{sign}$:

- Plus sign: push the number into the stack;
- Minus sign: push the opposite number into the stack;
- Multiplication and division signs: calculate the number with the top element of the stack, and replace the top element of the stack with the calculation result.

After the traversal ends, the sum of the elements in the stack is the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    int calculate(string s) {
        int v = 0, n = s.size();
        char sign = '+';
        stack<int> stk;
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            if (isdigit(c)) v = v * 10 + (c - '0');
            if (i == n - 1 || c == '+' || c == '-' || c == '*' || c == '/') {
                if (sign == '+')
                    stk.push(v);
                else if (sign == '-')
                    stk.push(-v);
                else if (sign == '*') {
                    int t = stk.top();
                    stk.pop();
                    stk.push(t * v);
                } else {
                    int t = stk.top();
                    stk.pop();
                    stk.push(t / v);
                }
                sign = c;
                v = 0;
            }
        }
        int ans = 0;
        while (!stk.empty()) {
            ans += stk.top();
            stk.pop();
        }
        return ans;
    }
};
```

---

<a id="lc-224"></a>
## 15. LC 224 — Basic Calculator (Hard)

[Official problem](https://leetcode.com/problems/basic-calculator) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0224.Basic%20Calculator/README_EN.md)

### Problem description

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

**Note:** You are **not** allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

### Constraints

- `1 <= s.length <= 3 * 10^5`

- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.

- `s` represents a valid expression.

- `'+'` is **not** used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).

- `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).

- There will be no two consecutive operators in the input.

- Every number and running calculation will fit in a signed 32-bit integer.

### Approach and complexity

We use a stack $\textit{stk}$ to save the current calculation result and operator, a variable $\textit{sign}$ to save the current sign, and a variable $\textit{ans}$ to save the final calculation result.

Next, we traverse each character of the string $s$:

- If the current character is a number, we use a loop to read the following consecutive numbers, and then add or subtract it to $\textit{ans}$ according to the current sign.
- If the current character is `'+'`, we change the variable $\textit{sign}$ to positive.
- If the current character is `'-'`, we change the variable $\textit{sign}$ to negative.
- If the current character is `'('`, we push the current $\textit{ans}$ and $\textit{sign}$ into the stack, and reset them to empty and 1, and start to calculate the new $\textit{ans}$ and $\textit{sign}$.
- If the current character is `')'`, we pop the top two elements of the stack, one is the operator, and the other is the number calculated before the bracket. We multiply the current number by the operator, and add the previous number to get the new $\textit{ans}$.

After traversing the string $s$, we return $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    int calculate(string s) {
        stack<int> stk;
        int ans = 0, sign = 1;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            if (isdigit(s[i])) {
                int x = 0;
                int j = i;
                while (j < n && isdigit(s[j])) {
                    x = x * 10 + (s[j] - '0');
                    ++j;
                }
                ans += sign * x;
                i = j - 1;
            } else if (s[i] == '+') {
                sign = 1;
            } else if (s[i] == '-') {
                sign = -1;
            } else if (s[i] == '(') {
                stk.push(ans);
                stk.push(sign);
                ans = 0;
                sign = 1;
            } else if (s[i] == ')') {
                ans *= stk.top();
                stk.pop();
                ans += stk.top();
                stk.pop();
            }
        }
        return ans;
    }
};
```

---

<a id="lc-32"></a>
## 16. LC 32 — Longest Valid Parentheses (Hard)

[Official problem](https://leetcode.com/problems/longest-valid-parentheses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0032.Longest%20Valid%20Parentheses/README_EN.md)

### Problem description

Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

### Constraints

- `0 <= s.length <= 3 * 10^4`

- `s[i]` is `'('`, or `')'`.

### Approach and complexity

Count opening and closing parentheses left to right; equal counts give a valid suffix of the current segment, while more closings force a reset. The reverse scan handles segments with excess openings by symmetrically resetting when openings exceed closings.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int open = 0, close = 0, best = 0;
        for (char c : s) {
            c == '(' ? ++open : ++close;
            if (open == close) best = max(best, 2 * close);
            else if (close > open) open = close = 0;
        }
        open = close = 0;
        for (auto it = s.rbegin(); it != s.rend(); ++it) {
            *it == '(' ? ++open : ++close;
            if (open == close) best = max(best, 2 * open);
            else if (open > close) open = close = 0;
        }
        return best;
    }
};
```

---

<a id="lc-402"></a>
## 17. LC 402 — Remove K Digits (Medium)

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
## 18. LC 316 — Remove Duplicate Letters (Hard)

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

<a id="lc-901"></a>
## 19. LC 901 — Online Stock Span (Medium)

[Official problem](https://leetcode.com/problems/online-stock-span) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0901.Online%20Stock%20Span/README_EN.md)

### Problem description

Design an algorithm that collects daily price quotes for some stock and returns **the span** of that stock's price for the current day.

The **span** of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

- For example, if the prices of the stock in the last four days are `[7,2,1,2]` and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal to 2 for 4 consecutive days.

- Also, if the prices of the stock in the last four days is `[7,34,1,2]` and the price of the stock today is `8`, then the span of today is `3` because starting from today, the price of the stock was less than or equal `8` for `3` consecutive days.

Implement the `StockSpanner` class:

- `StockSpanner()` Initializes the object of the class.

- `int next(int price)` Returns the **span** of the stock's price given that today's price is `price`.

### Constraints

- `1 <= price <= 10^5`

- At most `10^4` calls will be made to `next`.

### Approach and complexity

Based on the problem description, we know that for the current day's price $\textit{price}$, we start from this price and look backwards to find the first price that is larger than this price. The difference in indices $\textit{cnt}$ between these two prices is the span of the current day's price.

This is actually a classic monotonic stack model, where we find the first element larger than the current element on the left.

We maintain a stack where the prices from the bottom to the top of the stack are monotonically decreasing. Each element in the stack is a $(\textit{price}, \textit{cnt})$ data pair, where $\textit{price}$ represents the price, and $\textit{cnt}$ represents the span of the current price.

When the price $\textit{price}$ appears, we compare it with the top element of the stack. If the price of the top element of the stack is less than or equal to $\textit{price}$, we add the span $\textit{cnt}$ of the current day's price to the span of the top element of the stack, and then pop the top element of the stack. This continues until the price of the top element of the stack is greater than $\textit{price}$, or the stack is empty.

Finally, we push $(\textit{price}, \textit{cnt})$ onto the stack and return $\textit{cnt}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of times `next(price)` is called.

### C++20 solution

```cpp
class StockSpanner {
public:
    StockSpanner() {
    }

    int next(int price) {
        int cnt = 1;
        while (!stk.empty() && stk.top().first <= price) {
            cnt += stk.top().second;
            stk.pop();
        }
        stk.emplace(price, cnt);
        return cnt;
    }

private:
    stack<pair<int, int>> stk;
};
```

---

<a id="lc-853"></a>
## 20. LC 853 — Car Fleet (Medium)

[Official problem](https://leetcode.com/problems/car-fleet) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0853.Car%20Fleet/README_EN.md)

### Problem description

There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `i^th` car and `speed[i]` is the speed of the `i^th` car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.

If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

### Constraints

- `n == position.length == speed.length`

- `1 <= n <= 10^5`

- `0 < target <= 10^6`

- `0 <= position[i] < target`

- All the values of `position` are **unique**.

- `0 < speed[i] <= 10^6`

### Approach and complexity

Sort cars by position and scan from nearest to farthest from the target. A following car with arrival time no greater than the leading fleet merges into it; only a strictly larger arrival time starts a new fleet.

Time O(n log n); auxiliary space O(n) for sorted car data.

### C++20 solution

```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        ranges::sort(idx, [&](int i, int j) {
            return position[i] > position[j];
        });
        int ans = 0;
        double pre = 0;
        for (int i : idx) {
            double t = 1.0 * (target - position[i]) / speed[i];
            if (t > pre) {
                ++ans;
                pre = t;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-735"></a>
## 21. LC 735 — Asteroid Collision (Medium)

[Official problem](https://leetcode.com/problems/asteroid-collision) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0735.Asteroid%20Collision/README_EN.md)

### Problem description

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

### Constraints

- `2 <= asteroids.length <= 10^4`

- `-1000 <= asteroids[i] <= 1000`

- `asteroids[i] != 0`

### Approach and complexity

We traverse each asteroid $x$ from left to right. Since each asteroid may collide with multiple asteroids before it, we consider using a stack to store.

- For the current asteroid, if $x>0$, it will definitely not collide with the previous asteroid, and we can directly push $x$ into the stack.
- Otherwise, if the stack is not empty and the top element of the stack is greater than $0$, and the top element of the stack is less than $-x$, then the top element of the stack corresponds to the asteroid will explode, we loop to the top element of the stack Pop out until the condition is not satisfied. At this time, if the top element of the stack is equal to $-x$, then the two asteroids will explode, and we only need to pop the top element of the stack; if the stack is empty, or the top element of the stack is less than $0$, then the current asteroid will not collide, we will push $x$ into the stack.

Finally, we return the elements in the stack as the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{asteroids}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stk;
        for (int x : asteroids) {
            if (x > 0) {
                stk.push_back(x);
            } else {
                while (stk.size() && stk.back() > 0 && stk.back() < -x) {
                    stk.pop_back();
                }
                if (stk.size() && stk.back() == -x) {
                    stk.pop_back();
                } else if (stk.empty() || stk.back() < 0) {
                    stk.push_back(x);
                }
            }
        }
        return stk;
    }
};
```

---

<a id="lc-946"></a>
## 22. LC 946 — Validate Stack Sequences (Medium)

[Official problem](https://leetcode.com/problems/validate-stack-sequences) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0946.Validate%20Stack%20Sequences/README_EN.md)

### Problem description

Given two integer arrays `pushed` and `popped` each with distinct values, return `true` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or `false` otherwise.

### Constraints

- `1 <= pushed.length <= 1000`

- `0 <= pushed[i] <= 1000`

- All the elements of `pushed` are **unique**.

- `popped.length == pushed.length`

- `popped` is a permutation of `pushed`.

### Approach and complexity

We iterate through the $\textit{pushed}$ array. For the current element $x$ being iterated, we push it into the stack $\textit{stk}$. Then, we check if the top element of the stack is equal to the next element to be popped in the $\textit{popped}$ array. If they are equal, we pop the top element from the stack and increment the index $i$ of the next element to be popped in the $\textit{popped}$ array. Finally, if all elements can be popped in the order specified by the $\textit{popped}$ array, return $\textit{true}$; otherwise, return $\textit{false}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the $\textit{pushed}$ array.

### C++20 solution

```cpp
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> stk;
        int i = 0;
        for (int x : pushed) {
            stk.push(x);
            while (stk.size() && stk.top() == popped[i]) {
                stk.pop();
                ++i;
            }
        }
        return i == popped.size();
    }
};
```

---

<a id="lc-1047"></a>
## 23. LC 1047 — Remove All Adjacent Duplicates In String (Easy)

[Official problem](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1047.Remove%20All%20Adjacent%20Duplicates%20In%20String/README_EN.md)

### Problem description

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

We repeatedly make **duplicate removals** on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is **unique**.

### Constraints

- `1 <= s.length <= 10^5`

- `s` consists of lowercase English letters.

### Approach and complexity

Treat the growing output as a stack. Equal adjacent top/current characters cancel; otherwise append. The invariant is the fully reduced processed prefix.

Time O(n); auxiliary space O(n) for the working/result buffer.

### C++20 solution

```cpp
class Solution {
public:
    string removeDuplicates(string s) {
        string stk;
        for (char c : s) {
            if (!stk.empty() && stk[stk.size() - 1] == c) {
                stk.pop_back();
            } else {
                stk += c;
            }
        }
        return stk;
    }
};
```

---

<a id="lc-1209"></a>
## 24. LC 1209 — Remove All Adjacent Duplicates in String II (Medium)

[Official problem](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1200-1299/1209.Remove%20All%20Adjacent%20Duplicates%20in%20String%20II/README_EN.md)

### Problem description

You are given a string `s` and an integer `k`, a `k` **duplicate removal** consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `k` **duplicate removals** on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is **unique**.

### Constraints

- `1 <= s.length <= 10^5`

- `2 <= k <= 10^4`

- `s` only contains lowercase English letters.

### Approach and complexity

We can traverse the string $s$, maintaining a stack that stores the characters and their occurrence counts. When traversing to character $c$, if the character at the top of the stack is the same as $c$, we increment the count of the top element by one; otherwise, we push the character $c$ and count $1$ into the stack. When the count of the top element equals $k$, we pop the top element from the stack.

After traversing the string $s$, the elements remaining in the stack form the final result. We can pop the elements from the stack one by one, concatenate them into a string, and that's our answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char, int>> stk;
        for (char& c : s) {
            if (stk.size() && stk.back().first == c) {
                stk.back().second = (stk.back().second + 1) % k;
                if (stk.back().second == 0) {
                    stk.pop_back();
                }
            } else {
                stk.push_back({c, 1});
            }
        }
        string ans;
        for (auto [c, v] : stk) {
            ans += string(v, c);
        }
        return ans;
    }
};
```

---

<a id="lc-1249"></a>
## 25. LC 1249 — Minimum Remove to Make Valid Parentheses (Medium)

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

<a id="lc-1544"></a>
## 26. LC 1544 — Make The String Great (Easy)

[Official problem](https://leetcode.com/problems/make-the-string-great) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1500-1599/1544.Make%20The%20String%20Great/README_EN.md)

### Problem description

Given a string `s` of lower and upper case English letters.

A good string is a string which doesn't have **two adjacent characters** `s[i]` and `s[i + 1]` where:

- `0 <= i <= s.length - 2`

- `s[i]` is a lower-case letter and `s[i + 1]` is the same letter but in upper-case or **vice-versa**.

To make the string good, you can choose **two adjacent** characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

**Notice** that an empty string is also good.

### Constraints

- `1 <= s.length <= 100`

- `s` contains only lower and upper case English letters.

### Approach and complexity

A stack cancels adjacent equal letters of opposite case. Removing a pair may expose a new pair, which the same stack invariant handles.

Time O(n); auxiliary space O(n) for the output buffer.

### C++20 solution

```cpp
class Solution {
public:
    string makeGood(string s) {
        string stk;
        for (char c : s) {
            if (stk.empty() || abs(stk.back() - c) != 32) {
                stk += c;
            } else {
                stk.pop_back();
            }
        }
        return stk;
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

<a id="lc-856"></a>
## 29. LC 856 — Score of Parentheses (Medium)

[Official problem](https://leetcode.com/problems/score-of-parentheses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0856.Score%20of%20Parentheses/README_EN.md)

### Problem description

Given a balanced parentheses string `s`, return the **score** of the string.

The **score** of a balanced parentheses string is based on the following rule:

- `"()"` has score `1`.

- `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.

- `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

### Constraints

- `2 <= s.length <= 50`

- `s` consists of only `'('` and `')'`.

- `s` is a balanced parentheses string.

### Approach and complexity

By observing, we find that `()` is the only structure that contributes to the score, and the outer parentheses just add some multipliers to this structure. So, we only need to focus on `()`.

We use $d$ to maintain the current depth of parentheses. For each `(`, we increase the depth by one, and for each `)`, we decrease the depth by one. When we encounter `()`, we add $2^d$ to the answer.

Let's take `(()(()))` as an example. We first find the two closed parentheses `()` inside, and then add the corresponding $2^d$ to the score. In fact, we are calculating the score of `(()) + ((()))`.

```bash
( ( ) ( ( ) ) )
  ^ ^   ^ ^

( ( ) ) + ( ( ( ) ) )
  ^ ^         ^ ^
```

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string.

Related problems about parentheses:

- [678. Valid Parenthesis String](https://github.com/doocs/leetcode/blob/main/solution/0600-0699/0678.Valid%20Parenthesis%20String/README.md)
- [1021. Remove Outermost Parentheses](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1021.Remove%20Outermost%20Parentheses/README.md)
- [1096. Brace Expansion II](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1096.Brace%20Expansion%20II/README.md)
- [1249. Minimum Remove to Make Valid Parentheses](https://github.com/doocs/leetcode/blob/main/solution/1200-1299/1249.Minimum%20Remove%20to%20Make%20Valid%20Parentheses/README.md)
- [1541. Minimum Insertions to Balance a Parentheses String](https://github.com/doocs/leetcode/blob/main/solution/1500-1599/1541.Minimum%20Insertions%20to%20Balance%20a%20Parentheses%20String/README.md)
- [2116. Check if a Parentheses String Can Be Valid](https://github.com/doocs/leetcode/blob/main/solution/2100-2199/2116.Check%20if%20a%20Parentheses%20String%20Can%20Be%20Valid/README.md)

### C++20 solution

```cpp
class Solution {
public:
    int scoreOfParentheses(string s) {
        int ans = 0, d = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                ++d;
            } else {
                --d;
                if (s[i - 1] == '(') {
                    ans += 1 << d;
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1021"></a>
## 30. LC 1021 — Remove Outermost Parentheses (Easy)

[Official problem](https://leetcode.com/problems/remove-outermost-parentheses) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1021.Remove%20Outermost%20Parentheses/README_EN.md)

### Problem description

A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` nonempty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition: `s = P_1 + P_2 + ... + P_k`, where `P_i` are primitive valid parentheses strings.

Return `s` after removing the outermost parentheses of every primitive string in the primitive decomposition of `s`.

### Constraints

- `1 <= s.length <= 10^5`

- `s[i]` is either `'('` or `')'`.

- `s` is a valid parentheses string.

### Approach and complexity

Maintain nesting depth. Omit an opening parenthesis at depth zero and a closing one that returns depth to zero; these are exactly each primitive’s outer pair.

Time O(n); auxiliary space O(1) beyond output.

### C++20 solution

```cpp
class Solution {
public:
    string removeOuterParentheses(string s) {
        string ans;
        int cnt = 0;
        for (char& c : s) {
            if (c == '(') {
                if (++cnt > 1) {
                    ans.push_back(c);
                }
            } else {
                if (--cnt) {
                    ans.push_back(c);
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-933"></a>
## 31. LC 933 — Number of Recent Calls (Easy)

[Official problem](https://leetcode.com/problems/number-of-recent-calls) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0933.Number%20of%20Recent%20Calls/README_EN.md)

### Problem description

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` Initializes the counter with zero recent requests.

- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the inclusive range `[t - 3000, t]`, that is, the new request plus every earlier request that is no more than `3000` milliseconds older.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

### Constraints

- `1 <= t <= 10^9`

- Each test case will call `ping` with **strictly increasing** values of `t`.

- At most `10^4` calls will be made to `ping`.

### Approach and complexity

Append the new timestamp to a queue and remove timestamps strictly before t−3000. The remaining queue is exactly the inclusive request window.

Amortized O(1) per ping; O(W) storage for the window. Strictly increasing integer times imply W≤3001.

### C++20 solution

```cpp
class RecentCounter {
public:
    queue<int> q;

    RecentCounter() {
    }

    int ping(int t) {
        q.push(t);
        while (q.front() < t - 3000) q.pop();
        return q.size();
    }
};
```

---

<a id="lc-622"></a>
## 32. LC 622 — Design Circular Queue (Medium)

[Official problem](https://leetcode.com/problems/design-circular-queue) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0622.Design%20Circular%20Queue/README_EN.md)

### Problem description

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the `MyCircularQueue` class:

- `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.

- `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.

- `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.

- `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.

- `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.

- `boolean isEmpty()` Checks whether the circular queue is empty or not.

- `boolean isFull()` Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language.

### Constraints

- `1 <= k <= 1000`

- `0 <= value <= 1000`

- At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.

### Approach and complexity

We can use an array $q$ of length $k$ to simulate a circular queue, with a pointer $\textit{front}$ to record the position of the front element. Initially, the queue is empty, and $\textit{front}$ is $0$. Additionally, we use a variable $\textit{size}$ to record the number of elements in the queue, initially $\textit{size}$ is $0$.

When calling the `enQueue` method, we first check if the queue is full, i.e., $\textit{size} = k$. If it is full, we return $\textit{false}$. Otherwise, we insert the element at position $(\textit{front} + \textit{size}) \bmod k$, then $\textit{size} = \textit{size} + 1$, indicating that the number of elements in the queue has increased by $1$. Finally, we return $\textit{true}$.

When calling the `deQueue` method, we first check if the queue is empty, i.e., $\textit{size} = 0$. If it is empty, we return $\textit{false}$. Otherwise, we set $\textit{front} = (\textit{front} + 1) \bmod k$, indicating that the front element has been dequeued, then $\textit{size} = \textit{size} - 1$.

When calling the `Front` method, we first check if the queue is empty, i.e., $\textit{size} = 0$. If it is empty, we return $-1$. Otherwise, we return $q[\textit{front}]$.

When calling the `Rear` method, we first check if the queue is empty, i.e., $\textit{size} = 0$. If it is empty, we return $-1$. Otherwise, we return $q[(\textit{front} + \textit{size} - 1) \bmod k]$.

When calling the `isEmpty` method, we simply check if $\textit{size} = 0$.

When calling the `isFull` method, we simply check if $\textit{size} = k$.

In terms of time complexity, the above operations all have a time complexity of $O(1)$. The space complexity is $O(k)$.

### C++20 solution

```cpp
class MyCircularQueue {
private:
    int front;
    int size;
    int capacity;
    vector<int> q;

public:
    MyCircularQueue(int k) {
        capacity = k;
        q = vector<int>(k);
        front = size = 0;
    }

    bool enQueue(int value) {
        if (isFull()) return false;
        int idx = (front + size) % capacity;
        q[idx] = value;
        ++size;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;
        front = (front + 1) % capacity;
        --size;
        return true;
    }

    int Front() {
        if (isEmpty()) return -1;
        return q[front];
    }

    int Rear() {
        if (isEmpty()) return -1;
        int idx = (front + size - 1) % capacity;
        return q[idx];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }
};
```

---

<a id="lc-641"></a>
## 33. LC 641 — Design Circular Deque (Medium)

[Official problem](https://leetcode.com/problems/design-circular-deque) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0641.Design%20Circular%20Deque/README_EN.md)

### Problem description

Design your implementation of the circular double-ended queue (deque).

Implement the `MyCircularDeque` class:

- `MyCircularDeque(int k)` Initializes the deque with a maximum size of `k`.

- `boolean insertFront()` Adds an item at the front of Deque. Returns `true` if the operation is successful, or `false` otherwise.

- `boolean insertLast()` Adds an item at the rear of Deque. Returns `true` if the operation is successful, or `false` otherwise.

- `boolean deleteFront()` Deletes an item from the front of Deque. Returns `true` if the operation is successful, or `false` otherwise.

- `boolean deleteLast()` Deletes an item from the rear of Deque. Returns `true` if the operation is successful, or `false` otherwise.

- `int getFront()` Returns the front item from the Deque. Returns `-1` if the deque is empty.

- `int getRear()` Returns the last item from Deque. Returns `-1` if the deque is empty.

- `boolean isEmpty()` Returns `true` if the deque is empty, or `false` otherwise.

- `boolean isFull()` Returns `true` if the deque is full, or `false` otherwise.

### Constraints

- `1 <= k <= 1000`

- `0 <= value <= 1000`

- At most `2000` calls will be made to `insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, `isFull`.

### Approach and complexity

We can use an array to implement the circular deque. We maintain a pointer $\textit{front}$ pointing to the front of the queue, a variable $\textit{size}$ representing the number of elements in the queue, and a variable $\textit{capacity}$ representing the queue's capacity. We use an array $q$ to store the elements.

When $\textit{insertFront}$ is called, we first check if the queue is full; if so, return $\textit{false}$. Otherwise, we move $\textit{front}$ one position forward (using modular arithmetic for circular wrapping), insert the new element at $\textit{front}$, and increment $\textit{size}$ by 1.

When $\textit{insertLast}$ is called, we first check if the queue is full; if so, return $\textit{false}$. Otherwise, we compute the insertion position (using $\textit{front}$ and $\textit{size}$), insert the new element there, and increment $\textit{size}$ by 1.

When $\textit{deleteFront}$ is called, we first check if the queue is empty; if so, return $\textit{false}$. Otherwise, we move $\textit{front}$ one position backward (using modular arithmetic for circular wrapping) and decrement $\textit{size}$ by 1.

When $\textit{deleteLast}$ is called, we first check if the queue is empty; if so, return $\textit{false}$. Otherwise, we decrement $\textit{size}$ by 1.

When $\textit{getFront}$ is called, we first check if the queue is empty; if so, return $-1$. Otherwise, we return $q[\textit{front}]$.

When $\textit{getRear}$ is called, we first check if the queue is empty; if so, return $-1$. Otherwise, we compute the position of the rear element (using $\textit{front}$ and $\textit{size}$) and return the element at that position.

When $\textit{isEmpty}$ is called, we check whether $\textit{size}$ equals $0$.

When $\textit{isFull}$ is called, we check whether $\textit{size}$ equals $\textit{capacity}$.

All operations above have a time complexity of $O(1)$ and a space complexity of $O(k)$, where $k$ is the capacity of the deque.

### C++20 solution

```cpp
class MyCircularDeque {
public:
    vector<int> q;
    int front = 0;
    int size = 0;
    int capacity = 0;

    MyCircularDeque(int k) {
        q.assign(k, 0);
        capacity = k;
    }

    bool insertFront(int value) {
        if (isFull()) {
            return false;
        }
        if (!isEmpty()) {
            front = (front - 1 + capacity) % capacity;
        }
        q[front] = value;
        ++size;
        return true;
    }

    bool insertLast(int value) {
        if (isFull()) {
            return false;
        }
        int idx = (front + size) % capacity;
        q[idx] = value;
        ++size;
        return true;
    }

    bool deleteFront() {
        if (isEmpty()) {
            return false;
        }
        front = (front + 1) % capacity;
        --size;
        return true;
    }

    bool deleteLast() {
        if (isEmpty()) {
            return false;
        }
        --size;
        return true;
    }

    int getFront() {
        return isEmpty() ? -1 : q[front];
    }

    int getRear() {
        return isEmpty() ? -1 : q[(front + size - 1) % capacity];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }
};
```

---

<a id="lc-239"></a>
## 34. LC 239 — Sliding Window Maximum (Hard)

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

<a id="lc-1438"></a>
## 35. LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (Medium)

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

<a id="lc-862"></a>
## 36. LC 862 — Shortest Subarray with Sum at Least K (Hard)

[Official problem](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0862.Shortest%20Subarray%20with%20Sum%20at%20Least%20K/README_EN.md)

### Problem description

Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty **subarray** of `nums` with a sum of at least `k`. If there is no such **subarray**, return `-1`.

A **subarray** is a **contiguous** part of an array.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^5 <= nums[i] <= 10^5`

- `1 <= k <= 10^9`

### Approach and complexity

Prefix sums turn the goal into P[right]−P[left]≥k. Keep candidate prefix indices in increasing prefix-value order. Pop qualifying fronts to improve the answer and dominated backs because a later, smaller prefix is always better.

Time O(n); auxiliary space O(n). Use 64-bit prefix sums.

### C++20 solution

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long> s(n + 1);
        for (int i = 0; i < n; ++i) s[i + 1] = s[i] + nums[i];
        deque<int> q;
        int ans = n + 1;
        for (int i = 0; i <= n; ++i) {
            while (!q.empty() && s[i] - s[q.front()] >= k) {
                ans = min(ans, i - q.front());
                q.pop_front();
            }
            while (!q.empty() && s[q.back()] >= s[i]) q.pop_back();
            q.push_back(i);
        }
        return ans > n ? -1 : ans;
    }
};
```

---

<a id="lc-1696"></a>
## 37. LC 1696 — Jump Game VI (Medium)

[Official problem](https://leetcode.com/problems/jump-game-vi) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1696.Jump%20Game%20VI/README_EN.md)

### Problem description

You are given a **0-indexed** integer array `nums` and an integer `k`.

You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. That is, you can jump from index `i` to any index in the range `[i + 1, min(n - 1, i + k)]` **inclusive**.

You want to reach the last index of the array (index `n - 1`). Your **score** is the **sum** of all `nums[j]` for each index `j` you visited in the array.

Return the **maximum score** you can get.

### Constraints

- `1 <= nums.length, k <= 10^5`

- `-10^4 <= nums[i] <= 10^4`

### Approach and complexity

Keep only reachable indices with decreasing best scores. The front supplies the maximum score among the last k positions. Drop expired fronts and dominated backs; each index enters and leaves once. Store scores directly in the deque to avoid an n-element DP array.

Time O(n); auxiliary space O(min(n,k+1)).

### C++20 solution

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        deque<pair<int, int>> candidates;
        int score = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            while (!candidates.empty() && candidates.front().first < i - k) candidates.pop_front();
            score = nums[i] + (candidates.empty() ? 0 : candidates.front().second);
            while (!candidates.empty() && candidates.back().second <= score) candidates.pop_back();
            candidates.emplace_back(i, score);
        }
        return score;
    }
};
```

---

<a id="lc-2073"></a>
## 38. LC 2073 — Time Needed to Buy Tickets (Easy)

[Official problem](https://leetcode.com/problems/time-needed-to-buy-tickets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2000-2099/2073.Time%20Needed%20to%20Buy%20Tickets/README_EN.md)

### Problem description

There are `n` people in a line queuing to buy tickets, where the `0^th` person is at the **front** of the line and the `(n - 1)^th` person is at the **back** of the line.

You are given a **0-indexed** integer array `tickets` of length `n` where the number of tickets that the `i^th` person would like to buy is `tickets[i]`.

Each person takes **exactly 1 second** to buy a ticket. A person can only buy **1 ticket at a time** and has to go back to **the end** of the line (which happens **instantaneously**) in order to buy more tickets. If a person does not have any tickets left to buy, the person will **leave **the line.

Return the **time taken** for the person **initially** at position **k**** **(0-indexed) to finish buying tickets.

### Constraints

- `n == tickets.length`

- `1 <= n <= 100`

- `1 <= tickets[i] <= 100`

- `0 <= k < n`

### Approach and complexity

According to the problem description, when the $k^{th}$ person finishes buying tickets, all the people in front of the $k^{th}$ person will not buy more tickets than the $k^{th}$ person, and all the people behind the $k^{th}$ person will not buy more tickets than the $k^{th}$ person minus $1$.

Therefore, we can traverse the entire queue. For the $i^{th}$ person, if $i \leq k$, the time to buy tickets is $\min(\textit{tickets}[i], \textit{tickets}[k])$; otherwise, the time to buy tickets is $\min(\textit{tickets}[i], \textit{tickets}[k] - 1)$. We sum the buying time for all people to get the result.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the queue.

### C++20 solution

```cpp
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int ans = 0;
        for (int i = 0; i < tickets.size(); ++i) {
            ans += min(tickets[i], i <= k ? tickets[k] : tickets[k] - 1);
        }
        return ans;
    }
};
```

---

<a id="lc-649"></a>
## 39. LC 649 — Dota2 Senate (Medium)

[Official problem](https://leetcode.com/problems/dota2-senate) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0649.Dota2%20Senate/README_EN.md)

### Problem description

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise **one** of the two rights:

- **Ban one senator's right:** A senator can make another senator lose all his rights in this and all the following rounds.

- **Announce the victory:** If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string `senate` representing each senator's party belonging. The character `'R'` and `'D'` represent the Radiant party and the Dire party. Then if there are `n` senators, the size of the given string will be `n`.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be `"Radiant"` or `"Dire"`.

### Constraints

- `n == senate.length`

- `1 <= n <= 10^4`

- `senate[i]` is either `'R'` or `'D'`.

### Approach and complexity

We create two queues $qr$ and $qd$ to record the indices of the Radiant and Dire senators, respectively. Then we start the simulation, where in each round we dequeue one senator from each queue and perform different operations based on their factions:

- If the Radiant senator's index is less than the Dire senator's index, the Radiant senator can permanently ban the voting rights of the Dire senator. We add $n$ to the Radiant senator's index and enqueue it back to the end of the queue, indicating that this senator will participate in the next round of voting.
- If the Dire senator's index is less than the Radiant senator's index, the Dire senator can permanently ban the voting rights of the Radiant senator. We add $n$ to the Dire senator's index and enqueue it back to the end of the queue, indicating that this senator will participate in the next round of voting.

Finally, when there are only senators from one faction left in the queues, the senators from that faction win.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of senators.

### C++20 solution

```cpp
class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.size();
        queue<int> qr;
        queue<int> qd;
        for (int i = 0; i < n; ++i) {
            if (senate[i] == 'R') {
                qr.push(i);
            } else {
                qd.push(i);
            }
        }
        while (!qr.empty() && !qd.empty()) {
            int r = qr.front();
            int d = qd.front();
            qr.pop();
            qd.pop();
            if (r < d) {
                qr.push(r + n);
            } else {
                qd.push(d + n);
            }
        }
        return qr.empty() ? "Dire" : "Radiant";
    }
};
```

---

<a id="lc-1700"></a>
## 40. LC 1700 — Number of Students Unable to Eat Lunch (Easy)

[Official problem](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1700.Number%20of%20Students%20Unable%20to%20Eat%20Lunch/README_EN.md)

### Problem description

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

- If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue.

- Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `i^​​​​​​th` sandwich in the stack (`i = 0` is the top of the stack) and `students[j]` is the preference of the `j^​​​​​​th` student in the initial queue (`j = 0` is the front of the queue). Return the number of students that are unable to eat.

### Constraints

- `1 <= students.length, sandwiches.length <= 100`

- `students.length == sandwiches.length`

- `sandwiches[i]` is `0` or `1`.

- `students[i]` is `0` or `1`.

### Approach and complexity

We observe that the positions of the students can be adjusted, but the positions of the sandwiches cannot be adjusted. That is to say, if the sandwich in front is not taken, then all the sandwiches behind cannot be taken.

Therefore, we first use a counter $\textit{cnt}$ to count the types of sandwiches that students like and their corresponding quantities.

Then we traverse the sandwiches. If we cannot find a student who likes this sandwich in $\textit{cnt}$, it means that the sandwiches behind cannot be taken, and we return the current number of remaining students.

If the traversal is over, it means that all students have sandwiches to eat, and we return $0$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of sandwiches.

### C++20 solution

```cpp
class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int cnt[2] = {0};
        for (int& v : students) ++cnt[v];
        for (int& v : sandwiches) {
            if (cnt[v]-- == 0) {
                return cnt[v ^ 1];
            }
        }
        return 0;
    }
};
```

---

<a id="lc-1823"></a>
## 41. LC 1823 — Find the Winner of the Circular Game (Medium)

[Official problem](https://leetcode.com/problems/find-the-winner-of-the-circular-game) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1823.Find%20the%20Winner%20of%20the%20Circular%20Game/README_EN.md)

### Problem description

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the `i^th` friend brings you to the `(i+1)^th` friend for `1 <= i < n`, and moving clockwise from the `n^th` friend brings you to the `1^st` friend.

The rules of the game are as follows:

- **Start** at the `1^st` friend.

- Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and may count some friends more than once.

- The last friend you counted leaves the circle and loses the game.

- If there is still more than one friend in the circle, go back to step `2` **starting** from the friend **immediately clockwise** of the friend who just lost and repeat.

- Else, the last friend in the circle wins the game.

Given the number of friends, `n`, and an integer `k`, return the winner of the game.

### Constraints

- `1 <= k <= n <= 500`

**Follow up:**

Could you solve this problem in linear time with constant space?

### Approach and complexity

Let survivor be the zero-based winner for a circle of size i−1. Removing the kth person in a size-i circle shifts the smaller circle’s origin by k, so the new winner is (survivor+k)%i. Build upward from size one, then convert to one-based indexing.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int findTheWinner(int n, int k) {
        int survivor = 0;
        for (int size = 2; size <= n; ++size) survivor = (survivor + k) % size;
        return survivor + 1;
    }
};
```

---

<a id="lc-950"></a>
## 42. LC 950 — Reveal Cards In Increasing Order (Medium)

[Official problem](https://leetcode.com/problems/reveal-cards-in-increasing-order) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0950.Reveal%20Cards%20In%20Increasing%20Order/README_EN.md)

### Problem description

You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on the `i^th` card is `deck[i]`.

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

- Take the top card of the deck, reveal it, and take it out of the deck.

- If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.

- If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing order.

**Note** that the first entry in the answer is considered to be the top of the deck.

### Constraints

- `1 <= deck.length <= 1000`

- `1 <= deck[i] <= 10^6`

- All the values of `deck` are **unique**.

### Approach and complexity

Sort cards descending and reverse the reveal process with a deque: move the final card to the front, then prepend the next larger-to-smaller card. Reversing each forward operation constructs the unique required arrangement.

Time O(n log n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.rbegin(), deck.rend());
        deque<int> q;
        for (int v : deck) {
            if (!q.empty()) {
                q.push_front(q.back());
                q.pop_back();
            }
            q.push_front(v);
        }
        return vector<int>(q.begin(), q.end());
    }
};
```

---

<a id="lc-994"></a>
## 43. LC 994 — Rotting Oranges (Medium)

[Official problem](https://leetcode.com/problems/rotting-oranges) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0994.Rotting%20Oranges/README_EN.md)

### Problem description

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,

- `1` representing a fresh orange, or

- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

### Constraints

- `m == grid.length`

- `n == grid[i].length`

- `1 <= m, n <= 10`

- `grid[i][j]` is `0`, `1`, or `2`.

### Approach and complexity

First, we traverse the entire grid once, count the number of fresh oranges, denoted as $\textit{cnt}$, and add the coordinates of all rotten oranges to the queue $q$.

Next, we perform a breadth-first search. In each round of the search, we let all the rotten oranges in the queue rot the fresh oranges in four directions, until the queue is empty or the number of fresh oranges is $0$.

Finally, if the number of fresh oranges is $0$, we return the current round number, otherwise, we return $-1$.

The time complexity is $O(mn)$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns of the grid, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> q;
        int cnt = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++cnt;
                } else if (grid[i][j] == 2) {
                    q.emplace(i, j);
                }
            }
        }
        const int dirs[5] = {-1, 0, 1, 0, -1};
        for (int ans = 1; q.size() && cnt; ++ans) {
            for (int k = q.size(); k; --k) {
                auto [i, j] = q.front();
                q.pop();
                for (int d = 0; d < 4; ++d) {
                    int x = i + dirs[d], y = j + dirs[d + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                        grid[x][y] = 2;
                        q.emplace(x, y);
                        if (--cnt == 0) {
                            return ans;
                        }
                    }
                }
            }
        }
        return cnt > 0 ? -1 : 0;
    }
};
```

---

<a id="lc-102"></a>
## 44. LC 102 — Binary Tree Level Order Traversal (Medium)

[Official problem](https://leetcode.com/problems/binary-tree-level-order-traversal) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0102.Binary%20Tree%20Level%20Order%20Traversal/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- `-1000 <= Node.val <= 1000`

### Approach and complexity

We can use the BFS method to solve this problem. First, enqueue the root node, then continuously perform the following operations until the queue is empty:

- Traverse all nodes in the current queue, store their values in a temporary array $t$, and then enqueue their child nodes.
- Store the temporary array $t$ in the answer array.

Finally, return the answer array.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (!root) return ans;
        queue<TreeNode*> q{{root}};
        while (!q.empty()) {
            vector<int> t;
            for (int n = q.size(); n; --n) {
                auto node = q.front();
                q.pop();
                t.push_back(node->val);
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            ans.push_back(t);
        }
        return ans;
    }
};
```

---

<a id="lc-199"></a>
## 45. LC 199 — Binary Tree Right Side View (Medium)

[Official problem](https://leetcode.com/problems/binary-tree-right-side-view) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0199.Binary%20Tree%20Right%20Side%20View/README_EN.md)

### Problem description

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`.

- `-100 <= Node.val <= 100`

### Approach and complexity

We can use breadth-first search (BFS) and define a queue $q$ to store the nodes. We start by putting the root node into the queue. Each time, we take out all the nodes of the current level from the queue. For the current node, we first check if the right subtree exists; if it does, we put the right subtree into the queue. Then, we check if the left subtree exists; if it does, we put the left subtree into the queue. This way, the first node taken out from the queue each time is the rightmost node of that level.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if (!root) {
            return ans;
        }
        queue<TreeNode*> q{{root}};
        while (q.size()) {
            ans.push_back(q.front()->val);
            for (int k = q.size(); k; --k) {
                auto node = q.front();
                q.pop();
                if (node->right) {
                    q.push(node->right);
                }
                if (node->left) {
                    q.push(node->left);
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-542"></a>
## 46. LC 542 — 01 Matrix (Medium)

[Official problem](https://leetcode.com/problems/01-matrix) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0542.01%20Matrix/README_EN.md)

### Problem description

Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.

The distance between two cells sharing a common edge is `1`.

### Constraints

- `m == mat.length`

- `n == mat[i].length`

- `1 <= m, n <= 10^4`

- `1 <= m * n <= 10^4`

- `mat[i][j]` is either `0` or `1`.

- There is at least one `0` in `mat`.

**Note:** This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

### Approach and complexity

We create a matrix $\textit{ans}$ of the same size as $\textit{mat}$ and initialize all elements to $-1$.

Then, we traverse $\textit{mat}$, adding the coordinates $(i, j)$ of all $0$ elements to the queue $q$, and setting $\textit{ans}[i][j]$ to $0$.

Next, we use Breadth-First Search (BFS), removing an element $(i, j)$ from the queue and traversing its four directions. If the element in that direction $(x, y)$ satisfies $0 \leq x < m$, $0 \leq y < n$ and $\textit{ans}[x][y] = -1$, then we set $\textit{ans}[x][y]$ to $\textit{ans}[i][j] + 1$ and add $(x, y)$ to the queue $q$.

Finally, we return $\textit{ans}$.

The time complexity is $O(mn)$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns in the matrix $\textit{mat}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> ans(m, vector<int>(n, -1));
        queue<pair<int, int>> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 0) {
                    ans[i][j] = 0;
                    q.emplace(i, j);
                }
            }
        }
        vector<int> dirs = {-1, 0, 1, 0, -1};
        while (!q.empty()) {
            auto p = q.front();
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int x = p.first + dirs[i];
                int y = p.second + dirs[i + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && ans[x][y] == -1) {
                    ans[x][y] = ans[p.first][p.second] + 1;
                    q.emplace(x, y);
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-752"></a>
## 47. LC 752 — Open the Lock (Medium)

[Official problem](https://leetcode.com/problems/open-the-lock) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0752.Open%20the%20Lock/README_EN.md)

### Problem description

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the 4 wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

### Constraints

- `1 <= deadends.length <= 500`

- `deadends[i].length == 4`

- `target.length == 4`

- target **will not be** in the list `deadends`.

- `target` and `deadends[i]` consist of digits only.

### Approach and complexity

BFS over the 10⁴ lock states explores all one-wheel moves. Mark deadends and visited combinations so each reachable state is processed once; the first target visit is shortest.

Time and space O(10⁴) for this fixed four-wheel lock, including state storage; string operations have fixed length four.

### C++20 solution

```cpp
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> s(deadends.begin(), deadends.end());
        if (s.count("0000")) return -1;
        if (target == "0000") return 0;
        queue<string> q{{"0000"}};
        s.insert("0000");
        int ans = 0;
        while (!q.empty()) {
            ++ans;
            for (int n = q.size(); n > 0; --n) {
                string p = q.front();
                q.pop();
                for (string t : next(p)) {
                    if (target == t) return ans;
                    if (!s.count(t)) {
                        q.push(t);
                        s.insert(t);
                    }
                }
            }
        }
        return -1;
    }

    vector<string> next(string& t) {
        vector<string> res;
        for (int i = 0; i < 4; ++i) {
            char c = t[i];
            t[i] = c == '0' ? '9' : (char) (c - 1);
            res.push_back(t);
            t[i] = c == '9' ? '0' : (char) (c + 1);
            res.push_back(t);
            t[i] = c;
        }
        return res;
    }
};
```

---

<a id="lc-127"></a>
## 48. LC 127 — Word Ladder (Hard)

[Official problem](https://leetcode.com/problems/word-ladder) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0127.Word%20Ladder/README_EN.md)

### Problem description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:

- Every adjacent pair of words differs by a single letter.

- Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.

- `s_k == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the **number of words** in the **shortest transformation sequence** from `beginWord` to `endWord`, or `0` if no such sequence exists.

### Constraints

- `1 <= beginWord.length <= 10`

- `endWord.length == beginWord.length`

- `1 <= wordList.length <= 5000`

- `wordList[i].length == beginWord.length`

- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.

- `beginWord != endWord`

- All the words in `wordList` are **unique**.

### Approach and complexity

Expand the smaller frontier of a bidirectional BFS and remove visited words. The first meeting connects two shortest distances; expanding the smaller frontier usually reduces explored states.

Worst-case expected time O(N·26·L²), space O(NL), for N dictionary words of length L including string hashing/copying; bidirectional search improves typical exploration, not this worst-case bound.

### C++20 solution

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> words(wordList.begin(), wordList.end());
        if (!words.count(endWord)) return 0;
        queue<string> q1{{beginWord}};
        queue<string> q2{{endWord}};
        unordered_map<string, int> m1;
        unordered_map<string, int> m2;
        m1[beginWord] = 0;
        m2[endWord] = 0;
        while (!q1.empty() && !q2.empty()) {
            int t = q1.size() <= q2.size() ? extend(m1, m2, q1, words) : extend(m2, m1, q2, words);
            if (t != -1) return t + 1;
        }
        return 0;
    }

    int extend(unordered_map<string, int>& m1, unordered_map<string, int>& m2, queue<string>& q, unordered_set<string>& words) {
        for (int i = q.size(); i > 0; --i) {
            string s = q.front();
            int step = m1[s];
            q.pop();
            for (int j = 0; j < s.size(); ++j) {
                char ch = s[j];
                for (char k = 'a'; k <= 'z'; ++k) {
                    s[j] = k;
                    if (!words.count(s) || m1.count(s)) continue;
                    if (m2.count(s)) return step + 1 + m2[s];
                    m1[s] = step + 1;
                    q.push(s);
                }
                s[j] = ch;
            }
        }
        return -1;
    }
};
```

---

<a id="lc-210"></a>
## 49. LC 210 — Course Schedule II (Medium)

[Official problem](https://leetcode.com/problems/course-schedule-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0210.Course%20Schedule%20II/README_EN.md)

### Problem description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

### Constraints

- `1 <= numCourses <= 2000`

- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`

- `prerequisites[i].length == 2`

- `0 <= a_i, b_i < numCourses`

- `a_i != b_i`

- All the pairs `[a_i, b_i]` are **distinct**.

### Approach and complexity

Kahn’s topological sort starts with all zero-indegree courses. Removing a course releases its outgoing prerequisites; process each edge once. Fewer than n emitted nodes means a directed cycle.

Time O(V+E); auxiliary space O(V+E).

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        vector<int> indeg(numCourses);
        for (auto& p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].push_back(a);
            ++indeg[a];
        }
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.push(i);
            }
        }
        vector<int> ans;
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            ans.push_back(i);
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.push(j);
                }
            }
        }
        return ans.size() == numCourses ? ans : vector<int>();
    }
};
```

---

<a id="lc-2390"></a>
## 50. LC 2390 — Removing Stars From a String (Medium)

[Official problem](https://leetcode.com/problems/removing-stars-from-a-string) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2390.Removing%20Stars%20From%20a%20String/README_EN.md)

### Problem description

You are given a string `s`, which contains stars `*`.

In one operation, you can:

- Choose a star in `s`.

- Remove the closest **non-star** character to its **left**, as well as remove the star itself.

Return the string after **all** stars have been removed.

**Note:**

- The input will be generated such that the operation is always possible.

- It can be shown that the resulting string will always be unique.

### Constraints

- `1 <= s.length <= 10^5`

- `s` consists of lowercase English letters and stars `*`.

- The operation above can be performed on `s`.

### Approach and complexity

We can use a stack to simulate the operation process. Traverse the string $s$, and if the current character is not an asterisk, push it onto the stack; if the current character is an asterisk, pop the top element from the stack.

Finally, concatenate the elements in the stack into a string and return it.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $s$.

### C++20 solution

```cpp
class Solution {
public:
    string removeStars(string s) {
        string ans;
        for (char c : s) {
            if (c == '*') {
                ans.pop_back();
            } else {
                ans.push_back(c);
            }
        }
        return ans;
    }
};
```
