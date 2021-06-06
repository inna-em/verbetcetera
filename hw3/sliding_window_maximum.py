from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for i in range(len(nums)):
            if i >= k and nums[i - k] == q[0]:
                q.popleft()
            self.addElemToQueue(q, nums[i])
            if i >= k - 1:
                result.append(q[0])
        return result

    def addElemToQueue(self, q, elem):
        while q and q[-1] < elem:
            q.pop()
        q.append(elem)
