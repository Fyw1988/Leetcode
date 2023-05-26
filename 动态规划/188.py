class Solution:
    def maxProfit(self, k, prices) -> int:
        dp = [[0] * (2*k+1) for _ in range(2)]
        for i in range(len(dp[0])):
            if i % 2 != 0:
                dp[0][i] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(k):
                dp[i % 2][2*j+1] = max(dp[(i-1) % 2][2*j+1], dp[(i-1) % 2][2*j] - prices[i])
                dp[i % 2][2*j+2] = max(dp[(i-1) % 2][2*j+2], dp[(i-1) % 2][2*j+1] + prices[i])
        return max(max(dp[0]), max(dp[1]))


s = Solution()
print(s.maxProfit(k=2, prices=[3,2,6,5,0,3]))