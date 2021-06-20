class Trie:
    
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.children = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for word in words:
            curr = self.root
            for char in word[::-1]:
                if char not in curr.children:
                    curr.children[char] = Trie()
                curr = curr.children[char]
            curr.isEnd = True
        self.history = []
        

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        curr = self.root
        for i in range(-1, -len(self.history) - 1, -1):
            if curr.isEnd:
                return True
            if self.history[i] not in curr.children:
                return False
            curr = curr.children[self.history[i]]
        return curr.isEnd
