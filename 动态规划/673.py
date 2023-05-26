class Solution(object):
    def findNumberOfLIS(self, nums):
        # dp[i]：以nums[i]为结尾的最长递增序列的长度
        dp = [1] * len(nums)
        # count[i]：以nums[i]为结尾的最长递增子序列的个数
        count = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        maxL = max(dp)
        result = 0
        for i in range(len(count)):
            if dp[i] == maxL:
                result += count[i]
        return result


s = Solution()
print(s.findNumberOfLIS([2,2,2,2,2]))