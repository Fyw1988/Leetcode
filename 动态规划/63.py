class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n] * m
        dp[0][0] = -1 if obstacleGrid[0][0] == 1 else 1
        for i in range(m):
            for j in range(n):
                if i+j > 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = -1
                        continue
                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i][j-1], 0) + max(dp[i-1][j], 0)
        return max(dp[-1][-1], 0)