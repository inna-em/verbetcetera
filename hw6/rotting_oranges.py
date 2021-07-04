class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        curr_rotten = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    curr_rotten.append([i, j])
                    grid[i][j] = 0
        curr_rotten.append("dummy")
        shifts = ((1,0), (0,1), (-1,0), (0,-1))
        iterations = -1
        while curr_rotten:
            curr = curr_rotten.popleft()
            if curr == "dummy":
                iterations += 1
                if curr_rotten:
                    curr_rotten.append("dummy")
            else:
                for shift in shifts:
                    n_i = curr[0] + shift[0]
                    n_j = curr[1] + shift[1]
                    if 0 <= n_i < m and 0 <= n_j < n and grid[n_i][n_j] == 1:
                        curr_rotten.append([n_i, n_j])
                        grid[n_i][n_j] = 0
        if sum([sum(x) for x in grid]) > 0:
            return -1
        return iterations
