class Trie:
    
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.isEnd = True  

    def search(self, word: str) -> bool:
        
        def helper(word, node):
            for i, char in enumerate(word):
                if char != ".":
                    if char not in node.children:
                        return False
                    else:
                        node = node.children[char]
                else:
                    for child in node.children:
                        if helper(word[i+1:], node.children[child]):
                            return True
                    return False
            return node.isEnd
            
        return helper(word, self.root)
