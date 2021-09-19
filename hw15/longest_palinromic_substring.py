class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            l = max(self._expand(s, i, i), self._expand(s, i, i + 1))
            if l > end - start:
                start = i - (l - 1)//2
                end = i + l//2
        return s[start:end+1]
            
    def _expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
