class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        dp = [[False] * len(t) for _ in s]
        for i in range(len(t)):
            if t[i] == s[0]:
                for j in range(i, len(t)):
                    dp[0][j] = True
                break
        # print(dp)
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                dp[i][j] = dp[i-1][j-1] if s[i] == t[j] else dp[i][j-1]
        # print(dp)
        return dp[-1][-1]


s = Solution()
print(s.isSubsequence(s = "abc", t = "ahbgdc"))