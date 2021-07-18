class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)
        result = ''.join(self._quick_sort(nums)[::-1])
        return '0' if result[0] == '0' else result
        
    def _is_greater(self, num1: str, num2: str) -> bool:
        return int(num1 + num2) > int(num2 + num1)
        
    def _quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        smaller = []
        greater = []
        for num in nums[1::]:
            if self._is_greater(pivot, num):
                smaller.append(num)
            else:
                greater.append(num)
        return self._quick_sort(smaller) + [pivot] + self._quick_sort(greater)
