# 递归，但超时
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# dp
class Solution(object):
    def climbStairs(self, n):
        dp = [1, 2]
        for i in range(n):
            if i > 1:
                dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]