class DSU:
    def __init__(self, grid):
        self.parents = {}
        self.ranks = {}
        self.areas = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.parents[(i, j)] = (i, j)
                    self.ranks[(i, j)] = 1
                    self.areas[(i, j)] = 1
        
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return
        if self.ranks[xp] > self.ranks[yp]:
            self.parents[yp] = xp
            self.areas[xp] += 1
        elif self.ranks[xp] < self.ranks[yp]:
            self.parents[xp] = yp
            self.areas[yp] += 1
        else:
            self.parents[yp] = xp
            self.areas[xp] += 1
            self.ranks[xp] += 1
        


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dsu = DSU(grid)
        shifts = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q = deque()
                    q.append((i, j))
                    grid[i][j] = 0
                    while q:
                        cur = q.popleft()
                        for shift in shifts:
                            s_i, s_j = cur[0] + shift[0], cur[1] + shift[1]
                            if 0 <= s_i < len(grid) and 0 <= s_j < len(grid[0]) and grid[s_i][s_j] == 1:
                                dsu.union((cur[0], cur[1]), (s_i, s_j))
                                q.append((s_i, s_j))
                                grid[s_i][s_j] = 0
        max_area = 0
        for k, v in dsu.areas.items():
            max_area = max(max_area, v)
        return max_area
