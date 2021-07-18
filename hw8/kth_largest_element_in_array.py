class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        return self._select(l, r, len(nums) - k, nums)
        
    def _partition(self, nums, l, r, pivot_idx):
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        store_idx = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        nums[r], nums[store_idx] = nums[store_idx], nums[r] 
        return store_idx
    
    def _select(self, l, r, k, nums):
        if l == r:
            return nums[l]
        pivot_idx = random.randint(l, r) 
        pivot_idx = self._partition(nums, l, r, pivot_idx)
        if pivot_idx == k:
            return nums[k]
        elif pivot_idx > k:
            return self._select(l, pivot_idx - 1, k, nums)
        else:
            return self._select(pivot_idx + 1, r, k, nums)
