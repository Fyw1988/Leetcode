class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        nums = [i**2 for i in range(1, int(pow(n, 0.5))+1)]
        for num in nums:
            for i in range(num, n+1):
                dp[i] = min(dp[i], dp[i-num] + 1)
        return dp[-1]


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        nums = [i ** 2 for i in range(1, int(pow(n, 0.5)) + 1)]
        for i in range(1, n + 1):
            for num in nums:
                if i >= num:
                    dp[i] = min(dp[i], dp[i - num] + 1)
        return dp[-1]
