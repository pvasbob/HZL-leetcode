#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

// 1-two sum
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            auto it = seen.find(complement);

            if (it != seen.end()) {
                return {it->second, i};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};

// 3 — Longest Substring Without Repeating Characters
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        array<int, 256> lastSeen;
        lastSeen.fill(-1);

        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.size(); ++right) {
            unsigned char c = s[right];

            left = max(left, lastSeen[c] + 1);

            lastSeen[c] = right;

            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};

// ============================================

// 238. Product of Array Except Self
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);

        // Store the product of all elements before each index.
        for (int i = 1; i < n; ++i) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        // Multiply by the product of all elements after each index.
        int suffix = 1;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }

        return answer;
    }
};


// =====================================================

// 98. Validate Binary Search Tree
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return validate(root, LLONG_MIN, LLONG_MAX);
    }

private:
    bool validate(TreeNode* node, long long lower, long long upper) {
        if (node == nullptr) {
            return true;
        }

        if (node->val <= lower || node->val >= upper) {
            return false;
        }

        return validate(node->left, lower, node->val) &&
               validate(node->right, node->val, upper); 
    }
};


// 104. Maximum Depth of Binary Tree
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        return 1 + std::max(
            maxDepth(root->left),
            maxDepth(root->right)
        );
    }
};

// 94. Binary Tree Inorder Traversal Recursive
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// Recursive DFS
class Solution {
public:
    std::vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> result;
        inorder(root, result);
        return result;
    }

private:
    void inorder(TreeNode* node, std::vector<int>& result) {
        if (node == nullptr) {
            return;
        }

        inorder(node->left, result);
        result.push_back(node->val);
        inorder(node->right, result);
    }
};


// 94. Binary Tree Inorder Traversal Iterative
class Solution {
public:
    std::vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> result;
        std::stack<TreeNode*> stack;

        TreeNode* current = root;

        while (current != nullptr || !stack.empty()) {

            while (current != nullptr) {
                stack.push(current);
                current = current->left;
            }

            current = stack.top();
            stack.pop();

            result.push_back(current->val);

            current = current->right;
        }

        return result;
    }
};


// Binary Tree preorder Traversal Recursive
class Solution {
public:
    std::vector<int> preorderTraversal(TreeNode* root) {
        std::vector<int> result;
        preorder(root, result);
        return result;
    }

private:
    void preorder(TreeNode* node, std::vector<int>& result) {
        if (node == nullptr) {
            return;
        }

        result.push_back(node->val);    // Root
        preorder(node->left, result);   // Left
        preorder(node->right, result);  // Right
    }
};

// Binary Tree preorder Traversal Iterative
class Solution {
public:
    std::vector<int> preorderTraversal(TreeNode* root) {
        std::vector<int> result;

        if (root == nullptr) {
            return result;
        }

        std::stack<TreeNode*> stack;
        stack.push(root);

        while (!stack.empty()) {
            TreeNode* current = stack.top();
            stack.pop();

            result.push_back(current->val);

            if (current->right != nullptr) {
                stack.push(current->right);
            }

            if (current->left != nullptr) {
                stack.push(current->left);
            }
        }

        return result;
    }
};

// Binary Tree preorder Traversal Iterative
class Solution {
public:
    std::vector<int> preorderTraversal(TreeNode* root) {
        std::vector<int> result;
        std::stack<TreeNode*> stack;

        TreeNode* current = root;

        while (current != nullptr || !stack.empty()) {

            while (current != nullptr) {
                result.push_back(current->val);

                stack.push(current);
                current = current->left;
            }

            current = stack.top();
            stack.pop();

            current = current->right;
        }

        return result;
    }
};