class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1, 1, 1]
        for i in range(3, n+1):
            dp.append(max([j * max(dp[i-j], i-j) for j in range(1, i)]))
        return dp[-1]


# 稍微剪枝
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1, 1, 1]
        for i in range(3, n+1):
            dp.append(max([j * max(dp[i-j], i-j) for j in range(1, i//2+1)]))
        return dp[-1]