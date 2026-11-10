# 3. Linked List — C++20 solutions

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

1. [LC 206 — Reverse Linked List](#lc-206)
2. [LC 21 — Merge Two Sorted Lists](#lc-21)
3. [LC 141 — Linked List Cycle](#lc-141)
4. [LC 142 — Linked List Cycle II](#lc-142)
5. [LC 19 — Remove Nth Node From End of List](#lc-19)
6. [LC 2 — Add Two Numbers](#lc-2)
7. [LC 23 — Merge k Sorted Lists](#lc-23)
8. [LC 25 — Reverse Nodes in k-Group](#lc-25)
9. [LC 143 — Reorder List](#lc-143)
10. [LC 234 — Palindrome Linked List](#lc-234)
11. [LC 160 — Intersection of Two Linked Lists](#lc-160)
12. [LC 876 — Middle of the Linked List](#lc-876)
13. [LC 83 — Remove Duplicates from Sorted List](#lc-83)
14. [LC 82 — Remove Duplicates from Sorted List II](#lc-82)
15. [LC 92 — Reverse Linked List II](#lc-92)
16. [LC 24 — Swap Nodes in Pairs](#lc-24)
17. [LC 61 — Rotate List](#lc-61)
18. [LC 86 — Partition List](#lc-86)
19. [LC 138 — Copy List with Random Pointer](#lc-138)
20. [LC 146 — LRU Cache](#lc-146)
21. [LC 147 — Insertion Sort List](#lc-147)
22. [LC 148 — Sort List](#lc-148)
23. [LC 203 — Remove Linked List Elements](#lc-203)
24. [LC 237 — Delete Node in a Linked List](#lc-237)
25. [LC 328 — Odd Even Linked List](#lc-328)
26. [LC 430 — Flatten a Multilevel Doubly Linked List](#lc-430)
27. [LC 707 — Design Linked List](#lc-707)
28. [LC 725 — Split Linked List in Parts](#lc-725)
29. [LC 817 — Linked List Components](#lc-817)
30. [LC 1019 — Next Greater Node In Linked List](#lc-1019)
31. [LC 1171 — Remove Zero Sum Consecutive Nodes from Linked List](#lc-1171)
32. [LC 1721 — Swapping Nodes in a Linked List](#lc-1721)
33. [LC 1669 — Merge In Between Linked Lists](#lc-1669)
34. [LC 2095 — Delete the Middle Node of a Linked List](#lc-2095)
35. [LC 2130 — Maximum Twin Sum of a Linked List](#lc-2130)
36. [LC 2181 — Merge Nodes in Between Zeros](#lc-2181)
37. [LC 2487 — Remove Nodes From Linked List](#lc-2487)
38. [LC 2816 — Double a Number Represented as a Linked List](#lc-2816)
39. [LC 2807 — Insert Greatest Common Divisors in Linked List](#lc-2807)
40. [LC 445 — Add Two Numbers II](#lc-445)
41. [LC 369 — Plus One Linked List](#lc-369)
42. [LC 708 — Insert into a Sorted Circular Linked List](#lc-708)
43. [LC 426 — Convert Binary Search Tree to Sorted Doubly Linked List](#lc-426)
44. [LC 109 — Convert Sorted List to Binary Search Tree](#lc-109)
45. [LC 114 — Flatten Binary Tree to Linked List](#lc-114)
46. [LC 116 — Populating Next Right Pointers in Each Node](#lc-116)
47. [LC 117 — Populating Next Right Pointers in Each Node II](#lc-117)
48. [LC 622 — Design Circular Queue](#lc-622)
49. [LC 641 — Design Circular Deque](#lc-641)
50. [LC 460 — LFU Cache](#lc-460)

---

<a id="lc-206"></a>
## 1. LC 206 — Reverse Linked List (Easy)

[Official problem](https://leetcode.com/problems/reverse-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0206.Reverse%20Linked%20List/README_EN.md)

### Problem description

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

### Constraints

- The number of nodes in the list is the range `[0, 5000]`.

- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

### Approach and complexity

We create a dummy node $\textit{dummy}$, then traverse the linked list and insert each node after the $\textit{dummy}$ node. After traversal, return $\textit{dummy}.\textit{next}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* dummy = new ListNode();
        ListNode* curr = head;
        while (curr) {
            ListNode* next = curr->next;
            curr->next = dummy->next;
            dummy->next = curr;
            curr = next;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-21"></a>
## 2. LC 21 — Merge Two Sorted Lists (Easy)

[Official problem](https://leetcode.com/problems/merge-two-sorted-lists) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0021.Merge%20Two%20Sorted%20Lists/README_EN.md)

### Problem description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Constraints

- The number of nodes in both lists is in the range `[0, 50]`.

- `-100 <= Node.val <= 100`

- Both `list1` and `list2` are sorted in **non-decreasing** order.

### Approach and complexity

We can also use iteration to implement the merging of two sorted linked lists.

First, we define a dummy head node $\textit{dummy}$, then loop through the two linked lists, compare the head nodes of the two linked lists, add the smaller node to the end of $\textit{dummy}$, until one of the linked lists is empty, then add the remaining part of the other linked list to the end of $\textit{dummy}$.

Finally, return $\textit{dummy}.\textit{next}$.

The time complexity is $O(m + n)$, and the space complexity is $O(1)$, where $m$ and $n$ are the lengths of the two linked lists respectively.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                curr->next = list1;
                list1 = list1->next;
            } else {
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
        }
        curr->next = list1 ? list1 : list2;
        return dummy->next;
    }
};
```

---

<a id="lc-141"></a>
## 3. LC 141 — Linked List Cycle (Easy)

[Official problem](https://leetcode.com/problems/linked-list-cycle) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0141.Linked%20List%20Cycle/README_EN.md)

### Problem description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Constraints

- The number of the nodes in the list is in the range `[0, 10^4]`.

- `-10^5 <= Node.val <= 10^5`

- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

### Approach and complexity

We define two pointers, $\textit{fast}$ and $\textit{slow}$, both initially pointing to $\textit{head}$.

The fast pointer moves two steps at a time, and the slow pointer moves one step at a time, in a continuous loop. When the fast and slow pointers meet, it indicates that there is a cycle in the linked list. If the loop ends without the pointers meeting, it indicates that there is no cycle in the linked list.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the linked list.

### C++20 solution

```cpp
class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
};
```

---

<a id="lc-142"></a>
## 4. LC 142 — Linked List Cycle II (Medium)

[Official problem](https://leetcode.com/problems/linked-list-cycle-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0142.Linked%20List%20Cycle%20II/README_EN.md)

### Problem description

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. **Note that** `pos` **is not passed as a parameter**.

**Do not modify** the linked list.

### Constraints

- The number of the nodes in the list is in the range `[0, 10^4]`.

- `-10^5 <= Node.val <= 10^5`

- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

### Approach and complexity

We first use the fast and slow pointers to judge whether the linked list has a ring. If there is a ring, the fast and slow pointers will definitely meet, and the meeting node must be in the ring.

If there is no ring, the fast pointer will reach the tail of the linked list first, and return `null` directly.

If there is a ring, we then define an answer pointer $\textit{ans}$ to point to the head of the linked list, and then let $\textit{ans}$ and the slow pointer move forward together, moving one step at a time, until $\textit{ans}$ and the slow pointer meet, and the meeting node is the ring entrance node.

Why can this find the entrance node of the ring?

Let's assume that the distance from the head node of the linked list to the entrance of the ring is $x$, the distance from the entrance of the ring to the meeting node is $y$, and the distance from the meeting node to the entrance of the ring is $z$. Then the distance traveled by the slow pointer is $x + y$, and the distance traveled by the fast pointer is $x + y + k \times (y + z)$, where $k$ is the number of times the fast pointer goes around the ring.

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0142.Linked%20List%20Cycle%20II/images/linked-list-cycle-ii.png" /></p>

Because the speed of the fast pointer is twice that of the slow pointer, it is $2 \times (x + y) = x + y + k \times (y + z)$, which can be deduced that $x + y = k \times (y + z)$, that is $x = (k - 1) \times (y + z) + z$.

That is to say, if we define an answer pointer $\textit{ans}$ to point to the head of the linked list, and the $\textit{ans}$ and the slow pointer move forward together, they will definitely meet at the ring entrance.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* detectCycle(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                ListNode* ans = head;
                while (ans != slow) {
                    ans = ans->next;
                    slow = slow->next;
                }
                return ans;
            }
        }
        return nullptr;
    }
};
```

---

<a id="lc-19"></a>
## 5. LC 19 — Remove Nth Node From End of List (Medium)

[Official problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0019.Remove%20Nth%20Node%20From%20End%20of%20List/README_EN.md)

### Problem description

Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

### Constraints

- The number of nodes in the list is `sz`.

- `1 <= sz <= 30`

- `0 <= Node.val <= 100`

- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

### Approach and complexity

We define two pointers `fast` and `slow`, both initially pointing to the dummy head node of the linked list.

Next, the `fast` pointer moves forward $n$ steps first, then `fast` and `slow` pointers move forward together until the `fast` pointer reaches the end of the linked list. At this point, the node pointed to by `slow.next` is the predecessor of the $n$-th node from the end, and we can delete it.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* fast = dummy;
        ListNode* slow = dummy;
        while (n--) {
            fast = fast->next;
        }
        while (fast->next) {
            slow = slow->next;
            fast = fast->next;
        }
        slow->next = slow->next->next;
        return dummy->next;
    }
};
```

---

<a id="lc-2"></a>
## 6. LC 2 — Add Two Numbers (Medium)

[Official problem](https://leetcode.com/problems/add-two-numbers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0002.Add%20Two%20Numbers/README_EN.md)

### Problem description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.

- `0 <= Node.val <= 9`

- It is guaranteed that the list represents a number that does not have leading zeros.

### Approach and complexity

We traverse two linked lists $l_1$ and $l_2$ at the same time, and use the variable $\textit{carry}$ to indicate whether there is a carry.

Each time we traverse, we take out the current bit of the corresponding linked list, calculate the sum with the carry $\textit{carry}$, and then update the value of the carry. Then we add the current bit to the answer linked list. If both linked lists are traversed, and the carry is $0$, the traversal ends.

Finally, we return the head node of the answer linked list.

The time complexity is $O(\max (m, n))$, and the space complexity is $O(1)$, where $m$ and $n$ are the lengths of the two linked lists. We need to traverse the entire position of the two linked lists, and each position only needs $O(1)$ time.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        int carry = 0;
        ListNode* cur = &dummy;
        while (l1 || l2 || carry) {
            int s = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            carry = s / 10;
            cur->next = new ListNode(s % 10);
            cur = cur->next;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        return dummy.next;
    }
};
```

---

<a id="lc-23"></a>
## 7. LC 23 — Merge k Sorted Lists (Hard)

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

<a id="lc-25"></a>
## 8. LC 25 — Reverse Nodes in k-Group (Hard)

[Official problem](https://leetcode.com/problems/reverse-nodes-in-k-group) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0025.Reverse%20Nodes%20in%20k-Group/README_EN.md)

### Problem description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

### Constraints

- The number of nodes in the list is `n`.

- `1 <= k <= n <= 5000`

- `0 <= Node.val <= 1000`

**Follow-up:** Can you solve the problem in `O(1)` extra memory space?

### Approach and complexity

We can simulate the entire reversal process according to the problem description.

First, we define a helper function $\textit{reverse}$ to reverse a linked list. Then, we define a dummy head node $\textit{dummy}$ and set its $\textit{next}$ pointer to $\textit{head}$.

Next, we traverse the linked list, processing $k$ nodes at a time. If the remaining nodes are fewer than $k$, we do not perform the reversal. Otherwise, we extract $k$ nodes and call the $\textit{reverse}$ function to reverse these $k$ nodes. Then, we connect the reversed linked list back to the original linked list. We continue to process the next $k$ nodes until the entire linked list is traversed.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* pre = dummy;

        while (pre != nullptr) {
            ListNode* cur = pre;
            for (int i = 0; i < k; i++) {
                cur = cur->next;
                if (cur == nullptr) {
                    return dummy->next;
                }
            }

            ListNode* node = pre->next;
            ListNode* nxt = cur->next;
            cur->next = nullptr;
            pre->next = reverse(node);
            node->next = nxt;
            pre = node;
        }
        return dummy->next;
    }

private:
    ListNode* reverse(ListNode* head) {
        ListNode* dummy = new ListNode();
        ListNode* cur = head;
        while (cur != nullptr) {
            ListNode* nxt = cur->next;
            cur->next = dummy->next;
            dummy->next = cur;
            cur = nxt;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-143"></a>
## 9. LC 143 — Reorder List (Medium)

[Official problem](https://leetcode.com/problems/reorder-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0143.Reorder%20List/README_EN.md)

### Problem description

You are given the head of a singly linked-list. The list can be represented as:

L_0 → L_1 → … → L_n - 1 → L_n

Reorder the list to be on the following form:

L_0 → L_n → L_1 → L_n - 1 → L_2 → L_n - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

### Constraints

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.

- `1 <= Node.val <= 1000`

### Approach and complexity

We first use fast and slow pointers to find the midpoint of the linked list, then reverse the second half of the list, and finally merge the two halves.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* cur = slow->next;
        slow->next = nullptr;

        ListNode* pre = nullptr;
        while (cur) {
            ListNode* t = cur->next;
            cur->next = pre;
            pre = cur;
            cur = t;
        }
        cur = head;

        while (pre) {
            ListNode* t = pre->next;
            pre->next = cur->next;
            cur->next = pre;
            cur = pre->next;
            pre = t;
        }
    }
};
```

---

<a id="lc-234"></a>
## 10. LC 234 — Palindrome Linked List (Easy)

[Official problem](https://leetcode.com/problems/palindrome-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0234.Palindrome%20Linked%20List/README_EN.md)

### Problem description

Given the `head` of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

### Constraints

- The number of nodes in the list is in the range `[1, 10^5]`.

- `0 <= Node.val <= 9`

**Follow up:** Could you do it in `O(n)` time and `O(1)` space?

### Approach and complexity

We can use fast and slow pointers to find the middle of the linked list, then reverse the right half of the list. After that, we traverse both halves simultaneously, checking if the corresponding node values are equal. If any pair of values is unequal, it's not a palindrome linked list; otherwise, it is a palindrome linked list.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* pre = nullptr;
        ListNode* cur = slow->next;
        while (cur) {
            ListNode* t = cur->next;
            cur->next = pre;
            pre = cur;
            cur = t;
        }
        while (pre) {
            if (pre->val != head->val) return false;
            pre = pre->next;
            head = head->next;
        }
        return true;
    }
};
```

---

<a id="lc-160"></a>
## 11. LC 160 — Intersection of Two Linked Lists (Easy)

[Official problem](https://leetcode.com/problems/intersection-of-two-linked-lists) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0160.Intersection%20of%20Two%20Linked%20Lists/README_EN.md)

### Problem description

Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

For example, the following two linked lists begin to intersect at node `c1`:

![Problem illustration](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0160.Intersection%20of%20Two%20Linked%20Lists/images/160_statement.png)

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

**Note** that the linked lists must **retain their original structure** after the function returns.

**Custom Judge:**

The inputs to the **judge** are given as follows (your program is **not** given these inputs):

- `intersectVal` - The value of the node where the intersection occurs. This is `0` if there is no intersected node.

- `listA` - The first linked list.

- `listB` - The second linked list.

- `skipA` - The number of nodes to skip ahead in `listA` (starting from the head) to get to the intersected node.

- `skipB` - The number of nodes to skip ahead in `listB` (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, `headA` and `headB` to your program. If you correctly return the intersected node, then your solution will be **accepted**.

### Constraints

- The number of nodes of `listA` is in the `m`.

- The number of nodes of `listB` is in the `n`.

- `1 <= m, n <= 3 * 10^4`

- `1 <= Node.val <= 10^5`

- `0 <= skipA <= m`

- `0 <= skipB <= n`

- `intersectVal` is `0` if `listA` and `listB` do not intersect.

- `intersectVal == listA[skipA] == listB[skipB]` if `listA` and `listB` intersect.

**Follow up:** Could you write a solution that runs in `O(m + n)` time and use only `O(1)` memory?

### Approach and complexity

We use two pointers $a$ and $b$ to point to the heads of the two linked lists $\textit{headA}$ and $\textit{headB}$, respectively.

Traverse the linked lists simultaneously. When $a$ reaches the end of $\textit{headA}$, redirect it to the head of $\textit{headB}$. Similarly, when $b$ reaches the end of $\textit{headB}$, redirect it to the head of $\textit{headA}$.

If the two pointers meet, the node they point to is the first common node. If they do not meet, it means the two linked lists have no common nodes, and both pointers will point to `null`. Return either pointer.

The time complexity is $O(m + n)$, and the space complexity is $O(1)$, where $m$ and $n$ are the lengths of the linked lists $\textit{headA}$ and $\textit{headB}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        ListNode *a = headA, *b = headB;
        while (a != b) {
            a = a ? a->next : headB;
            b = b ? b->next : headA;
        }
        return a;
    }
};
```

---

<a id="lc-876"></a>
## 12. LC 876 — Middle of the Linked List (Easy)

[Official problem](https://leetcode.com/problems/middle-of-the-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0876.Middle%20of%20the%20Linked%20List/README_EN.md)

### Problem description

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return **the second middle** node.

### Constraints

- The number of nodes in the list is in the range `[1, 100]`.

- `1 <= Node.val <= 100`

### Approach and complexity

We define two pointers $\textit{fast}$ and $\textit{slow}$, both initially pointing to the head of the linked list.

The fast pointer $\textit{fast}$ moves two steps at a time, while the slow pointer $\textit{slow}$ moves one step at a time. When the fast pointer reaches the end of the linked list, the node pointed to by the slow pointer is the middle node.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```

---

<a id="lc-83"></a>
## 13. LC 83 — Remove Duplicates from Sorted List (Easy)

[Official problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0083.Remove%20Duplicates%20from%20Sorted%20List/README_EN.md)

### Problem description

Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list **sorted** as well.

### Constraints

- The number of nodes in the list is in the range `[0, 300]`.

- `-100 <= Node.val <= 100`

- The list is guaranteed to be **sorted** in ascending order.

### Approach and complexity

We use a pointer $\textit{cur}$ to traverse the linked list. If the element corresponding to the current $\textit{cur}$ is the same as the element corresponding to $\textit{cur}.\textit{next}$, we set the $\textit{next}$ pointer of $\textit{cur}$ to point to the next node of $\textit{cur}.\textit{next}$. Otherwise, it means that the element corresponding to $\textit{cur}$ in the linked list is not duplicated, so we can move the $\textit{cur}$ pointer to the next node.

After the traversal ends, return the head node of the linked list.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* cur = head;
        while (cur != nullptr && cur->next != nullptr) {
            if (cur->val == cur->next->val) {
                cur->next = cur->next->next;
            } else {
                cur = cur->next;
            }
        }
        return head;
    }
};
```

---

<a id="lc-82"></a>
## 14. LC 82 — Remove Duplicates from Sorted List II (Medium)

[Official problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0082.Remove%20Duplicates%20from%20Sorted%20List%20II/README_EN.md)

### Problem description

You are given the `head` of a **sorted** linked list.

Delete all nodes that have **duplicate** numbers, leaving only **distinct** numbers from the original list.

Return the linked list **sorted** as well.

### Constraints

- The number of nodes in the list is in the range `[0, 300]`.

- `-100 <= Node.val <= 100`

- The list is guaranteed to be **sorted** in ascending order.

### Approach and complexity

First, we create a dummy head node $\textit{dummy}$, and set $\textit{dummy}.\textit{next} = \textit{head}$. Then we create a pointer $\textit{pre}$ pointing to $\textit{dummy}$, and a pointer $\textit{cur}$ pointing to $\textit{head}$, and start traversing the linked list.

When the node value pointed by $\textit{cur}$ is the same as the node value pointed by $\textit{cur}.\textit{next}$, we let $\textit{cur}$ keep moving forward until the node value pointed by $\textit{cur}$ is different from the node value pointed by $\textit{cur}.\textit{next}$. At this point, we check whether $\textit{pre}.\textit{next}$ is equal to $\textit{cur}$. If they are equal, it means there are no duplicate nodes between $\textit{pre}$ and $\textit{cur}$, so we move $\textit{pre}$ to the position of $\textit{cur}$; otherwise, it means there are duplicate nodes between $\textit{pre}$ and $\textit{cur}$, so we set $\textit{pre}.\textit{next}$ to $\textit{cur}.\textit{next}$. Then we continue to move $\textit{cur}$ forward. Continue the above operation until $\textit{cur}$ is null, and the traversal ends.

Finally, return $\textit{dummy}.\textit{next}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* pre = dummy;
        ListNode* cur = head;
        while (cur) {
            while (cur->next && cur->next->val == cur->val) {
                cur = cur->next;
            }
            if (pre->next == cur) {
                pre = cur;
            } else {
                pre->next = cur->next;
            }
            cur = cur->next;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-92"></a>
## 15. LC 92 — Reverse Linked List II (Medium)

[Official problem](https://leetcode.com/problems/reverse-linked-list-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0092.Reverse%20Linked%20List%20II/README_EN.md)

### Problem description

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

### Constraints

- The number of nodes in the list is `n`.

- `1 <= n <= 500`

- `-500 <= Node.val <= 500`

- `1 <= left <= right <= n`

**Follow up:** Could you do it in one pass?

### Approach and complexity

Define a dummy head node `dummy`, pointing to the head node `head` of the linked list. Then define a pointer `pre` pointing to `dummy`. Start traversing the linked list from the dummy head node. When you traverse to the $\textit{left}$ node, point `pre` to this node. Then start traversing `right - left + 1` times from this node, and insert the nodes you traverse into the back of `pre`. Finally, return `dummy.next`.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head->next || left == right) {
            return head;
        }
        ListNode* dummy = new ListNode(0, head);
        ListNode* pre = dummy;
        for (int i = 0; i < left - 1; ++i) {
            pre = pre->next;
        }
        ListNode *p = pre, *q = pre->next;
        ListNode* cur = q;
        for (int i = 0; i < right - left + 1; ++i) {
            ListNode* t = cur->next;
            cur->next = pre;
            pre = cur;
            cur = t;
        }
        p->next = pre;
        q->next = cur;
        return dummy->next;
    }
};
```

---

<a id="lc-24"></a>
## 16. LC 24 — Swap Nodes in Pairs (Medium)

[Official problem](https://leetcode.com/problems/swap-nodes-in-pairs) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0024.Swap%20Nodes%20in%20Pairs/README_EN.md)

### Problem description

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

### Constraints

- The number of nodes in the list is in the range `[0, 100]`.

- `0 <= Node.val <= 100`

### Approach and complexity

We set a dummy head node $\textit{dummy}$, initially pointing to $\textit{head}$, and then set two pointers $\textit{pre}$ and $\textit{cur}$, initially $\textit{pre}$ points to $\textit{dummy}$, and $\textit{cur}$ points to $\textit{head}$.

Next, we traverse the linked list. Each time we need to swap the two nodes after $\textit{pre}$, so we first judge whether $\textit{cur}$ and $\textit{cur}.\textit{next}$ are empty. If they are not empty, we perform the swap, otherwise we terminate the loop.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* pre = dummy;
        ListNode* cur = head;
        while (cur && cur->next) {
            ListNode* t = cur->next;
            cur->next = t->next;
            t->next = cur;
            pre->next = t;
            pre = cur;
            cur = cur->next;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-61"></a>
## 17. LC 61 — Rotate List (Medium)

[Official problem](https://leetcode.com/problems/rotate-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0061.Rotate%20List/README_EN.md)

### Problem description

Given the `head` of a linked list, rotate the list to the right by `k` places.

### Constraints

- The number of nodes in the list is in the range `[0, 500]`.

- `-100 <= Node.val <= 100`

- `0 <= k <= 2 * 10^9`

### Approach and complexity

First, we check whether the number of nodes in the linked list is less than $2$. If so, we directly return $\textit{head}$.

Otherwise, we first count the number of nodes $n$ in the linked list, and then take the modulus of $k$ by $n$ to get the effective value of $k$.

If the effective value of $k$ is $0$, it means that the linked list does not need to be rotated, and we can directly return $\textit{head}$.

Otherwise, we use fast and slow pointers, let the fast pointer move $k$ steps first, and then let the fast and slow pointers move together until the fast pointer moves to the end of the linked list. At this time, the next node of the slow pointer is the new head node of the linked list.

Finally, we concatenate the linked list.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next) {
            return head;
        }
        ListNode* cur = head;
        int n = 0;
        while (cur) {
            ++n;
            cur = cur->next;
        }
        k %= n;
        if (k == 0) {
            return head;
        }
        ListNode* fast = head;
        ListNode* slow = head;
        while (k--) {
            fast = fast->next;
        }
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        ListNode* ans = slow->next;
        slow->next = nullptr;
        fast->next = head;
        return ans;
    }
};
```

---

<a id="lc-86"></a>
## 18. LC 86 — Partition List (Medium)

[Official problem](https://leetcode.com/problems/partition-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0086.Partition%20List/README_EN.md)

### Problem description

Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal** to `x`.

You should **preserve** the original relative order of the nodes in each of the two partitions.

### Constraints

- The number of nodes in the list is in the range `[0, 200]`.

- `-100 <= Node.val <= 100`

- `-200 <= x <= 200`

### Approach and complexity

We create two linked lists $l$ and $r$, one to store nodes less than $x$ and the other to store nodes greater than or equal to $x$. Then we concatenate them.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the original linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* l = new ListNode();
        ListNode* r = new ListNode();
        ListNode* tl = l;
        ListNode* tr = r;
        for (; head; head = head->next) {
            if (head->val < x) {
                tl->next = head;
                tl = tl->next;
            } else {
                tr->next = head;
                tr = tr->next;
            }
        }
        tr->next = nullptr;
        tl->next = r->next;
        return l->next;
    }
};
```

---

<a id="lc-138"></a>
## 19. LC 138 — Copy List with Random Pointer (Medium)

[Official problem](https://leetcode.com/problems/copy-list-with-random-pointer) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0138.Copy%20List%20with%20Random%20Pointer/README_EN.md)

### Problem description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`

- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

### Constraints

- `0 <= n <= 1000`

- `-10^4 <= Node.val <= 10^4`

- `Node.random` is `null` or is pointing to some node in the linked list.

### Approach and complexity

In Solution 1, we used an additional hash table to store the mapping between the original nodes and the copied nodes. We can also achieve this without using extra space, as follows:

1. Traverse the original linked list, and for each node, create a new node and insert it between the original node and the original node's next node.
2. Traverse the linked list again, and set the $\textit{random}$ pointer of the new node based on the $\textit{random}$ pointer of the original node.
3. Finally, split the linked list into the original linked list and the copied linked list.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return nullptr;
        }
        Node* cur = head;
        while (cur != nullptr) {
            Node* node = new Node(cur->val);
            node->next = cur->next;
            cur->next = node;
            cur = node->next;
        }
        cur = head;
        while (cur != nullptr) {
            cur->next->random = cur->random == nullptr ? nullptr : cur->random->next;
            cur = cur->next->next;
        }
        cur = head;
        Node* ans = head->next;
        while (cur->next != nullptr) {
            Node* node = cur->next;
            cur->next = node->next;
            cur = node;
        }
        return ans;
    }
};
```

---

<a id="lc-146"></a>
## 20. LC 146 — LRU Cache (Medium)

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

<a id="lc-147"></a>
## 21. LC 147 — Insertion Sort List (Medium)

[Official problem](https://leetcode.com/problems/insertion-sort-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0147.Insertion%20Sort%20List/README_EN.md)

### Problem description

Given the `head` of a singly linked list, sort the list using **insertion sort**, and return the sorted list's head.

The steps of the **insertion sort** algorithm:

- Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.

- At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.

- It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

![Problem illustration](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0147.Insertion%20Sort%20List/images/Insertion-sort-example-300px.gif)

### Constraints

- The number of nodes in the list is in the range `[1, 5000]`.

- `-5000 <= Node.val <= 5000`

### Approach and complexity

Maintain a sorted prefix. When the next node is already at least the prefix maximum, extend the prefix in O(1). Otherwise detach that node and insert it at the first suitable position starting at a dummy head.

Time O(n²) worst case, O(n) on already sorted input; auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode dummy(0, head);
        ListNode* tail = head;
        while (tail && tail->next) {
            ListNode* node = tail->next;
            if (tail->val <= node->val) { tail = node; continue; }
            ListNode* before = &dummy;
            while (before->next->val <= node->val) before = before->next;
            tail->next = node->next;
            node->next = before->next;
            before->next = node;
        }
        return dummy.next;
    }
};
```

---

<a id="lc-148"></a>
## 22. LC 148 — Sort List (Medium)

[Official problem](https://leetcode.com/problems/sort-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0148.Sort%20List/README_EN.md)

### Problem description

Given the `head` of a linked list, return the list after sorting it in **ascending order**.

### Constraints

- The number of nodes in the list is in the range `[0, 5 * 10^4]`.

- `-10^5 <= Node.val <= 10^5`

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?

### Approach and complexity

Merge adjacent sorted runs of lengths 1,2,4,… . Split by cutting next pointers, then merge runs by relinking their existing nodes. Each pass visits O(n) nodes; bottom-up iteration eliminates recursive stack space.

Time O(n log n); auxiliary space O(1). Mutates list links.

### C++20 solution

```cpp
class Solution {
    ListNode* split(ListNode* head, int size) {
        if (!head) return nullptr;
        for (int i = 1; i < size && head->next; ++i) head = head->next;
        ListNode* rest = head->next;
        head->next = nullptr;
        return rest;
    }
public:
    ListNode* sortList(ListNode* head) {
        int n = 0;
        for (auto p = head; p; p = p->next) ++n;
        ListNode dummy(0, head);
        for (int size = 1; size < n; size *= 2) {
            ListNode* current = dummy.next;
            ListNode* tail = &dummy;
            while (current) {
                ListNode* a = current;
                ListNode* b = split(a, size);
                current = split(b, size);
                while (a && b) {
                    ListNode*& smaller = a->val <= b->val ? a : b;
                    tail->next = smaller;
                    smaller = smaller->next;
                    tail = tail->next;
                }
                tail->next = a ? a : b;
                while (tail->next) tail = tail->next;
            }
        }
        return dummy.next;
    }
};
```

---

<a id="lc-203"></a>
## 23. LC 203 — Remove Linked List Elements (Easy)

[Official problem](https://leetcode.com/problems/remove-linked-list-elements) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0203.Remove%20Linked%20List%20Elements/README_EN.md)

### Problem description

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.

### Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.

- `1 <= Node.val <= 50`

- `0 <= val <= 50`

### Approach and complexity

A dummy predecessor makes head deletion identical to interior deletion. Unlink matching next nodes and advance only when retaining a node.

Time O(n); auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode();
        dummy->next = head;
        ListNode* p = dummy;
        while (p->next) {
            if (p->next->val == val) {
                p->next = p->next->next;
            } else {
                p = p->next;
            }
        }
        return dummy->next;
    }
};
```

---

<a id="lc-237"></a>
## 24. LC 237 — Delete Node in a Linked List (Medium)

[Official problem](https://leetcode.com/problems/delete-node-in-a-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0237.Delete%20Node%20in%20a%20Linked%20List/README_EN.md)

### Problem description

There is a singly-linked list `head` and we want to delete a node `node` in it.

You are given the node to be deleted `node`. You will **not be given access** to the first node of `head`.

All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

- The value of the given node should not exist in the linked list.

- The number of nodes in the linked list should decrease by one.

- All the values before `node` should be in the same order.

- All the values after `node` should be in the same order.

**Custom testing:**

- For the input, you should provide the entire linked list `head` and the node to be given `node`. `node` should not be the last node of the list and should be an actual node in the list.

- We will build the linked list and pass the node to your function.

- The output will be the entire list after calling your function.

### Constraints

- The number of the nodes in the given list is in the range `[2, 1000]`.

- `-1000 <= Node.val <= 1000`

- The value of each node in the list is **unique**.

- The `node` to be deleted is **in the list** and is **not a tail** node.

### Approach and complexity

We can replace the value of the current node with the value of the next node, and then delete the next node. This can achieve the purpose of deleting the current node.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```

---

<a id="lc-328"></a>
## 25. LC 328 — Odd Even Linked List (Medium)

[Official problem](https://leetcode.com/problems/odd-even-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0328.Odd%20Even%20Linked%20List/README_EN.md)

### Problem description

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

### Constraints

- The number of nodes in the linked list is in the range `[0, 10^4]`.

- `-10^6 <= Node.val <= 10^6`

### Approach and complexity

We can use two pointers $a$ and $b$ to represent the tail nodes of the odd and even nodes respectively. Initially, pointer $a$ points to the head node $\textit{head}$ of the list, and pointer $b$ points to the second node $\textit{head}.\textit{next}$ of the list. In addition, we use a pointer $c$ to point to the head node $\textit{head}.\textit{next}$ of the even nodes, which is the initial position of pointer $b$.

We traverse the list, set pointer $a$ to point to the next node of $b$, i.e., $a.\textit{next} = b.\textit{next}$, then move pointer $a$ back by one position, i.e., $a = a.\textit{next}$; set pointer $b$ to point to the next node of $a$, i.e., $b.\textit{next} = a.\textit{next}$, then move pointer $b$ back by one position, i.e., $b = b.\textit{next}$. Continue to traverse until $b$ reaches the end of the list.

Finally, we set the tail node $a$ of the odd nodes to point to the head node $c$ of the even nodes, i.e., $a.\textit{next} = c$, then return the head node $\textit{head}$ of the list.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the list, and we need to traverse the list once.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head) {
            return nullptr;
        }
        ListNode* a = head;
        ListNode *b = head->next, *c = b;
        while (b && b->next) {
            a->next = b->next;
            a = a->next;
            b->next = a->next;
            b = b->next;
        }
        a->next = c;
        return head;
    }
};
```

---

<a id="lc-430"></a>
## 26. LC 430 — Flatten a Multilevel Doubly Linked List (Medium)

[Official problem](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0430.Flatten%20a%20Multilevel%20Doubly%20Linked%20List/README_EN.md)

### Problem description

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional **child pointer**. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a **multilevel data structure** as shown in the example below.

Given the `head` of the first level of the list, **flatten** the list so that all the nodes appear in a single-level, doubly linked list. Let `curr` be a node with a child list. The nodes in the child list should appear **after** `curr` and **before** `curr.next` in the flattened list.

Return the `head` of the flattened list. The nodes in the list must have **all** of their child pointers set to `null`.

### Constraints

- The number of Nodes will not exceed `1000`.

- `1 <= Node.val <= 10^5`

**How the multilevel linked list is represented in test cases:**

We use the multilevel linked list from **Example 1** above:

1---2---3---4---5---6--NULL
|
7---8---9---10--NULL
|
11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1, 2, 3, 4, 5, 6, null]
|
[null, null, 7, 8, 9, 10, null]
|
[ null, 11, 12, null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

### Approach and complexity

Depth-first flattening splices a child list between its parent and the old next node, joining all prev/next pointers and clearing child pointers. Return the flattened tail to connect pending siblings.

Time O(n); auxiliary space O(d), where d is maximum recursion depth and may be n.

### C++20 solution

```cpp
class Solution {
public:
    Node* flatten(Node* head) {
        flattenGetTail(head);
        return head;
    }

    Node* flattenGetTail(Node* head) {
        Node* cur = head;
        Node* tail = nullptr;

        while (cur) {
            Node* next = cur->next;
            if (cur->child) {
                Node* child = cur->child;
                Node* childTail = flattenGetTail(cur->child);

                cur->child = nullptr;
                cur->next = child;
                child->prev = cur;
                childTail->next = next;

                if (next)
                    next->prev = childTail;

                tail = childTail;
            } else {
                tail = cur;
            }

            cur = next;
        }

        return tail;
    }
};
```

---

<a id="lc-707"></a>
## 27. LC 707 — Design Linked List (Medium)

[Official problem](https://leetcode.com/problems/design-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0707.Design%20Linked%20List/README_EN.md)

### Problem description

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are **0-indexed**.

Implement the `MyLinkedList` class:

- `MyLinkedList()` Initializes the `MyLinkedList` object.

- `int get(int index)` Get the value of the `index^th` node in the linked list. If the index is invalid, return `-1`.

- `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.

- `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.

- `void addAtIndex(int index, int val)` Add a node of value `val` before the `index^th` node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node **will not be inserted**.

- `void deleteAtIndex(int index)` Delete the `index^th` node in the linked list, if the index is valid.

### Constraints

- `0 <= index, val <= 1000`

- Please do not use the built-in LinkedList library.

- At most `2000` calls will be made to `get`, `addAtHead`, `addAtTail`, `addAtIndex` and `deleteAtIndex`.

### Approach and complexity

Use std::list to own nodes and links. Validate indices before traversal. Locate indexed positions from the closer end; end insertions and removals are constant-time and all allocated nodes are released automatically. This design problem supplies no ListNode type, so the implementation is fully self-contained.

get/addAtIndex/deleteAtIndex O(n) worst case, O(min(index,n−index)) traversal; addAtHead/addAtTail O(1). Persistent storage O(n).

### C++20 solution

```cpp
class MyLinkedList {
    list<int> nodes;
    list<int>::iterator locate(int index) {
        if (index <= static_cast<int>(nodes.size()) / 2) return next(nodes.begin(), index);
        return prev(nodes.end(), static_cast<int>(nodes.size()) - index);
    }
public:
    MyLinkedList() = default;
    int get(int index) {
        if (index < 0 || index >= static_cast<int>(nodes.size())) return -1;
        return *locate(index);
    }
    void addAtHead(int val) { nodes.push_front(val); }
    void addAtTail(int val) { nodes.push_back(val); }
    void addAtIndex(int index, int val) {
        index = max(0, index);
        if (index > static_cast<int>(nodes.size())) return;
        nodes.insert(locate(index), val);
    }
    void deleteAtIndex(int index) {
        if (index < 0 || index >= static_cast<int>(nodes.size())) return;
        nodes.erase(locate(index));
    }
};
```

---

<a id="lc-725"></a>
## 28. LC 725 — Split Linked List in Parts (Medium)

[Official problem](https://leetcode.com/problems/split-linked-list-in-parts) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0725.Split%20Linked%20List%20in%20Parts/README_EN.md)

### Problem description

Given the `head` of a singly linked list and an integer `k`, split the linked list into `k` consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the `k` parts.

### Constraints

- The number of nodes in the list is in the range `[0, 1000]`.

- `0 <= Node.val <= 1000`

- `1 <= k <= 50`

### Approach and complexity

First, we traverse the linked list to obtain its length $n$, and then we calculate the average length $\textit{cnt} = \lfloor \frac{n}{k} \rfloor$ and the remainder $\textit{mod} = n \bmod k$. For the first $\textit{mod}$ parts, each part has a length of $\textit{cnt} + 1$, while the lengths of the remaining parts are $\textit{cnt}$.

Next, we just need to traverse the linked list and split it into $k$ parts.

The time complexity is $O(n)$, and the space complexity is $O(k)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n = 0;
        for (ListNode* cur = head; cur != nullptr; cur = cur->next) {
            ++n;
        }
        int cnt = n / k, mod = n % k;
        vector<ListNode*> ans(k, nullptr);
        ListNode* cur = head;
        for (int i = 0; i < k && cur != nullptr; ++i) {
            ans[i] = cur;
            int m = cnt + (i < mod ? 1 : 0);
            for (int j = 1; j < m; ++j) {
                cur = cur->next;
            }
            ListNode* nxt = cur->next;
            cur->next = nullptr;
            cur = nxt;
        }
        return ans;
    }
};
```

---

<a id="lc-817"></a>
## 29. LC 817 — Linked List Components (Medium)

[Official problem](https://leetcode.com/problems/linked-list-components) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0817.Linked%20List%20Components/README_EN.md)

### Problem description

You are given the `head` of a linked list containing unique integer values and an integer array `nums` that is a subset of the linked list values.

Return the number of **connected** **components** in `nums`. A connected component is a non-empty, maximal sequence of **consecutive** nodes in the linked list such that every node's value belongs to nums.

### Constraints

- The number of nodes in the linked list is `n`.

- `1 <= n <= 10^4`

- `0 <= Node.val < n`

- All the values `Node.val` are **unique**.

- `1 <= nums.length <= n`

- `0 <= nums[i] < n`

- All the values of `nums` are **unique**.

### Approach and complexity

Store selected values in a hash set. A component ends exactly at a selected node whose next node is absent or unselected; count these ends.

Expected time O(n+k); auxiliary space O(k).

### C++20 solution

```cpp
class Solution {
public:
    int numComponents(ListNode* head, vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int ans = 0;
        while (head) {
            while (head && !s.count(head->val)) head = head->next;
            ans += head != nullptr;
            while (head && s.count(head->val)) head = head->next;
        }
        return ans;
    }
};
```

---

<a id="lc-1019"></a>
## 30. LC 1019 — Next Greater Node In Linked List (Medium)

[Official problem](https://leetcode.com/problems/next-greater-node-in-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1019.Next%20Greater%20Node%20In%20Linked%20List/README_EN.md)

### Problem description

You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `i^th` node (**1-indexed**). If the `i^th` node does not have a next greater node, set `answer[i] = 0`.

### Constraints

- The number of nodes in the list is `n`.

- `1 <= n <= 10^4`

- `1 <= Node.val <= 10^9`

### Approach and complexity

The problem requires finding the next larger node for each node in the linked list, that is, finding the first node to the right of each node in the linked list that is larger than it. We first traverse the linked list and store the values in the linked list in an array $\textit{nums}$. For each element in the array $\textit{nums}$, we just need to find the first element to its right that is larger than it. The problem of finding the next larger element can be solved using a monotonic stack.

We traverse the array $\textit{nums}$ from back to front, maintaining a stack $\textit{stk}$ that is monotonically decreasing from the bottom to the top. During the traversal, if the top element of the stack is less than or equal to the current element, we loop to pop the top element of the stack until the top element of the stack is larger than the current element or the stack is empty.

If the stack is empty at this time, it means that the current element does not have a next larger element, otherwise, the next larger element of the current element is the top element of the stack, and we update the answer array $\textit{ans}$. Then we push the current element into the stack and continue the traversal.

After the traversal is over, we return the answer array $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> nums;
        for (; head; head = head->next) {
            nums.push_back(head->val);
        }
        stack<int> stk;
        int n = nums.size();
        vector<int> ans(n);
        for (int i = n - 1; ~i; --i) {
            while (!stk.empty() && stk.top() <= nums[i]) {
                stk.pop();
            }
            if (!stk.empty()) {
                ans[i] = stk.top();
            }
            stk.push(nums[i]);
        }
        return ans;
    }
};
```

---

<a id="lc-1171"></a>
## 31. LC 1171 — Remove Zero Sum Consecutive Nodes from Linked List (Medium)

[Official problem](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1100-1199/1171.Remove%20Zero%20Sum%20Consecutive%20Nodes%20from%20Linked%20List/README_EN.md)

### Problem description

Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list. You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

### Constraints

- The given linked list will contain between `1` and `1000` nodes.

- Each node in the linked list has `-1000 <= node.val <= 1000`.

### Approach and complexity

If two prefix sums of the linked list are equal, it means that the sum of the continuous node sequence between the two prefix sums is $0$, so we can remove this part of the continuous nodes.

We first traverse the linked list and use a hash table $\textit{last}$ to record the prefix sum and the corresponding linked list node. For the same prefix sum $s$, the later node overwrites the previous node.

Next, we traverse the linked list again. If the current node $\textit{cur}$ has a prefix sum $s$ that appears in $\textit{last}$, it means that the sum of all nodes between $\textit{cur}$ and $\textit{last}[s]$ is $0$, so we directly modify the pointer of $\textit{cur}$ to $\textit{last}[s].\textit{next}$, which removes this part of the continuous nodes with a sum of $0$. We continue to traverse and delete all continuous nodes with a sum of $0$.

Finally, we return the head node of the linked list $\textit{dummy}.\textit{next}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        unordered_map<int, ListNode*> last;
        ListNode* cur = dummy;
        int s = 0;
        while (cur) {
            s += cur->val;
            last[s] = cur;
            cur = cur->next;
        }
        s = 0;
        cur = dummy;
        while (cur) {
            s += cur->val;
            cur->next = last[s]->next;
            cur = cur->next;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-1721"></a>
## 32. LC 1721 — Swapping Nodes in a Linked List (Medium)

[Official problem](https://leetcode.com/problems/swapping-nodes-in-a-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1721.Swapping%20Nodes%20in%20a%20Linked%20List/README_EN.md)

### Problem description

You are given the `head` of a linked list, and an integer `k`.

Return the head of the linked list after **swapping** the values of the `k^th` node from the beginning and the `k^th` node from the end (the list is **1-indexed**).

### Constraints

- The number of nodes in the list is `n`.

- `1 <= k <= n <= 10^5`

- `0 <= Node.val <= 100`

### Approach and complexity

We can first use a fast pointer `fast` to find the $k$th node of the linked list, and use a pointer `p` to point to it. Then, we use a slow pointer `slow` to start from the head node of the linked list, and move both pointers forward at the same time. When the fast pointer reaches the last node of the linked list, the slow pointer `slow` points to the $k$th node from the end of the linked list, and we use a pointer `q` to point to it. At this point, we only need to swap the values of `p` and `q`.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* fast = head;
        while (--k) {
            fast = fast->next;
        }
        ListNode* slow = head;
        ListNode* p = fast;
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        ListNode* q = slow;
        swap(p->val, q->val);
        return head;
    }
};
```

---

<a id="lc-1669"></a>
## 33. LC 1669 — Merge In Between Linked Lists (Medium)

[Official problem](https://leetcode.com/problems/merge-in-between-linked-lists) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1669.Merge%20In%20Between%20Linked%20Lists/README_EN.md)

### Problem description

You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively.

Remove `list1`'s nodes from the `a^th` node to the `b^th` node, and put `list2` in their place.

The blue edges and nodes in the following figure indicate the result:

![Problem illustration](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1669.Merge%20In%20Between%20Linked%20Lists/images/fig1.png)

Build the result list and return its head.

### Constraints

- `3 <= list1.length <= 10^4`

- `1 <= a <= b < list1.length - 1`

- `1 <= list2.length <= 10^4`

### Approach and complexity

We can directly simulate the operations described in the problem.

In the implementation, we use two pointers $p$ and $q$, both initially pointing to the head node of $\textit{list1}$.

Then we move pointers $p$ and $q$ forward, until pointer $p$ points to the node before the $a$-th node in $\textit{list1}$, and pointer $q$ points to the $b$-th node in $\textit{list1}$. At this point, we set the $\textit{next}$ pointer of $p$ to the head node of $\textit{list2}$, and set the $\textit{next}$ pointer of the tail node of $\textit{list2}$ to the node pointed to by the $\textit{next}$ pointer of $q$. This completes the operation required by the problem.

The time complexity is $O(m + n)$, and the space complexity is $O(1)$, where $m$ and $n$ are the lengths of $\textit{list1}$ and $\textit{list2}$ respectively.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        auto p = list1, q = list1;
        while (--a) {
            p = p->next;
        }
        while (b--) {
            q = q->next;
        }
        p->next = list2;
        while (p->next) {
            p = p->next;
        }
        p->next = q->next;
        q->next = nullptr;
        return list1;
    }
};
```

---

<a id="lc-2095"></a>
## 34. LC 2095 — Delete the Middle Node of a Linked List (Medium)

[Official problem](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2000-2099/2095.Delete%20the%20Middle%20Node%20of%20a%20Linked%20List/README_EN.md)

### Problem description

You are given the `head` of a linked list. **Delete** the **middle node**, and return the `head` of the modified linked list.

The **middle node** of a linked list of size `n` is the `⌊n / 2⌋^th` node from the start using **0-based indexing**, where `⌊x⌋` denotes the largest integer less than or equal to `x`.

- For `n` = `1`, `2`, `3`, `4`, and `5`, the middle nodes are `0`, `1`, `1`, `2`, and `2`, respectively.

### Constraints

- The number of nodes in the list is in the range `[1, 10^5]`.

- `1 <= Node.val <= 10^5`

### Approach and complexity

The fast and slow pointer technique is a common method used to solve problems related to linked lists. We can maintain two pointers, a slow pointer $\textit{slow}$ and a fast pointer $\textit{fast}$. Initially, $\textit{slow}$ points to a dummy node, whose $\textit{next}$ pointer points to the head node $\textit{head}$ of the list, while $\textit{fast}$ points to the head node $\textit{head}$.

Then, we move the slow pointer one position backward and the fast pointer two positions backward each time, until the fast pointer reaches the end of the list. At this point, the node next to the node pointed by the slow pointer is the middle node of the list. We can remove the middle node by setting the $\textit{next}$ pointer of the node pointed by the slow pointer to point to the next next node.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* slow = dummy;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        slow->next = slow->next->next;
        return dummy->next;
    }
};
```

---

<a id="lc-2130"></a>
## 35. LC 2130 — Maximum Twin Sum of a Linked List (Medium)

[Official problem](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2100-2199/2130.Maximum%20Twin%20Sum%20of%20a%20Linked%20List/README_EN.md)

### Problem description

In a linked list of size `n`, where `n` is **even**, the `i^th` node (**0-indexed**) of the linked list is known as the **twin** of the `(n-1-i)^th` node, if `0 <= i <= (n / 2) - 1`.

- For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum **is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return the **maximum twin sum** of the linked list.

### Constraints

- The number of nodes in the list is an **even** integer in the range `[2, 10^5]`.

- `1 <= Node.val <= 10^5`

### Approach and complexity

Find the midpoint, reverse the second half, and traverse the halves together. Mirrored original positions become aligned, so maximize each pair’s sum.

Time O(n); auxiliary space O(1). This implementation modifies the input links.

### C++20 solution

```cpp
class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* pa = head;
        ListNode* q = slow->next;
        slow->next = nullptr;
        ListNode* pb = reverse(q);
        int ans = 0;
        while (pa) {
            ans = max(ans, pa->val + pb->val);
            pa = pa->next;
            pb = pb->next;
        }
        return ans;
    }

    ListNode* reverse(ListNode* head) {
        ListNode* dummy = new ListNode();
        ListNode* curr = head;
        while (curr) {
            ListNode* next = curr->next;
            curr->next = dummy->next;
            dummy->next = curr;
            curr = next;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-2181"></a>
## 36. LC 2181 — Merge Nodes in Between Zeros (Medium)

[Official problem](https://leetcode.com/problems/merge-nodes-in-between-zeros) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2100-2199/2181.Merge%20Nodes%20in%20Between%20Zeros/README_EN.md)

### Problem description

You are given the `head` of a linked list, which contains a series of integers **separated** by `0`'s. The **beginning** and **end** of the linked list will have `Node.val == 0`.

For **every **two consecutive `0`'s, **merge** all the nodes lying in between them into a single node whose value is the **sum** of all the merged nodes. The modified list should not contain any `0`'s.

Return the `head` of the modified linked list.

### Constraints

- The number of nodes in the list is in the range `[3, 2 * 10^5]`.

- `0 <= Node.val <= 1000`

- There are **no** two consecutive nodes with `Node.val == 0`.

- The **beginning** and **end** of the linked list have `Node.val == 0`.

### Approach and complexity

Scan after the initial zero, accumulate each segment, and write its sum into the next available output node at each closing zero. The write position never passes unread data; terminate the compacted list after the final sum.

Time O(n); auxiliary space O(1). Mutates the input list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* write = head;
        ListNode* tail = nullptr;
        int sum = 0;
        for (auto p = head->next; p; p = p->next) {
            if (p->val) sum += p->val;
            else { write->val = sum; tail = write; write = write->next; sum = 0; }
        }
        tail->next = nullptr;
        return head;
    }
};
```

---

<a id="lc-2487"></a>
## 37. LC 2487 — Remove Nodes From Linked List (Medium)

[Official problem](https://leetcode.com/problems/remove-nodes-from-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2400-2499/2487.Remove%20Nodes%20From%20Linked%20List/README_EN.md)

### Problem description

You are given the `head` of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the `head` of the modified linked list.

### Constraints

- The number of the nodes in the given list is in the range `[1, 10^5]`.

- `1 <= Node.val <= 10^5`

### Approach and complexity

After reversing the list, the maximum seen so far is the maximum originally to the node’s right. Retain a node iff its value is at least that maximum. Prepending retained nodes restores original order without a second full reversal.

Time O(n); auxiliary space O(1). Relinks existing nodes; skipped nodes remain caller-owned.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        ListNode* reversed = nullptr;
        while (head) {
            auto next = head->next;
            head->next = reversed;
            reversed = head;
            head = next;
        }
        ListNode* result = nullptr;
        int maximum = INT_MIN;
        while (reversed) {
            auto next = reversed->next;
            if (reversed->val >= maximum) {
                maximum = reversed->val;
                reversed->next = result;
                result = reversed;
            }
            reversed = next;
        }
        return result;
    }
};
```

---

<a id="lc-2816"></a>
## 38. LC 2816 — Double a Number Represented as a Linked List (Medium)

[Official problem](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2800-2899/2816.Double%20a%20Number%20Represented%20as%20a%20Linked%20List/README_EN.md)

### Problem description

You are given the `head` of a **non-empty** linked list representing a non-negative integer without leading zeroes.

Return the `head` of the linked list after **doubling** it.

### Constraints

- The number of nodes in the list is in the range `[1, 10^4]`

- `0 <= Node.val <= 9`

- The input is generated such that the list represents a number that does not have leading zeros, except the number `0` itself.

### Approach and complexity

First, we reverse the linked list, then simulate the multiplication operation, and finally reverse the linked list back.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        head = reverse(head);
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        int mul = 2, carry = 0;
        while (head) {
            int x = head->val * mul + carry;
            carry = x / 10;
            cur->next = new ListNode(x % 10);
            cur = cur->next;
            head = head->next;
        }
        if (carry) {
            cur->next = new ListNode(carry);
        }
        return reverse(dummy->next);
    }

    ListNode* reverse(ListNode* head) {
        ListNode* dummy = new ListNode();
        ListNode* cur = head;
        while (cur) {
            ListNode* next = cur->next;
            cur->next = dummy->next;
            dummy->next = cur;
            cur = next;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-2807"></a>
## 39. LC 2807 — Insert Greatest Common Divisors in Linked List (Medium)

[Official problem](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2800-2899/2807.Insert%20Greatest%20Common%20Divisors%20in%20Linked%20List/README_EN.md)

### Problem description

Given the head of a linked list `head`, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the **greatest common divisor** of them.

Return the linked list after insertion.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

### Constraints

- The number of nodes in the list is in the range `[1, 5000]`.

- `1 <= Node.val <= 1000`

### Approach and complexity

We use two pointers $\textit{pre}$ and $\textit{cur}$ to point to the current node and the next node respectively. We only need to insert a new node between $\textit{pre}$ and $\textit{cur}$. Therefore, each time we calculate the greatest common divisor $x$ of $\textit{pre}$ and $\textit{cur}$, we insert a new node with value $x$ between $\textit{pre}$ and $\textit{cur}$. Then we update $\textit{pre} = \textit{cur}$ and $\textit{cur} = \textit{cur}.\textit{next}$, and continue to traverse the linked list until $\textit{cur}$ is null.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list, and $M$ is the maximum value of the nodes in the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* pre = head;
        for (ListNode* cur = head->next; cur; cur = cur->next) {
            int x = gcd(pre->val, cur->val);
            pre->next = new ListNode(x, cur);
            pre = cur;
        }
        return head;
    }
};
```

---

<a id="lc-445"></a>
## 40. LC 445 — Add Two Numbers II (Medium)

[Official problem](https://leetcode.com/problems/add-two-numbers-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0445.Add%20Two%20Numbers%20II/README_EN.md)

### Problem description

You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.

- `0 <= Node.val <= 9`

- It is guaranteed that the list represents a number that does not have leading zeros.

**Follow up:** Could you solve it without reversing the input lists?

### Approach and complexity

Store digits in two stacks so addition can proceed from the least significant side without reversing inputs. Prepend each result digit while carrying.

Time O(m+n); auxiliary space O(m+n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1;
        stack<int> s2;
        for (; l1; l1 = l1->next) s1.push(l1->val);
        for (; l2; l2 = l2->next) s2.push(l2->val);
        ListNode* dummy = new ListNode();
        int carry = 0;
        while (!s1.empty() || !s2.empty() || carry) {
            int s = carry;
            if (!s1.empty()) {
                s += s1.top();
                s1.pop();
            }
            if (!s2.empty()) {
                s += s2.top();
                s2.pop();
            }
            // ListNode* node = new ListNode(s % 10, dummy->next);
            // dummy->next = node;
            dummy->next = new ListNode(s % 10, dummy->next);
            carry = s / 10;
        }
        return dummy->next;
    }
};
```

---

<a id="lc-369"></a>
## 41. LC 369 — Plus One Linked List (Medium)

[Official problem](https://leetcode.com/problems/plus-one-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0369.Plus%20One%20Linked%20List/README_EN.md)

### Problem description

Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the `head` of the list.

### Constraints

- The number of nodes in the linked list is in the range `[1, 100]`.

- `0 <= Node.val <= 9`

- The number represented by the linked list does not contain leading zeros except for the zero itself.

### Approach and complexity

We first set a dummy head node $\textit{dummy}$, initially with a value of $0$, and the successor node of $\textit{dummy}$ is the linked list $\textit{head}$.

Next, we traverse the linked list starting from the dummy head node, find the last node that is not $9$, increment its value by $1$, and set the values of all nodes after this node to $0$.

Finally, we check if the value of the dummy head node is $1$. If it is $1$, we return $\textit{dummy}$; otherwise, we return the successor node of $\textit{dummy}$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the linked list.

### C++20 solution

```cpp
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* target = dummy;
        for (; head; head = head->next) {
            if (head->val != 9) {
                target = head;
            }
        }
        target->val++;
        for (target = target->next; target; target = target->next) {
            target->val = 0;
        }
        return dummy->val ? dummy : dummy->next;
    }
};
```

---

<a id="lc-708"></a>
## 42. LC 708 — Insert into a Sorted Circular Linked List (Medium)

[Official problem](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0708.Insert%20into%20a%20Sorted%20Circular%20Linked%20List/README_EN.md)

### Problem description

Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value `insertVal` into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is `null`), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

### Constraints

- The number of nodes in the list is in the range `[0, 5 * 10^4]`.

- `-10^6 <= Node.val, insertVal <= 10^6`

### Approach and complexity

Walk the cycle to find either a normal sorted gap containing the new value or the maximum-to-minimum wrap where an extreme value belongs. If every value is equal, any gap works.

Time O(n); auxiliary space O(1), excluding the new output node.

### C++20 solution

```cpp
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        Node* node = new Node(insertVal);
        if (!head) {
            node->next = node;
            return node;
        }
        Node *prev = head, *curr = head->next;
        while (curr != head) {
            if ((prev->val <= insertVal && insertVal <= curr->val) || (prev->val > curr->val && (insertVal >= prev->val || insertVal <= curr->val))) break;
            prev = curr;
            curr = curr->next;
        }
        prev->next = node;
        node->next = curr;
        return head;
    }
};
```

---

<a id="lc-426"></a>
## 43. LC 426 — Convert Binary Search Tree to Sorted Doubly Linked List (Medium)

[Official problem](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/README_EN.md)

### Problem description

Convert a **Binary Search Tree** to a sorted **Circular Doubly-Linked List** in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation **in place**. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- `-1000 <= Node.val <= 1000`

- All the values of the tree are **unique**.

### Approach and complexity

Inorder traversal yields sorted BST nodes. Link each node to its predecessor, retain the first and last, and finally close the two circular links.

Time O(n); auxiliary space O(h) for recursion.

### C++20 solution

```cpp
class Solution {
public:
    Node* prev;
    Node* head;

    Node* treeToDoublyList(Node* root) {
        if (!root) return nullptr;
        prev = nullptr;
        head = nullptr;
        dfs(root);
        prev->right = head;
        head->left = prev;
        return head;
    }

    void dfs(Node* root) {
        if (!root) return;
        dfs(root->left);
        if (prev) {
            prev->right = root;
            root->left = prev;
        } else
            head = root;
        prev = root;
        dfs(root->right);
    }
};
```

---

<a id="lc-109"></a>
## 44. LC 109 — Convert Sorted List to Binary Search Tree (Medium)

[Official problem](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0109.Convert%20Sorted%20List%20to%20Binary%20Search%20Tree/README_EN.md)

### Problem description

Given the `head` of a singly linked list where elements are sorted in **ascending order**, convert it to a **height-balanced** binary search tree.

### Constraints

- The number of nodes in `head` is in the range `[0, 2 * 10^4]`.

- `-10^5 <= Node.val <= 10^5`

### Approach and complexity

Count nodes, construct a balanced left subtree of n/2 nodes, consume the next list node as the root, and construct the remaining right subtree. The inorder consumption matches the sorted list, so no array or repeated midpoint scan is needed.

Time O(n); auxiliary space O(log n), excluding the returned tree.

### C++20 solution

```cpp
class Solution {
    TreeNode* build(ListNode*& cursor, int count) {
        if (!count) return nullptr;
        TreeNode* left = build(cursor, count / 2);
        TreeNode* root = new TreeNode(cursor->val);
        cursor = cursor->next;
        root->left = left;
        root->right = build(cursor, count - count / 2 - 1);
        return root;
    }
public:
    TreeNode* sortedListToBST(ListNode* head) {
        int n = 0;
        for (auto p = head; p; p = p->next) ++n;
        return build(head, n);
    }
};
```

---

<a id="lc-114"></a>
## 45. LC 114 — Flatten Binary Tree to Linked List (Medium)

[Official problem](https://leetcode.com/problems/flatten-binary-tree-to-linked-list) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0114.Flatten%20Binary%20Tree%20to%20Linked%20List/README_EN.md)

### Problem description

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.

- The "linked list" should be in the same order as a **pre-order**** traversal** of the binary tree.

### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- `-100 <= Node.val <= 100`

**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?

### Approach and complexity

The visit order of preorder traversal is "root, left subtree, right subtree". After the last node of the left subtree is visited, the right subtree node of the root node will be visited next.

Therefore, for the current node, if its left child node is not null, we find the rightmost node of the left subtree as the predecessor node, and then assign the right child node of the current node to the right child node of the predecessor node. Then assign the left child node of the current node to the right child node of the current node, and set the left child node of the current node to null. Then take the right child node of the current node as the next node and continue processing until all nodes are processed.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the tree.

### C++20 solution

```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        while (root) {
            if (root->left) {
                TreeNode* pre = root->left;
                while (pre->right) {
                    pre = pre->right;
                }
                pre->right = root->right;
                root->right = root->left;
                root->left = nullptr;
            }
            root = root->right;
        }
    }
};
```

---

<a id="lc-116"></a>
## 46. LC 116 — Populating Next Right Pointers in Each Node (Medium)

[Official problem](https://leetcode.com/problems/populating-next-right-pointers-in-each-node) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0116.Populating%20Next%20Right%20Pointers%20in%20Each%20Node/README_EN.md)

### Problem description

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
int val;
Node *left;
Node *right;
Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

### Constraints

- The number of nodes in the tree is in the range `[0, 2^12 - 1]`.

- `-1000 <= Node.val <= 1000`

**Follow-up:**

- You may only use constant extra space.

- The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

### Approach and complexity

For each parent on a perfect-tree level, connect its left child to its right child and its right child to the next parent’s left child. Previously constructed next pointers replace a BFS queue.

Time O(n); auxiliary space O(1). The perfect-tree condition is essential.

### C++20 solution

```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return root;
        root->next = nullptr;
        for (Node* level = root; level->left; level = level->left) {
            for (Node* p = level; p; p = p->next) {
                p->left->next = p->right;
                p->right->next = p->next ? p->next->left : nullptr;
            }
        }
        return root;
    }
};
```

---

<a id="lc-117"></a>
## 47. LC 117 — Populating Next Right Pointers in Each Node II (Medium)

[Official problem](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0117.Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II/README_EN.md)

### Problem description

Given a binary tree

struct Node {
int val;
Node *left;
Node *right;
Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

### Constraints

- The number of nodes in the tree is in the range `[0, 6000]`.

- `-100 <= Node.val <= 100`

**Follow-up:**

- You may only use constant extra space.

- The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

### Approach and complexity

The space complexity of Solution 1 is relatively high because it requires a queue to store the nodes of each level. We can implement it with constant space.

We define two pointers $\textit{prev}$ and $\textit{next}$, which point to the previous node and the first node of the next level, respectively. When traversing the nodes of the current level, we string the nodes of the next level together and find the first node of the next level. After the current level is traversed, we assign the first node $\textit{next}$ of the next level to $\textit{node}$ and continue to traverse.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    Node* connect(Node* root) {
        Node* node = root;
        Node* prev = nullptr;
        Node* next = nullptr;
        auto modify = [&](Node* curr) {
            if (!curr) {
                return;
            }
            if (!next) {
                next = curr;
            }
            if (prev) {
                prev->next = curr;
            }
            prev = curr;
        };
        while (node) {
            prev = next = nullptr;
            while (node) {
                modify(node->left);
                modify(node->right);
                node = node->next;
            }
            node = next;
        }
        return root;
    }
};
```

---

<a id="lc-622"></a>
## 48. LC 622 — Design Circular Queue (Medium)

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
## 49. LC 641 — Design Circular Deque (Medium)

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

<a id="lc-460"></a>
## 50. LC 460 — LFU Cache (Hard)

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
