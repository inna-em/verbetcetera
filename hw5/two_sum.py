class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair not in hm:
                hm[num] = i
            else:
                return [hm[pair], i]
