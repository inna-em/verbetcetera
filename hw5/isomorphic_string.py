class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.positions(s) == self.positions(t)
        
    def positions(self, s):
        letters = {}
        positions = {}
        n = 1
        for i, char in enumerate(s):
            if char not in letters:
                letters[char] = n
                positions[letters[char]] = [i]
                n += 1
            else:
                positions[letters[char]].append(i)
        return positions
