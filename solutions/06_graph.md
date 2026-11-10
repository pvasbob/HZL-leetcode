# 6. Graph — C++20 solutions

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

1. [LC 200 — Number of Islands](#lc-200)
2. [LC 133 — Clone Graph](#lc-133)
3. [LC 207 — Course Schedule](#lc-207)
4. [LC 210 — Course Schedule II](#lc-210)
5. [LC 994 — Rotting Oranges](#lc-994)
6. [LC 547 — Number of Provinces](#lc-547)
7. [LC 695 — Max Area of Island](#lc-695)
8. [LC 417 — Pacific Atlantic Water Flow](#lc-417)
9. [LC 127 — Word Ladder](#lc-127)
10. [LC 752 — Open the Lock](#lc-752)
11. [LC 785 — Is Graph Bipartite?](#lc-785)
12. [LC 797 — All Paths From Source to Target](#lc-797)
13. [LC 841 — Keys and Rooms](#lc-841)
14. [LC 743 — Network Delay Time](#lc-743)
15. [LC 787 — Cheapest Flights Within K Stops](#lc-787)
16. [LC 1631 — Path With Minimum Effort](#lc-1631)
17. [LC 778 — Swim in Rising Water](#lc-778)
18. [LC 1584 — Min Cost to Connect All Points](#lc-1584)
19. [LC 684 — Redundant Connection](#lc-684)
20. [LC 721 — Accounts Merge](#lc-721)
21. [LC 399 — Evaluate Division](#lc-399)
22. [LC 909 — Snakes and Ladders](#lc-909)
23. [LC 1091 — Shortest Path in Binary Matrix](#lc-1091)
24. [LC 542 — 01 Matrix](#lc-542)
25. [LC 130 — Surrounded Regions](#lc-130)
26. [LC 733 — Flood Fill](#lc-733)
27. [LC 1971 — Find if Path Exists in Graph](#lc-1971)
28. [LC 1319 — Number of Operations to Make Network Connected](#lc-1319)
29. [LC 1466 — Reorder Routes to Make All Paths Lead to the City Zero](#lc-1466)
30. [LC 802 — Find Eventual Safe States](#lc-802)
31. [LC 886 — Possible Bipartition](#lc-886)
32. [LC 990 — Satisfiability of Equality Equations](#lc-990)
33. [LC 1192 — Critical Connections in a Network](#lc-1192)
34. [LC 332 — Reconstruct Itinerary](#lc-332)
35. [LC 269 — Alien Dictionary](#lc-269)
36. [LC 310 — Minimum Height Trees](#lc-310)
37. [LC 329 — Longest Increasing Path in a Matrix](#lc-329)
38. [LC 934 — Shortest Bridge](#lc-934)
39. [LC 1162 — As Far from Land as Possible](#lc-1162)
40. [LC 1926 — Nearest Exit from Entrance in Maze](#lc-1926)
41. [LC 433 — Minimum Genetic Mutation](#lc-433)
42. [LC 1129 — Shortest Path with Alternating Colors](#lc-1129)
43. [LC 1514 — Path with Maximum Probability](#lc-1514)
44. [LC 1361 — Validate Binary Tree Nodes](#lc-1361)
45. [LC 1376 — Time Needed to Inform All Employees](#lc-1376)
46. [LC 1791 — Find Center of Star Graph](#lc-1791)
47. [LC 1615 — Maximal Network Rank](#lc-1615)
48. [LC 2368 — Reachable Nodes With Restrictions](#lc-2368)
49. [LC 1557 — Minimum Number of Vertices to Reach All Nodes](#lc-1557)
50. [LC 1765 — Map of Highest Peak](#lc-1765)

---

<a id="lc-200"></a>
## 1. LC 200 — Number of Islands (Medium)

[Official problem](https://leetcode.com/problems/number-of-islands) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0200.Number%20of%20Islands/README_EN.md)

### Problem description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Constraints

- `m == grid.length`

- `n == grid[i].length`

- `1 <= m, n <= 300`

- `grid[i][j]` is `'0'` or `'1'`.

### Approach and complexity

Scan every cell. When the value is `'1'`, flood the island with an explicit stack, rewrite connected land to `'0'`, and add one to the answer.

The time complexity is $O(mn)$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns in the grid, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int ans = 0;
        int dirs[5] = {-1, 0, 1, 0, -1};
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != '1') {
                    continue;
                }
                vector<pair<int, int>> stk{{i, j}};
                grid[i][j] = '0';
                while (!stk.empty()) {
                    auto [a, b] = stk.back();
                    stk.pop_back();
                    for (int k = 0; k < 4; ++k) {
                        int x = a + dirs[k], y = b + dirs[k + 1];
                        if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == '1') {
                            grid[x][y] = '0';
                            stk.emplace_back(x, y);
                        }
                    }
                }
                ++ans;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-133"></a>
## 2. LC 133 — Clone Graph (Medium)

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

<a id="lc-207"></a>
## 3. LC 207 — Course Schedule (Medium)

[Official problem](https://leetcode.com/problems/course-schedule) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0207.Course%20Schedule/README_EN.md)

### Problem description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `b_i` first if you want to take course `a_i`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Constraints

- `1 <= numCourses <= 2000`

- `0 <= prerequisites.length <= 5000`

- `prerequisites[i].length == 2`

- `0 <= a_i, b_i < numCourses`

- All the pairs prerequisites[i] are **unique**.

### Approach and complexity

For this problem, we can consider the courses as nodes in a graph, and prerequisites as edges in the graph. Thus, we can transform this problem into determining whether there is a cycle in the directed graph.

Specifically, we can use the idea of topological sorting. For each node with an in-degree of $0$, we reduce the in-degree of its out-degree nodes by $1$, until all nodes have been traversed.

If all nodes have been traversed, it means there is no cycle in the graph, and we can complete all courses; otherwise, we cannot complete all courses.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the number of courses and prerequisites respectively.

### C++20 solution

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
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
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            --numCourses;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.push(j);
                }
            }
        }
        return numCourses == 0;
    }
};
```

---

<a id="lc-210"></a>
## 4. LC 210 — Course Schedule II (Medium)

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

<a id="lc-994"></a>
## 5. LC 994 — Rotting Oranges (Medium)

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

<a id="lc-547"></a>
## 6. LC 547 — Number of Provinces (Medium)

[Official problem](https://leetcode.com/problems/number-of-provinces) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0547.Number%20of%20Provinces/README_EN.md)

### Problem description

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i^th` city and the `j^th` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of **provinces**.

### Constraints

- `1 <= n <= 200`

- `n == isConnected.length`

- `n == isConnected[i].length`

- `isConnected[i][j]` is `1` or `0`.

- `isConnected[i][i] == 1`

- `isConnected[i][j] == isConnected[j][i]`

### Approach and complexity

We create an array $\textit{vis}$ to record whether each city has been visited.

Next, we traverse each city $i$. If the city has not been visited, we start a depth-first search from that city. Using the matrix $\textit{isConnected}$, we find the cities directly connected to this city. These cities and the current city belong to the same province. We continue the depth-first search for these cities until all cities in the same province have been visited. This counts as one province, so we increment the answer $\textit{ans}$ by $1$. Then, we move to the next unvisited city and repeat the process until all cities have been traversed.

Finally, return the answer.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the number of cities.

### C++20 solution

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        int ans = 0;
        vector<char> vis = vector<char>(n, 0);
        auto dfs = [&](auto&& dfs, int i) -> void {
            vis[i] = true;
            for (int j = 0; j < n; ++j) {
                if (!vis[j] && isConnected[i][j]) {
                    dfs(dfs, j);
                }
            }
        };
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                dfs(dfs, i);
                ++ans;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-695"></a>
## 7. LC 695 — Max Area of Island (Medium)

[Official problem](https://leetcode.com/problems/max-area-of-island) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0695.Max%20Area%20of%20Island/README_EN.md)

### Problem description

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return the maximum **area** of an island in `grid`. If there is no island, return `0`.

### Constraints

- `m == grid.length`

- `n == grid[i].length`

- `1 <= m, n <= 50`

- `grid[i][j]` is either `0` or `1`.

### Approach and complexity

Flood-fill each unvisited land component, marking cells once and counting its area. Return the maximum component size.

Time O(mn); auxiliary space O(mn) worst case for flood-fill traversal.

### C++20 solution

```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int dirs[5] = {-1, 0, 1, 0, -1};
        int ans = 0;
        function<int(int, int)> dfs = [&](int i, int j) {
            if (grid[i][j] == 0) {
                return 0;
            }
            int ans = 1;
            grid[i][j] = 0;
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    ans += dfs(x, y);
                }
            }
            return ans;
        };
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

<a id="lc-417"></a>
## 8. LC 417 — Pacific Atlantic Water Flow (Medium)

[Official problem](https://leetcode.com/problems/pacific-atlantic-water-flow) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0417.Pacific%20Atlantic%20Water%20Flow/README_EN.md)

### Problem description

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a **2D list** of grid coordinates `result` where `result[i] = [r_i, c_i]` denotes that rain water can flow from cell `(r_i, c_i)` to **both** the Pacific and Atlantic oceans.

### Constraints

- `m == heights.length`

- `n == heights[r].length`

- `1 <= m, n <= 200`

- `0 <= heights[r][c] <= 10^5`

### Approach and complexity

We can start from the boundaries of the Pacific and Atlantic oceans and perform breadth-first search (BFS) respectively to find all cells that can flow to the Pacific and Atlantic oceans. Finally, we take the intersection of the two results, which represents cells that can flow to both the Pacific and Atlantic oceans.

Specifically, we define a queue $q_1$ to store all cells adjacent to the Pacific ocean, and define a boolean matrix $\textit{vis}_1$ to record which cells can flow to the Pacific ocean. Similarly, we define queue $q_2$ and boolean matrix $\textit{vis}_2$ to handle the Atlantic ocean. Initially, we add all cells adjacent to the Pacific ocean to queue $q_1$ and mark them as visited in $\textit{vis}_1$. Similarly, we add all cells adjacent to the Atlantic ocean to queue $q_2$ and mark them as visited in $\textit{vis}_2$.

Then, we perform BFS on $q_1$ and $q_2$ respectively. In each BFS, we dequeue a cell $(x, y)$ from the queue and check its four adjacent cells $(nx, ny)$. If an adjacent cell is within the matrix bounds, has not been visited, and its height is not less than the current cell's height (i.e., water can flow to that cell), we add it to the queue and mark it as visited.

Finally, we traverse the entire matrix to find cells that are marked as visited in both $\textit{vis}_1$ and $\textit{vis}_2$. These cells are our answer.

The time complexity is $O(mn)$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns in the matrix, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> vis1(m, vector<bool>(n, false)), vis2(m, vector<bool>(n, false));
        queue<pair<int, int>> q1, q2;
        vector<int> dirs = {-1, 0, 1, 0, -1};

        for (int i = 0; i < m; ++i) {
            q1.emplace(i, 0);
            vis1[i][0] = true;
            q2.emplace(i, n - 1);
            vis2[i][n - 1] = true;
        }
        for (int j = 0; j < n; ++j) {
            q1.emplace(0, j);
            vis1[0][j] = true;
            q2.emplace(m - 1, j);
            vis2[m - 1][j] = true;
        }

        auto bfs = [&](queue<pair<int, int>>& q, vector<vector<bool>>& vis) {
            while (!q.empty()) {
                auto [x, y] = q.front();
                q.pop();
                for (int k = 0; k < 4; ++k) {
                    int nx = x + dirs[k], ny = y + dirs[k + 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n
                        && !vis[nx][ny]
                        && heights[nx][ny] >= heights[x][y]) {
                        vis[nx][ny] = true;
                        q.emplace(nx, ny);
                    }
                }
            }
        };

        bfs(q1, vis1);
        bfs(q2, vis2);

        vector<vector<int>> ans;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (vis1[i][j] && vis2[i][j])
                    ans.push_back({i, j});
        return ans;
    }
};
```

---

<a id="lc-127"></a>
## 9. LC 127 — Word Ladder (Hard)

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

<a id="lc-752"></a>
## 10. LC 752 — Open the Lock (Medium)

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

<a id="lc-785"></a>
## 11. LC 785 — Is Graph Bipartite? (Medium)

[Official problem](https://leetcode.com/problems/is-graph-bipartite) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0785.Is%20Graph%20Bipartite/README_EN.md)

### Problem description

There is an **undirected** graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. More formally, for each `v` in `graph[u]`, there is an undirected edge between node `u` and node `v`. The graph has the following properties:

- There are no self-edges (`graph[u]` does not contain `u`).

- There are no parallel edges (`graph[u]` does not contain duplicate values).

- If `v` is in `graph[u]`, then `u` is in `graph[v]` (the graph is undirected).

- The graph may not be connected, meaning there may be two nodes `u` and `v` such that there is no path between them.

A graph is **bipartite** if the nodes can be partitioned into two independent sets `A` and `B` such that **every** edge in the graph connects a node in set `A` and a node in set `B`.

Return `true` if and only if it is **bipartite**.

### Constraints

- `graph.length == n`

- `1 <= n <= 100`

- `0 <= graph[u].length < n`

- `0 <= graph[u][i] <= n - 1`

- `graph[u]` does not contain `u`.

- All the values of `graph[u]` are **unique**.

- If `graph[u]` contains `v`, then `graph[v]` contains `u`.

### Approach and complexity

Traverse all nodes for coloring. For example, initially color them white, and use DFS to color the adjacent nodes with another color. If the target color to be colored is different from the color that the node has already been colored, it means that it cannot form a bipartite graph.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes.

### C++20 solution

```cpp
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n);
        auto dfs = [&](auto&& dfs, int a, int c) -> bool {
            color[a] = c;
            for (int b : graph[a]) {
                if (color[b] == c || (color[b] == 0 && !dfs(dfs, b, -c))) {
                    return false;
                }
            }
            return true;
        };
        for (int i = 0; i < n; ++i) {
            if (color[i] == 0 && !dfs(dfs, i, 1)) {
                return false;
            }
        }
        return true;
    }
};
```

---

<a id="lc-797"></a>
## 12. LC 797 — All Paths From Source to Target (Medium)

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

<a id="lc-841"></a>
## 13. LC 841 — Keys and Rooms (Medium)

[Official problem](https://leetcode.com/problems/keys-and-rooms) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0841.Keys%20and%20Rooms/README_EN.md)

### Problem description

There are `n` rooms labeled from `0` to `n - 1` and all the rooms are locked except for room `0`. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of **distinct keys** in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array `rooms` where `rooms[i]` is the set of keys that you can obtain if you visited room `i`, return `true` if you can visit **all** the rooms, or `false` otherwise.

### Constraints

- `n == rooms.length`

- `2 <= n <= 1000`

- `0 <= rooms[i].length <= 1000`

- `1 <= sum(rooms[i].length) <= 3000`

- `0 <= rooms[i][j] < n`

- All the values of `rooms[i]` are **unique**.

### Approach and complexity

Start at room $0$ and walk the reachable rooms with an explicit stack. The stack begins with $0$. When room $i$ is popped, skip it if it has already been visited; otherwise mark it and push the room behind each key found in $i$. A repeated key only pushes that room again, and the later pop is skipped.

Finally, check whether every room was visited. If so, return true; otherwise some room cannot be reached.

The time complexity is $O(n + m)$, and the space complexity is $O(n)$, where $n$ is the number of nodes, and $m$ is the number of edges.

### C++20 solution

```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<char> vis(n);
        vector<int> stk = {0};
        while (!stk.empty()) {
            int i = stk.back();
            stk.pop_back();
            if (vis[i]) {
                continue;
            }
            vis[i] = 1;
            for (int j : rooms[i]) {
                stk.push_back(j);
            }
        }
        for (char v : vis) {
            if (!v) {
                return false;
            }
        }
        return true;
    }
};
```

---

<a id="lc-743"></a>
## 14. LC 743 — Network Delay Time (Medium)

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

<a id="lc-787"></a>
## 15. LC 787 — Cheapest Flights Within K Stops (Medium)

[Official problem](https://leetcode.com/problems/cheapest-flights-within-k-stops) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0787.Cheapest%20Flights%20Within%20K%20Stops/README_EN.md)

### Problem description

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return **the cheapest price** from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

### Constraints

- `2 <= n <= 100`

- `0 <= flights.length <= (n * (n - 1) / 2)`

- `flights[i].length == 3`

- `0 <= from_i, to_i < n`

- `from_i != to_i`

- `1 <= price_i <= 10^4`

- There will not be any multiple flights between two cities.

- `0 <= src, dst, k < n`

- `src != dst`

### Approach and complexity

Use k+1 Bellman–Ford rounds. Each round reads a frozen copy of previous distances so paths gain at most one edge per round; in-place reads would violate the stop limit.

Time O((k+1)E+n(k+1)); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        const int inf = 0x3f3f3f3f;
        vector<int> dist(n, inf);
        vector<int> backup;
        dist[src] = 0;
        for (int i = 0; i < k + 1; ++i) {
            backup = dist;
            for (auto& e : flights) {
                int f = e[0], t = e[1], p = e[2];
                dist[t] = min(dist[t], backup[f] + p);
            }
        }
        return dist[dst] == inf ? -1 : dist[dst];
    }
};
```

---

<a id="lc-1631"></a>
## 16. LC 1631 — Path With Minimum Effort (Medium)

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
## 17. LC 778 — Swim in Rising Water (Hard)

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

<a id="lc-1584"></a>
## 18. LC 1584 — Min Cost to Connect All Points (Medium)

[Official problem](https://leetcode.com/problems/min-cost-to-connect-all-points) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1500-1599/1584.Min%20Cost%20to%20Connect%20All%20Points/README_EN.md)

### Problem description

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x_i, y_i]`.

The cost of connecting two points `[x_i, y_i]` and `[x_j, y_j]` is the **manhattan distance** between them: `|x_i - x_j| + |y_i - y_j|`, where `|val|` denotes the absolute value of `val`.

Return the minimum cost to make all points connected. All points are connected if there is **exactly one** simple path between any two points.

### Constraints

- `1 <= points.length <= 1000`

- `-10^6 <= x_i, y_i <= 10^6`

- All pairs `(x_i, y_i)` are distinct.

### Approach and complexity

Maintain each unselected point’s cheapest Manhattan edge to the current tree. Select the minimum and update distances directly from coordinates. The cut property makes each chosen edge safe. Computing weights on demand avoids storing the complete graph.

Time O(n²); auxiliary space O(n). A Manhattan-MST sweep can achieve O(n log n) with substantially more complex candidate-edge generation; dense Prim is practical for n≤1000.

### C++20 solution

```cpp
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<int> distance(n, INT_MAX);
        vector<bool> used(n);
        distance[0] = 0;
        int cost = 0;
        for (int count = 0; count < n; ++count) {
            int v = -1;
            for (int i = 0; i < n; ++i)
                if (!used[i] && (v == -1 || distance[i] < distance[v])) v = i;
            used[v] = true;
            cost += distance[v];
            for (int i = 0; i < n; ++i)
                if (!used[i]) distance[i] = min(distance[i],
                    abs(points[i][0] - points[v][0]) + abs(points[i][1] - points[v][1]));
        }
        return cost;
    }
};
```

---

<a id="lc-684"></a>
## 19. LC 684 — Redundant Connection (Medium)

[Official problem](https://leetcode.com/problems/redundant-connection) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0600-0699/0684.Redundant%20Connection/README_EN.md)

### Problem description

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the graph.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

### Constraints

- `n == edges.length`

- `3 <= n <= 1000`

- `edges[i].length == 2`

- `1 <= a_i < b_i <= edges.length`

- `a_i != b_i`

- There are no repeated edges.

- The given graph is connected.

### Approach and complexity

According to the problem description, we need to find an edge that can be removed so that the remaining part is a tree with $n$ nodes. We can traverse each edge and determine whether the two nodes of this edge are in the same connected component. If they are in the same connected component, it means this edge is redundant and can be removed, so we directly return this edge. Otherwise, we merge the two nodes connected by this edge into the same connected component.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$, where $n$ is the number of edges.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> p(n);
        iota(p.begin(), p.end(), 0);
        function<int(int)> find = [&](int x) {
            return x == p[x] ? x : p[x] = find(p[x]);
        };
        for (int i = 0;; ++i) {
            int pa = find(edges[i][0] - 1);
            int pb = find(edges[i][1] - 1);
            if (pa == pb) {
                return edges[i];
            }
            p[pa] = pb;
        }
    }
};
```

---

<a id="lc-721"></a>
## 20. LC 721 — Accounts Merge (Medium)

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

<a id="lc-399"></a>
## 21. LC 399 — Evaluate Division (Medium)

[Official problem](https://leetcode.com/problems/evaluate-division) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0399.Evaluate%20Division/README_EN.md)

### Problem description

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [A_i, B_i]` and `values[i]` represent the equation `A_i / B_i = values[i]`. Each `A_i` or `B_i` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [C_j, D_j]` represents the `j^th` query where you must find the answer for `C_j / D_j = ?`.

Return the answers to all queries. If a single answer cannot be determined, return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

**Note: **The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

### Constraints

- `1 <= equations.length <= 20`

- `equations[i].length == 2`

- `1 <= A_i.length, B_i.length <= 5`

- `values.length == equations.length`

- `0.0 < values[i] <= 20.0`

- `1 <= queries.length <= 20`

- `queries[i].length == 2`

- `1 <= C_j.length, D_j.length <= 5`

- `A_i, B_i, C_j, D_j` consist of lower case English letters and digits.

### Approach and complexity

Weighted union-find stores the ratio from each variable to its representative. Joining an equation adjusts root weights; connected query variables have a ratio determined by their weights to the shared root.

For V variables, E equations, Q queries, conservative time O((E+Q)V) without rank balancing; path compression improves practice. Space O(V), including worst-case recursive find depth.

### C++20 solution

```cpp
class Solution {
public:
    unordered_map<string, string> p;
    unordered_map<string, double> w;

    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int n = equations.size();
        for (auto e : equations) {
            p[e[0]] = e[0];
            p[e[1]] = e[1];
            w[e[0]] = 1.0;
            w[e[1]] = 1.0;
        }
        for (int i = 0; i < n; ++i) {
            vector<string> e = equations[i];
            string a = e[0], b = e[1];
            string pa = find(a), pb = find(b);
            if (pa == pb) continue;
            p[pa] = pb;
            w[pa] = w[b] * values[i] / w[a];
        }
        int m = queries.size();
        vector<double> ans(m);
        for (int i = 0; i < m; ++i) {
            string c = queries[i][0], d = queries[i][1];
            ans[i] = p.find(c) == p.end() || p.find(d) == p.end() || find(c) != find(d) ? -1.0 : w[c] / w[d];
        }
        return ans;
    }

    string find(string x) {
        if (p[x] != x) {
            string origin = p[x];
            p[x] = find(p[x]);
            w[x] *= w[origin];
        }
        return p[x];
    }
};
```

---

<a id="lc-909"></a>
## 22. LC 909 — Snakes and Ladders (Medium)

[Official problem](https://leetcode.com/problems/snakes-and-ladders) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0909.Snakes%20and%20Ladders/README_EN.md)

### Problem description

You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n^2` in a **Boustrophedon style** starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square `1` of the board. In each move, starting from square `curr`, do the following:

- Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n^2)]`.

- This choice simulates the result of a standard **6-sided die roll**: i.e., there are always at most 6 destinations, regardless of the size of the board.

- If `next` has a snake or ladder, you **must** move to the destination of that snake or ladder. Otherwise, you move to `next`.

- The game ends when you reach the square `n^2`.

A board square on row `r` and column `c` has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n^2` are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do **not** follow the subsequent snake or ladder.

- For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your destination square is `2`. You follow the ladder to square `3`, but do **not** follow the subsequent ladder to `4`.

Return the least number of dice rolls required to reach the square `n^2`. If it is not possible to reach the square, return `-1`.

### Constraints

- `n == board.length == board[i].length`

- `2 <= n <= 20`

- `board[i][j]` is either `-1` or in the range `[1, n^2]`.

- The squares labeled `1` and `n^2` are not the starting points of any snake or ladder.

### Approach and complexity

We can use the Breadth-First Search (BFS) method, starting from the starting point, moving forward 1 to 6 steps each time, and then checking for snakes or ladders. If there are any, move to the destination of the snake or ladder; otherwise, move to the next square.

Specifically, we use a queue $q$ to store the current reachable square numbers, initially putting number $1$ into the queue. At the same time, we use a set $\textit{vis}$ to record the squares that have been reached to avoid revisiting them, initially adding number $1$ to the set $\textit{vis}$.

In each operation, we take out the square number $x$ at the front of the queue. If $x$ is the endpoint, we can return the current number of steps. Otherwise, we move $x$ forward 1 to 6 steps, setting the new number as $y$. If $y$ falls outside the board, we skip it directly. Otherwise, we need to find the row and column corresponding to $y$. Since the row numbers decrease from bottom to top, and the column numbers depend on the parity of the row, we need to perform some calculations to get the row and column corresponding to $y$.

If the square corresponding to $y$ has a snake or ladder, we need to move to the destination of the snake or ladder, denoted as $z$. If $z$ has not been visited, we add $z$ to the queue and set, allowing us to continue the breadth-first search.

If we ultimately cannot reach the endpoint, we return $-1$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$, where $n$ is the length of the side of the board.

### C++20 solution

```cpp
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        queue<int> q{{1}};
        int m = n * n;
        vector<bool> vis(m + 1);
        vis[1] = true;

        for (int ans = 0; !q.empty(); ++ans) {
            for (int k = q.size(); k > 0; --k) {
                int x = q.front();
                q.pop();
                if (x == m) {
                    return ans;
                }
                for (int y = x + 1; y <= min(x + 6, m); ++y) {
                    int i = (y - 1) / n, j = (y - 1) % n;
                    if (i % 2 == 1) {
                        j = n - j - 1;
                    }
                    i = n - i - 1;
                    int z = board[i][j] == -1 ? y : board[i][j];
                    if (!vis[z]) {
                        vis[z] = true;
                        q.push(z);
                    }
                }
            }
        }
        return -1;
    }
};
```

---

<a id="lc-1091"></a>
## 23. LC 1091 — Shortest Path in Binary Matrix (Medium)

[Official problem](https://leetcode.com/problems/shortest-path-in-binary-matrix) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1000-1099/1091.Shortest%20Path%20in%20Binary%20Matrix/README_EN.md)

### Problem description

Given an `n x n` binary matrix `grid`, return the length of the shortest **clear path** in the matrix. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

- All the visited cells of the path are `0`.

- All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

### Constraints

- `n == grid.length`

- `n == grid[i].length`

- `1 <= n <= 100`

- `grid[i][j] is 0 or 1`

### Approach and complexity

BFS on eight-direction moves starts at the open top-left cell. Mark cells when enqueued; BFS distance counts visited cells and the first bottom-right arrival is shortest.

Time O(n²); auxiliary space O(n²).

### C++20 solution

```cpp
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if (grid[0][0]) {
            return -1;
        }
        int n = grid.size();
        grid[0][0] = 1;
        queue<pair<int, int>> q;
        q.emplace(0, 0);
        for (int ans = 1; !q.empty(); ++ans) {
            for (int k = q.size(); k; --k) {
                auto [i, j] = q.front();
                q.pop();
                if (i == n - 1 && j == n - 1) {
                    return ans;
                }
                for (int x = i - 1; x <= i + 1; ++x) {
                    for (int y = j - 1; y <= j + 1; ++y) {
                        if (x >= 0 && x < n && y >= 0 && y < n && !grid[x][y]) {
                            grid[x][y] = 1;
                            q.emplace(x, y);
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```

---

<a id="lc-542"></a>
## 24. LC 542 — 01 Matrix (Medium)

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

<a id="lc-130"></a>
## 25. LC 130 — Surrounded Regions (Medium)

[Official problem](https://leetcode.com/problems/surrounded-regions) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0130.Surrounded%20Regions/README_EN.md)

### Problem description

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

- **Connect**: A cell is connected to adjacent cells horizontally or vertically.

- **Region**: To form a region **connect every** `'O'` cell.

- **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed **by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

### Constraints

- `m == board.length`

- `n == board[i].length`

- `1 <= m, n <= 200`

- `board[i][j]` is `'X'` or `'O'`.

### Approach and complexity

We can start from the boundary of the matrix, taking each 'O' on the matrix boundary as a starting point, and perform depth-first search. All 'O's found in the search are replaced with '.'.

Then we traverse the matrix again, for each position:

- If it is '.', replace it with 'O';
- Otherwise, if it is 'O', replace it with 'X'.

The time complexity is $O(mn)$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns in the matrix, respectively.

### C++20 solution

```cpp
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        int dirs[5] = {-1, 0, 1, 0, -1};
        function<void(int, int)> dfs = [&](int i, int j) {
            if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') {
                return;
            }
            board[i][j] = '.';
            for (int k = 0; k < 4; ++k) {
                dfs(i + dirs[k], j + dirs[k + 1]);
            }
        };
        for (int i = 0; i < m; ++i) {
            dfs(i, 0);
            dfs(i, n - 1);
        }
        for (int j = 1; j < n - 1; ++j) {
            dfs(0, j);
            dfs(m - 1, j);
        }
        for (auto& row : board) {
            for (auto& c : row) {
                if (c == '.') {
                    c = 'O';
                } else if (c == 'O') {
                    c = 'X';
                }
            }
        }
    }
};
```

---

<a id="lc-733"></a>
## 26. LC 733 — Flood Fill (Easy)

[Official problem](https://leetcode.com/problems/flood-fill) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0700-0799/0733.Flood%20Fill/README_EN.md)

### Problem description

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**:

- Begin with the starting pixel and change its color to `color`.

- Perform the same process for each pixel that is **directly adjacent** (pixels that share a side with the original pixel, either horizontally or vertically) and shares the **same color** as the starting pixel.

- Keep **repeating** this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.

- The process **stops** when there are **no more** adjacent pixels of the original color to update.

Return the **modified** image after performing the flood fill.

### Constraints

- `m == image.length`

- `n == image[i].length`

- `1 <= m, n <= 50`

- `0 <= image[i][j], color < 2^16`

- `0 <= sr < m`

- `0 <= sc < n`

### Approach and complexity

We first check if the initial pixel's color is equal to the target color. If it is, we return the original image directly. Otherwise, we can use the breadth-first search method, starting from $(sr, sc)$, to change the color of all eligible pixels to the target color.

Specifically, we define a queue $q$ and add the initial pixel $(sr, sc)$ to the queue. Then, we continuously take pixels $(i, j)$ from the queue, change their color to the target color, and add the pixels in the four directions (up, down, left, right) that have the same original color as the initial pixel to the queue. When the queue is empty, we have completed the flood fill.

The time complexity is $O(mn)$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns of the 2D array $\textit{image}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] == color) return image;
        int oc = image[sr][sc];
        image[sr][sc] = color;
        queue<pair<int, int>> q;
        q.push({sr, sc});
        int dirs[5] = {-1, 0, 1, 0, -1};
        while (!q.empty()) {
            auto [a, b] = q.front();
            q.pop();
            for (int k = 0; k < 4; ++k) {
                int x = a + dirs[k];
                int y = b + dirs[k + 1];
                if (x >= 0 && x < image.size() && y >= 0 && y < image[0].size() && image[x][y] == oc) {
                    q.push({x, y});
                    image[x][y] = color;
                }
            }
        }
        return image;
    }
};
```

---

<a id="lc-1971"></a>
## 27. LC 1971 — Find if Path Exists in Graph (Easy)

[Official problem](https://leetcode.com/problems/find-if-path-exists-in-graph) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1900-1999/1971.Find%20if%20Path%20Exists%20in%20Graph/README_EN.md)

### Problem description

There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u_i, v_i]` denotes a bi-directional edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` if there is a **valid path** from `source` to `destination`, or `false` otherwise.

### Constraints

- `1 <= n <= 2 * 10^5`

- `0 <= edges.length <= 2 * 10^5`

- `edges[i].length == 2`

- `0 <= u_i, v_i <= n - 1`

- `u_i != v_i`

- `0 <= source, destination <= n - 1`

- There are no duplicate edges.

- There are no self edges.

### Approach and complexity

We first convert $\textit{edges}$ into an adjacency list $g$. If $\textit{source}$ is $\textit{destination}$, we return $\textit{true}$ immediately. Otherwise an explicit stack starts at the source: a vertex is recorded in $\textit{vis}$ when it is pushed, a neighbor that is the destination returns $\textit{true}$, and only unmarked neighbors are pushed. An empty stack means there is no path.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the number of nodes and edges, respectively.

### C++20 solution

```cpp
class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if (source == destination) {
            return true;
        }
        vector<vector<int>> g(n);
        for (const auto& e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        vector<char> vis(n);
        vis[source] = 1;
        vector<int> stk{source};
        while (!stk.empty()) {
            int i = stk.back();
            stk.pop_back();
            for (int j : g[i]) {
                if (j == destination) {
                    return true;
                }
                if (!vis[j]) {
                    vis[j] = 1;
                    stk.push_back(j);
                }
            }
        }
        return false;
    }
};
```

---

<a id="lc-1319"></a>
## 28. LC 1319 — Number of Operations to Make Network Connected (Medium)

[Official problem](https://leetcode.com/problems/number-of-operations-to-make-network-connected) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1319.Number%20of%20Operations%20to%20Make%20Network%20Connected/README_EN.md)

### Problem description

There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between computers `a_i` and `b_i`. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `connections`. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return `-1`.

### Constraints

- `1 <= n <= 10^5`

- `1 <= connections.length <= min(n * (n - 1) / 2, 10^5)`

- `connections[i].length == 2`

- `0 <= a_i, b_i < n`

- `a_i != b_i`

- There are no repeated connections.

- No two computers are connected by more than one cable.

### Approach and complexity

We can use a union-find data structure to maintain the connectivity between computers. Traverse all connections, and for each connection $(a, b)$, if $a$ and $b$ are already connected, then this connection is redundant, and we increment the count of redundant connections. Otherwise, we connect $a$ and $b$, and decrement the number of connected components.

Finally, if the number of connected components minus one is greater than the number of redundant connections, it means we cannot connect all computers, so we return -1. Otherwise, we return the number of connected components minus one.

The time complexity is $O(m \log n)$, and the space complexity is $O(n)$, where $n$ and $m$ are the number of computers and the number of connections, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        vector<int> p(n);
        iota(p.begin(), p.end(), 0);
        int cnt = 0;
        function<int(int)> find = [&](int x) -> int {
            if (p[x] != x) {
                p[x] = find(p[x]);
            }
            return p[x];
        };
        for (const auto& c : connections) {
            int pa = find(c[0]), pb = find(c[1]);
            if (pa == pb) {
                ++cnt;
            } else {
                p[pa] = pb;
                --n;
            }
        }
        return cnt >= n - 1 ? n - 1 : -1;
    }
};
```

---

<a id="lc-1466"></a>
## 29. LC 1466 — Reorder Routes to Make All Paths Lead to the City Zero (Medium)

[Official problem](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1400-1499/1466.Reorder%20Routes%20to%20Make%20All%20Paths%20Lead%20to%20the%20City%20Zero/README_EN.md)

### Problem description

There are `n` cities numbered from `0` to `n - 1` and `n - 1` roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by `connections` where `connections[i] = [a_i, b_i]` represents a road from city `a_i` to city `b_i`.

This year, there will be a big event in the capital (city `0`), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city `0`. Return the **minimum** number of edges changed.

It's **guaranteed** that each city can reach city `0` after reorder.

### Constraints

- `2 <= n <= 5 * 10^4`

- `connections.length == n - 1`

- `connections[i].length == 2`

- `0 <= a_i, b_i <= n - 1`

- `a_i != b_i`

### Approach and complexity

The route map given in the problem has $n$ nodes and $n-1$ edges. If we ignore the direction of the edges, then these $n$ nodes form a tree. The problem requires us to change the direction of some edges so that each node can reach node $0$.

We might as well consider starting from node $0$ and reaching all other nodes. The direction is opposite to the problem description, which means that when we build the graph, for the directed edge $[a, b]$, we should regard it as the directed edge $[b, a]$. That is to say, if it is from $a$ to $b$, we need to change the direction once; if it is from $b$ to $a$, no direction change is needed.

An explicit stack walks the tree from node $0$. After a node is popped, each neighbor that is not the parent adds its edge weight to the answer and is pushed. A forward edge has weight $1$, and a reverse edge has weight $0$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes in the problem.

### C++20 solution

```cpp
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<vector<pair<int, int>>> g(n);
        for (auto& e : connections) {
            int a = e[0], b = e[1];
            g[a].emplace_back(b, 1);
            g[b].emplace_back(a, 0);
        }
        int ans = 0;
        vector<pair<int, int>> stk{{0, -1}};
        while (!stk.empty()) {
            auto cur = stk.back();
            stk.pop_back();
            int a = cur.first, fa = cur.second;
            for (auto& [b, c] : g[a]) {
                if (b != fa) {
                    ans += c;
                    stk.emplace_back(b, a);
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-802"></a>
## 30. LC 802 — Find Eventual Safe States (Medium)

[Official problem](https://leetcode.com/problems/find-eventual-safe-states) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0802.Find%20Eventual%20Safe%20States/README_EN.md)

### Problem description

There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`. The graph is represented by a **0-indexed** 2D integer array `graph` where `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in `graph[i]`.

A node is a **terminal node** if there are no outgoing edges. A node is a **safe node** if every possible path starting from that node leads to a **terminal node** (or another safe node).

Return an array containing all the **safe nodes** of the graph. The answer should be sorted in **ascending** order.

### Constraints

- `n == graph.length`

- `1 <= n <= 10^4`

- `0 <= graph[i].length <= n`

- `0 <= graph[i][j] <= n - 1`

- `graph[i]` is sorted in a strictly increasing order.

- The graph may contain self-loops.

- The number of edges in the graph will be in the range `[1, 4 * 10^4]`.

### Approach and complexity

Reverse every edge and peel terminal nodes using outdegree counts. A node becomes safe exactly when all its successors have been removed as safe. Cyclic nodes and nodes leading into cycles remain.

Time O(V+E); auxiliary space O(V+E).

### C++20 solution

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> indeg(n);
        vector<vector<int>> rg(n);
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            for (int j : graph[i]) rg[j].push_back(i);
            indeg[i] = graph[i].size();
            if (indeg[i] == 0) q.push(i);
        }
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            for (int j : rg[i])
                if (--indeg[j] == 0) q.push(j);
        }
        vector<int> ans;
        for (int i = 0; i < n; ++i)
            if (indeg[i] == 0) ans.push_back(i);
        return ans;
    }
};
```

---

<a id="lc-886"></a>
## 31. LC 886 — Possible Bipartition (Medium)

[Official problem](https://leetcode.com/problems/possible-bipartition) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0800-0899/0886.Possible%20Bipartition/README_EN.md)

### Problem description

We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

Given the integer `n` and the array `dislikes` where `dislikes[i] = [a_i, b_i]` indicates that the person labeled `a_i` does not like the person labeled `b_i`, return `true` if it is possible to split everyone into two groups in this way.

### Constraints

- `1 <= n <= 2000`

- `0 <= dislikes.length <= 10^4`

- `dislikes[i].length == 2`

- `1 <= a_i < b_i <= n`

- All the pairs of `dislikes` are **unique**.

### Approach and complexity

Color each connected component iteratively, assigning opposite colors across every edge. An edge joining equal colors proves no bipartition exists.

Time O(V+E); auxiliary space O(V+E), including adjacency lists and traversal stack.

### C++20 solution

```cpp
class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<vector<int>> g(n);
        for (auto& e : dislikes) {
            int a = e[0] - 1, b = e[1] - 1;
            g[a].push_back(b);
            g[b].push_back(a);
        }
        vector<int> color(n);
        for (int start = 0; start < n; ++start) {
            if (color[start]) {
                continue;
            }
            color[start] = 1;
            vector<int> stk{start};
            while (!stk.empty()) {
                int i = stk.back();
                stk.pop_back();
                for (int j : g[i]) {
                    if (color[j] == color[i]) {
                        return false;
                    }
                    if (color[j] == 0) {
                        color[j] = 3 - color[i];
                        stk.push_back(j);
                    }
                }
            }
        }
        return true;
    }
};
```

---

<a id="lc-990"></a>
## 32. LC 990 — Satisfiability of Equality Equations (Medium)

[Official problem](https://leetcode.com/problems/satisfiability-of-equality-equations) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0990.Satisfiability%20of%20Equality%20Equations/README_EN.md)

### Problem description

You are given an array of strings `equations` that represent relationships between variables where each string `equations[i]` is of length `4` and takes one of two different forms: `"x_i==y_i"` or `"x_i!=y_i"`.Here, `x_i` and `y_i` are lowercase letters (not necessarily different) that represent one-letter variable names.

Return `true` if it is possible to assign integers to variable names so as to satisfy all the given equations, or `false` otherwise.

### Constraints

- `1 <= equations.length <= 500`

- `equations[i].length == 4`

- `equations[i][0]` is a lowercase letter.

- `equations[i][1]` is either `'='` or `'!'`.

- `equations[i][2]` is `'='`.

- `equations[i][3]` is a lowercase letter.

### Approach and complexity

First unite variables constrained equal, then check all inequalities. An inequality inside one equality component is impossible.

Time O(E·A) is a conservative union-find bound without rank, and space O(A), with fixed A=26; under this alphabet it is O(E).

### C++20 solution

```cpp
class Solution {
public:
    vector<int> p;

    bool equationsPossible(vector<string>& equations) {
        p.resize(26);
        for (int i = 0; i < 26; ++i) p[i] = i;
        for (auto& e : equations) {
            int a = e[0] - 'a', b = e[3] - 'a';
            if (e[1] == '=') p[find(a)] = find(b);
        }
        for (auto& e : equations) {
            int a = e[0] - 'a', b = e[3] - 'a';
            if (e[1] == '!' && find(a) == find(b)) return false;
        }
        return true;
    }

    int find(int x) {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }
};
```

---

<a id="lc-1192"></a>
## 33. LC 1192 — Critical Connections in a Network (Hard)

[Official problem](https://leetcode.com/problems/critical-connections-in-a-network) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1100-1199/1192.Critical%20Connections%20in%20a%20Network/README_EN.md)

### Problem description

There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between servers `a_i` and `b_i`. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

### Constraints

- `2 <= n <= 10^5`

- `n - 1 <= connections.length <= 10^5`

- `0 <= a_i, b_i <= n - 1`

- `a_i != b_i`

- There are no repeated connections.

### Approach and complexity

Discovery times and low-link values identify bridges. On returning from child v to u, (u,v) is a bridge exactly when low[v]>discovery[u]. An explicit DFS stack avoids a possible 100000-frame recursion. Edge IDs distinguish the parent edge from other edges.

Time O(V+E); auxiliary space O(V+E).

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<pair<int, int>>> graph(n);
        for (int id = 0; id < static_cast<int>(connections.size()); ++id) {
            int a = connections[id][0], b = connections[id][1];
            graph[a].emplace_back(b, id); graph[b].emplace_back(a, id);
        }
        vector<int> discovery(n, -1), low(n), parent(n, -1), parentEdge(n, -1), next(n);
        vector<vector<int>> result;
        int timer = 0;
        for (int start = 0; start < n; ++start) {
            if (discovery[start] != -1) continue;
            vector<int> stack{start};
            discovery[start] = low[start] = timer++;
            while (!stack.empty()) {
                int u = stack.back();
                if (next[u] < static_cast<int>(graph[u].size())) {
                    auto [v, edge] = graph[u][next[u]++];
                    if (edge == parentEdge[u]) continue;
                    if (discovery[v] == -1) {
                        parent[v] = u; parentEdge[v] = edge;
                        discovery[v] = low[v] = timer++;
                        stack.push_back(v);
                    } else low[u] = min(low[u], discovery[v]);
                } else {
                    stack.pop_back();
                    if (parent[u] != -1) {
                        int p = parent[u];
                        if (low[u] > discovery[p]) result.push_back({p, u});
                        low[p] = min(low[p], low[u]);
                    }
                }
            }
        }
        return result;
    }
};
```

---

<a id="lc-332"></a>
## 34. LC 332 — Reconstruct Itinerary (Hard)

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

<a id="lc-269"></a>
## 35. LC 269 — Alien Dictionary (Hard)

[Official problem](https://leetcode.com/problems/alien-dictionary) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0269.Alien%20Dictionary/README_EN.md)

### Problem description

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are **sorted lexicographically** by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `"".`

Otherwise, return a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules. If there are multiple solutions, return **any of them**.

### Constraints

- `1 <= words.length <= 100`

- `1 <= words[i].length <= 100`

- `words[i]` consists of only lowercase English letters.

### Approach and complexity

Compare adjacent words: their first differing characters establish a directed alphabet edge. Reject a longer word before its exact prefix. Topological sorting gives a valid alphabet order; a cycle makes the input impossible.

Time O(S+A²), space O(A²), where S is total input length and A≤26 is alphabet size.

### C++20 solution

```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {
        vector<vector<bool>> g(26, vector<bool>(26));
        vector<bool> s(26);
        int cnt = 0;
        int n = words.size();
        for (int i = 0; i < n - 1; ++i) {
            for (char c : words[i]) {
                if (cnt == 26) break;
                c -= 'a';
                if (!s[c]) {
                    ++cnt;
                    s[c] = true;
                }
            }
            int m = words[i].size();
            for (int j = 0; j < m; ++j) {
                if (j >= words[i + 1].size()) return "";
                char c1 = words[i][j], c2 = words[i + 1][j];
                if (c1 == c2) continue;
                if (g[c2 - 'a'][c1 - 'a']) return "";
                g[c1 - 'a'][c2 - 'a'] = true;
                break;
            }
        }
        for (char c : words[n - 1]) {
            if (cnt == 26) break;
            c -= 'a';
            if (!s[c]) {
                ++cnt;
                s[c] = true;
            }
        }
        vector<int> indegree(26);
        for (int i = 0; i < 26; ++i)
            for (int j = 0; j < 26; ++j)
                if (i != j && s[i] && s[j] && g[i][j])
                    ++indegree[j];
        queue<int> q;
        for (int i = 0; i < 26; ++i)
            if (s[i] && indegree[i] == 0)
                q.push(i);
        string ans = "";
        while (!q.empty()) {
            int t = q.front();
            ans += (t + 'a');
            q.pop();
            for (int i = 0; i < 26; ++i)
                if (i != t && s[i] && g[t][i])
                    if (--indegree[i] == 0)
                        q.push(i);
        }
        return ans.size() < cnt ? "" : ans;
    }
};
```

---

<a id="lc-310"></a>
## 36. LC 310 — Minimum Height Trees (Medium)

[Official problem](https://leetcode.com/problems/minimum-height-trees) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0310.Minimum%20Height%20Trees/README_EN.md)

### Problem description

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labelled from `0` to `n - 1`, and an array of `n - 1` `edges` where `edges[i] = [a_i, b_i]` indicates that there is an undirected edge between the two nodes `a_i` and `b_i` in the tree, you can choose any node of the tree as the root. When you select a node `x` as the root, the result tree has height `h`. Among all possible rooted trees, those with minimum height (i.e. `min(h)`) are called **minimum height trees** (MHTs).

Return a list of all **MHTs'** root labels. You can return the answer in **any order**.

The **height** of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

### Constraints

- `1 <= n <= 2 * 10^4`

- `edges.length == n - 1`

- `0 <= a_i, b_i < n`

- `a_i != b_i`

- All the pairs `(a_i, b_i)` are distinct.

- The given input is **guaranteed** to be a tree and there will be **no repeated** edges.

### Approach and complexity

If the tree only has one node, then this node is the root of the minimum height tree. We can directly return this node.

If the tree has multiple nodes, there must be leaf nodes. A leaf node is a node that only has one adjacent node. We can use topological sorting to peel off the leaf nodes from the outside to the inside. When we reach the last layer, the remaining nodes are the root nodes of the minimum height tree.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) {
            return {0};
        }
        vector<vector<int>> g(n);
        vector<int> degree(n);
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            g[a].push_back(b);
            g[b].push_back(a);
            ++degree[a];
            ++degree[b];
        }
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (degree[i] == 1) {
                q.push(i);
            }
        }
        vector<int> ans;
        while (!q.empty()) {
            ans.clear();
            for (int i = q.size(); i > 0; --i) {
                int a = q.front();
                q.pop();
                ans.push_back(a);
                for (int b : g[a]) {
                    if (--degree[b] == 1) {
                        q.push(b);
                    }
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-329"></a>
## 37. LC 329 — Longest Increasing Path in a Matrix (Hard)

[Official problem](https://leetcode.com/problems/longest-increasing-path-in-a-matrix) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0329.Longest%20Increasing%20Path%20in%20a%20Matrix/README_EN.md)

### Problem description

Given an `m x n` integers `matrix`, return the length of the longest increasing path in `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

### Constraints

- `m == matrix.length`

- `n == matrix[i].length`

- `1 <= m, n <= 200`

- `0 <= matrix[i][j] <= 2^31 - 1`

### Approach and complexity

Direct edges from smaller cells to larger neighbors. Start with cells having no smaller neighbors and repeatedly remove an entire frontier. The number of layers is the longest increasing path because each layer extends the longest predecessor chain by one.

Time O(mn); auxiliary space O(mn). Avoids recursion depth proportional to the number of cells.

### C++20 solution

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        constexpr array<int, 5> direction{-1, 0, 1, 0, -1};
        vector<vector<int>> degree(m, vector<int>(n));
        queue<pair<int, int>> ready;
        for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) {
            for (int k = 0; k < 4; ++k) {
                int x = i + direction[k], y = j + direction[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] < matrix[i][j]) ++degree[i][j];
            }
            if (!degree[i][j]) ready.emplace(i, j);
        }
        int layers = 0;
        while (!ready.empty()) {
            ++layers;
            for (int size = ready.size(); size; --size) {
                auto [i, j] = ready.front(); ready.pop();
                for (int k = 0; k < 4; ++k) {
                    int x = i + direction[k], y = j + direction[k + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] > matrix[i][j] && --degree[x][y] == 0)
                        ready.emplace(x, y);
                }
            }
        }
        return layers;
    }
};
```

---

<a id="lc-934"></a>
## 38. LC 934 — Shortest Bridge (Medium)

[Official problem](https://leetcode.com/problems/shortest-bridge) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0934.Shortest%20Bridge/README_EN.md)

### Problem description

You are given an `n x n` binary matrix `grid` where `1` represents land and `0` represents water.

An **island** is a 4-directionally connected group of `1`'s not connected to any other `1`'s. There are **exactly two islands** in `grid`.

You may change `0`'s to `1`'s to connect the two islands to form **one island**.

Return the smallest number of `0`'s you must flip to connect the two islands.

### Constraints

- `n == grid.length == grid[i].length`

- `2 <= n <= 100`

- `grid[i][j]` is either `0` or `1`.

- There are exactly two islands in `grid`.

### Approach and complexity

Mark the first island and seed BFS with its cells. Expand across water until reaching the second island; the number of water layers crossed is the minimum flips.

Time O(n²); auxiliary space O(n²), including flood-fill/BFS state.

### C++20 solution

```cpp
class Solution {
public:
    const static inline vector<int> dirs = {-1, 0, 1, 0, -1};

    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size();
        queue<pair<int, int>> q;
        function<void(int, int)> dfs = [&](int i, int j) {
            grid[i][j] = 2;
            q.emplace(i, j);
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == 1) {
                    dfs(x, y);
                }
            }
        };
        for (int i = 0, x = 1; i < n && x; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) {
                    dfs(i, j);
                    x = 0;
                    break;
                }
            }
        }
        int ans = 0;
        while (1) {
            for (int h = q.size(); h; --h) {
                auto [i, j] = q.front();
                q.pop();
                for (int k = 0; k < 4; ++k) {
                    int x = i + dirs[k], y = j + dirs[k + 1];
                    if (x >= 0 && x < n && y >= 0 && y < n) {
                        if (grid[x][y] == 1) return ans;
                        if (grid[x][y] == 0) {
                            grid[x][y] = 2;
                            q.emplace(x, y);
                        }
                    }
                }
            }
            ++ans;
        }
    }
};
```

---

<a id="lc-1162"></a>
## 39. LC 1162 — As Far from Land as Possible (Medium)

[Official problem](https://leetcode.com/problems/as-far-from-land-as-possible) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1100-1199/1162.As%20Far%20from%20Land%20as%20Possible/README_EN.md)

### Problem description

Given an `n x n` `grid` containing only values `0` and `1`, where `0` represents water and `1` represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return `-1`.

The distance used in this problem is the Manhattan distance: the distance between two cells `(x0, y0)` and `(x1, y1)` is `|x0 - x1| + |y0 - y1|`.

### Constraints

- `n == grid.length`

- `n == grid[i].length`

- `1 <= n <= 100`

- `grid[i][j]` is `0` or `1`

### Approach and complexity

We can add all land cells to the queue $q$. If the queue is empty, or the number of elements in the queue equals the number of cells in the grid, it means that the grid contains only land or ocean, so return $-1$.

Otherwise, we start BFS from the land cells. Define the initial step count $\textit{ans}=-1$.

In each round of search, we spread all cells in the queue in four directions. If a cell is an ocean cell, we mark it as a land cell and add it to the queue. After a round of spreading, we increase the step count by $1$. Repeat this process until the queue is empty.

Finally, we return the step count $\textit{ans}$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$, where $n$ is the side length of the grid.

### C++20 solution

```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size();
        queue<pair<int, int>> q;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) {
                    q.emplace(i, j);
                }
            }
        }
        int ans = -1;
        if (q.empty() || q.size() == n * n) {
            return ans;
        }
        int dirs[5] = {-1, 0, 1, 0, -1};
        while (!q.empty()) {
            for (int m = q.size(); m; --m) {
                auto [i, j] = q.front();
                q.pop();
                for (int k = 0; k < 4; ++k) {
                    int x = i + dirs[k], y = j + dirs[k + 1];
                    if (x >= 0 && x < n && y >= 0 && y < n && !grid[x][y]) {
                        grid[x][y] = 1;
                        q.emplace(x, y);
                    }
                }
            }
            ++ans;
        }
        return ans;
    }
};
```

---

<a id="lc-1926"></a>
## 40. LC 1926 — Nearest Exit from Entrance in Maze (Medium)

[Official problem](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1900-1999/1926.Nearest%20Exit%20from%20Entrance%20in%20Maze/README_EN.md)

### Problem description

You are given an `m x n` matrix `maze` (**0-indexed**) with empty cells (represented as `'.'`) and walls (represented as `'+'`). You are also given the `entrance` of the maze, where `entrance = [entrance_row, entrance_col]` denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell **up**, **down**, **left**, or **right**. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the **nearest exit** from the `entrance`. An **exit** is defined as an **empty cell** that is at the **border** of the `maze`. The `entrance` **does not count** as an exit.

Return the **number of steps** in the shortest path from the `entrance` to the nearest exit, or `-1` if no such path exists.

### Constraints

- `maze.length == m`

- `maze[i].length == n`

- `1 <= m, n <= 100`

- `maze[i][j]` is either `'.'` or `'+'`.

- `entrance.length == 2`

- `0 <= entrance_row < m`

- `0 <= entrance_col < n`

- `entrance` will always be an empty cell.

### Approach and complexity

We can start from the entrance and perform a breadth-first search (BFS). Each time we reach a new empty cell, we mark it as visited and add it to the queue until we find an empty cell on the boundary, then return the number of steps.

Specifically, we define a queue $q$, initially adding $\textit{entrance}$ to the queue. We define a variable $\textit{ans}$ to record the number of steps, initially set to $1$. Then we start the BFS. In each round, we take out all elements from the queue and traverse them. For each element, we try to move in four directions. If the new position is an empty cell, we add it to the queue and mark it as visited. If the new position is an empty cell on the boundary, we return $\textit{ans}$. If the queue is empty, we return $-1$. After this round of search, we increment $\textit{ans}$ by one and continue to the next round of search.

If we finish the traversal without finding an empty cell on the boundary, we return $-1$.

The time complexity is $O(mn)$, and the space complexity is $O(mn)$, where $m$ and $n$ are the number of rows and columns in the maze, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size(), n = maze[0].size();
        int dirs[5] = {-1, 0, 1, 0, -1};
        queue<pair<int, int>> q;
        q.emplace(entrance[0], entrance[1]);
        maze[entrance[0]][entrance[1]] = '+';
        for (int ans = 1; !q.empty(); ++ans) {
            for (int k = q.size(); k; --k) {
                auto [i, j] = q.front();
                q.pop();
                for (int d = 0; d < 4; ++d) {
                    int x = i + dirs[d], y = j + dirs[d + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == '.') {
                        if (x == 0 || x == m - 1 || y == 0 || y == n - 1) {
                            return ans;
                        }
                        maze[x][y] = '+';
                        q.emplace(x, y);
                    }
                }
            }
        }
        return -1;
    }
};
```

---

<a id="lc-433"></a>
## 41. LC 433 — Minimum Genetic Mutation (Medium)

[Official problem](https://leetcode.com/problems/minimum-genetic-mutation) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0433.Minimum%20Genetic%20Mutation/README_EN.md)

### Problem description

A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `startGene` to a gene string `endGene` where one mutation is defined as one single character changed in the gene string.

- For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in `bank` to make it a valid gene string.

Given the two gene strings `startGene` and `endGene` and the gene bank `bank`, return the minimum number of mutations needed to mutate from `startGene` to `endGene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

### Constraints

- `0 <= bank.length <= 10`

- `startGene.length == endGene.length == bank[i].length == 8`

- `startGene`, `endGene`, and `bank[i]` consist of only the characters `['A', 'C', 'G', 'T']`.

### Approach and complexity

We define a queue `q` to store the current gene sequence and the number of changes, and a set `vis` to store the visited gene sequences. Initially, we add the starting gene sequence `start` to the queue `q` and the set `vis`.

Then, we continuously take out a gene sequence from the queue `q`. If this gene sequence equals the target gene sequence, we return the current number of changes. Otherwise, we iterate through the gene bank `bank`, calculate the difference value between the current gene sequence and the gene sequence in the gene bank. If the difference value is $1$ and the gene sequence in the gene bank has not been visited, we add it to the queue `q` and the set `vis`.

If the queue `q` is empty, it means that the gene change cannot be completed, so we return $-1$.

The time complexity is $O(C \times nm)$, and the space complexity is $O(nm)$, where $n$ and $m$ are the lengths of the gene sequence and the gene bank respectively, and $C$ is the size of the character set of the gene sequence. In this problem, $C = 4$.

### C++20 solution

```cpp
class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        queue<pair<string, int>> q{{{startGene, 0}}};
        unordered_set<string> vis = {startGene};
        while (!q.empty()) {
            auto [gene, depth] = q.front();
            q.pop();
            if (gene == endGene) {
                return depth;
            }
            for (const string& next : bank) {
                int c = 2;
                for (int k = 0; k < 8 && c; ++k) {
                    c -= gene[k] != next[k];
                }
                if (c && !vis.contains(next)) {
                    vis.insert(next);
                    q.push({next, depth + 1});
                }
            }
        }
        return -1;
    }
};
```

---

<a id="lc-1129"></a>
## 42. LC 1129 — Shortest Path with Alternating Colors (Medium)

[Official problem](https://leetcode.com/problems/shortest-path-with-alternating-colors) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1100-1199/1129.Shortest%20Path%20with%20Alternating%20Colors/README_EN.md)

### Problem description

You are given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to `n - 1`. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays `redEdges` and `blueEdges` where:

- `redEdges[i] = [a_i, b_i]` indicates that there is a directed red edge from node `a_i` to node `b_i` in the graph, and

- `blueEdges[j] = [u_j, v_j]` indicates that there is a directed blue edge from node `u_j` to node `v_j` in the graph.

Return an array `answer` of length `n`, where each `answer[x]` is the length of the shortest path from node `0` to node `x` such that the edge colors alternate along the path, or `-1` if such a path does not exist.

### Constraints

- `1 <= n <= 100`

- `0 <= redEdges.length, blueEdges.length <= 400`

- `redEdges[i].length == blueEdges[j].length == 2`

- `0 <= a_i, b_i, u_j, v_j < n`

### Approach and complexity

The problem is essentially a shortest path problem, which we can consider solving using BFS.

First, we preprocess all the edges, categorizing all the edges by color and storing them in a multi-dimensional array $g$. Where $g[0]$ stores all red edges, and $g[1]$ stores all blue edges.

Next, we define the following data structures or variables:

- Queue $q$: used to store the currently searched node and the color of the current edge;
- Set $\textit{vis}$: used to store the nodes that have been searched and the color of the current edge;
- Variable $d$: used to represent the current search level, i.e., the distance from the currently searched node to the starting point;
- Array $\textit{ans}$: used to store the shortest distance from each node to the starting point. Initially, we initialize all elements in the $\textit{ans}$ array to $-1$, indicating that the distance from all nodes to the starting point is unknown.

We first enqueue the starting point $0$ and the color of the starting edge $0$ or $1$, indicating that we start from the starting point and the current edge is red or blue.

Next, we start the BFS search. Each time we take out a node $(i, c)$ from the queue, if the answer of the current node has not been updated, then we update the answer of the current node to the current level $d$, i.e., $\textit{ans}[i] = d$. Then, we flip the color of the current edge $c$, i.e., if the current edge is red, we change it to blue, and vice versa. We take out all edges corresponding to the color, if the other end node $j$ of the edge has not been searched, then we enqueue it.

After the search is over, return the answer array.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$, where $n$ and $m$ are the number of nodes and edges, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
        vector<vector<vector<int>>> g(2, vector<vector<int>>(n));
        for (auto& e : redEdges) {
            g[0][e[0]].push_back(e[1]);
        }
        for (auto& e : blueEdges) {
            g[1][e[0]].push_back(e[1]);
        }
        queue<pair<int, int>> q;
        q.emplace(0, 0);
        q.emplace(0, 1);
        vector<vector<char>> vis = vector<vector<char>>(n, vector<char>(2, 0));
        vector<int> ans(n, -1);
        int d = 0;
        while (!q.empty()) {
            for (int k = q.size(); k; --k) {
                auto [i, c] = q.front();
                q.pop();
                if (ans[i] == -1) {
                    ans[i] = d;
                }
                vis[i][c] = true;
                c ^= 1;
                for (int& j : g[c][i]) {
                    if (!vis[j][c]) {
                        q.emplace(j, c);
                    }
                }
            }
            ++d;
        }
        return ans;
    }
};
```

---

<a id="lc-1514"></a>
## 43. LC 1514 — Path with Maximum Probability (Medium)

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

<a id="lc-1361"></a>
## 44. LC 1361 — Validate Binary Tree Nodes (Medium)

[Official problem](https://leetcode.com/problems/validate-binary-tree-nodes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1361.Validate%20Binary%20Tree%20Nodes/README_EN.md)

### Problem description

You have `n` binary tree nodes numbered from `0` to `n - 1` where node `i` has two children `leftChild[i]` and `rightChild[i]`, return `true` if and only if **all** the given nodes form **exactly one** valid binary tree.

If node `i` has no left child then `leftChild[i]` will equal `-1`, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

### Constraints

- `n == leftChild.length == rightChild.length`

- `1 <= n <= 10^4`

- `-1 <= leftChild[i], rightChild[i] <= n - 1`

### Approach and complexity

We can first count the indegree of each node, i.e., how many parents point to it. If there is no node with indegree $0$, it means there is a cycle in the graph, so we return `false` directly; otherwise, that node is the root.

Next, we perform a breadth-first search starting from the root. During the traversal, if a child node has already been visited, it means the node has multiple parents or there is a cycle in the graph, so we return `false` directly.

After the traversal, we check whether the number of visited nodes equals $n$. If so, all nodes form exactly one valid binary tree and we return `true`; otherwise, we return `false`.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes.

### C++20 solution

```cpp
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        vector<int> indeg(n, 0);
        for (int c : leftChild) {
            if (c != -1) {
                indeg[c]++;
            }
        }
        for (int c : rightChild) {
            if (c != -1) {
                indeg[c]++;
            }
        }

        int root = -1;
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) {
                root = i;
                break;
            }
        }
        if (root == -1) {
            return false;
        }

        queue<int> q;
        unordered_set<int> vis;

        q.push(root);
        vis.insert(root);

        while (!q.empty()) {
            int i = q.front();
            q.pop();

            int j = leftChild[i];
            if (j != -1) {
                if (vis.count(j)) {
                    return false;
                }
                vis.insert(j);
                q.push(j);
            }

            j = rightChild[i];
            if (j != -1) {
                if (vis.count(j)) {
                    return false;
                }
                vis.insert(j);
                q.push(j);
            }
        }

        return vis.size() == n;
    }
};
```

---

<a id="lc-1376"></a>
## 45. LC 1376 — Time Needed to Inform All Employees (Medium)

[Official problem](https://leetcode.com/problems/time-needed-to-inform-all-employees) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1376.Time%20Needed%20to%20Inform%20All%20Employees/README_EN.md)

### Problem description

A company has `n` employees with a unique ID for each employee from `0` to `n - 1`. The head of the company is the one with `headID`.

Each employee has one direct manager given in the `manager` array where `manager[i]` is the direct manager of the `i-th` employee, `manager[headID] = -1`. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The `i-th` employee needs `informTime[i]` minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

### Constraints

- `1 <= n <= 10^5`

- `0 <= headID < n`

- `manager.length == n`

- `0 <= manager[i] < n`

- `manager[headID] == -1`

- `informTime.length == n`

- `0 <= informTime[i] <= 1000`

- `informTime[i] == 0` if employee `i` has no subordinates.

- It is **guaranteed** that all the employees can be informed.

### Approach and complexity

We first build an adjacent list $g$ according to the $\textit{manager}$ array, where $g[i]$ represents all direct subordinates of employee $i$.

The time for employee $i$ to inform the whole subtree is $\textit{informTime}[i]$ plus the maximum time among the direct reports, or $0$ when there are no reports. An explicit stack walks from $\textit{headID}$ in postorder and writes that time when the node is left. The answer is the head's time.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of employees.

### C++20 solution

```cpp
class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        vector<vector<int>> g(n);
        for (int i = 0; i < n; ++i) {
            if (manager[i] >= 0) {
                g[manager[i]].push_back(i);
            }
        }
        vector<int> time(n);
        vector<array<int, 2>> stk{{headID, 0}};
        while (!stk.empty()) {
            auto [i, state] = stk.back();
            stk.pop_back();
            if (state == 0) {
                stk.push_back({i, 1});
                for (int j : g[i]) {
                    stk.push_back({j, 0});
                }
            } else {
                int ans = 0;
                for (int j : g[i]) {
                    ans = max(ans, time[j] + informTime[i]);
                }
                time[i] = ans;
            }
        }
        return time[headID];
    }
};
```

---

<a id="lc-1791"></a>
## 46. LC 1791 — Find Center of Star Graph (Easy)

[Official problem](https://leetcode.com/problems/find-center-of-star-graph) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1791.Find%20Center%20of%20Star%20Graph/README_EN.md)

### Problem description

There is an undirected **star** graph consisting of `n` nodes labeled from `1` to `n`. A star graph is a graph where there is one **center** node and **exactly** `n - 1` edges that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [u_i, v_i]` indicates that there is an edge between the nodes `u_i` and `v_i`. Return the center of the given star graph.

### Constraints

- `3 <= n <= 10^5`

- `edges.length == n - 1`

- `edges[i].length == 2`

- `1 <= u_i, v_i <= n`

- `u_i != v_i`

- The given `edges` represent a valid star graph.

### Approach and complexity

The characteristic of the center point is that it is connected to all other points. Therefore, as long as we compare the points of the first two edges, if there are the same points, then this point is the center point.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int a = edges[0][0], b = edges[0][1];
        int c = edges[1][0], d = edges[1][1];
        return a == c || a == d ? a : b;
    }
};
```

---

<a id="lc-1615"></a>
## 47. LC 1615 — Maximal Network Rank (Medium)

[Official problem](https://leetcode.com/problems/maximal-network-rank) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1600-1699/1615.Maximal%20Network%20Rank/README_EN.md)

### Problem description

There is an infrastructure of `n` cities with some number of `roads` connecting these cities. Each `roads[i] = [a_i, b_i]` indicates that there is a bidirectional road between cities `a_i` and `b_i`.

The **network rank** of **two different cities** is defined as the total number of **directly** connected roads to **either** city. If a road is directly connected to both cities, it is only counted **once**.

The **maximal network rank **of the infrastructure is the **maximum network rank** of all pairs of different cities.

Given the integer `n` and the array `roads`, return the **maximal network rank** of the entire infrastructure.

### Constraints

- `2 <= n <= 100`

- `0 <= roads.length <= n * (n - 1) / 2`

- `roads[i].length == 2`

- `0 <= a_i, b_i <= n-1`

- `a_i != b_i`

- Each pair of cities has **at most one** road connecting them.

### Approach and complexity

We can use a one-dimensional array $\textit{cnt}$ to record the degree of each city and a two-dimensional array $g$ to record whether there is a road between each pair of cities. If there is a road between city $a$ and city $b$, then $g[a][b] = g[b][a] = 1$; otherwise, $g[a][b] = g[b][a] = 0$.

Next, we enumerate each pair of cities $(a, b)$, where $a \lt b$, and calculate their network rank, which is $\textit{cnt}[a] + \textit{cnt}[b] - g[a][b]$. The maximum value among these is the answer.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$, where $n$ is the number of cities.

### C++20 solution

```cpp
class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<int> cnt = vector<int>(n, 0);
        vector<vector<int>> g = vector<vector<int>>(n, vector<int>(n, 0));
        for (auto& r : roads) {
            int a = r[0], b = r[1];
            g[a][b] = g[b][a] = 1;
            ++cnt[a];
            ++cnt[b];
        }
        int ans = 0;
        for (int a = 0; a < n; ++a) {
            for (int b = a + 1; b < n; ++b) {
                ans = max(ans, cnt[a] + cnt[b] - g[a][b]);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-2368"></a>
## 48. LC 2368 — Reachable Nodes With Restrictions (Medium)

[Official problem](https://leetcode.com/problems/reachable-nodes-with-restrictions) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2300-2399/2368.Reachable%20Nodes%20With%20Restrictions/README_EN.md)

### Problem description

There is an undirected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given a 2D integer array `edges` of length `n - 1` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree. You are also given an integer array `restricted` which represents **restricted** nodes.

Return the **maximum** number of nodes you can reach from node `0` without visiting a restricted node.

Note that node `0` will **not** be a restricted node.

### Constraints

- `2 <= n <= 10^5`

- `edges.length == n - 1`

- `edges[i].length == 2`

- `0 <= a_i, b_i < n`

- `a_i != b_i`

- `edges` represents a valid tree.

- `1 <= restricted.length < n`

- `1 <= restricted[i] < n`

- All the values of `restricted` are **unique**.

### Approach and complexity

First, we construct an adjacency list $g$ based on the given edges, where $g[i]$ represents the list of nodes adjacent to node $i$. Then we define a hash table $\textit{vis}$ to record the restricted nodes or nodes that have been visited, and initially add the restricted nodes to $\textit{vis}$.

Next, an explicit stack walks from node $0$. When node $i$ is popped and still unvisited, we add it to $\textit{vis}$, count it, and push its unvisited neighbors.

Finally, we return the number of nodes counted.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of nodes.

### C++20 solution

```cpp
class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        vector<vector<int>> g(n);
        vector<int> vis(n);
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            g[a].emplace_back(b);
            g[b].emplace_back(a);
        }
        for (int i : restricted) {
            vis[i] = true;
        }
        int ans = 0;
        vector<int> stk{0};
        while (!stk.empty()) {
            int i = stk.back();
            stk.pop_back();
            if (vis[i]) {
                continue;
            }
            vis[i] = true;
            ++ans;
            for (int j : g[i]) {
                if (!vis[j]) {
                    stk.emplace_back(j);
                }
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1557"></a>
## 49. LC 1557 — Minimum Number of Vertices to Reach All Nodes (Medium)

[Official problem](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1500-1599/1557.Minimum%20Number%20of%20Vertices%20to%20Reach%20All%20Nodes/README_EN.md)

### Problem description

Given a** directed acyclic graph**, with `n` vertices numbered from `0` to `n-1`, and an array `edges` where `edges[i] = [from_i, to_i]` represents a directed edge from node `from_i` to node `to_i`.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

### Constraints

- `2 <= n <= 10^5`

- `1 <= edges.length <= min(10^5, n * (n - 1) / 2)`

- `edges[i].length == 2`

- `0 <= from_i, to_i < n`

- All pairs `(from_i, to_i)` are distinct.

### Approach and complexity

In a DAG every zero-indegree vertex must be chosen because no other vertex reaches it. Starting from all such vertices reaches every remaining vertex by following a topological order.

Time O(V+E); auxiliary space O(V), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> cnt(n);
        for (auto& e : edges) {
            ++cnt[e[1]];
        }
        vector<int> ans;
        for (int i = 0; i < n; ++i) {
            if (cnt[i] == 0) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
```

---

<a id="lc-1765"></a>
## 50. LC 1765 — Map of Highest Peak (Medium)

[Official problem](https://leetcode.com/problems/map-of-highest-peak) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1700-1799/1765.Map%20of%20Highest%20Peak/README_EN.md)

### Problem description

You are given an integer matrix `isWater` of size `m x n` that represents a map of **land** and **water** cells.

- If `isWater[i][j] == 0`, cell `(i, j)` is a **land** cell.

- If `isWater[i][j] == 1`, cell `(i, j)` is a **water** cell.

You must assign each cell a height in a way that follows these rules:

- The height of each cell must be non-negative.

- If the cell is a **water** cell, its height must be `0`.

- Any two adjacent cells must have an absolute height difference of **at most** `1`. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is **maximized**.

Return an integer matrix `height` of size `m x n` where `height[i][j]` is cell `(i, j)`'s height. If there are multiple solutions, return **any** of them.

### Constraints

- `m == isWater.length`

- `n == isWater[i].length`

- `1 <= m, n <= 1000`

- `isWater[i][j]` is `0` or `1`.

- There is at least **one** water cell.

**Note:** This question is the same as 542: https://leetcode.com/problems/01-matrix/

### Approach and complexity

All water cells start at height zero in a multi-source BFS. Assign unvisited neighbors one greater than their predecessor. Distance to the nearest water is the largest height compatible with all adjacent-difference constraints.

Time O(mn); auxiliary space O(mn), excluding output.

### C++20 solution

```cpp
class Solution {
public:
    const int dirs[5] = {-1, 0, 1, 0, -1};

    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int m = isWater.size(), n = isWater[0].size();
        vector<vector<int>> ans(m, vector<int>(n));
        queue<pair<int, int>> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans[i][j] = isWater[i][j] - 1;
                if (ans[i][j] == 0) {
                    q.emplace(i, j);
                }
            }
        }
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && ans[x][y] == -1) {
                    ans[x][y] = ans[i][j] + 1;
                    q.emplace(x, y);
                }
            }
        }
        return ans;
    }
};
```
