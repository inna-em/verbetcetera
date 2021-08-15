class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for x in range(m)] for y in range(n)]
        i = 0
        while i < m:
            if obstacleGrid[0][i] == 1:
                i = m
            else:
                dp[0][i] = 1
                i += 1
        j = 0
        while j < n:
            if obstacleGrid[j][0] == 1:
                j = n
            else:
                dp[j][0] = 1
                j += 1
        for r in range(1, n):
            for c in range(1,m):
                if obstacleGrid[r][c] == 1:
                    continue
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]
