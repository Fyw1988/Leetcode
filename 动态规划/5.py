# 动态规划
class Solution(object):
    def longestPalindrome(self, s):
        dp = [[False] * len(s) for _ in range(len(s))]
        maxS = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j-i+1 > len(maxS):
                    maxS = s[i:j+1]
        return maxS


# 双指针
class Solution2(object):
    def longestPalindrome(self, s):
        maxS = ''
        for i in range(len(s)):
            sub = self.extend(s, i, i)
            maxS = sub if len(sub) > len(maxS) else maxS
            sub = self.extend(s, i, i+1)
            maxS = sub if len(sub) > len(maxS) else maxS
        return maxS

    def extend(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break
        return s[i+1:j]


s = Solution2()
print(s.longestPalindrome("cbbd"))