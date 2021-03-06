import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.l.append(val)
        self.d[val] = len(self.l) - 1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        v = self.l.pop()
        if v != val and self.l:
            print(self.d[val])
            self.l[self.d[val]] = v
            self.d[v] = self.d[val]
        del self.d[val]
        return True
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randint(0, len(self.l) - 1)
        return self.l[i]
