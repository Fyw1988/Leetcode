class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict:
                    dp[i] = dp[j] or dp[i]

        return dp[-1]


class Solution:
    def wordBreak(self, s, wordDict):
        '''排列'''
        dp = [False]*(len(s) + 1)
        dp[0] = True
        # 遍历背包
        for j in range(1, len(s) + 1):
            # 遍历单词
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        return dp[len(s)]


class Solution:
    def wordBreak(self, s, wordDict):
        '''排列'''
        dp = [False]*(len(s) + 1)
        dp[0] = True
        # 遍历背包
        for word in wordDict:
            for j in range(len(word), len(s) + 1):
            # 遍历单词
                dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        return dp[len(s)]


s = Solution()
print(s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))