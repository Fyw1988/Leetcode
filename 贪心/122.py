# 贪心 在山谷购入，山顶卖出
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cur = -1
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0 and cur == -1:
                cur = prices[i]   # 买入
                continue
            if prices[i+1] - prices[i] < 0 and cur != -1:
                profit += prices[i] - cur
                cur = -1
        if cur != -1:
            profit += prices[-1] - cur  # 到头了，不卖砸手里
        return profit


# 另一种贪心思路
# 由于题目说同一天可以同时买和卖股票，所以直接把所有两天的利润加起来
# 但是我觉得这种思路不够“贪心”，而应该叫“见好就收”
class Solution:
    def maxProfit(self, prices):
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result
