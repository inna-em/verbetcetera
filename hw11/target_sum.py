class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def helper(summ, i):
            if i == len(nums):
                if summ == target:
                    return 1
                else:
                    return 0
            if (summ, i) in memo:
                return memo[(summ, i)]
            sum_plus = helper(summ + nums[i], i + 1)
            sum_minus = helper(summ - nums[i], i + 1)
            memo[(summ, i)] = sum_plus + sum_minus
            return memo[(summ, i)]
            
        return helper(0, 0)
