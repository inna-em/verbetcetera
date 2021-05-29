class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] > nums[r]:
            while l < r - 1:
                mid = (l + r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < nums[r]:
                    r = mid
                elif nums[mid] > nums[r]:
                    l = mid
            if target < nums[0]:
                l = r
                r = len(nums) - 1
            elif target > nums[0]:
                r = l
                l = 0
            elif target == nums[0]:
                return 0
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1
