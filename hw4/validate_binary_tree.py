class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        max_val, min_val = float('inf'), float('-inf')
        return self.helper(root, max_val,min_val)
    
    def helper(self, node, max_val, min_val):
        if not node:
            return True
        if node.val >= max_val or node.val <= min_val:
            return False
        return self.helper(node.left, node.val, min_val) and self.helper(node.right, max_val, node.val)
        
