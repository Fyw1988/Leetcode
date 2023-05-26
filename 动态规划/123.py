class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0] = [0, -prices[0], 0, -prices[0], 0]
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        return max(dp[-1])


class Solution2:
    def maxProfit(self, prices) -> int:
        dp = [[0] * 5 for _ in range(2)]
        dp[0] = [0, -prices[0], 0, -prices[0], 0]
        print(dp)
        for i in range(1, len(prices)):
            dp[i % 2][0] = dp[(i-1) % 2][0]
            dp[i % 2][1] = max(dp[(i-1) % 2][1], dp[(i-1) % 2][0] - prices[i])
            dp[i % 2][2] = max(dp[(i-1) % 2][2], dp[(i-1) % 2][1] + prices[i])
            dp[i % 2][3] = max(dp[(i-1) % 2][3], dp[(i-1) % 2][2] - prices[i])
            dp[i % 2][4] = max(dp[(i-1) % 2][4], dp[(i-1) % 2][3] + prices[i])
        print(dp)
        return max(max(dp[0]), max(dp[1]))


prices = [3,2,6,5,0,3]
s = Solution2()
print(s.maxProfit(prices))