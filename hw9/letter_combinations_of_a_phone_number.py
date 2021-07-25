class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self._digits = digits
        self._letters = {"2": {"a", "b" ,"c"}, 
                   "3": {"d", "e", "f"}, 
                   "4": {"g", "h", "i"}, 
                   "5": {"j", "k", "l"}, 
                   "6": {"m", "n", "o"}, 
                   "7": {"p", "q", "r", "s"}, 
                   "8": {"t", "u", "v"}, 
                   "9": {"w", "x", "y", "z"}}
        self._result = []
        if len(digits) > 0:
            self._backtracking(0, [])
        return self._result
            
    def _backtracking(self, i, tmp):
        if i >= len(self._digits):
            self._result.append(''.join(tmp))
            return
        for l in self._letters[self._digits[i]]:
            tmp.append(l)
            self._backtracking(i + 1, tmp)
            tmp.pop()
