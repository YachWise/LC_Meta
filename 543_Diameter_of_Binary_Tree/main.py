
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.max_diameter

