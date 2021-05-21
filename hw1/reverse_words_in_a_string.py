class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        result = []
        word_end = len(s) - 1
        word_start = 0
        i = len(s)-1
        while i > 0:
            if s[i] == " ":
                word_start = i+1
                result.append(s[word_start:word_end + 1])
                while s[i] == " ":
                    i -= 1
                word_end = i
            i -= 1
        result.append(s[0:word_end + 1])
        return ' '.join(result)
