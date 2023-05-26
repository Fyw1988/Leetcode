# 动态规划
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True
                        result += 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j]:
                            result += 1

        return result


# s = Solution()
# print(s.countSubstrings('aaaaa'))


# 双指针
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s))
            result += self.extend(s, i, i+1, len(s))
        return result

    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res