class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diam = 0
        self.helper(root)
        return  self.diam
    
    def helper(self, node):
        if not node:
            return 0
        m_depth_r = self.helper(node.right)
        m_depth_l = self.helper(node.left)
        self.diam = max(self.diam, m_depth_r + m_depth_l)
        return 1 + max(m_depth_r, m_depth_l)
