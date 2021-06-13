class Solution:   
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result
        
        
    def helper(self, node, result):
        if not node:
            return
        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)
        
