# 5. Binary Tree & Bst — C++20 solutions

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

1. [LC 104 — Maximum Depth of Binary Tree](#lc-104)
2. [LC 94 — Binary Tree Inorder Traversal](#lc-94)
3. [LC 98 — Validate Binary Search Tree](#lc-98)
4. [LC 102 — Binary Tree Level Order Traversal](#lc-102)
5. [LC 226 — Invert Binary Tree](#lc-226)
6. [LC 100 — Same Tree](#lc-100)
7. [LC 101 — Symmetric Tree](#lc-101)
8. [LC 543 — Diameter of Binary Tree](#lc-543)
9. [LC 110 — Balanced Binary Tree](#lc-110)
10. [LC 112 — Path Sum](#lc-112)
11. [LC 113 — Path Sum II](#lc-113)
12. [LC 124 — Binary Tree Maximum Path Sum](#lc-124)
13. [LC 235 — Lowest Common Ancestor of a Binary Search Tree](#lc-235)
14. [LC 236 — Lowest Common Ancestor of a Binary Tree](#lc-236)
15. [LC 230 — Kth Smallest Element in a BST](#lc-230)
16. [LC 105 — Construct Binary Tree from Preorder and Inorder Traversal](#lc-105)
17. [LC 106 — Construct Binary Tree from Inorder and Postorder Traversal](#lc-106)
18. [LC 297 — Serialize and Deserialize Binary Tree](#lc-297)
19. [LC 108 — Convert Sorted Array to Binary Search Tree](#lc-108)
20. [LC 700 — Search in a Binary Search Tree](#lc-700)
21. [LC 701 — Insert into a Binary Search Tree](#lc-701)
22. [LC 450 — Delete Node in a BST](#lc-450)
23. [LC 95 — Unique Binary Search Trees II](#lc-95)
24. [LC 96 — Unique Binary Search Trees](#lc-96)
25. [LC 144 — Binary Tree Preorder Traversal](#lc-144)
26. [LC 145 — Binary Tree Postorder Traversal](#lc-145)
27. [LC 199 — Binary Tree Right Side View](#lc-199)
28. [LC 103 — Binary Tree Zigzag Level Order Traversal](#lc-103)
29. [LC 111 — Minimum Depth of Binary Tree](#lc-111)
30. [LC 257 — Binary Tree Paths](#lc-257)
31. [LC 129 — Sum Root to Leaf Numbers](#lc-129)
32. [LC 437 — Path Sum III](#lc-437)
33. [LC 572 — Subtree of Another Tree](#lc-572)
34. [LC 617 — Merge Two Binary Trees](#lc-617)
35. [LC 637 — Average of Levels in Binary Tree](#lc-637)
36. [LC 662 — Maximum Width of Binary Tree](#lc-662)
37. [LC 654 — Maximum Binary Tree](#lc-654)
38. [LC 669 — Trim a Binary Search Tree](#lc-669)
39. [LC 783 — Minimum Distance Between BST Nodes](#lc-783)
40. [LC 938 — Range Sum of BST](#lc-938)
41. [LC 987 — Vertical Order Traversal of a Binary Tree](#lc-987)
42. [LC 1026 — Maximum Difference Between Node and Ancestor](#lc-1026)
43. [LC 114 — Flatten Binary Tree to Linked List](#lc-114)
44. [LC 116 — Populating Next Right Pointers in Each Node](#lc-116)
45. [LC 173 — Binary Search Tree Iterator](#lc-173)
46. [LC 222 — Count Complete Tree Nodes](#lc-222)
47. [LC 337 — House Robber III](#lc-337)
48. [LC 404 — Sum of Left Leaves](#lc-404)
49. [LC 508 — Most Frequent Subtree Sum](#lc-508)
50. [LC 863 — All Nodes Distance K in Binary Tree](#lc-863)

---

<a id="lc-104"></a>
## 1. LC 104 — Maximum Depth of Binary Tree (Easy)

[Official problem](https://leetcode.com/problems/maximum-depth-of-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0104.Maximum%20Depth%20of%20Binary%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.

- `-100 <= Node.val <= 100`

### Approach and complexity

Recursively traverse the left and right subtrees, calculate the maximum depth of the left and right subtrees, and then take the maximum value plus $1$.

The time complexity is $O(n)$, where $n$ is the number of nodes in the binary tree. Each node is traversed only once in the recursion.

### C++20 solution

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int l = maxDepth(root->left), r = maxDepth(root->right);
        return 1 + max(l, r);
    }
};
```

---

<a id="lc-94"></a>
## 2. LC 94 — Binary Tree Inorder Traversal (Easy)

[Official problem](https://leetcode.com/problems/binary-tree-inorder-traversal) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0094.Binary%20Tree%20Inorder%20Traversal/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`.

- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

### Approach and complexity

Morris traversal does not require a stack, so the space complexity is $O(1)$. The core idea is:

Traverse the binary tree nodes,

1. If the left subtree of the current node `root` is null, **add the current node value to the result list `ans`**, and update the current node to `root.right`.
2. If the left subtree of the current node `root` is not null, find the rightmost node `prev` of the left subtree (which is the predecessor node of the `root` node in in-order traversal):
    - If the right subtree of the predecessor node `prev` is null, point the right subtree of the predecessor node to the current node `root`, and update the current node to `root.left`.
    - If the right subtree of the predecessor node `prev` is not null, **add the current node value to the result list `ans`**, then point the right subtree of the predecessor node to null (i.e., disconnect `prev` and `root`), and update the current node to `root.right`.
3. Repeat the above steps until the binary tree node is null, and the traversal ends.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        while (root) {
            if (!root->left) {
                ans.push_back(root->val);
                root = root->right;
            } else {
                TreeNode* prev = root->left;
                while (prev->right && prev->right != root) {
                    prev = prev->right;
                }
                if (!prev->right) {
                    prev->right = root;
                    root = root->left;
                } else {
                    ans.push_back(root->val);
                    prev->right = nullptr;
                    root = root->right;
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-98"></a>
## 3. LC 98 — Validate Binary Search Tree (Medium)

[Official problem](https://leetcode.com/problems/validate-binary-search-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0098.Validate%20Binary%20Search%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **strictly less than** the node's key.

- The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.

- Both the left and right subtrees must also be binary search trees.

### Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.

- `-2^31 <= Node.val <= 2^31 - 1`

### Approach and complexity

We can perform a recursive in-order traversal on the binary tree. If the result of the traversal is strictly ascending, then this tree is a binary search tree.

Therefore, we use a variable `prev` to save the last node we traversed. Initially, `prev = -∞`. Then we recursively traverse the left subtree. If the left subtree is not a binary search tree, we directly return `False`. Otherwise, we check whether the value of the current node is greater than `prev`. If not, we return `False`. Otherwise, we update `prev` to the value of the current node, and then recursively traverse the right subtree.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        TreeNode* prev = nullptr;
        function<bool(TreeNode*)> dfs = [&](TreeNode* root) {
            if (!root) {
                return true;
            }
            if (!dfs(root->left)) {
                return false;
            }
            if (prev && prev->val >= root->val) {
                return false;
            }
            prev = root;
            return dfs(root->right);
        };
        return dfs(root);
    }
};
```

---

<a id="lc-102"></a>
## 4. LC 102 — Binary Tree Level Order Traversal (Medium)

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

<a id="lc-226"></a>
## 5. LC 226 — Invert Binary Tree (Easy)

[Official problem](https://leetcode.com/problems/invert-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0226.Invert%20Binary%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, invert the tree, and return its root.

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`.

- `-100 <= Node.val <= 100`

### Approach and complexity

First, we check if $\textit{root}$ is null. If it is, we return $\textit{null}$. Then, we recursively invert the left and right subtrees, set the inverted right subtree as the new left subtree, and set the inverted left subtree as the new right subtree. Finally, we return $\textit{root}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) {
            return root;
        }
        TreeNode* l = invertTree(root->left);
        TreeNode* r = invertTree(root->right);
        root->left = r;
        root->right = l;
        return root;
    }
};
```

---

<a id="lc-100"></a>
## 6. LC 100 — Same Tree (Easy)

[Official problem](https://leetcode.com/problems/same-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0100.Same%20Tree/README_EN.md)

### Problem description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Constraints

- The number of nodes in both trees is in the range `[0, 100]`.

- `-10^4 <= Node.val <= 10^4`

### Approach and complexity

We can use the DFS recursive method to solve this problem.

First, determine whether the root nodes of the two binary trees are the same. If both root nodes are null, then the two binary trees are the same. If only one of the root nodes is null, then the two binary trees are definitely different. If both root nodes are not null, then determine whether their values are the same. If they are not the same, then the two binary trees are definitely different. If they are the same, then determine whether the left subtrees of the two binary trees are the same and whether the right subtrees are the same. The two binary trees are the same only when all the above conditions are met.

The time complexity is $O(\min(m, n))$, and the space complexity is $O(\min(m, n))$, where $m$ and $n$ are the number of nodes in the two binary trees, respectively. The space complexity mainly depends on the number of layers of recursive calls, which will not exceed the number of nodes in the smaller binary tree.

### C++20 solution

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == q) return true;
        if (!p || !q || p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

---

<a id="lc-101"></a>
## 7. LC 101 — Symmetric Tree (Easy)

[Official problem](https://leetcode.com/problems/symmetric-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0101.Symmetric%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

### Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.

- `-100 <= Node.val <= 100`

**Follow up:** Could you solve it both recursively and iteratively?

### Approach and complexity

We design a function $\textit{dfs}(\textit{root1}, \textit{root2})$ to determine whether two binary trees are symmetric. The answer is $\textit{dfs}(\textit{root}.\textit{left}, \textit{root}.\textit{right})$.

The logic of the function $\textit{dfs}(\textit{root1}, \textit{root2})$ is as follows:

- If both $\textit{root1}$ and $\textit{root2}$ are null, the two binary trees are symmetric, and we return `true`;
- If only one of $\textit{root1}$ and $\textit{root2}$ is null, or $\textit{root1}.\textit{val} \neq \textit{root2}.\textit{val}$, we return `false`;
- Otherwise, we check whether the left subtree of $\textit{root1}$ is symmetric with the right subtree of $\textit{root2}$, and whether the right subtree of $\textit{root1}$ is symmetric with the left subtree of $\textit{root2}$, using recursion.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        auto dfs = [&](auto&& dfs, TreeNode* root1, TreeNode* root2) -> bool {
            if (root1 == root2) {
                return true;
            }
            if (!root1 || !root2 || root1->val != root2->val) {
                return false;
            }
            return dfs(dfs, root1->left, root2->right) && dfs(dfs, root1->right, root2->left);
        };
        return dfs(dfs, root->left, root->right);
    }
};
```

---

<a id="lc-543"></a>
## 8. LC 543 — Diameter of Binary Tree (Easy)

[Official problem](https://leetcode.com/problems/diameter-of-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0543.Diameter%20of%20Binary%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

### Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.

- `-100 <= Node.val <= 100`

### Approach and complexity

We can enumerate each node of the binary tree, and for each node, calculate the maximum depth of its left and right subtrees, $l$ and $r$, respectively. The diameter of the node is $l + r$. The maximum diameter among all nodes is the diameter of the binary tree.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        auto dfs = [&](auto&& dfs, TreeNode* root) -> int {
            if (!root) {
                return 0;
            }
            int l = dfs(dfs, root->left);
            int r = dfs(dfs, root->right);
            ans = max(ans, l + r);
            return 1 + max(l, r);
        };
        dfs(dfs, root);
        return ans;
    }
};
```

---

<a id="lc-110"></a>
## 9. LC 110 — Balanced Binary Tree (Easy)

[Official problem](https://leetcode.com/problems/balanced-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0110.Balanced%20Binary%20Tree/README_EN.md)

### Problem description

Given a binary tree, determine if it is **height-balanced**.

### Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.

- `-10^4 <= Node.val <= 10^4`

### Approach and complexity

We define a function $\textit{height}(\textit{root})$ to calculate the height of a binary tree, with the following logic:

- If the binary tree $\textit{root}$ is null, return $0$.
- Otherwise, recursively calculate the heights of the left and right subtrees, denoted as $l$ and $r$ respectively. If either $l$ or $r$ is $-1$, or the absolute difference between $l$ and $r$ is greater than $1$, then return $-1$. Otherwise, return $\max(l, r) + 1$.

Therefore, if the function $\textit{height}(\textit{root})$ returns $-1$, it means the binary tree $\textit{root}$ is not balanced. Otherwise, it is balanced.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        function<int(TreeNode*)> height = [&](TreeNode* root) {
            if (!root) {
                return 0;
            }
            int l = height(root->left);
            int r = height(root->right);
            if (l == -1 || r == -1 || abs(l - r) > 1) {
                return -1;
            }
            return 1 + max(l, r);
        };
        return height(root) >= 0;
    }
};
```

---

<a id="lc-112"></a>
## 10. LC 112 — Path Sum (Easy)

[Official problem](https://leetcode.com/problems/path-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0112.Path%20Sum/README_EN.md)

### Problem description

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

### Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.

- `-1000 <= Node.val <= 1000`

- `-1000 <= targetSum <= 1000`

### Approach and complexity

Starting from the root node, recursively traverse the tree and update the value of the node to the path sum from the root node to that node. When you traverse to a leaf node, determine whether this path sum is equal to the target value. If it is equal, return `true`, otherwise return `false`.

The time complexity is $O(n)$, where $n$ is the number of nodes in the binary tree. Each node is visited once.

### C++20 solution

```cpp
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        function<bool(TreeNode*, int)> dfs = [&](TreeNode* root, int s) -> int {
            if (!root) return false;
            s += root->val;
            if (!root->left && !root->right && s == targetSum) return true;
            return dfs(root->left, s) || dfs(root->right, s);
        };
        return dfs(root, 0);
    }
};
```

---

<a id="lc-113"></a>
## 11. LC 113 — Path Sum II (Medium)

[Official problem](https://leetcode.com/problems/path-sum-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0113.Path%20Sum%20II/README_EN.md)

### Problem description

Given the `root` of a binary tree and an integer `targetSum`, return all **root-to-leaf** paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node **values**, not node references.

A **root-to-leaf** path is a path starting from the root and ending at any leaf node. A **leaf** is a node with no children.

### Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.

- `-1000 <= Node.val <= 1000`

- `-1000 <= targetSum <= 1000`

### Approach and complexity

We start from the root node, recursively traverse all paths from the root node to the leaf nodes, and record the path sum. When we traverse to a leaf node, if the current path sum equals $\textit{targetSum}$, then we add this path to the answer.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        vector<int> t;
        function<void(TreeNode*, int)> dfs = [&](TreeNode* root, int s) {
            if (!root) return;
            s -= root->val;
            t.emplace_back(root->val);
            if (!root->left && !root->right && s == 0) ans.emplace_back(t);
            dfs(root->left, s);
            dfs(root->right, s);
            t.pop_back();
        };
        dfs(root, targetSum);
        return ans;
    }
};
```

---

<a id="lc-124"></a>
## 12. LC 124 — Binary Tree Maximum Path Sum (Hard)

[Official problem](https://leetcode.com/problems/binary-tree-maximum-path-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0124.Binary%20Tree%20Maximum%20Path%20Sum/README_EN.md)

### Problem description

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum **path sum** of any **non-empty** path.

### Constraints

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.

- `-1000 <= Node.val <= 1000`

### Approach and complexity

When thinking about the classic routine of recursion problems in binary trees, we consider:

1. Termination condition (when to terminate recursion)
2. Recursively process the left and right subtrees
3. Merge the calculation results of the left and right subtrees

For this problem, we design a function $\textit{dfs}(\textit{root})$, which returns the maximum path sum of the binary tree with $\textit{root}$ as the root node.

The execution logic of the function $\textit{dfs}(\textit{root})$ is as follows:

If $\textit{root}$ does not exist, then $\textit{dfs}(\textit{root})$ returns $0$;

Otherwise, we recursively calculate the maximum path sum of the left and right subtrees of $\textit{root}$, denoted as $\textit{left}$ and $\textit{right}$. If $\textit{left}$ is less than $0$, then we set it to $0$, similarly, if $\textit{right}$ is less than $0$, then we set it to $0$.

Then, we update the answer with $\textit{root}.\textit{val} + \textit{left} + \textit{right}$. Finally, the function returns $\textit{root}.\textit{val} + \max(\textit{left}, \textit{right})$.

In the main function, we call $\textit{dfs}(\textit{root})$ to get the maximum path sum of each node, and the maximum value among them is the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int ans = -1001;
        function<int(TreeNode*)> dfs = [&](TreeNode* root) {
            if (!root) {
                return 0;
            }
            int left = max(0, dfs(root->left));
            int right = max(0, dfs(root->right));
            ans = max(ans, left + right + root->val);
            return root->val + max(left, right);
        };
        dfs(root);
        return ans;
    }
};
```

---

<a id="lc-235"></a>
## 13. LC 235 — Lowest Common Ancestor of a Binary Search Tree (Easy)

[Official problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0235.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/README_EN.md)

### Problem description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

### Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.

- `-10^9 <= Node.val <= 10^9`

- All `Node.val` are **unique**.

- `p != q`

- `p` and `q` will exist in the BST.

### Approach and complexity

Starting from the root node, we traverse the tree. If the current node's value is less than both $p$ and $q$ values, it means that $p$ and $q$ should be in the right subtree of the current node, so we move to the right child. If the current node's value is greater than both $p$ and $q$ values, it means that $p$ and $q$ should be in the left subtree, so we move to the left child. Otherwise, it means the current node is the lowest common ancestor of $p$ and $q$, so we return the current node.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the binary search tree.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while (1) {
            if (root->val < min(p->val, q->val)) {
                root = root->right;
            } else if (root->val > max(p->val, q->val)) {
                root = root->left;
            } else {
                return root;
            }
        }
    }
};
```

---

<a id="lc-236"></a>
## 14. LC 236 — Lowest Common Ancestor of a Binary Tree (Medium)

[Official problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0236.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree/README_EN.md)

### Problem description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”

### Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.

- `-10^9 <= Node.val <= 10^9`

- All `Node.val` are **unique**.

- `p != q`

- `p` and `q` will exist in the tree.

### Approach and complexity

We recursively traverse the binary tree:

If the current node is null or equals to $p$ or $q$, then we return the current node;

Otherwise, we recursively traverse the left and right subtrees, and record the returned results as $\textit{left}$ and $\textit{right}$. If both $\textit{left}$ and $\textit{right}$ are not null, it means that $p$ and $q$ are in the left and right subtrees respectively, so the current node is the nearest common ancestor; If only one of $\textit{left}$ and $\textit{right}$ is not null, we return the one that is not null.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr || root == p || root == q) {
            return root;
        }
        auto left = lowestCommonAncestor(root->left, p, q);
        auto right = lowestCommonAncestor(root->right, p, q);
        if (left && right) {
            return root;
        }
        return left ? left : right;
    }
};
```

---

<a id="lc-230"></a>
## 15. LC 230 — Kth Smallest Element in a BST (Medium)

[Official problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0230.Kth%20Smallest%20Element%20in%20a%20BST/README_EN.md)

### Problem description

Given the `root` of a binary search tree, and an integer `k`, return the `k^th` smallest value (**1-indexed**) of all the values of the nodes in the tree.

### Constraints

- The number of nodes in the tree is `n`.

- `1 <= k <= n <= 10^4`

- `0 <= Node.val <= 10^4`

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

### Approach and complexity

Iterative inorder traversal visits a BST in ascending order. Stop at the kth pop instead of traversing the whole tree.

Time O(h+k); auxiliary space O(h), where h is tree height.

### C++20 solution

```cpp
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> stk;
        while (root || !stk.empty()) {
            if (root) {
                stk.push(root);
                root = root->left;
            } else {
                root = stk.top();
                stk.pop();
                if (--k == 0) return root->val;
                root = root->right;
            }
        }
        return 0;
    }
};
```

---

<a id="lc-105"></a>
## 16. LC 105 — Construct Binary Tree from Preorder and Inorder Traversal (Medium)

[Official problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0105.Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/README_EN.md)

### Problem description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

### Constraints

- `1 <= preorder.length <= 3000`

- `inorder.length == preorder.length`

- `-3000 <= preorder[i], inorder[i] <= 3000`

- `preorder` and `inorder` consist of **unique** values.

- Each value of `inorder` also appears in `preorder`.

- `preorder` is **guaranteed** to be the preorder traversal of the tree.

- `inorder` is **guaranteed** to be the inorder traversal of the tree.

### Approach and complexity

The first node $\textit{preorder}[0]$ in the pre-order sequence is the root node. We find the position $k$ of the root node in the in-order sequence, which can divide the in-order sequence into the left subtree $\textit{inorder}[0..k]$ and the right subtree $\textit{inorder}[k+1..]$.

Through the intervals of the left and right subtrees, we can calculate the number of nodes in the left and right subtrees, assumed to be $a$ and $b$. Then in the pre-order nodes, the $a$ nodes after the root node are the left subtree, and the $b$ nodes after that are the right subtree.

Therefore, we design a function $\textit{dfs}(i, j, n)$, where $i$ and $j$ represent the starting positions of the pre-order sequence and the in-order sequence, respectively, and $n$ represents the number of nodes. The return value of the function is the binary tree constructed with $\textit{preorder}[i..i+n-1]$ as the pre-order sequence and $\textit{inorder}[j..j+n-1]$ as the in-order sequence.

The execution process of the function $\textit{dfs}(i, j, n)$ is as follows:

- If $n \leq 0$, it means there are no nodes, return a null node.
- Take out the first node $v = \textit{preorder}[i]$ of the pre-order sequence as the root node, and then use the hash table $d$ to find the position $k$ of the root node in the in-order sequence. Then the number of nodes in the left subtree is $k - j$, and the number of nodes in the right subtree is $n - k + j - 1$.
- Recursively construct the left subtree $l = \textit{dfs}(i + 1, j, k - j)$ and the right subtree $r = \textit{dfs}(i + 1 + k - j, k + 1, n - k + j - 1)$.
- Finally, return the binary tree with $v$ as the root node and $l$ and $r$ as the left and right subtrees, respectively.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n = preorder.size();
        unordered_map<int, int> d;
        for (int i = 0; i < n; ++i) {
            d[inorder[i]] = i;
        }
        function<TreeNode*(int, int, int)> dfs = [&](int i, int j, int n) -> TreeNode* {
            if (n <= 0) {
                return nullptr;
            }
            int v = preorder[i];
            int k = d[v];
            TreeNode* l = dfs(i + 1, j, k - j);
            TreeNode* r = dfs(i + 1 + k - j, k + 1, n - 1 - (k - j));
            return new TreeNode(v, l, r);
        };
        return dfs(0, 0, n);
    }
};
```

---

<a id="lc-106"></a>
## 17. LC 106 — Construct Binary Tree from Inorder and Postorder Traversal (Medium)

[Official problem](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0106.Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal/README_EN.md)

### Problem description

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

### Constraints

- `1 <= inorder.length <= 3000`

- `postorder.length == inorder.length`

- `-3000 <= inorder[i], postorder[i] <= 3000`

- `inorder` and `postorder` consist of **unique** values.

- Each value of `postorder` also appears in `inorder`.

- `inorder` is **guaranteed** to be the inorder traversal of the tree.

- `postorder` is **guaranteed** to be the postorder traversal of the tree.

### Approach and complexity

The last node in the post-order traversal is the root node. We can find the position of the root node in the in-order traversal, and then recursively construct the left and right subtrees.

Specifically, we first use a hash table $d$ to store the position of each node in the in-order traversal. Then we design a recursive function $\textit{dfs}(i, j, n)$, where $i$ and $j$ represent the starting positions of the in-order and post-order traversals, respectively, and $n$ represents the number of nodes in the subtree. The function logic is as follows:

- If $n \leq 0$, it means the subtree is empty, return a null node.
- Otherwise, take out the last node $v$ of the post-order traversal, and then find the position $k$ of $v$ in the in-order traversal using the hash table $d$. Then the number of nodes in the left subtree is $k - i$, and the number of nodes in the right subtree is $n - k + i - 1$.
- Recursively construct the left subtree $\textit{dfs}(i, j, k - i)$ and the right subtree $\textit{dfs}(k + 1, j + k - i, n - k + i - 1)$, connect them to the root node, and finally return the root node.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int, int> d;
        int n = inorder.size();
        for (int i = 0; i < n; ++i) {
            d[inorder[i]] = i;
        }
        function<TreeNode*(int, int, int)> dfs = [&](int i, int j, int n) -> TreeNode* {
            if (n <= 0) {
                return nullptr;
            }
            int v = postorder[j + n - 1];
            int k = d[v];
            auto l = dfs(i, j, k - i);
            auto r = dfs(k + 1, j + k - i, n - k + i - 1);
            return new TreeNode(v, l, r);
        };
        return dfs(0, 0, n);
    }
};
```

---

<a id="lc-297"></a>
## 18. LC 297 — Serialize and Deserialize Binary Tree (Hard)

[Official problem](https://leetcode.com/problems/serialize-and-deserialize-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0297.Serialize%20and%20Deserialize%20Binary%20Tree/README_EN.md)

### Problem description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

### Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.

- `-1000 <= Node.val <= 1000`

### Approach and complexity

We can use level order traversal to serialize the binary tree. Starting from the root node, we add the nodes of the binary tree to the queue in the order from top to bottom, from left to right. Then we dequeue the nodes in the queue one by one. If the node is not null, we add its value to the serialized string; otherwise, we add a special character `#`. Finally, we return the serialized string.

During deserialization, we split the serialized string by the delimiter to get a string array, and then add the elements in the string array to the queue in order. The elements in the queue are the nodes of the binary tree. We dequeue the elements from the queue one by one. If the element is not `#`, we convert it to an integer and use it as the value of the node, and then add the node to the queue; otherwise, we set it to `null`. Finally, we return the root node.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) {
            return "";
        }
        queue<TreeNode*> q{{root}};
        string ans;
        while (!q.empty()) {
            auto node = q.front();
            q.pop();
            if (node) {
                ans += to_string(node->val) + " ";
                q.push(node->left);
                q.push(node->right);
            } else {
                ans += "# ";
            }
        }
        ans.pop_back();
        return ans;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "") {
            return nullptr;
        }
        stringstream ss(data);
        string t;
        ss >> t;
        TreeNode* root = new TreeNode(stoi(t));
        queue<TreeNode*> q{{root}};
        while (!q.empty()) {
            auto node = q.front();
            q.pop();
            ss >> t;
            if (t != "#") {
                node->left = new TreeNode(stoi(t));
                q.push(node->left);
            }
            ss >> t;
            if (t != "#") {
                node->right = new TreeNode(stoi(t));
                q.push(node->right);
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```

---

<a id="lc-108"></a>
## 19. LC 108 — Convert Sorted Array to Binary Search Tree (Easy)

[Official problem](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0108.Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree/README_EN.md)

### Problem description

Given an integer array `nums` where the elements are sorted in **ascending order**, convert it to a **height-balanced** binary search tree.

### Constraints

- `1 <= nums.length <= 10^4`

- `-10^4 <= nums[i] <= 10^4`

- `nums` is sorted in a **strictly increasing** order.

### Approach and complexity

We design a recursive function $\textit{dfs}(l, r)$, which represents that the values of the nodes to be constructed in the current binary search tree are within the index range $[l, r]$ of the array $\textit{nums}$. This function returns the root node of the constructed binary search tree.

The execution process of the function $\textit{dfs}(l, r)$ is as follows:

1. If $l > r$, it means the current array is empty, so return `null`.
2. If $l \leq r$, take the element at index $\textit{mid} = \lfloor \frac{l + r}{2} \rfloor$ of the array as the root node of the current binary search tree, where $\lfloor x \rfloor$ denotes the floor function of $x$.
3. Recursively construct the left subtree of the current binary search tree, with the root node's value being the element at index $\textit{mid} - 1$ of the array. The values of the nodes in the left subtree are within the index range $[l, \textit{mid} - 1]$ of the array.
4. Recursively construct the right subtree of the current binary search tree, with the root node's value being the element at index $\textit{mid} + 1$ of the array. The values of the nodes in the right subtree are within the index range $[\textit{mid} + 1, r]$ of the array.
5. Return the root node of the current binary search tree.

The answer is the return value of the function $\textit{dfs}(0, n - 1)$.

The time complexity is $O(n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{nums}$.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        auto dfs = [&](auto&& dfs, int l, int r) -> TreeNode* {
            if (l > r) {
                return nullptr;
            }
            int mid = (l + r) >> 1;
            return new TreeNode(nums[mid], dfs(dfs, l, mid - 1), dfs(dfs, mid + 1, r));
        };
        return dfs(dfs, 0, nums.size() - 1);
    }
};
```

---

<a id="lc-700"></a>
## 20. LC 700 — Search in a Binary Search Tree (Easy)

[Official problem](https://leetcode.com/problems/search-in-a-binary-search-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0700.Search%20in%20a%20Binary%20Search%20Tree/README_EN.md)

### Problem description

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

### Constraints

- The number of nodes in the tree is in the range `[1, 5000]`.

- `1 <= Node.val <= 10^7`

- `root` is a binary search tree.

- `1 <= val <= 10^7`

### Approach and complexity

We check if the current node is null or if the current node's value equals the target value. If so, we return the current node.

Otherwise, if the current node's value is greater than the target value, we recursively search the left subtree; otherwise, we recursively search the right subtree.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root || root->val == val) {
            return root;
        }
        return root->val > val ? searchBST(root->left, val) : searchBST(root->right, val);
    }
};
```

---

<a id="lc-701"></a>
## 21. LC 701 — Insert into a Binary Search Tree (Medium)

[Official problem](https://leetcode.com/problems/insert-into-a-binary-search-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0701.Insert%20into%20a%20Binary%20Search%20Tree/README_EN.md)

### Problem description

You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the root node of the BST after the insertion. It is **guaranteed** that the new value does not exist in the original BST.

**Notice** that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return **any of them**.

### Constraints

- The number of nodes in the tree will be in the range `[0, 10^4]`.

- `-10^8 <= Node.val <= 10^8`

- All the values `Node.val` are **unique**.

- `-10^8 <= val <= 10^8`

- It's **guaranteed** that `val` does not exist in the original BST.

### Approach and complexity

If the root node is null, we directly create a new node with the value $\textit{val}$ and return it.

If the root node's value is greater than $\textit{val}$, we recursively insert $\textit{val}$ into the left subtree and update the root of the left subtree with the returned root node.

If the root node's value is less than $\textit{val}$, we recursively insert $\textit{val}$ into the right subtree and update the root of the right subtree with the returned root node.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            return new TreeNode(val);
        }
        if (root->val > val) {
            root->left = insertIntoBST(root->left, val);
        } else {
            root->right = insertIntoBST(root->right, val);
        }
        return root;
    }
};
```

---

<a id="lc-450"></a>
## 22. LC 450 — Delete Node in a BST (Medium)

[Official problem](https://leetcode.com/problems/delete-node-in-a-bst) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0450.Delete%20Node%20in%20a%20BST/README_EN.md)

### Problem description

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the **root node reference** (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

- Search for a node to remove.

- If the node is found, delete the node.

### Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.

- `-10^5 <= Node.val <= 10^5`

- Each node has a **unique** value.

- `root` is a valid binary search tree.

- `-10^5 <= key <= 10^5`

**Follow up:** Could you solve it with time complexity `O(height of tree)`?

### Approach and complexity

Search using the BST ordering. A node with at most one child is replaced by that child; with two children, replace its value by its inorder successor and remove that successor.

Time O(h); auxiliary space O(h) for recursive calls.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return root;
        if (root->val > key) {
            root->left = deleteNode(root->left, key);
            return root;
        }
        if (root->val < key) {
            root->right = deleteNode(root->right, key);
            return root;
        }
        if (!root->left) return root->right;
        if (!root->right) return root->left;
        TreeNode* node = root->right;
        while (node->left) node = node->left;
        node->left = root->left;
        root = root->right;
        return root;
    }
};
```

---

<a id="lc-95"></a>
## 23. LC 95 — Unique Binary Search Trees II (Medium)

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

<a id="lc-96"></a>
## 24. LC 96 — Unique Binary Search Trees (Medium)

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

<a id="lc-144"></a>
## 25. LC 144 — Binary Tree Preorder Traversal (Easy)

[Official problem](https://leetcode.com/problems/binary-tree-preorder-traversal) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0144.Binary%20Tree%20Preorder%20Traversal/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`.

- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

### Approach and complexity

Morris traversal does not require a stack, and its space complexity is $O(1)$. The core idea is:

Traverse the binary tree nodes,

1. If the left subtree of the current node `root` is empty, add the current node value to the result list $\textit{ans}$, and update the current node to `root.right`.
1. If the left subtree of the current node `root` is not empty, find the rightmost node `pre` of the left subtree (which is the predecessor of the `root` node in inorder traversal):
    - If the right subtree of the predecessor node `pre` is empty, add the current node value to the result list $\textit{ans}$, then point the right subtree of the predecessor node to the current node `root`, and update the current node to `root.left`.
    - If the right subtree of the predecessor node `pre` is not empty, point the right subtree of the predecessor node to null (i.e., disconnect `pre` and `root`), and update the current node to `root.right`.
1. Repeat the above steps until the binary tree node is null, and the traversal ends.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        while (root) {
            if (!root->left) {
                ans.push_back(root->val);
                root = root->right;
            } else {
                TreeNode* prev = root->left;
                while (prev->right && prev->right != root) {
                    prev = prev->right;
                }
                if (!prev->right) {
                    ans.push_back(root->val);
                    prev->right = root;
                    root = root->left;
                } else {
                    prev->right = nullptr;
                    root = root->right;
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-145"></a>
## 26. LC 145 — Binary Tree Postorder Traversal (Easy)

[Official problem](https://leetcode.com/problems/binary-tree-postorder-traversal) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0145.Binary%20Tree%20Postorder%20Traversal/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

### Constraints

- The number of the nodes in the tree is in the range `[0, 100]`.

- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

### Approach and complexity

Morris traversal does not require a stack, and its space complexity is $O(1)$. The core idea is:

Traverse the binary tree nodes,

1. If the right subtree of the current node `root` is empty, add the current node value to the result list $\textit{ans}$, and update the current node to `root.left`.
1. If the right subtree of the current node `root` is not empty, find the leftmost node `next` of the right subtree (which is the successor of the `root` node in inorder traversal):
    - If the left subtree of the successor node `next` is empty, add the current node value to the result list $\textit{ans}$, then point the left subtree of the successor node to the current node `root`, and update the current node to `root.right`.
    - If the left subtree of the successor node `next` is not empty, point the left subtree of the successor node to null (i.e., disconnect `next` and `root`), and update the current node to `root.left`.
1. Repeat the above steps until the binary tree node is null, and the traversal ends.
1. Finally, return the reverse of the result list.

> The idea of Morris postorder traversal is consistent with Morris preorder traversal, just change the "root-left-right" of preorder to "root-right-left", and finally reverse the result to become "left-right-root".

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        while (root) {
            if (!root->right) {
                ans.push_back(root->val);
                root = root->left;
            } else {
                TreeNode* next = root->right;
                while (next->left && next->left != root) {
                    next = next->left;
                }
                if (next->left != root) {
                    ans.push_back(root->val);
                    next->left = root;
                    root = root->right;
                } else {
                    next->left = nullptr;
                    root = root->left;
                }
            }
        }
        ranges::reverse(ans);
        return ans;
    }
};
```

---

<a id="lc-199"></a>
## 27. LC 199 — Binary Tree Right Side View (Medium)

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

<a id="lc-103"></a>
## 28. LC 103 — Binary Tree Zigzag Level Order Traversal (Medium)

[Official problem](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0103.Binary%20Tree%20Zigzag%20Level%20Order%20Traversal/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- `-100 <= Node.val <= 100`

### Approach and complexity

To implement zigzag level order traversal, we need to add a flag `left` on the basis of level order traversal. This flag is used to mark the order of the node values in the current level. If `left` is `true`, the node values of the current level are stored in the result array `ans` from left to right. If `left` is `false`, the node values of the current level are stored in the result array `ans` from right to left.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (!root) {
            return ans;
        }
        queue<TreeNode*> q{{root}};
        int left = 1;
        while (!q.empty()) {
            vector<int> t;
            for (int n = q.size(); n; --n) {
                auto node = q.front();
                q.pop();
                t.emplace_back(node->val);
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            if (!left) {
                ranges::reverse(t);
            }
            ans.emplace_back(t);
            left ^= 1;
        }
        return ans;
    }
};
```

---

<a id="lc-111"></a>
## 29. LC 111 — Minimum Depth of Binary Tree (Easy)

[Official problem](https://leetcode.com/problems/minimum-depth-of-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0111.Minimum%20Depth%20of%20Binary%20Tree/README_EN.md)

### Problem description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

### Constraints

- The number of nodes in the tree is in the range `[0, 10^5]`.

- `-1000 <= Node.val <= 1000`

### Approach and complexity

Use a queue to implement breadth-first search, initially adding the root node to the queue. Each time, take a node from the queue. If this node is a leaf node, directly return the current depth. If this node is not a leaf node, add all non-null child nodes of this node to the queue. Continue to search the next layer of nodes until a leaf node is found.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) {
            return 0;
        }
        queue<TreeNode*> q{{root}};
        int ans = 0;
        while (1) {
            ++ans;
            for (int n = q.size(); n; --n) {
                auto node = q.front();
                q.pop();
                if (!node->left && !node->right) {
                    return ans;
                }
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
        }
    }
};
```

---

<a id="lc-257"></a>
## 30. LC 257 — Binary Tree Paths (Easy)

[Official problem](https://leetcode.com/problems/binary-tree-paths) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0257.Binary%20Tree%20Paths/README_EN.md)

### Problem description

You are given the `root` of a binary tree.

Return all **root-to-leaf** paths in **any order**.

A **leaf** is a node with no children.

### Constraints

- The number of nodes in the tree is in the range `[1, 100]`.

- `-100 <= Node.val <= 100`

### Approach and complexity

We can use depth-first search to traverse the entire binary tree. Each time, we add the current node to the path. If the current node is a leaf node, we add the entire path to the answer. Otherwise, we continue to recursively traverse the child nodes of the node. Finally, when the recursion ends and returns to the current node, we need to remove the current node from the path.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        vector<string> t;
        function<void(TreeNode*)> dfs = [&](TreeNode* root) {
            if (!root) {
                return;
            }
            t.push_back(to_string(root->val));
            if (!root->left && !root->right) {
                ans.push_back(join(t));
            } else {
                dfs(root->left);
                dfs(root->right);
            }
            t.pop_back();
        };
        dfs(root);
        return ans;
    }

    string join(vector<string>& t, string sep = "->") {
        string ans;
        for (int i = 0; i < t.size(); ++i) {
            if (i > 0) {
                ans += sep;
            }
            ans += t[i];
        }
        return ans;
    }
};
```

---

<a id="lc-129"></a>
## 31. LC 129 — Sum Root to Leaf Numbers (Medium)

[Official problem](https://leetcode.com/problems/sum-root-to-leaf-numbers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0129.Sum%20Root%20to%20Leaf%20Numbers/README_EN.md)

### Problem description

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

### Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.

- `0 <= Node.val <= 9`

- The depth of the tree will not exceed `10`.

### Approach and complexity

We can design a function $\textit{dfs}(\textit{root}, s)$, which represents the sum of all path numbers from the current node $\textit{root}$ to the leaf nodes, given that the current path number is $s$. The answer is $\textit{dfs}(\textit{root}, 0)$.

The calculation of the function $\textit{dfs}(\textit{root}, s)$ is as follows:

- If the current node $\textit{root}$ is null, return $0$.
- Otherwise, add the value of the current node to $s$, i.e., $s = s \times 10 + \textit{root}.\textit{val}$.
- If the current node is a leaf node, return $s$.
- Otherwise, return $\textit{dfs}(\textit{root}.\textit{left}, s) + \textit{dfs}(\textit{root}.\textit{right}, s)$.

The time complexity is $O(n)$, and the space complexity is $O(\log n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        function<int(TreeNode*, int)> dfs = [&](TreeNode* root, int s) -> int {
            if (!root) return 0;
            s = s * 10 + root->val;
            if (!root->left && !root->right) return s;
            return dfs(root->left, s) + dfs(root->right, s);
        };
        return dfs(root, 0);
    }
};
```

---

<a id="lc-437"></a>
## 32. LC 437 — Path Sum III (Medium)

[Official problem](https://leetcode.com/problems/path-sum-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0437.Path%20Sum%20III/README_EN.md)

### Problem description

Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values along the path equals `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

### Constraints

- The number of nodes in the tree is in the range `[0, 1000]`.

- `-10^9 <= Node.val <= 10^9`

- `-1000 <= targetSum <= 1000`

### Approach and complexity

We can use the idea of prefix sums to recursively traverse the binary tree while using a hash table $\textit{cnt}$ to count the occurrences of each prefix sum along the path from the root to the current node.

We design a recursive function $\textit{dfs}(\textit{node}, s)$, where $\textit{node}$ represents the current node being traversed, and $s$ represents the prefix sum along the path from the root to the current node. The return value of the function is the number of paths ending at $\textit{node}$ or its subtree nodes with a sum equal to $\textit{targetSum}$. The final answer is $\textit{dfs}(\textit{root}, 0)$.

The recursive process of $\textit{dfs}(\textit{node}, s)$ is as follows:

- If the current node $\textit{node}$ is null, return $0$.
- Calculate the prefix sum $s$ along the path from the root to the current node.
- Use $\textit{cnt}[s - \textit{targetSum}]$ to represent the number of paths ending at the current node with a sum equal to $\textit{targetSum}$. Here, $\textit{cnt}[s - \textit{targetSum}]$ is the count of prefix sums equal to $s - \textit{targetSum}$ in $\textit{cnt}$.
- Increment the count of the prefix sum $s$ by $1$, i.e., $\textit{cnt}[s] = \textit{cnt}[s] + 1$.
- Recursively traverse the left and right child nodes of the current node by calling $\textit{dfs}(\textit{node}.\textit{left}, s)$ and $\textit{dfs}(\textit{node}.\textit{right}, s)$, and add their return values.
- After the return value is calculated, decrement the count of the prefix sum $s$ by $1$, i.e., $\textit{cnt}[s] = \textit{cnt}[s] - 1$.
- Finally, return the result.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> cnt;
        cnt[0] = 1;
        auto dfs = [&](auto&& dfs, TreeNode* node, long long s) -> int {
            if (!node) {
                return 0;
            }
            s += node->val;
            int ans = cnt[s - targetSum];
            ++cnt[s];
            ans += dfs(dfs, node->left, s) + dfs(dfs, node->right, s);
            --cnt[s];
            return ans;
        };
        return dfs(dfs, root, 0);
    }
};
```

---

<a id="lc-572"></a>
## 33. LC 572 — Subtree of Another Tree (Easy)

[Official problem](https://leetcode.com/problems/subtree-of-another-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0572.Subtree%20of%20Another%20Tree/README_EN.md)

### Problem description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of` subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Constraints

- The number of nodes in the `root` tree is in the range `[1, 2000]`.

- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.

- `-10^4 <= root.val <= 10^4`

- `-10^4 <= subRoot.val <= 10^4`

### Approach and complexity

Preorder serialization including null markers uniquely encodes a tree. A subtree’s serialization is a contiguous token sequence in the full tree’s serialization. KMP finds it in linear time. Use a null token outside the int value domain and compare numeric tokens to avoid textual boundary collisions.

Time O(n+m); auxiliary space O(n+m), including explicit traversal stacks and token arrays.

### C++20 solution

```cpp
class Solution {
    vector<long long> serialize(TreeNode* root) {
        vector<long long> tokens;
        vector<TreeNode*> stack{root};
        while (!stack.empty()) {
            auto node = stack.back(); stack.pop_back();
            if (!node) { tokens.push_back(LLONG_MIN); continue; }
            tokens.push_back(node->val);
            stack.push_back(node->right); stack.push_back(node->left);
        }
        return tokens;
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        auto text = serialize(root), pattern = serialize(subRoot);
        vector<int> prefix(pattern.size());
        for (int i = 1, j = 0; i < static_cast<int>(pattern.size()); ++i) {
            while (j && pattern[i] != pattern[j]) j = prefix[j - 1];
            if (pattern[i] == pattern[j]) ++j;
            prefix[i] = j;
        }
        int j = 0;
        for (long long token : text) {
            while (j && token != pattern[j]) j = prefix[j - 1];
            if (token == pattern[j]) ++j;
            if (j == static_cast<int>(pattern.size())) return true;
        }
        return false;
    }
};
```

---

<a id="lc-617"></a>
## 34. LC 617 — Merge Two Binary Trees (Easy)

[Official problem](https://leetcode.com/problems/merge-two-binary-trees) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0617.Merge%20Two%20Binary%20Trees/README_EN.md)

### Problem description

You are given two binary trees `root1` and `root2`.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

**Note:** The merging process must start from the root nodes of both trees.

### Constraints

- The number of nodes in both trees is in the range `[0, 2000]`.

- `-10^4 <= Node.val <= 10^4`

### Approach and complexity

At overlapping nodes add values, and recursively merge corresponding children. If only one subtree exists, reuse it.

Time O(min(n,m)) over overlapping nodes, auxiliary space O(min(h₁,h₂)) for recursion. The output aliases and modifies input nodes.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if (!root1) return root2;
        if (!root2) return root1;
        TreeNode* node = new TreeNode(root1->val + root2->val);
        node->left = mergeTrees(root1->left, root2->left);
        node->right = mergeTrees(root1->right, root2->right);
        return node;
    }
};
```

---

<a id="lc-637"></a>
## 35. LC 637 — Average of Levels in Binary Tree (Easy)

[Official problem](https://leetcode.com/problems/average-of-levels-in-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0637.Average%20of%20Levels%20in%20Binary%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within `10^-5` of the actual answer will be accepted.

### Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.

- `-2^31 <= Node.val <= 2^31 - 1`

### Approach and complexity

We can use the Breadth-First Search (BFS) method to traverse the nodes of each level and calculate the average value of each level.

Specifically, we define a queue $q$, initially adding the root node to the queue. Each time, we take out all the nodes in the queue, calculate their average value, add it to the answer array, and then add their child nodes to the queue. Repeat this process until the queue is empty.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> q{{root}};
        vector<double> ans;
        while (!q.empty()) {
            int n = q.size();
            long long s = 0;
            for (int i = 0; i < n; ++i) {
                root = q.front();
                q.pop();
                s += root->val;
                if (root->left) {
                    q.push(root->left);
                }
                if (root->right) {
                    q.push(root->right);
                }
            }
            ans.push_back(s * 1.0 / n);
        }
        return ans;
    }
};
```

---

<a id="lc-662"></a>
## 36. LC 662 — Maximum Width of Binary Tree (Medium)

[Official problem](https://leetcode.com/problems/maximum-width-of-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0662.Maximum%20Width%20of%20Binary%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the **maximum width** of the given tree.

The **maximum width** of a tree is the maximum **width** among all levels.

The **width** of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is **guaranteed** that the answer will in the range of a **32-bit** signed integer.

### Constraints

- The number of nodes in the tree is in the range `[1, 3000]`.

- `-100 <= Node.val <= 100`

### Approach and complexity

Use complete-tree positions to account for gaps, but subtract the first position at each level before forming child positions. A 64-bit unsigned index also safely handles temporary child positions up to twice the guaranteed 32-bit width.

Time O(n); auxiliary space O(w), with w actual nodes in the widest BFS level.

### C++20 solution

```cpp
class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        queue<pair<TreeNode*, uint64_t>> queue;
        queue.emplace(root, 0);
        uint64_t best = 0;
        while (!queue.empty()) {
            uint64_t base = queue.front().second, last = 0;
            for (int size = queue.size(); size; --size) {
                auto [node, position] = queue.front(); queue.pop();
                position -= base; last = position;
                if (node->left) queue.emplace(node->left, 2 * position);
                if (node->right) queue.emplace(node->right, 2 * position + 1);
            }
            best = max(best, last + 1);
        }
        return static_cast<int>(best);
    }
};
```

---

<a id="lc-654"></a>
## 37. LC 654 — Maximum Binary Tree (Medium)

[Official problem](https://leetcode.com/problems/maximum-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0654.Maximum%20Binary%20Tree/README_EN.md)

### Problem description

You are given an integer array `nums` with no duplicates. A **maximum binary tree** can be built recursively from `nums` using the following algorithm:

- Create a root node whose value is the maximum value in `nums`.

- Recursively build the left subtree on the **subarray prefix** to the **left** of the maximum value.

- Recursively build the right subtree on the **subarray suffix** to the **right** of the maximum value.

Return the **maximum binary tree** built from `nums`.

### Constraints

- `1 <= nums.length <= 1000`

- `0 <= nums[i] <= 1000`

- All integers in `nums` are **unique**.

### Approach and complexity

A decreasing stack holds the current right spine. Pop smaller nodes into the new node’s left subtree; the remaining top’s right child becomes the new node. Each node is pushed and popped at most once.

Time O(n); auxiliary space O(n), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        stack<TreeNode*> stk;
        for (int v : nums) {
            TreeNode* node = new TreeNode(v);
            TreeNode* last = nullptr;
            while (!stk.empty() && stk.top()->val < v) {
                last = stk.top();
                stk.pop();
            }
            node->left = last;
            if (!stk.empty()) {
                stk.top()->right = node;
            }
            stk.push(node);
        }
        while (stk.size() > 1) {
            stk.pop();
        }
        return stk.top();
    }
};
```

---

<a id="lc-669"></a>
## 38. LC 669 — Trim a Binary Search Tree (Easy)

[Official problem](https://leetcode.com/problems/trim-a-binary-search-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0669.Trim%20a%20Binary%20Search%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary search tree and the lowest and highest boundaries as `low` and `high`, trim the tree so that all its elements lies in `[low, high]`. Trimming the tree should **not** change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a **unique answer**.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

### Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.

- `0 <= Node.val <= 10^4`

- The value of each node in the tree is **unique**.

- `root` is guaranteed to be a valid binary search tree.

- `0 <= low <= high <= 10^4`

### Approach and complexity

BST ordering lets a root below low discard its entire left subtree, and a root above high discard its entire right subtree. Recursively trim surviving branches.

Time O(n) worst case; auxiliary space O(h) for recursion.

### C++20 solution

```cpp
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        if (!root) return root;
        if (root->val > high) return trimBST(root->left, low, high);
        if (root->val < low) return trimBST(root->right, low, high);
        root->left = trimBST(root->left, low, high);
        root->right = trimBST(root->right, low, high);
        return root;
    }
};
```

---

<a id="lc-783"></a>
## 39. LC 783 — Minimum Distance Between BST Nodes (Easy)

[Official problem](https://leetcode.com/problems/minimum-distance-between-bst-nodes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0783.Minimum%20Distance%20Between%20BST%20Nodes/README_EN.md)

### Problem description

Given the `root` of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

### Constraints

- The number of nodes in the tree is in the range `[2, 100]`.

- `0 <= Node.val <= 10^5`

**Note:** This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

### Approach and complexity

The problem requires us to find the minimum difference between the values of any two nodes. Since the inorder traversal of a binary search tree is an increasing sequence, we only need to find the minimum difference between the values of two adjacent nodes in the inorder traversal.

We can use a recursive method to implement the inorder traversal. During the process, we use a variable $\textit{pre}$ to save the value of the previous node. This way, we can calculate the minimum difference between the values of two adjacent nodes during the traversal.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary search tree.

### C++20 solution

```cpp
class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        const int inf = 1 << 30;
        int ans = inf, pre = -inf;
        auto dfs = [&](auto&& dfs, TreeNode* root) -> void {
            if (!root) {
                return;
            }
            dfs(dfs, root->left);
            ans = min(ans, root->val - pre);
            pre = root->val;
            dfs(dfs, root->right);
        };
        dfs(dfs, root);
        return ans;
    }
};
```

---

<a id="lc-938"></a>
## 40. LC 938 — Range Sum of BST (Easy)

[Official problem](https://leetcode.com/problems/range-sum-of-bst) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0938.Range%20Sum%20of%20BST/README_EN.md)

### Problem description

Given the `root` node of a binary search tree and two integers `low` and `high`, return the sum of values of all nodes with a value in the **inclusive** range `[low, high]`.

### Constraints

- The number of nodes in the tree is in the range `[1, 2 * 10^4]`.

- `1 <= Node.val <= 10^5`

- `1 <= low <= high <= 10^5`

- All `Node.val` are **unique**.

### Approach and complexity

We design a function $\textit{dfs}(\textit{root})$, which represents the sum of the values of all nodes in the subtree with $\textit{root}$ as the root, and the values are within the range $[\textit{low}, \textit{high}]$. The answer is $\textit{dfs}(\textit{root})$.

The execution logic of the function $\textit{dfs}(\textit{root})$ is as follows:

- If $\textit{root}$ is null, return $0$.
- If the value $x$ of $\textit{root}$ is within the range $[\textit{low}, \textit{high}]$, then the initial answer of the function $\textit{dfs}(\textit{root})$ is $x$, otherwise it is $0$.
- If $x > \textit{low}$, it means that there may be nodes in the left subtree of $\textit{root}$ with values within the range $[\textit{low}, \textit{high}]$, so we need to recursively call $\textit{dfs}(\textit{root}.\textit{left})$ and add the result to the answer.
- If $x < \textit{high}$, it means that there may be nodes in the right subtree of $\textit{root}$ with values within the range $[\textit{low}, \textit{high}]$, so we need to recursively call $\textit{dfs}(\textit{root}.\textit{right})$ and add the result to the answer.
- Finally, return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary search tree.

### C++20 solution

```cpp
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        function<int(TreeNode*)> dfs = [&](TreeNode* root) {
            if (!root) {
                return 0;
            }
            int x = root->val;
            int ans = low <= x && x <= high ? x : 0;
            if (x > low) {
                ans += dfs(root->left);
            }
            if (x < high) {
                ans += dfs(root->right);
            }
            return ans;
        };
        return dfs(root);
    }
};
```

---

<a id="lc-987"></a>
## 41. LC 987 — Vertical Order Traversal of a Binary Tree (Hard)

[Official problem](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0987.Vertical%20Order%20Traversal%20of%20a%20Binary%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, calculate the **vertical order traversal** of the binary tree.

For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.

The **vertical order traversal** of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the **vertical order traversal** of the binary tree.

### Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.

- `0 <= Node.val <= 1000`

### Approach and complexity

We design a function $\textit{dfs}(\textit{root}, i, j)$, where $i$ and $j$ represent the row and column of the current node. We can record the row and column information of the nodes through depth-first search, store it in an array or list $\textit{nodes}$, and then sort $\textit{nodes}$ in the order of column, row, and value.

Next, we traverse $\textit{nodes}$, putting the values of nodes in the same column into the same list, and finally return these lists.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<tuple<int, int, int>> nodes;
        function<void(TreeNode*, int, int)> dfs = [&](TreeNode* root, int i, int j) {
            if (!root) {
                return;
            }
            nodes.emplace_back(j, i, root->val);
            dfs(root->left, i + 1, j - 1);
            dfs(root->right, i + 1, j + 1);
        };
        dfs(root, 0, 0);
        ranges::sort(nodes);
        vector<vector<int>> ans;
        int prev = -2000;
        for (auto [j, _, val] : nodes) {
            if (j != prev) {
                prev = j;
                ans.emplace_back();
            }
            ans.back().push_back(val);
        }
        return ans;
    }
};
```

---

<a id="lc-1026"></a>
## 42. LC 1026 — Maximum Difference Between Node and Ancestor (Medium)

[Official problem](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1026.Maximum%20Difference%20Between%20Node%20and%20Ancestor/README_EN.md)

### Problem description

Given the `root` of a binary tree, find the maximum value `v` for which there exist **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.

### Constraints

- The number of nodes in the tree is in the range `[2, 5000]`.

- `0 <= Node.val <= 10^5`

### Approach and complexity

For each node, to find the maximum difference with its ancestor nodes, we only need to find the difference between the maximum and minimum values of the ancestor nodes. The maximum difference among all nodes and their ancestor nodes is the answer.

Therefore, we design a function $\textit{dfs}(\textit{root}, mi, mx)$, where the current node being searched is $\textit{root}$, the maximum value of its ancestor nodes is $mx$, and the minimum value is $mi$. The function updates the maximum difference $\textit{ans}$.

The logic of the function $\textit{dfs}(\textit{root}, mi, mx)$ is as follows:

- If $\textit{root}$ is null, return directly.
- Otherwise, we update $\textit{ans} = \max(\textit{ans}, |mi - \textit{root}.\textit{val}|, |mx - \textit{root}.\textit{val}|)$.
- Then update $mi = \min(mi, \textit{root}.\textit{val})$, $mx = \max(mx, \textit{root}.\textit{val})$, and recursively search the left and right subtrees.

In the main function, we call $\textit{dfs}(\textit{root}, \textit{root}.\textit{val}, \textit{root}.\textit{val})$, and finally return $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        int ans = 0;
        function<void(TreeNode*, int, int)> dfs = [&](TreeNode* root, int mi, int mx) {
            if (!root) {
                return;
            }
            ans = max({ans, abs(mi - root->val), abs(mx - root->val)});
            mi = min(mi, root->val);
            mx = max(mx, root->val);
            dfs(root->left, mi, mx);
            dfs(root->right, mi, mx);
        };
        dfs(root, root->val, root->val);
        return ans;
    }
};
```

---

<a id="lc-114"></a>
## 43. LC 114 — Flatten Binary Tree to Linked List (Medium)

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
## 44. LC 116 — Populating Next Right Pointers in Each Node (Medium)

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

<a id="lc-173"></a>
## 45. LC 173 — Binary Search Tree Iterator (Medium)

[Official problem](https://leetcode.com/problems/binary-search-tree-iterator) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0173.Binary%20Search%20Tree%20Iterator/README_EN.md)

### Problem description

Implement the `BSTIterator` class that represents an iterator over the **in-order traversal** of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.

- `int next()` Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

### Constraints

- The number of nodes in the tree is in the range `[1, 10^5]`.

- `0 <= Node.val <= 10^6`

- At most `10^5` calls will be made to `hasNext`, and `next`.

**Follow up:**

- Could you implement `next()` and `hasNext()` to run in average `O(1)` time and use `O(h)` memory, where `h` is the height of the tree?

### Approach and complexity

Store the unvisited left spine. Pop its next node and push the left spine of that node’s right subtree.

Initialization O(h), next amortized O(1), O(h) worst case, hasNext O(1); persistent space O(h).

### C++20 solution

```cpp
class BSTIterator {
public:
    std::stack<TreeNode*> nodes;
    BSTIterator(TreeNode* root) {
        for (; root != nullptr; root = root->left) {
            nodes.push(root);
        }
    }

    int next() {
        TreeNode* cur = nodes.top();
        nodes.pop();
        TreeNode* node = cur->right;
        for (; node != nullptr; node = node->left) {
            nodes.push(node);
        }
        return cur->val;
    }

    bool hasNext() {
        return !nodes.empty();
    }
};
```

---

<a id="lc-222"></a>
## 46. LC 222 — Count Complete Tree Nodes (Easy)

[Official problem](https://leetcode.com/problems/count-complete-tree-nodes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0222.Count%20Complete%20Tree%20Nodes/README_EN.md)

### Problem description

Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

According to **Wikipedia**, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2^h` nodes inclusive at the last level `h`.

Design an algorithm that runs in less than O(n) time complexity.

### Constraints

- The number of nodes in the tree is in the range `[0, 5 * 10^4]`.

- `0 <= Node.val <= 5 * 10^4`

- The tree is guaranteed to be **complete**.

### Approach and complexity

For this problem, we can also take advantage of the characteristics of a complete binary tree to design a faster algorithm.

Characteristics of a complete binary tree: leaf nodes can only appear on the bottom and second-to-bottom layers, and the leaf nodes on the bottom layer are concentrated on the left side of the tree. It should be noted that a full binary tree is definitely a complete binary tree, but a complete binary tree is not necessarily a full binary tree.

If the number of layers in a full binary tree is $h$, then the total number of nodes is $2^h - 1$.

We first count the heights of the left and right subtrees of $\textit{root}$, denoted as $\textit{left}$ and $\textit{right}$.

1. If $\textit{left} = \textit{right}$, it means that the left subtree is a full binary tree, so the total number of nodes in the left subtree is $2^{\textit{left}} - 1$. Plus the $\textit{root}$ node, it is $2^{\textit{left}}$. Then we recursively count the right subtree.
1. If $\textit{left} > \textit{right}$, it means that the right subtree is a full binary tree, so the total number of nodes in the right subtree is $2^{\textit{right}} - 1$. Plus the $\textit{root}$ node, it is $2^{\textit{right}}$. Then we recursively count the left subtree.

The time complexity is $O(\log^2 n)$.

### C++20 solution

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (!root) {
            return 0;
        }
        int left = depth(root->left);
        int right = depth(root->right);
        if (left == right) {
            return (1 << left) + countNodes(root->right);
        }
        return (1 << right) + countNodes(root->left);
    }

    int depth(TreeNode* root) {
        int d = 0;
        for (; root; root = root->left) {
            ++d;
        }
        return d;
    }
};
```

---

<a id="lc-337"></a>
## 47. LC 337 — House Robber III (Medium)

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

<a id="lc-404"></a>
## 48. LC 404 — Sum of Left Leaves (Easy)

[Official problem](https://leetcode.com/problems/sum-of-left-leaves) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0404.Sum%20of%20Left%20Leaves/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the sum of all left leaves.

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.

### Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.

- `-1000 <= Node.val <= 1000`

### Approach and complexity

First, we check if `root` is null. If it is, we return $0$.

Otherwise, we recursively call the `sumOfLeftLeaves` function to calculate the sum of all left leaves in `root`'s right subtree, and assign the result to the answer variable $\textit{ans}$. Then we check if `root`'s left child exists. If it does, we check if it is a leaf node. If it is a leaf node, we add its value to the answer variable $\textit{ans}$. Otherwise, we recursively call the `sumOfLeftLeaves` function to calculate the sum of all left leaves in `root`'s left subtree, and add the result to the answer variable $\textit{ans}$.

Finally, we return the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (!root) {
            return 0;
        }
        int ans = sumOfLeftLeaves(root->right);
        if (root->left) {
            if (!root->left->left && !root->left->right) {
                ans += root->left->val;
            } else {
                ans += sumOfLeftLeaves(root->left);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-508"></a>
## 49. LC 508 — Most Frequent Subtree Sum (Medium)

[Official problem](https://leetcode.com/problems/most-frequent-subtree-sum) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0508.Most%20Frequent%20Subtree%20Sum/README_EN.md)

### Problem description

Given the `root` of a binary tree, return the most frequent **subtree sum**. If there is a tie, return all the values with the highest frequency in any order.

The **subtree sum** of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

### Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.

- `-10^5 <= Node.val <= 10^5`

### Approach and complexity

A hash table $\textit{cnt}$ records how often each subtree sum appears. An explicit stack walks the binary tree in postorder. On entry we push an exit marker, then the right child and the left child. On exit the children's sums are already stored, the current sum is those two plus the node value, and $\textit{cnt}$ is updated.

Finally we keep every subtree sum whose frequency is maximal.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        unordered_map<int, int> cnt;
        unordered_map<TreeNode*, int> sub;
        int mx = 0;
        vector<pair<TreeNode*, int>> stk{{root, 0}};
        while (!stk.empty()) {
            auto [node, state] = stk.back();
            stk.pop_back();
            if (!node) {
                continue;
            }
            if (state == 0) {
                stk.emplace_back(node, 1);
                if (node->right) {
                    stk.emplace_back(node->right, 0);
                }
                if (node->left) {
                    stk.emplace_back(node->left, 0);
                }
                continue;
            }
            int l = node->left ? sub[node->left] : 0;
            int r = node->right ? sub[node->right] : 0;
            int s = node->val + l + r;
            mx = max(mx, ++cnt[s]);
            sub[node] = s;
        }
        vector<int> ans;
        for (const auto& [k, v] : cnt) {
            if (v == mx) {
                ans.push_back(k);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-863"></a>
## 50. LC 863 — All Nodes Distance K in Binary Tree (Medium)

[Official problem](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0863.All%20Nodes%20Distance%20K%20in%20Binary%20Tree/README_EN.md)

### Problem description

Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

You can return the answer in **any order**.

### Constraints

- The number of nodes in the tree is in the range `[1, 500]`.

- `0 <= Node.val <= 500`

- All the values `Node.val` are **unique**.

- `target` is the value of one of the nodes in the tree.

- `0 <= k <= 1000`

### Approach and complexity

We first use DFS to traverse the entire tree and save each node's parent node in the hash table $g$.

Next, we use DFS again, starting from $\textit{target}$, to search for nodes at a distance of $k$ both upwards and downwards, and add them to the result array.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the binary tree.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        unordered_map<TreeNode*, TreeNode*> g;
        vector<int> ans;

        auto dfs = [&](auto&& dfs, TreeNode* node, TreeNode* fa) {
            if (!node) return;
            g[node] = fa;
            dfs(dfs, node->left, node);
            dfs(dfs, node->right, node);
        };

        auto dfs2 = [&](auto&& dfs2, TreeNode* node, TreeNode* fa, int k) {
            if (!node) return;
            if (k == 0) {
                ans.push_back(node->val);
                return;
            }
            for (auto&& nxt : {node->left, node->right, g[node]}) {
                if (nxt != fa) {
                    dfs2(dfs2, nxt, node, k - 1);
                }
            }
        };

        dfs(dfs, root, nullptr);
        dfs2(dfs2, target, nullptr, k);
        return ans;
    }
};
```
