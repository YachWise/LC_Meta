**543. Diameter of Binary Tree**

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

**Example 1**

         1
        / \
       2   3
      / \
     4   5

Input: root = [1,2,3,4,5]

Output: 3

Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3]

**Example 2**
Input: root = [1,2]

Output: 1

**Example Scope Questions**

1. Can I assume the tree will only contain numbers?
2. Can I assume the TreeNode class will be provided for me?
3. Can I assume the numbers will be non-negative?
4. Do we know the upperbounds of the node?