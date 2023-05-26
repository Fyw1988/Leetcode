class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 2: return max(nums)
        dp1, dp2 = self.dp(nums[0:-1]), self.dp(nums[1:])
        return max(dp1[-1], dp2[-1], dp2[-2])

    def dp(self, nums):
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp


s = Solution()
print(s.rob([1,2,3,1]))