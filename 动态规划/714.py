class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        dp = [[0] * 2 for _ in range(2)]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i % 2][0] = max(dp[(i-1) % 2][0], dp[(i-1) % 2][1] - prices[i])
            dp[i % 2][1] = max(dp[(i-1) % 2][1], dp[(i-1) % 2][0] + prices[i] - fee)
        return max(max(dp[0]), max(dp[1]))


s = Solution()
print(s.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))