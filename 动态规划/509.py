class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n+1)
        try:
            dp[0], dp[1] = 0, 1
        except:
            return n
        for i in range(n+1):
            if i < 2:
                continue
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


# 一种占用空间更小的写法
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c = 0, 1, 0
        for i in range(1, n):
            c = a + b
            a, b = b, c
        return c