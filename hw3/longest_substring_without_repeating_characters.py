class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        res_max = 0
        curr_sum = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                curr_sum = i - j + 1
                res_max = max(res_max, curr_sum)
            else:
                while s[j] != s[i]:
                    seen.discard(s[j])
                    j += 1
                j += 1
                curr_sum = i - j + 1
        return res_max
