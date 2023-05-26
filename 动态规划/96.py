class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(sum([max(dp[j - 1], 1) * max(dp[i - j], 1) for j in range(1, i + 1)]))
        return dp[-1]