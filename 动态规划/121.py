class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return max(dp[-1][0], dp[-1][1])


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))