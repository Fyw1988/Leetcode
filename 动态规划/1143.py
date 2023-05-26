class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        result = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                dp[i][j] = self.getMax([dp[n][:j] for n in range(i)]) + 1 if text1[i-1] == text2[j-1] else 0
                result = max(dp[i][j], result)
        return result

    def getMax(self, nums):
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                result = max(result, nums[i][j])
        return result


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]