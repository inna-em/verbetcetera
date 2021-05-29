class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m-1] > nums[m]:
                r = m
            else:
                l = m + 1
        return
