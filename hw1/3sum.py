class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 2:
            if i > 0:
                while nums[i] == nums[i-1]:
                    i += 1
                    if i >= len(nums) - 2:
                        break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[j] + nums[k]
                if s == - nums[i]:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1]:
                        j += 1
                        if j >= k:
                            break
                    k -= 1
                    while nums[k] == nums[k+1]:
                        k -= 1
                        if k <= j:
                            break
                elif s < - nums[i]:
                    j += 1
                else:
                    k -= 1
            i += 1
        return result
