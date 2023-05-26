class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + 1 if nums[i] > nums[i-1] else 1
        return max(dp)