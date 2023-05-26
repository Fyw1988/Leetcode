class Solution(object):
    def maxProfit(self, prices):
        minPrice, maxProfit = 10**4+1, 0
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(prices[i]-minPrice, maxProfit)
        return maxProfit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))