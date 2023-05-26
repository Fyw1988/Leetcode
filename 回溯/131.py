class Solution(object):
    def __init__(self):
        self.results = []
        self.path = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.backtracking(s, 0)
        return self.results

    def backtracking(self, s, indexbegin):
        if indexbegin == len(s):
            self.results.append(self.path[:])
            return

        for i in range(indexbegin, len(s)):

            sub = s[indexbegin:i + 1]
            if self.ispalindrom(sub):
                self.path.append(sub)
                self.backtracking(s, i + 1)
                self.path.pop()
            else:
                continue

    def ispalindrom(self, s):
        return s == s[::-1]


s = Solution()
print(s.partition("cdd"))