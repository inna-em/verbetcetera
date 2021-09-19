class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        lps = self._preprocess(needle)
        print(lps)
        return self._find(lps, haystack, needle)
    
    def _preprocess(self, needle):
        lps = [0 for _ in range(len(needle))]
        l = 0
        for i in range(1, len(needle)):
            while l > 0 and needle[l] != needle[i]:
                l = lps[l-1]
            if needle[i] == needle[l]:
                l += 1
            lps[i] = l
        return lps
                    
        
    def _find(self, lps, haystack, needle):
        i, j = 0, 0 # i - haystack, j - needle
        for i in range(len(haystack)):
            while j > 0 and needle[j] != haystack[i]:
                j = lps[j-1]
            if needle[j] == haystack[i]:
                if j == len(needle) - 1:
                    return (i - len(needle) + 1)
                    j = lps[j] 
                else:
                    j += 1
        return -1
