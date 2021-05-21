class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        curr_max = nums[0]
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            curr_max = max(curr_max, curr_sum)
        return curr_max
