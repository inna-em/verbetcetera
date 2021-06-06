class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                rep = ''
                while stack[-1] != "[":
                    p = stack.pop()
                    rep = p + rep
                stack.pop()
                num = ''
                while len(stack)>0 and stack[-1].isdigit():
                    n = stack.pop()
                    num = n + num
                number = int(num)
                for _ in range(number):
                    stack.append(rep)
        return "".join(stack)
