class Solution:
    def coinChange(self, coins, amount) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                if dp[i] >= 0 and dp[i-coin] >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
                elif dp[i] < 0 and dp[i-coin] < 0:
                    dp[i] = -1
                else:
                    dp[i] = max(dp[i], dp[i-coin]+1)
            # print(dp)
        return dp[-1]


class Solution:
    def coinChange(self, coins, amount) -> int:
        '''版本一'''
        # 初始化
        dp = [float("inf")]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


class Solution:
    def coinChange(self, coins, amount) -> int:
        '''版本二'''
        # 初始化
        dp = [float("inf")]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for j in range(1, amount + 1):
            # 遍历背包
            for coin in coins:
                if j >= coin:
                	dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1