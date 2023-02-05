import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        func_map = {"+": operator.add,
                   "-": operator.sub,
                   "*": operator.mul,
                   "/": self.floordiv}
        for symb in tokens:
            if symb not in func_map:
                stack.append(int(symb))
            else:
                x = stack.pop()
                y = stack.pop()
                n = func_map[symb](y, x)
                stack.append(n)
        return stack[0]
    
    
    def floordiv(self, x, y):
        return int(x / y)
