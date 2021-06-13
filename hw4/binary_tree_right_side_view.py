from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        row = []
        q = deque()
        if root:
            q.append(root)
            q.append('dummy')
        while q:
            node = q.popleft()
            if node != 'dummy':
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                result.append(row[-1])
                row = []
                if q:
                    q.append('dummy')
        return result
