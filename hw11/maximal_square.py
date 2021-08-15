class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_len = 0 
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                max_len = 1
        for j in range(len(matrix[0])):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                max_len = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len**2
