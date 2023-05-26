class Solution:
    def lastStoneWeightII(self, stones) -> int:
        target = sum(stones)
        target //= 2
        dp = [0] * (target + 1)
        for i in range(0, len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
            # print(dp)
        return abs(sum(stones) - dp[-1] - dp[-1])


s = Solution()
print(s.lastStoneWeightII([2,7,4,1,8,1]))