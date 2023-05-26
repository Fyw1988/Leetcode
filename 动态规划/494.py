class Solution:
    def findTargetSumWays(self, nums, target):
        sumValue = sum(nums)
        if abs(target) > sumValue or (target+sumValue) % 2 != 0: return 0
        target = (target + sumValue) // 2
        dp = [0 for _ in range(target + 1)]
        # 初始化
        dp[0] = 1
        # print(dp)
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j] + dp[j - nums[i]]
            # print(dp)
        return dp[-1]


class Solution:
    def findTargetSumWays(self, nums, target):
        sumValue = sum(nums)
        #注意边界条件为 target>sumValue or target<-sumValue or  (sumValue + target) % 2 == 1
        if abs(target) > sumValue or (sumValue + target) % 2 == 1: return 0
        bagSize = (sumValue + target) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagSize]

# s = Solution()
# print(s.findTargetSumWays([9,7,0,3,9,8,6,5,7,6], 2))