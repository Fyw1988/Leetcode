class Solution:
    def maxProfit(self, prices) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = dp[i-1] + max(0, prices[i]-prices[i-1])
        return max(dp)