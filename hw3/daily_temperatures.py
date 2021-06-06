class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        temp_stack = []
        for i in range(n):
            while temp_stack and temp_stack[-1][1] < temperatures[i]:
                temp = temp_stack.pop()
                result[temp[0]] = i - temp[0]
            temp_stack.append((i, temperatures[i]))
        return result
