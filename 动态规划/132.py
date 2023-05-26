# 超时了
class Solution(object):
    def minCut(self, s):
        dp = [0] * len(s)
        for i in range(len(dp)):
            dp[i] = i
        for i in range(len(s)):
            for j in range(i):
                if self.isPalindrome(s[:i + 1]):
                    dp[i] = 0
                elif self.isPalindrome(s[j + 1:i + 1]):
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]

    def isPalindrome(self, str):
        left, right = 0, len(str)-1
        while left <= right:
            if str[left] == str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# 用两个dp数组记录
class Solution(object):
    def minCut(self, s):
        isPalindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        isPalindrome[i][j] = True
                    else:
                        isPalindrome[i][j] = isPalindrome[i+1][j-1]

        dp = [0] * len(s)
        for i in range(len(dp)):
            dp[i] = i
        for i in range(len(s)):
            for j in range(i):
                if isPalindrome[0][i]:
                    dp[i] = 0
                elif isPalindrome[j+1][i]:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]


# 回溯
class Solution2(object):
    def __init__(self):
        self.path = []
        self.result = 2000

    def minCut(self, s):
        self.backtracking(s, 0)
        return self.result-1

    def backtracking(self, s, startIndex):
        if startIndex == len(s):
            self.result = min(len(self.path), self.result)
            return

        for i in range(startIndex, len(s)):
            if self.isPalindrome(s[startIndex:i+1]):
                self.path.append(s[startIndex:i+1])
                self.backtracking(s, i+1)
                self.path.pop()
            else:
                continue

    def isPalindrome(self, s):
        return s == s[::-1]


s = Solution2()
print(s.minCut('aab'))