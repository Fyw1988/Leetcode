class Solution(object):
    def __init__(self):
        self.path = []
        self.results = []

    def partition(self, s):
        self.backtracking(s, 0)
        return self.results

    def backtracking(self, s, startIndex):
        if startIndex == len(s):
            self.results.append(self.path[:])
            return

        for i in range(startIndex, len(s)):
            if self.isPalind(s[startIndex:i+1]):
                self.path.append(s[startIndex:i+1])
                self.backtracking(s, i+1)
                self.path.pop()

    def isPalind(self, s):
        return s == s[::-1]