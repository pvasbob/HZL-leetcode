# 12. Bit Manipulation & Math — C++20 solutions

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

1. [LC 136 — Single Number](#lc-136)
2. [LC 191 — Number of 1 Bits](#lc-191)
3. [LC 338 — Counting Bits](#lc-338)
4. [LC 190 — Reverse Bits](#lc-190)
5. [LC 268 — Missing Number](#lc-268)
6. [LC 371 — Sum of Two Integers](#lc-371)
7. [LC 201 — Bitwise AND of Numbers Range](#lc-201)
8. [LC 231 — Power of Two](#lc-231)
9. [LC 342 — Power of Four](#lc-342)
10. [LC 326 — Power of Three](#lc-326)
11. [LC 461 — Hamming Distance](#lc-461)
12. [LC 477 — Total Hamming Distance](#lc-477)
13. [LC 137 — Single Number II](#lc-137)
14. [LC 260 — Single Number III](#lc-260)
15. [LC 287 — Find the Duplicate Number](#lc-287)
16. [LC 29 — Divide Two Integers](#lc-29)
17. [LC 7 — Reverse Integer](#lc-7)
18. [LC 9 — Palindrome Number](#lc-9)
19. [LC 50 — Pow(x, n)](#lc-50)
20. [LC 69 — Sqrt(x)](#lc-69)
21. [LC 204 — Count Primes](#lc-204)
22. [LC 202 — Happy Number](#lc-202)
23. [LC 172 — Factorial Trailing Zeroes](#lc-172)
24. [LC 66 — Plus One](#lc-66)
25. [LC 67 — Add Binary](#lc-67)
26. [LC 43 — Multiply Strings](#lc-43)
27. [LC 415 — Add Strings](#lc-415)
28. [LC 989 — Add to Array-Form of Integer](#lc-989)
29. [LC 8 — String to Integer (atoi)](#lc-8)
30. [LC 13 — Roman to Integer](#lc-13)
31. [LC 12 — Integer to Roman](#lc-12)
32. [LC 168 — Excel Sheet Column Title](#lc-168)
33. [LC 171 — Excel Sheet Column Number](#lc-171)
34. [LC 118 — Pascal's Triangle](#lc-118)
35. [LC 119 — Pascal's Triangle II](#lc-119)
36. [LC 62 — Unique Paths](#lc-62)
37. [LC 96 — Unique Binary Search Trees](#lc-96)
38. [LC 89 — Gray Code](#lc-89)
39. [LC 78 — Subsets](#lc-78)
40. [LC 1863 — Sum of All Subset XOR Totals](#lc-1863)
41. [LC 1318 — Minimum Flips to Make a OR b Equal to c](#lc-1318)
42. [LC 2220 — Minimum Bit Flips to Convert Number](#lc-2220)
43. [LC 2433 — Find The Original Array of Prefix Xor](#lc-2433)
44. [LC 1442 — Count Triplets That Can Form Two Arrays of Equal XOR](#lc-1442)
45. [LC 1310 — XOR Queries of a Subarray](#lc-1310)
46. [LC 421 — Maximum XOR of Two Numbers in an Array](#lc-421)
47. [LC 2013 — Detect Squares](#lc-2013)
48. [LC 149 — Max Points on a Line](#lc-149)
49. [LC 223 — Rectangle Area](#lc-223)
50. [LC 593 — Valid Square](#lc-593)

---

<a id="lc-136"></a>
## 1. LC 136 — Single Number (Easy)

[Official problem](https://leetcode.com/problems/single-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0136.Single%20Number/README_EN.md)

### Problem description

Given a **non-empty** array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

### Constraints

- `1 <= nums.length <= 3 * 10^4`

- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

- Each element in the array appears twice except for one element which appears only once.

### Approach and complexity

The XOR operation has the following properties:

- Any number XOR 0 is still the original number, i.e., $x \oplus 0 = x$;
- Any number XOR itself is 0, i.e., $x \oplus x = 0$;

Performing XOR operation on all elements in the array will result in the number that only appears once.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int v : nums) {
            ans ^= v;
        }
        return ans;
    }
};
```

---

<a id="lc-191"></a>
## 2. LC 191 — Number of 1 Bits (Easy)

[Official problem](https://leetcode.com/problems/number-of-1-bits) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0191.Number%20of%201%20Bits/README_EN.md)

### Problem description

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

### Constraints

- `1 <= n <= 2^31 - 1`

**Follow up:** If this function is called many times, how would you optimize it?

### Approach and complexity

popcount counts set bits of the unsigned word directly, allowing the implementation to use a hardware population-count instruction when available.

Time O(1) for the fixed 32-bit input; auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) { return std::popcount(n); }
};
```

---

<a id="lc-338"></a>
## 3. LC 338 — Counting Bits (Easy)

[Official problem](https://leetcode.com/problems/counting-bits) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0338.Counting%20Bits/README_EN.md)

### Problem description

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the **number of **`1`**'s** in the binary representation of `i`.

Do not solve it with built-in functions (i.e., like `__builtin_popcount` in C++).

### Constraints

- `0 <= n <= 10^5`

**Follow up:**

- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?

### Approach and complexity

Removing the lowest set bit gives a smaller integer with one fewer set bit. Reuse that already computed answer.

Time O(n); auxiliary space O(1) beyond the returned n+1 counts.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1);
        for (int i = 1; i <= n; ++i) {
            ans[i] = ans[i & (i - 1)] + 1;
        }
        return ans;
    }
};
```

---

<a id="lc-190"></a>
## 4. LC 190 — Reverse Bits (Easy)

[Official problem](https://leetcode.com/problems/reverse-bits) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0190.Reverse%20Bits/README_EN.md)

### Problem description

Reverse bits of a given 32 bits signed integer.

### Constraints

- `0 <= n <= 2^31 - 2`

- `n` is even.

**Follow up:** If this function is called many times, how would you optimize it?

### Approach and complexity

We can extract each bit of $n$ from the lowest bit to the highest bit, and then place it at the corresponding position of $\textit{ans}$.

For example, for the $i$-th bit, we can extract the $i$-th bit of $n$ and place it at the $(31 - i)$-th bit of $\textit{ans}$ by $(n \& 1) \ll (31 - i)$, and then right shift $n$ by one bit.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans = 0;
        for (int i = 0; i < 32 && n; ++i) {
            ans |= (n & 1) << (31 - i);
            n >>= 1;
        }
        return ans;
    }
};
```

---

<a id="lc-268"></a>
## 5. LC 268 — Missing Number (Easy)

[Official problem](https://leetcode.com/problems/missing-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0268.Missing%20Number/README_EN.md)

### Problem description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

### Constraints

- `n == nums.length`

- `1 <= n <= 10^4`

- `0 <= nums[i] <= n`

- All the numbers of `nums` are **unique**.

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

### Approach and complexity

The XOR operation has the following properties:

- Any number XOR 0 is still the original number, i.e., $x \oplus 0 = x$;
- Any number XOR itself is 0, i.e., $x \oplus x = 0$;

Therefore, we can traverse the array, perform XOR operation between each element and the numbers $[0,..n]$, and the final result will be the missing number.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int ans = n;
        for (int i = 0; i < n; ++i) {
            ans ^= (i ^ nums[i]);
        }
        return ans;
    }
};
```

---

<a id="lc-371"></a>
## 6. LC 371 — Sum of Two Integers (Medium)

[Official problem](https://leetcode.com/problems/sum-of-two-integers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0371.Sum%20of%20Two%20Integers/README_EN.md)

### Problem description

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

### Constraints

- `-1000 <= a, b <= 1000`

### Approach and complexity

XOR adds bits without carries; the shifted AND supplies carries. Repeat until no carry remains. Use unsigned arithmetic to avoid signed left-shift undefined behavior.

Time O(w), auxiliary space O(1), for fixed word width w=32.

### C++20 solution

```cpp
class Solution {
public:
    int getSum(int a, int b) {
        while (b) {
            unsigned int carry = (unsigned int) (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
};
```

---

<a id="lc-201"></a>
## 7. LC 201 — Bitwise AND of Numbers Range (Medium)

[Official problem](https://leetcode.com/problems/bitwise-and-of-numbers-range) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0201.Bitwise%20AND%20of%20Numbers%20Range/README_EN.md)

### Problem description

Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

### Constraints

- `0 <= left <= right <= 2^31 - 1`

### Approach and complexity

Remove differing low bits until the bounds share their highest common prefix, then restore the removed zero bits. Any varying lower bit becomes zero in the interval AND.

Time O(w), auxiliary space O(1), with w≤31 for the stated nonnegative bounds.

### C++20 solution

```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        while (left < right) {
            right &= (right - 1);
        }
        return right;
    }
};
```

---

<a id="lc-231"></a>
## 8. LC 231 — Power of Two (Easy)

[Official problem](https://leetcode.com/problems/power-of-two) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0231.Power%20of%20Two/README_EN.md)

### Problem description

Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2^x`.

### Constraints

- `-2^31 <= n <= 2^31 - 1`

**Follow up:** Could you solve it without loops/recursion?

### Approach and complexity

According to the properties of bit manipulation, executing $\texttt{n\&(n-1)}$ can eliminate the last bit $1$ in the binary form of $n$. Therefore, if $n > 0$ and $\texttt{n\&(n-1)}$ results in $0$, then $n$ is a power of $2$.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
};
```

---

<a id="lc-342"></a>
## 9. LC 342 — Power of Four (Easy)

[Official problem](https://leetcode.com/problems/power-of-four) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0342.Power%20of%20Four/README_EN.md)

### Problem description

Given an integer `n`, return `true` if it is a power of four. Otherwise, return `false`.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4^x`.

### Constraints

- `-2^31 <= n <= 2^31 - 1`

**Follow up:** Could you solve it without loops/recursion?

### Approach and complexity

If a number is a power of $4$, then it must be greater than $0$. Suppose this number is $4^x$, which is $2^{2x}$. Therefore, its binary representation has only one $1$, and this $1$ appears at an even position.

First, we check if the number is greater than $0$. Then, we verify if the number is $2^{2x}$ by checking if the bitwise AND of $n$ and $n-1$ is $0$. Finally, we check if the $1$ appears at an even position by verifying if the bitwise AND of $n$ and `0xAAAAAAAA` is $0$. If all three conditions are met, then the number is a power of $4$.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    bool isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0xaaaaaaaa) == 0;
    }
};
```

---

<a id="lc-326"></a>
## 10. LC 326 — Power of Three (Easy)

[Official problem](https://leetcode.com/problems/power-of-three) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0300-0399/0326.Power%20of%20Three/README_EN.md)

### Problem description

Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3^x`.

### Constraints

- `-2^31 <= n <= 2^31 - 1`

**Follow up:** Could you solve it without loops/recursion?

### Approach and complexity

If $n$ is a power of $3$, then the maximum value of $n$ is $3^{19} = 1162261467$. Therefore, we only need to check if $n$ is a divisor of $3^{19}$.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
};
```

---

<a id="lc-461"></a>
## 11. LC 461 — Hamming Distance (Easy)

[Official problem](https://leetcode.com/problems/hamming-distance) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0461.Hamming%20Distance/README_EN.md)

### Problem description

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return the **Hamming distance** between them.

### Constraints

- `0 <= x, y <= 2^31 - 1`

**Note:** This question is the same as 2220: Minimum Bit Flips to Convert Number.

### Approach and complexity

A bit differs exactly where x XOR y has a one. Count those positions using C++20 popcount.

Time O(1) for fixed-width integers; auxiliary space O(1).

### C++20 solution

```cpp
class Solution {
public:
    int hammingDistance(int x, int y) { return popcount(static_cast<unsigned>(x ^ y)); }
};
```

---

<a id="lc-477"></a>
## 12. LC 477 — Total Hamming Distance (Medium)

[Official problem](https://leetcode.com/problems/total-hamming-distance) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0477.Total%20Hamming%20Distance/README_EN.md)

### Problem description

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array `nums`, return the sum of **Hamming distances** between all the pairs of the integers in `nums`.

### Constraints

- `1 <= nums.length <= 10^4`

- `0 <= nums[i] <= 10^9`

- The answer for the given input will fit in a **32-bit** integer.

### Approach and complexity

We enumerate each bit in the range $[0, 31]$. For the current enumerated bit $i$, we count the number of numbers where the $i$-th bit is $1$, denoted as $a$. Therefore, the number of numbers where the $i$-th bit is $0$ is $b = n - a$, where $n$ is the length of the array. In this way, the sum of the Hamming distance on the $i$-th bit is $a \times b$. We add the Hamming distances of all bits to get the answer.

The time complexity is $O(n \log M)$, and the space complexity is $O(1)$, where $n$ and $M$ are the length of the array and the maximum value in the array, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int ans = 0, n = nums.size();
        for (int i = 0; i < 32; ++i) {
            int a = 0;
            for (int x : nums) {
                a += x >> i & 1;
            }
            int b = n - a;
            ans += a * b;
        }
        return ans;
    }
};
```

---

<a id="lc-137"></a>
## 13. LC 137 — Single Number II (Medium)

[Official problem](https://leetcode.com/problems/single-number-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0137.Single%20Number%20II/README_EN.md)

### Problem description

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

### Constraints

- `1 <= nums.length <= 3 * 10^4`

- `-2^31 <= nums[i] <= 2^31 - 1`

- Each element in `nums` appears exactly **three times** except for one element which appears **once**.

### Approach and complexity

We can use a more efficient method that uses digital circuits to simulate the above bitwise operation.

Each binary bit of an integer can only represent 2 states, 0 or 1. However, we need to represent the sum of the $i$-th bit of all integers traversed so far modulo 3. Therefore, we can use two integers $a$ and $b$ to represent it. There are three possible cases:

1. The $i$-th bit of integer $a$ is 0 and the $i$-th bit of integer $b$ is 0, which means the modulo 3 result is 0;
2. The $i$-th bit of integer $a$ is 0 and the $i$-th bit of integer $b$ is 1, which means the modulo 3 result is 1;
3. The $i$-th bit of integer $a$ is 1 and the $i$-th bit of integer $b$ is 0, which means the modulo 3 result is 2.

We use integer $c$ to represent the number to be read in, and the truth table is as follows:

| $a_i$ | $b_i$ | $c_i$ | New $a_i$ | New $b_i$ |
| ----- | ----- | ----- | --------- | --------- |
| 0     | 0     | 0     | 0         | 0         |
| 0     | 0     | 1     | 0         | 1         |
| 0     | 1     | 0     | 0         | 1         |
| 0     | 1     | 1     | 1         | 0         |
| 1     | 0     | 0     | 1         | 0         |
| 1     | 0     | 1     | 0         | 0         |

Based on the truth table, we can write the logical expression:

$$
a_i = a_i' b_i c_i + a_i b_i' c_i'
$$

and:

$$
b_i = a_i' b_i' c_i + a_i' b_i c_i' = a_i' (b_i \oplus c_i)
$$

The final result is $b$, because when the binary bit of $b$ is 1, it means that the number appears only once.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int a = 0, b = 0;
        for (int c : nums) {
            int aa = (~a & b & c) | (a & ~b & ~c);
            int bb = ~a & (b ^ c);
            a = aa;
            b = bb;
        }
        return b;
    }
};
```

---

<a id="lc-260"></a>
## 14. LC 260 — Single Number III (Medium)

[Official problem](https://leetcode.com/problems/single-number-iii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0260.Single%20Number%20III/README_EN.md)

### Problem description

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in **any order**.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

### Constraints

- `2 <= nums.length <= 3 * 10^4`

- `-2^31 <= nums[i] <= 2^31 - 1`

- Each integer in `nums` will appear twice, only two integers will appear once.

### Approach and complexity

The XOR operation has the following properties:

- Any number XOR 0 is still the original number, i.e., $x \oplus 0 = x$;
- Any number XOR itself is 0, i.e., $x \oplus x = 0$;

Since all numbers in the array appear twice except for two numbers, we can perform XOR operation on all numbers in the array to get the XOR result of the two numbers that only appear once.

Since these two numbers are not equal, there is at least one bit that is 1 in the XOR result. We can use the $\textit{lowbit}$ operation to find the lowest bit of 1 in the XOR result, and divide all numbers in the array into two groups based on whether this bit is 1 or not. This way, the two numbers that only appear once are separated into different groups.

Perform XOR operation on each group separately to obtain the two numbers $a$ and $b$ that only appear once.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long long xs = 0;
        for (int& x : nums) {
            xs ^= x;
        }
        int lb = xs & -xs;
        int a = 0;
        for (int& x : nums) {
            if (x & lb) {
                a ^= x;
            }
        }
        int b = xs ^ a;
        return {a, b};
    }
};
```

---

<a id="lc-287"></a>
## 15. LC 287 — Find the Duplicate Number (Medium)

[Official problem](https://leetcode.com/problems/find-the-duplicate-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0287.Find%20the%20Duplicate%20Number/README_EN.md)

### Problem description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return this repeated number.

You must solve the problem **without** modifying the array `nums` and using only constant extra space.

### Constraints

- `1 <= n <= 10^5`

- `nums.length == n + 1`

- `1 <= nums[i] <= n`

- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

Follow up:

- How can we prove that at least one duplicate number must exist in `nums`?

- Can you solve the problem in linear runtime complexity?

### Approach and complexity

Treat i→nums[i] as a functional graph. Values in [1,n] keep every step valid; the repeated value is the cycle entry reachable from index zero. First find a meeting inside the cycle, then restart one pointer at zero and advance both to the entry.

Time O(n); auxiliary space O(1). Does not modify the input.

### C++20 solution

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow != fast);
        slow = 0;
        while (slow != fast) { slow = nums[slow]; fast = nums[fast]; }
        return slow;
    }
};
```

---

<a id="lc-29"></a>
## 16. LC 29 — Divide Two Integers (Medium)

[Official problem](https://leetcode.com/problems/divide-two-integers) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0029.Divide%20Two%20Integers/README_EN.md)

### Problem description

Given two integers `dividend` and `divisor`, divide two integers **without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Return the **quotient** after dividing `dividend` by `divisor`.

**Note: **Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: `[−2^31, 2^31 − 1]`. For this problem, if the quotient is **strictly greater than** `2^31 - 1`, then return `2^31 - 1`, and if the quotient is **strictly less than** `-2^31`, then return `-2^31`.

### Constraints

- `-2^31 <= dividend, divisor <= 2^31 - 1`

- `divisor != 0`

### Approach and complexity

Division is essentially subtraction. The problem requires us to calculate the integer result after dividing two numbers, which is actually calculating how many divisors and a number less than the divisor constitute the dividend. However, only one subtraction can be done in one loop, which is too inefficient and will lead to timeout. This can be optimized by using the idea of fast power.

It should be noted that since the problem explicitly requires that only 32-bit signed integers can be used at most, the divisor and dividend need to be converted to negative numbers for calculation. Because converting to positive numbers may cause overflow, such as when the dividend is `INT32_MIN`, it will be greater than `INT32_MAX` when converted to a positive number.

Assuming the dividend is $a$ and the divisor is $b$, the time complexity is $O(\log a \log b)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int divide(int a, int b) {
        if (b == 1) {
            return a;
        }
        if (a == INT_MIN && b == -1) {
            return INT_MAX;
        }
        bool sign = (a > 0 && b > 0) || (a < 0 && b < 0);
        a = a > 0 ? -a : a;
        b = b > 0 ? -b : b;
        int ans = 0;
        while (a <= b) {
            int x = b;
            int cnt = 1;
            while (x >= -(1 << 30) && a <= x + x) {
                x += x;
                cnt <<= 1;
            }
            ans += cnt;
            a -= x;
        }
        return sign ? ans : -ans;
    }
};
```

---

<a id="lc-7"></a>
## 17. LC 7 — Reverse Integer (Medium)

[Official problem](https://leetcode.com/problems/reverse-integer) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0007.Reverse%20Integer/README_EN.md)

### Problem description

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

### Constraints

- `-2^31 <= x <= 2^31 - 1`

### Approach and complexity

Let's denote $mi$ and $mx$ as $-2^{31}$ and $2^{31} - 1$ respectively, then the reverse result of $x$, $\textit{ans}$, needs to satisfy $mi \le \textit{ans} \le mx$.

We can continuously take the remainder of $x$ to get the last digit $y$ of $x$, and add $y$ to the end of $\textit{ans}$. Before adding $y$, we need to check if $\textit{ans}$ overflows. That is, check whether $\textit{ans} \times 10 + y$ is within the range $[mi, mx]$.

If $x \gt 0$, it needs to satisfy $\textit{ans} \times 10 + y \leq mx$, that is, $\textit{ans} \times 10 + y \leq \left \lfloor \frac{mx}{10} \right \rfloor \times 10 + 7$. Rearranging gives $(\textit{ans} - \left \lfloor \frac{mx}{10} \right \rfloor) \times 10 \leq 7 - y$.

Next, we discuss the conditions for the inequality to hold:

- When $\textit{ans} \lt \left \lfloor \frac{mx}{10} \right \rfloor$, the inequality obviously holds;
- When $\textit{ans} = \left \lfloor \frac{mx}{10} \right \rfloor$, the necessary and sufficient condition for the inequality to hold is $y \leq 7$. If $\textit{ans} = \left \lfloor \frac{mx}{10} \right \rfloor$ and we can still add numbers, it means that the number is at the highest digit, that is, $y$ must not exceed $2$, therefore, the inequality must hold;
- When $\textit{ans} \gt \left \lfloor \frac{mx}{10} \right \rfloor$, the inequality obviously does not hold.

In summary, when $x \gt 0$, the necessary and sufficient condition for the inequality to hold is $\textit{ans} \leq \left \lfloor \frac{mx}{10} \right \rfloor$.

Similarly, when $x \lt 0$, the necessary and sufficient condition for the inequality to hold is $\textit{ans} \geq \left \lfloor \frac{mi}{10} \right \rfloor$.

Therefore, we can check whether $\textit{ans}$ overflows by checking whether $\textit{ans}$ is within the range $[\left \lfloor \frac{mi}{10} \right \rfloor, \left \lfloor \frac{mx}{10} \right \rfloor]$. If it overflows, return $0$. Otherwise, add $y$ to the end of $\textit{ans}$, and then remove the last digit of $x$, that is, $x \gets \left \lfloor \frac{x}{10} \right \rfloor$.

The time complexity is $O(\log |x|)$, and the space complexity is $O(1)$, where $|x|$ is the absolute value of $x$.

### C++20 solution

```cpp
class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        for (; x; x /= 10) {
            if (ans < INT_MIN / 10 || ans > INT_MAX / 10) {
                return 0;
            }
            ans = ans * 10 + x % 10;
        }
        return ans;
    }
};
```

---

<a id="lc-9"></a>
## 18. LC 9 — Palindrome Number (Easy)

[Official problem](https://leetcode.com/problems/palindrome-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0009.Palindrome%20Number/README_EN.md)

### Problem description

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

### Constraints

- `-2^31 <= x <= 2^31 - 1`

**Follow up:** Could you solve it without converting the integer to a string?

### Approach and complexity

First, we determine special cases:

- If $x < 0$, then $x$ is not a palindrome, directly return `false`;
- If $x > 0$ and the last digit of $x$ is $0$, then $x$ is not a palindrome, directly return `false`;
- If the last digit of $x$ is not $0$, then $x$ might be a palindrome, continue the following steps.

We reverse the second half of $x$ and compare it with the first half. If they are equal, then $x$ is a palindrome, otherwise, $x$ is not a palindrome.

For example, for $x = 1221$, we can reverse the second half from "21" to "12" and compare it with the first half "12". Since they are equal, we know that $x$ is a palindrome.

Let's see how to reverse the second half.

For the number $1221$, if we perform $1221 \bmod 10$, we will get the last digit $1$. To get the second last digit, we can first remove the last digit from $1221$ by dividing by $10$, $1221 / 10 = 122$, then get the remainder of the previous result divided by $10$, $122 \bmod 10 = 2$, to get the second last digit.

If we continue this process, we will get more reversed digits.

By continuously multiplying the last digit to the variable $y$, we can get the number in reverse order.

In the code implementation, we can repeatedly "take out" the last digit of $x$ and "add" it to the end of $y$, loop until $y \ge x$. If at this time $x = y$, or $x = y / 10$, then $x$ is a palindrome.

The time complexity is $O(\log_{10}(n))$, and the space complexity is $O(1)$, where $n$ is $x$. For each iteration, we will divide the input by $10$, so the time complexity is $O(\log_{10}(n))$.

### C++20 solution

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x && x % 10 == 0)) {
            return false;
        }
        int y = 0;
        for (; y < x; x /= 10) {
            y = y * 10 + x % 10;
        }
        return x == y || x == y / 10;
    }
};
```

---

<a id="lc-50"></a>
## 19. LC 50 — Pow(x, n) (Medium)

[Official problem](https://leetcode.com/problems/powx-n) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0050.Pow%28x%2C%20n%29/README_EN.md)

### Problem description

Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `x^n`).

### Constraints

- `-100.0 < x < 100.0`

- `-2^31 <= n <= 2^31-1`

- `n` is an integer.

- Either `x` is not zero or `n > 0`.

- `-10^4 <= x^n <= 10^4`

### Approach and complexity

The core idea of the fast powering algorithm is to decompose the exponent $n$ into the sum of $1$s on several binary bits, and then transform the $n$th power of $x$ into the product of several powers of $x$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the exponent.

### C++20 solution

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        auto qpow = [](double a, long long n) {
            double ans = 1;
            for (; n; n >>= 1) {
                if (n & 1) {
                    ans *= a;
                }
                a *= a;
            }
            return ans;
        };
        return n >= 0 ? qpow(x, n) : 1 / qpow(x, -(long long) n);
    }
};
```

---

<a id="lc-69"></a>
## 20. LC 69 — Sqrt(x) (Easy)

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

<a id="lc-204"></a>
## 21. LC 204 — Count Primes (Medium)

[Official problem](https://leetcode.com/problems/count-primes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0204.Count%20Primes/README_EN.md)

### Problem description

Given an integer `n`, return the number of prime numbers that are strictly less than `n`.

### Constraints

- `0 <= n <= 5 * 10^6`

### Approach and complexity

The sieve marks multiples of every unmarked prime, starting at its square because smaller multiples were handled by earlier primes. Count unmarked integers below n.

Time O(n log log n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int countPrimes(int n) {
        vector<bool> primes(n, true);
        int ans = 0;
        for (int i = 2; i < n; ++i) {
            if (primes[i]) {
                ++ans;
                for (int j = i; j < n; j += i) primes[j] = false;
            }
        }
        return ans;
    }
};
```

---

<a id="lc-202"></a>
## 22. LC 202 — Happy Number (Easy)

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

<a id="lc-172"></a>
## 23. LC 172 — Factorial Trailing Zeroes (Medium)

[Official problem](https://leetcode.com/problems/factorial-trailing-zeroes) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0172.Factorial%20Trailing%20Zeroes/README_EN.md)

### Problem description

Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

### Constraints

- `0 <= n <= 10^4`

**Follow up:** Could you write a solution that works in logarithmic time complexity?

### Approach and complexity

The problem is actually asking how many factors of $5$ are there in $[1,n]$.

Let's take $130$ as an example for analysis:

1. Divide by $5$ for the first time, get $26$, indicating that there are $26$ numbers containing the factor $5$;
2. Divide by $5$ for the second time, get $5$, indicating that there are $5$ numbers containing the factor $5^2$;
3. Divide by $5$ for the third time, get $1$, indicating that there is $1$ number containing the factor $5^3$;
4. Sum up to get the count of all factors of $5$ in $[1,n]$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        int ans = 0;
        while (n) {
            n /= 5;
            ans += n;
        }
        return ans;
    }
};
```

---

<a id="lc-66"></a>
## 24. LC 66 — Plus One (Easy)

[Official problem](https://leetcode.com/problems/plus-one) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0066.Plus%20One/README_EN.md)

### Problem description

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

### Constraints

- `1 <= digits.length <= 100`

- `0 <= digits[i] <= 9`

- `digits` does not contain any leading `0`'s.

### Approach and complexity

We start traversing from the last element of the array, add one to the current element, and then take the modulus by $10$. If the result is not $0$, it means that there is no carry for the current element, and we can directly return the array. Otherwise, the current element is $0$ and needs to be carried over. We continue to traverse the previous element and repeat the above operation. If we still haven't returned after traversing the array, it means that all elements in the array are $0$, and we need to insert a $1$ at the beginning of the array.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; --i) {
            ++digits[i];
            digits[i] %= 10;
            if (digits[i] != 0) return digits;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

---

<a id="lc-67"></a>
## 25. LC 67 — Add Binary (Easy)

[Official problem](https://leetcode.com/problems/add-binary) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0067.Add%20Binary/README_EN.md)

### Problem description

Given two binary strings `a` and `b`, return their sum as a binary string.

### Constraints

- `1 <= a.length, b.length <= 10^4`

- `a` and `b` consist only of `'0'` or `'1'` characters.

- Each string does not contain leading zeros except for the zero itself.

### Approach and complexity

We use a variable $\textit{carry}$ to record the current carry, and two pointers $i$ and $j$ to point to the end of $a$ and $b$ respectively, and add them bit by bit from the end to the beginning.

The time complexity is $O(\max(m, n))$, and the space complexity is $O(1)$, where $m$ and $n$ are the lengths of strings $a$ and $b$ respectively.

### C++20 solution

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string ans;
        int i = a.size() - 1, j = b.size() - 1;
        for (int carry = 0; i >= 0 || j >= 0 || carry; --i, --j) {
            carry += (i >= 0 ? a[i] - '0' : 0) + (j >= 0 ? b[j] - '0' : 0);
            ans.push_back((carry % 2) + '0');
            carry /= 2;
        }
        ranges::reverse(ans);
        return ans;
    }
};
```

---

<a id="lc-43"></a>
## 26. LC 43 — Multiply Strings (Medium)

[Official problem](https://leetcode.com/problems/multiply-strings) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0043.Multiply%20Strings/README_EN.md)

### Problem description

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

### Constraints

- `1 <= num1.length, num2.length <= 200`

- `num1` and `num2` consist of digits only.

- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

### Approach and complexity

Assume the lengths of $\textit{num1}$ and $\textit{num2}$ are $m$ and $n$ respectively, then the length of their product can be at most $m + n$.

The proof is as follows:

- If $\textit{num1}$ and $\textit{num2}$ both take the minimum value, then their product is ${10}^{m - 1} \times {10}^{n - 1} = {10}^{m + n - 2}$, with a length of $m + n - 1$.
- If $\textit{num1}$ and $\textit{num2}$ both take the maximum value, then their product is $({10}^m - 1) \times ({10}^n - 1) = {10}^{m + n} - {10}^m - {10}^n + 1$, with a length of $m + n$.

Therefore, we can apply for an array of length $m + n$ to store each digit of the product.

From the least significant digit to the most significant digit, we calculate each digit of the product in turn, and finally convert the array into a string.

Note to check whether the most significant digit is $0$, if it is, remove it.

The time complexity is $O(mn)$, and the space complexity is $O(m + n)$, where $m$ and $n$ are the lengths of $\textit{num1}$ and $\textit{num2}$ respectively.

### C++20 solution

```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }
        int m = num1.size(), n = num2.size();
        vector<int> arr(m + n);
        for (int i = m - 1; i >= 0; --i) {
            int a = num1[i] - '0';
            for (int j = n - 1; j >= 0; --j) {
                int b = num2[j] - '0';
                arr[i + j + 1] += a * b;
            }
        }
        for (int i = arr.size() - 1; i; --i) {
            arr[i - 1] += arr[i] / 10;
            arr[i] %= 10;
        }
        int i = arr[0] ? 0 : 1;
        string ans;
        for (; i < arr.size(); ++i) {
            ans += '0' + arr[i];
        }
        return ans;
    }
};
```

---

<a id="lc-415"></a>
## 27. LC 415 — Add Strings (Easy)

[Official problem](https://leetcode.com/problems/add-strings) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0415.Add%20Strings/README_EN.md)

### Problem description

Given two non-negative integers, `num1` and `num2` represented as string, return the sum of `num1` and `num2` as a string.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`). You must also not convert the inputs to integers directly.

### Constraints

- `1 <= num1.length, num2.length <= 10^4`

- `num1` and `num2` consist of only digits.

- `num1` and `num2` don't have any leading zeros except for the zero itself.

### Approach and complexity

We use two pointers $i$ and $j$ to point to the end of the two strings respectively, and start adding bit by bit from the end. Each time we take out the corresponding digits $a$ and $b$, calculate their sum $a + b + c$, where $c$ represents the carry from the last addition. Finally, we append the units digit of $a + b + c$ to the end of the answer string, and then take the tens digit of $a + b + c$ as the value of the carry $c$, and loop this process until the pointers of both strings have pointed to the beginning of the string and the value of the carry $c$ is $0$.

Finally, reverse the answer string and return it.

The time complexity is $O(\max(m, n))$, and the space complexity is $O(1)$, where $m$ and $n$ are the lengths of the two strings respectively.

The following code also implements string subtraction, refer to the `subStrings(num1, num2)` function.

### C++20 solution

```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = num1.size() - 1, j = num2.size() - 1;
        string ans;
        for (int c = 0; i >= 0 || j >= 0 || c; --i, --j) {
            int a = i < 0 ? 0 : num1[i] - '0';
            int b = j < 0 ? 0 : num2[j] - '0';
            c += a + b;
            ans += to_string(c % 10);
            c /= 10;
        }
        ranges::reverse(ans);
        return ans;
    }

    string subStrings(string num1, string num2) {
        int m = num1.size(), n = num2.size();
        bool neg = m < n || (m == n && num1 < num2);
        if (neg) {
            swap(num1, num2);
        }
        int i = num1.size() - 1, j = num2.size() - 1;
        string ans;
        for (int c = 0; i >= 0; --i, --j) {
            c = (num1[i] - '0') - c - (j < 0 ? 0 : num2[j] - '0');
            ans += to_string((c + 10) % 10);
            c = c < 0 ? 1 : 0;
        }
        while (ans.size() > 1 && ans.back() == '0') {
            ans.pop_back();
        }
        if (neg) {
            ans.push_back('-');
        }
        ranges::reverse(ans);
        return ans;
    }
};
```

---

<a id="lc-989"></a>
## 28. LC 989 — Add to Array-Form of Integer (Easy)

[Official problem](https://leetcode.com/problems/add-to-array-form-of-integer) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0900-0999/0989.Add%20to%20Array-Form%20of%20Integer/README_EN.md)

### Problem description

The **array-form** of an integer `num` is an array representing its digits in left to right order.

- For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return the **array-form** of the integer `num + k`.

### Constraints

- `1 <= num.length <= 10^4`

- `0 <= num[i] <= 9`

- `num` does not contain any leading zeros except for the zero itself.

- `1 <= k <= 10^4`

### Approach and complexity

We can start from the last digit of the array and add each digit of the array to $k$. Then, divide $k$ by $10$, and use the remainder as the current digit's value, with the quotient as the carry. Continue this process until the array is fully traversed and $k = 0$. Finally, reverse the answer array.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of $\textit{num}$.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> ans;
        for (int i = num.size() - 1; i >= 0 || k > 0; --i) {
            k += (i >= 0 ? num[i] : 0);
            ans.push_back(k % 10);
            k /= 10;
        }
        ranges::reverse(ans);
        return ans;
    }
};
```

---

<a id="lc-8"></a>
## 29. LC 8 — String to Integer (atoi) (Medium)

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

---

<a id="lc-13"></a>
## 30. LC 13 — Roman to Integer (Easy)

[Official problem](https://leetcode.com/problems/roman-to-integer) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0013.Roman%20to%20Integer/README_EN.md)

### Problem description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

**Symbol** **Value**
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 

- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 

- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

### Constraints

- `1 <= s.length <= 15`

- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.

- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

### Approach and complexity

First, we use a hash table $d$ to record the numerical value corresponding to each character. Then, we traverse the string $s$ from left to right. If the numerical value corresponding to the current character is less than the numerical value corresponding to the character on the right, we subtract the numerical value corresponding to the current character. Otherwise, we add the numerical value corresponding to the current character.

The time complexity is $O(n)$, and the space complexity is $O(m)$, where $n$ and $m$ are the length of the string $s$ and the size of the character set, respectively.

### C++20 solution

```cpp
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> nums{
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };
        int ans = nums[s.back()];
        for (int i = 0; i < s.size() - 1; ++i) {
            int sign = nums[s[i]] < nums[s[i + 1]] ? -1 : 1;
            ans += sign * nums[s[i]];
        }
        return ans;
    }
};
```

---

<a id="lc-12"></a>
## 31. LC 12 — Integer to Roman (Medium)

[Official problem](https://leetcode.com/problems/integer-to-roman) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0012.Integer%20to%20Roman/README_EN.md)

### Problem description

Seven different symbols represent Roman numerals with the following values:

Symbol
Value

I
1

V
5

X
10

L
50

C
100

D
500

M
1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

- If the value starts with 4 or 9 use the **subtractive form** representing one symbol subtracted from the following symbol, for example, 4 is 1 (`I`) less than 5 (`V`): `IV` and 9 is 1 (`I`) less than 10 (`X`): `IX`. Only the following subtractive forms are used: 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`) and 900 (`CM`).

- Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiple times. If you need to append a symbol 4 times use the **subtractive form**.

Given an integer, convert it to a Roman numeral.

### Constraints

- `1 <= num <= 3999`

### Approach and complexity

We can first list all possible symbols $cs$ and their corresponding values $vs$, then enumerate each value $vs[i]$ from large to small. Each time, we use as many symbols $cs[i]$ corresponding to this value as possible, until the number $\textit{num}$ becomes $0$.

The time complexity is $O(m)$, and the space complexity is $O(m)$, where $m$ is the number of symbols.

### C++20 solution

```cpp
class Solution {
public:
    string intToRoman(int num) {
        vector<string> cs = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        vector<int> vs = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string ans;
        for (int i = 0; i < cs.size(); ++i) {
            while (num >= vs[i]) {
                num -= vs[i];
                ans += cs[i];
            }
        }
        return ans;
    }
};
```

---

<a id="lc-168"></a>
## 32. LC 168 — Excel Sheet Column Title (Easy)

[Official problem](https://leetcode.com/problems/excel-sheet-column-title) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0168.Excel%20Sheet%20Column%20Title/README_EN.md)

### Problem description

Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

### Constraints

- `1 <= columnNumber <= 2^31 - 1`

### Approach and complexity

Excel uses digits 1 through 26 rather than 0 through 25. Subtract one before taking each remainder, append its letter, and reverse the result.

Time O(log₂₆ n); auxiliary space O(1), excluding the output.

### C++20 solution

```cpp
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result;
        while (columnNumber) {
            --columnNumber;
            result += static_cast<char>('A' + columnNumber % 26);
            columnNumber /= 26;
        }
        ranges::reverse(result);
        return result;
    }
};
```

---

<a id="lc-171"></a>
## 33. LC 171 — Excel Sheet Column Number (Easy)

[Official problem](https://leetcode.com/problems/excel-sheet-column-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0171.Excel%20Sheet%20Column%20Number/README_EN.md)

### Problem description

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

### Constraints

- `1 <= columnTitle.length <= 7`

- `columnTitle` consists only of uppercase English letters.

- `columnTitle` is in the range `["A", "FXSHRXW"]`.

### Approach and complexity

The column name in Excel is a representation in base 26. For example, "AB" represents the column number $1 \times 26 + 2 = 28$.

Therefore, we can iterate through the string `columnTitle`, convert each character to its corresponding value, and then calculate the result.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the string $\textit{columnTitle}$.

### C++20 solution

```cpp
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans = 0;
        for (char& c : columnTitle) {
            ans = ans * 26 + (c - 'A' + 1);
        }
        return ans;
    }
};
```

---

<a id="lc-118"></a>
## 34. LC 118 — Pascal's Triangle (Easy)

[Official problem](https://leetcode.com/problems/pascals-triangle) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0118.Pascal%27s%20Triangle/README_EN.md)

### Problem description

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![Problem illustration](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0118.Pascal%27s%20Triangle/images/PascalTriangleAnimated2.gif)

### Constraints

- `1 <= numRows <= 30`

### Approach and complexity

We first create an answer array $f$, then set the first row of $f$ to $[1]$. Next, starting from the second row, the first and last elements of each row are $1$, and for other elements $f[i][j] = f[i - 1][j - 1] + f[i - 1][j]$.

The time complexity is $O(n^2)$, and the space complexity is $O(1)$, where $n$ is the given number of rows.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> f;
        f.push_back(vector<int>(1, 1));
        for (int i = 0; i < numRows - 1; ++i) {
            vector<int> g;
            g.push_back(1);
            for (int j = 1; j < f[i].size(); ++j) {
                g.push_back(f[i][j - 1] + f[i][j]);
            }
            g.push_back(1);
            f.push_back(g);
        }
        return f;
    }
};
```

---

<a id="lc-119"></a>
## 35. LC 119 — Pascal's Triangle II (Easy)

[Official problem](https://leetcode.com/problems/pascals-triangle-ii) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0119.Pascal%27s%20Triangle%20II/README_EN.md)

### Problem description

Given an integer `rowIndex`, return the `rowIndex^th` (**0-indexed**) row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![Problem illustration](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0119.Pascal%27s%20Triangle%20II/images/PascalTriangleAnimated2.gif)

### Constraints

- `0 <= rowIndex <= 33`

**Follow up:** Could you optimize your algorithm to use only `O(rowIndex)` extra space?

### Approach and complexity

We create an array $f$ of length $\textit{rowIndex} + 1$, initially all elements are $1$.

Next, starting from the second row, we calculate the value of the $j$th element in the current row from back to front, $f[j] = f[j] + f[j - 1]$, where $j \in [1, i - 1]$.

Finally, return $f$.

The time complexity is $O(n^2)$, and the space complexity is $O(n)$, where $n$ is the given number of rows.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> f(rowIndex + 1, 1);
        for (int i = 2; i < rowIndex + 1; ++i) {
            for (int j = i - 1; j; --j) {
                f[j] += f[j - 1];
            }
        }
        return f;
    }
};
```

---

<a id="lc-62"></a>
## 36. LC 62 — Unique Paths (Medium)

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

<a id="lc-96"></a>
## 37. LC 96 — Unique Binary Search Trees (Medium)

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

<a id="lc-89"></a>
## 38. LC 89 — Gray Code (Medium)

[Official problem](https://leetcode.com/problems/gray-code) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0089.Gray%20Code/README_EN.md)

### Problem description

An **n-bit gray code sequence** is a sequence of `2^n` integers where:

- Every integer is in the **inclusive** range `[0, 2^n - 1]`,

- The first integer is `0`,

- An integer appears **no more than once** in the sequence,

- The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and

- The binary representation of the **first** and **last** integers differs by **exactly one bit**.

Given an integer `n`, return any valid **n-bit gray code sequence**.

### Constraints

- `1 <= n <= 16`

### Approach and complexity

Gray code is a type of encoding method that we often encounter in engineering. Its basic feature is that only one bit of binary number is different between any two adjacent codes.

The rule for converting binary code to binary Gray code is to keep the highest bit of the binary code as the highest bit of the Gray code, and the second highest bit of the Gray code is the XOR of the highest bit and the second highest bit of the binary code. The calculation of the remaining bits of the Gray code is similar to the second highest bit.

Assume that a binary number is represented as $B_{n-1}B_{n-2}...B_2B_1B_0$, and its Gray code is represented as $G_{n-1}G_{n-2}...G_2G_1G_0$. The highest bit is retained, so $G_{n-1} = B_{n-1}$; and the other bits $G_i = B_{i+1} \oplus B_{i}$, where $i=0,1,2..,n-2$.

Therefore, for an integer $x$, we can use the function $\textit{gray}(x)$ to get its Gray code:

```java
int gray(x) {
    return x ^ (x >> 1);
}
```

We directly map the integers $[0,..2^n - 1]$ to the corresponding Gray codes to get the answer array.

The time complexity is $O(2^n)$, and the space complexity is $O(1)$, where $n$ is the integer given in the problem.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> ans;
        for (int i = 0; i < 1 << n; ++i) {
            ans.push_back(i ^ (i >> 1));
        }
        return ans;
    }
};
```

---

<a id="lc-78"></a>
## 39. LC 78 — Subsets (Medium)

[Official problem](https://leetcode.com/problems/subsets) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0000-0099/0078.Subsets/README_EN.md)

### Problem description

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Constraints

- `1 <= nums.length <= 10`

- `-10 <= nums[i] <= 10`

- All the numbers of `nums` are **unique**.

### Approach and complexity

We design a function $\textit{dfs}(i)$, which represents starting the search from the $i$th element of the array for all subsets. The execution logic of the function $\textit{dfs}(i)$ is as follows:

- If $i = n$, it means the current search has ended. Add the current subset $t$ to the answer array $\textit{ans}$, and then return.
- Otherwise, we can choose not to select the current element and directly execute $\textit{dfs}(i + 1)$; or we can choose the current element, i.e., add the current element $\textit{nums}[i]$ to the subset $t$, and then execute $\textit{dfs}(i + 1)$. Note that we need to remove $\textit{nums}[i]$ from the subset $t$ after executing $\textit{dfs}(i + 1)$ (backtracking).

In the main function, we call $\textit{dfs}(0)$, i.e., start searching all subsets from the first element of the array. Finally, return the answer array $\textit{ans}$.

The time complexity is $O(n 2^n)$, and the space complexity is $O(n)$, where $n$ is the length of the array. There are a total of $2^n$ subsets, and each subset takes $O(n)$ time to construct.

### C++20 solution

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> t;
        function<void(int)> dfs = [&](int i) -> void {
            if (i == nums.size()) {
                ans.push_back(t);
                return;
            }
            dfs(i + 1);
            t.push_back(nums[i]);
            dfs(i + 1);
            t.pop_back();
        };
        dfs(0);
        return ans;
    }
};
```

---

<a id="lc-1863"></a>
## 40. LC 1863 — Sum of All Subset XOR Totals (Easy)

[Official problem](https://leetcode.com/problems/sum-of-all-subset-xor-totals) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1800-1899/1863.Sum%20of%20All%20Subset%20XOR%20Totals/README_EN.md)

### Problem description

The **XOR total** of an array is defined as the bitwise `XOR` of** all its elements**, or `0` if the array is** empty**.

- For example, the **XOR total** of the array `[2,5,6]` is `2 XOR 5 XOR 6 = 1`.

Given an array `nums`, return the **sum** of all **XOR totals** for every **subset** of `nums`. 

**Note:** Subsets with the **same** elements should be counted **multiple** times.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

### Constraints

- `1 <= nums.length <= 12`

- `1 <= nums[i] <= 20`

### Approach and complexity

For any bit present in at least one element, exactly half of all subsets have that XOR bit set: pairing subsets by toggling one element containing that bit flips its parity. Therefore the answer is OR(nums)·2ⁿ⁻¹.

Time O(n); auxiliary space O(1). The specified n and value bounds keep the result within int.

### C++20 solution

```cpp
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        unsigned bits = 0;
        for (int x : nums) bits |= static_cast<unsigned>(x);
        return static_cast<int>(bits << (nums.size() - 1));
    }
};
```

---

<a id="lc-1318"></a>
## 41. LC 1318 — Minimum Flips to Make a OR b Equal to c (Medium)

[Official problem](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1318.Minimum%20Flips%20to%20Make%20a%20OR%20b%20Equal%20to%20c/README_EN.md)

### Problem description

Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips required in some bits of `a` and `b` to make ( `a` OR `b` == `c` ). (bitwise OR operation).

Flip operation consists of change **any** single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

### Constraints

- `1 <= a <= 10^9`

- `1 <= b <= 10^9`

- `1 <= c <= 10^9`

### Approach and complexity

We can enumerate each bit of the binary representation of $a$, $b$, and $c$, denoted as $x$, $y$, and $z$ respectively. If the bitwise OR operation result of $x$ and $y$ is different from $z$, we then check if both $x$ and $y$ are $1$. If so, we need to flip twice, otherwise, we only need to flip once. We accumulate all the required flip times.

The time complexity is $O(\log M)$, and the space complexity is $O(1)$, where $M$ is the maximum value of the numbers in the problem.

### C++20 solution

```cpp
class Solution {
public:
    int minFlips(int a, int b, int c) {
        int ans = 0;
        for (int i = 0; i < 32; ++i) {
            int x = a >> i & 1, y = b >> i & 1, z = c >> i & 1;
            ans += z == 0 ? x + y : (x == 0 && y == 0 ? 1 : 0);
        }
        return ans;
    }
};
```

---

<a id="lc-2220"></a>
## 42. LC 2220 — Minimum Bit Flips to Convert Number (Easy)

[Official problem](https://leetcode.com/problems/minimum-bit-flips-to-convert-number) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2200-2299/2220.Minimum%20Bit%20Flips%20to%20Convert%20Number/README_EN.md)

### Problem description

A **bit flip** of a number `x` is choosing a bit in the binary representation of `x` and **flipping** it from either `0` to `1` or `1` to `0`.

- For example, for `x = 7`, the binary representation is `111` and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get `110`, flip the second bit from the right to get `101`, flip the fifth bit from the right (a leading zero) to get `10111`, etc.

Given two integers `start` and `goal`, return the **minimum** number of **bit flips** to convert `start` to `goal`.

### Constraints

- `0 <= start, goal <= 10^9`

**Note:** This question is the same as 461: Hamming Distance.

### Approach and complexity

According to the problem description, we only need to count the number of 1s in the binary representation of $\textit{start} \oplus \textit{goal}$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$, where $n$ is the size of the integers in the problem.

### C++20 solution

```cpp
class Solution {
public:
    int minBitFlips(int start, int goal) {
        return popcount(static_cast<unsigned int>(start ^ goal));
    }
};
```

---

<a id="lc-2433"></a>
## 43. LC 2433 — Find The Original Array of Prefix Xor (Medium)

[Official problem](https://leetcode.com/problems/find-the-original-array-of-prefix-xor) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2400-2499/2433.Find%20The%20Original%20Array%20of%20Prefix%20Xor/README_EN.md)

### Problem description

You are given an **integer** array `pref` of size `n`. Find and return the array `arr` of size `n` that satisfies:

- `pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`.

Note that `^` denotes the **bitwise-xor** operation.

It can be proven that the answer is **unique**.

### Constraints

- `1 <= pref.length <= 10^5`

- `0 <= pref[i] <= 10^6`

### Approach and complexity

According to the problem statement, we have equation one:

$$
\textit{pref}[i]=\textit{arr}[0] \oplus \textit{arr}[1] \oplus \cdots \oplus \textit{arr}[i]
$$

So, we also have equation two:

$$
\textit{pref}[i-1]=\textit{arr}[0] \oplus \textit{arr}[1] \oplus \cdots \oplus \textit{arr}[i-1]
$$

We perform a bitwise XOR operation on equations one and two, and get:

$$
\textit{pref}[i] \oplus \textit{pref}[i-1]=\textit{arr}[i]
$$

That is, each item in the answer array is obtained by performing a bitwise XOR operation on the adjacent two items in the prefix XOR array.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the prefix XOR array.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        vector<int> ans = {pref[0]};
        for (int i = 1; i < n; ++i) {
            ans.push_back(pref[i - 1] ^ pref[i]);
        }
        return ans;
    }
};
```

---

<a id="lc-1442"></a>
## 44. LC 1442 — Count Triplets That Can Form Two Arrays of Equal XOR (Medium)

[Official problem](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1400-1499/1442.Count%20Triplets%20That%20Can%20Form%20Two%20Arrays%20of%20Equal%20XOR/README_EN.md)

### Problem description

Given an array of integers `arr`.

We want to select three indices `i`, `j` and `k` where `(0 <= i < j <= k < arr.length)`.

Let's define `a` and `b` as follows:

- `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`

- `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

Note that **^** denotes the **bitwise-xor** operation.

Return the number of triplets (`i`, `j` and `k`) Where `a == b`.

### Constraints

- `1 <= arr.length <= 300`

- `1 <= arr[i] <= 10^8`

### Approach and complexity

With prefix positions 0…n, a valid triplet requires equal XOR at positions i and k+1. For a new position p and each earlier equal prefix at q, there are p−q−1 choices for the middle boundary. Counts and sums of q aggregate these contributions in O(1) expected time.

Expected time O(n); auxiliary space O(n).

### C++20 solution

```cpp
class Solution {
public:
    int countTriplets(vector<int>& arr) {
        unordered_map<int, pair<long long, long long>> seen;
        seen[0] = {1, 0};
        int prefix = 0;
        long long answer = 0;
        for (int p = 1; p <= static_cast<int>(arr.size()); ++p) {
            prefix ^= arr[p - 1];
            auto& [count, sum] = seen[prefix];
            answer += count * (p - 1) - sum;
            ++count;
            sum += p;
        }
        return static_cast<int>(answer);
    }
};
```

---

<a id="lc-1310"></a>
## 45. LC 1310 — XOR Queries of a Subarray (Medium)

[Official problem](https://leetcode.com/problems/xor-queries-of-a-subarray) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/1300-1399/1310.XOR%20Queries%20of%20a%20Subarray/README_EN.md)

### Problem description

You are given an array `arr` of positive integers. You are also given the array `queries` where `queries[i] = [left_i, right_i]`.

For each query `i` compute the **XOR** of elements from `left_i` to `right_i` (that is, `arr[left_i] XOR arr[left_i + 1] XOR ... XOR arr[right_i]` ).

Return an array `answer` where `answer[i]` is the answer to the `i^th` query.

### Constraints

- `1 <= arr.length, queries.length <= 3 * 10^4`

- `1 <= arr[i] <= 10^9`

- `queries[i].length == 2`

- `0 <= left_i <= right_i < arr.length`

### Approach and complexity

We can use a prefix XOR array $s$ of length $n+1$ to store the prefix XOR results of the array $\textit{arr}$, where $s[i] = s[i-1] \oplus \textit{arr}[i-1]$. That is, $s[i]$ represents the XOR result of the first $i$ elements of $\textit{arr}$.

For a query $[l, r]$, we can obtain:

$$
\begin{aligned}
\textit{arr}[l] \oplus \textit{arr}[l+1] \oplus \cdots \oplus \textit{arr}[r] &= (\textit{arr}[0] \oplus \textit{arr}[1] \oplus \cdots \oplus \textit{arr}[l-1]) \oplus (\textit{arr}[0] \oplus \textit{arr}[1] \oplus \cdots \oplus \textit{arr}[r]) \\
&= s[l] \oplus s[r+1]
\end{aligned}
$$

The time complexity is $O(n+m)$, and the space complexity is $O(n)$, where $n$ and $m$ are the lengths of the array $\textit{arr}$ and the query array $\textit{queries}$, respectively.

### C++20 solution

```cpp
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        vector<int> s = vector<int>(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            s[i] = s[i - 1] ^ arr[i - 1];
        }
        vector<int> ans;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            ans.push_back(s[r + 1] ^ s[l]);
        }
        return ans;
    }
};
```

---

<a id="lc-421"></a>
## 46. LC 421 — Maximum XOR of Two Numbers in an Array (Medium)

[Official problem](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0400-0499/0421.Maximum%20XOR%20of%20Two%20Numbers%20in%20an%20Array/README_EN.md)

### Problem description

Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]`, where `0 <= i <= j < n`.

### Constraints

- `1 <= nums.length <= 2 * 10^5`

- `0 <= nums[i] <= 2^31 - 1`

### Approach and complexity

Insert binary prefixes into a bit trie. For each value prefer the opposite bit at every level, making the XOR as large as possible lexicographically from the highest bit.

Time O(nw); auxiliary space O(nw), w≤31.

### C++20 solution

```cpp
class Trie {
public:
    Trie* children[2];

    Trie()
        : children{nullptr, nullptr} {}

    void insert(int x) {
        Trie* node = this;
        for (int i = 30; ~i; --i) {
            int v = x >> i & 1;
            if (!node->children[v]) {
                node->children[v] = new Trie();
            }
            node = node->children[v];
        }
    }

    int search(int x) {
        Trie* node = this;
        int ans = 0;
        for (int i = 30; ~i; --i) {
            int v = x >> i & 1;
            if (node->children[v ^ 1]) {
                ans |= 1 << i;
                node = node->children[v ^ 1];
            } else {
                node = node->children[v];
            }
        }
        return ans;
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie* trie = new Trie();
        int ans = 0;
        for (int x : nums) {
            trie->insert(x);
            ans = max(ans, trie->search(x));
        }
        return ans;
    }
};
```

---

<a id="lc-2013"></a>
## 47. LC 2013 — Detect Squares (Medium)

[Official problem](https://leetcode.com/problems/detect-squares) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/2000-2099/2013.Detect%20Squares/README_EN.md)

### Problem description

You are given a stream of points on the X-Y plane. Design an algorithm that:

- **Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.

- Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.

An **axis-aligned square** is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

- `DetectSquares()` Initializes the object with an empty data structure.

- `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.

- `int count(int[] point)` Counts the number of ways to form **axis-aligned squares** with point `point = [x, y]` as described above.

### Constraints

- `point.length == 2`

- `0 <= x, y <= 1000`

- At most `3000` calls **in total** will be made to `add` and `count`.

### Approach and complexity

We can use a hash table $\textit{cnt}$ to maintain all the information of the points, where $\textit{cnt}[x][y]$ represents the count of point $(x, y)$.

When calling the $\textit{add}(x, y)$ method, we increase the value of $\textit{cnt}[x][y]$ by $1$.

When calling the $\textit{count}(x_1, y_1)$ method, we need to get three other points to form an axis-aligned square. We can enumerate the point $(x_2, y_1)$ that is parallel to the $x$-axis and at a distance $d$ from $(x_1, y_1)$. If such a point exists, based on these two points, we can determine the other two points as $(x_1, y_1 + d)$ and $(x_2, y_1 + d)$, or $(x_1, y_1 - d)$ and $(x_2, y_1 - d)$. We can add up the number of schemes for these two situations.

In terms of time complexity, the time complexity of calling the $\textit{add}(x, y)$ method is $O(1)$, and the time complexity of calling the $\textit{count}(x_1, y_1)$ method is $O(n)$; the space complexity is $O(n)$. Here, $n$ is the number of points in the data stream.

### C++20 solution

```cpp
class DetectSquares {
public:
    DetectSquares() {
    }

    void add(vector<int> point) {
        int x = point[0], y = point[1];
        ++cnt[x][y];
    }

    int count(vector<int> point) {
        int x1 = point[0], y1 = point[1];
        if (!cnt.count(x1)) {
            return 0;
        }
        int ans = 0;
        for (auto& [x2, cnt2] : cnt) {
            if (x2 != x1) {
                int d = x2 - x1;
                auto& cnt1 = cnt[x1];
                ans += cnt2[y1] * cnt1[y1 + d] * cnt2[y1 + d];
                ans += cnt2[y1] * cnt1[y1 - d] * cnt2[y1 - d];
            }
        }
        return ans;
    }

private:
    unordered_map<int, unordered_map<int, int>> cnt;
};
```

---

<a id="lc-149"></a>
## 48. LC 149 — Max Points on a Line (Hard)

[Official problem](https://leetcode.com/problems/max-points-on-a-line) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0100-0199/0149.Max%20Points%20on%20a%20Line/README_EN.md)

### Problem description

Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the **X-Y** plane, return the maximum number of points that lie on the same straight line.

### Constraints

- `1 <= points.length <= 300`

- `points[i].length == 2`

- `-10^4 <= x_i, y_i <= 10^4`

- All the `points` are **unique**.

### Approach and complexity

For each anchor, reduce direction differences by gcd and normalize the sign so opposite rays of the same line share a key. Count directions from that anchor; the largest count plus one gives the maximum collinear set.

Expected time O(n² log M), auxiliary space O(n), with coordinate-difference bound M. Arithmetic fits 32 bits under the specified coordinate limits.

### C++20 solution

```cpp
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int best = 1, n = points.size();
        for (int i = 0; i < n; ++i) {
            unordered_map<string, int> count;
            for (int j = i + 1; j < n; ++j) {
                int dx = points[j][0] - points[i][0], dy = points[j][1] - points[i][1];
                int divisor = std::gcd(dx, dy);
                dx /= divisor; dy /= divisor;
                if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy; }
                string key = to_string(dx) + ":" + to_string(dy);
                best = max(best, 1 + ++count[key]);
            }
        }
        return best;
    }
};
```

---

<a id="lc-223"></a>
## 49. LC 223 — Rectangle Area (Medium)

[Official problem](https://leetcode.com/problems/rectangle-area) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0200-0299/0223.Rectangle%20Area/README_EN.md)

### Problem description

Given the coordinates of two **rectilinear** rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its **bottom-left** corner `(ax1, ay1)` and its **top-right** corner `(ax2, ay2)`.

The second rectangle is defined by its **bottom-left** corner `(bx1, by1)` and its **top-right** corner `(bx2, by2)`.

### Constraints

- `-10^4 <= ax1 <= ax2 <= 10^4`

- `-10^4 <= ay1 <= ay2 <= 10^4`

- `-10^4 <= bx1 <= bx2 <= 10^4`

- `-10^4 <= by1 <= by2 <= 10^4`

### Approach and complexity

First, we calculate the area of the two rectangles separately, denoted as $a$ and $b$. Then we calculate the overlapping width $\textit{width}$ and height $\textit{height}$. The overlapping area is $\max(\textit{width}, 0) \times \max(\textit{height}, 0)$. Finally, we subtract the overlapping area from $a$ and $b$.

The time complexity is $O(1)$, and the space complexity is $O(1)$.

### C++20 solution

```cpp
class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int a = (ax2 - ax1) * (ay2 - ay1);
        int b = (bx2 - bx1) * (by2 - by1);
        int width = min(ax2, bx2) - max(ax1, bx1);
        int height = min(ay2, by2) - max(ay1, by1);
        return a + b - max(height, 0) * max(width, 0);
    }
};
```

---

<a id="lc-593"></a>
## 50. LC 593 — Valid Square (Medium)

[Official problem](https://leetcode.com/problems/valid-square) · [Pinned reference](https://github.com/doocs/leetcode/blob/d234cf451a6bdf182ef9fccad9071faa7eb9af6b/solution/0500-0599/0593.Valid%20Square/README_EN.md)

### Problem description

Given the coordinates of four points in 2D space `p1`, `p2`, `p3` and `p4`, return `true` if the four points construct a square.

The coordinate of a point `p_i` is represented as `[x_i, y_i]`. The input is **not** given in any order.

A **valid square** has four equal sides with positive length and four equal angles (90-degree angles).

### Constraints

- `p1.length == p2.length == p3.length == p4.length == 2`

- `-10^4 <= x_i, y_i <= 10^4`

### Approach and complexity

The six pairwise squared distances must consist of four equal nonzero sides followed by two equal diagonals, each twice a side’s squared length. This also rejects coincident and merely rectangular points without relying on point order.

Time O(1); auxiliary space O(1). Use 64-bit squared differences.

### C++20 solution

```cpp
class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        array<const vector<int>*, 4> points{&p1, &p2, &p3, &p4};
        array<long long, 6> distances{};
        int next = 0;
        for (int i = 0; i < 4; ++i) for (int j = i + 1; j < 4; ++j) {
            long long dx = (*points[i])[0] - (*points[j])[0];
            long long dy = (*points[i])[1] - (*points[j])[1];
            distances[next++] = dx * dx + dy * dy;
        }
        ranges::sort(distances);
        return distances[0] > 0 && distances[0] == distances[1] && distances[1] == distances[2] &&
            distances[2] == distances[3] && distances[4] == distances[5] && distances[4] == 2 * distances[0];
    }
};
```
