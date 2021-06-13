class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = root.val
        self.helper(root)
        return self.max_sum
        
    def helper(self, node):
        if not node:
            return 0
        l, r = self.helper(node.left),self. helper(node.right)
        self.max_sum = max(self.max_sum, node.val + l + r)
        tmp = node.val + max(l, r)
        return tmp if tmp > 0 else 0
