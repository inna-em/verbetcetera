class DSU:
    def __init__(self, stones):
        self.parents = {}
        self.rank = defaultdict(int)
        for stone in stones:
            self.parents[(stone[0], stone[1])] = (stone[0], stone[1])
            self.rank[(stone[0], stone[1])] = 1
            
    def find(self, x):
        if (x[0], x[1]) != self.parents[(x[0], x[1])]:
            self.parents[(x[0], x[1])] = self.find(self.parents[(x[0], x[1])])
        return self.parents[(x[0], x[1])]
    
    def union(self, x, y):
        x_tup, y_tup = (x[0], x[1]), (y[0], y[1])
        xp = self.find(x_tup)
        yp = self.find(y_tup)
        if xp == yp:
            return
        if self.rank[xp] > self.rank[yp]:
            self.parents[yp] = xp
        elif self.rank[xp] < self.rank[yp]:
            self.parents[xp] = yp
        else:
            self.parents[yp] = xp
            self.rank[xp] += 1
        
    def is_connected(self, x, y):
        return x[0] == y[0] or x[1] == y[1]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU(stones)
        for i, stone in enumerate(stones):
            for j, pair in enumerate(stones[i+1::]):
                if dsu.is_connected(stone, pair):
                    dsu.union(stone, pair)         
        result = 0
        for k, v in dsu.parents.items():
            if k != v:
                result += 1
                
        return result
        
