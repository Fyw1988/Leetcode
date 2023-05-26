# 贪心
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -10e4
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            res = res if res > s else s
            if s < 0:
                s = 0

        return res


# DP
class Solution2:
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)