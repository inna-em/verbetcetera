class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            node = None
            
            if l <= r:
                m = (l + r) // 2
                node = TreeNode()
                node.val = nums[m]
                node.left = helper(l, m - 1)
                node.right = helper(m + 1, r)
                
            return node
        
        return helper(0, len(nums) - 1)
