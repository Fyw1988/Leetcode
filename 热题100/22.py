class Solution(object):
    def __init__(self):
        self.path = []
        self.state = 0
        self.results = []
        self.type = ['(', ')']

    def generateParenthesis(self, n):
        self.backtracking(n)
        return self.results

    def backtracking(self, n):
        if self.state == 0 and len(self.path) == 2 * n:
            self.results.append(''.join(self.path[:]))
            return

        if len(self.path) >= 2 * n:
            return

        for i in self.type:
            temp = self.state
            if i == '(':
                self.state += 1
            else:
                self.state -= 1
            if self.state < 0 or self.state > n:
                self.state = temp
                continue
            self.path.append(i)
            self.backtracking(n)
            self.path.pop()
            self.state = temp
