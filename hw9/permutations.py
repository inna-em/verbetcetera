class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def backtrack(tmp, idxs):
            if len(tmp) == len(nums):
                result.append(tmp.copy())
                return
            for i, num in enumerate(nums):
                if i in idxs:
                    continue
                tmp.append(nums[i])
                idxs.add(i)
                backtrack(tmp, idxs)
                tmp.pop()
                idxs.discard(i)
                
        backtrack([], set())
        
        return result
