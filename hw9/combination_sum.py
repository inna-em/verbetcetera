class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtracking(i, tmp, summ):
            if summ == target:
                result.append(tmp.copy())
                return
            if summ > target:
                return
            for j in range(i, len(candidates)):
                tmp.append(candidates[j])
                summ += candidates[j]
                backtracking(j, tmp, summ)
                tmp.pop()
                summ -= candidates[j]
        
        backtracking(0, [], 0)
        
        return result
