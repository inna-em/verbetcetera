class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = 0
                    q = deque()
                    q.append((i, j))
                    grid[i][j] = 0
                    while q:
                        node = q.popleft()
                        curr_area += 1
                        for s in n:
                            si, sj = s[0], s[1]
                            ni, nj = node[0] + si, node[1] + sj
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                                q.append((ni, nj))
                                grid[ni][nj] = 0
                    max_area = max(max_area, curr_area)
        return max_area
