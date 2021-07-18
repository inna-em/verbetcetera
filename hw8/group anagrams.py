class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            k = self.anagramKey(word)
            if k not in d:
                d[k] = [word]
            else:
                d[k].append(word)
        result = []
        for group in d.values():
            result.append(group)
        return result
        
        
    def anagramKey(self, s):
        return ''.join(sorted(s))
