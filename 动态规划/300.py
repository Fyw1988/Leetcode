# 错误示例
class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] if nums[i] <= nums[i-1] else dp[i-1] + 1
        return dp[-1]


class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)


s = Solution()
print(s.lengthOfLIS([4,10,4,3,8,9]))