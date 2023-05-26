class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if len(cost) < 3: return min(cost)
        dp1 = [0, cost[0], cost[0]]
        dp2 = [0, 0, cost[1]]
        for i in range(len(cost)+1):
            if i > 2:
                dp1.append(min(dp1[i-1] + cost[i-1], dp1[i-2] + cost[i-2]))
                dp2.append(min(dp2[i-1] + cost[i-1], dp2[i-2] + cost[i-2]))
        return min(dp1[-1], dp2[-1])


# 简化写法
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if len(cost) < 3: return min(cost)
        dp = [0, 0]
        for i in range(len(cost)+1):
            if i > 1:
                dp.append(min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]))
        return dp[-1]