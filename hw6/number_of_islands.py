class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        shifts = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    q = deque()
                    q.append([i, j])
                    grid[i][j] = "0"
                    while q:
                        ic, jc = q.popleft()
                        for s in shifts:
                            s_i, s_j = ic + s[0], jc + s[1]
                            if 0 <= s_i < m and 0 <= s_j < n and grid[s_i][s_j] == "1":
                                q.append([s_i, s_j])
                                grid[s_i][s_j] = "0"
        return islands
