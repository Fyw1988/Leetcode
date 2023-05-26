class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0] if nums[0] > 0 else 0
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], 0)
        if max(dp) > 0:
            return max(dp)
        else:
            return max(nums)