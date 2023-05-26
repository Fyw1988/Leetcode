class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for str in strs:
            count0, count1 = self.count01(str)
            for i in range(m, count0-1, -1):
                for j in range(n, count1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-count0][j-count1] + 1)
        return dp[-1][-1]

    def count01(self, str):
        return int(str.count('0')), int(str.count('1'))


s = Solution()
print(s.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))