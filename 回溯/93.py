class Solution(object):
    def __init__(self):
        self.path = []
        self.results = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.backtracking(s, 0)
        return self.results

    def backtracking(self, s, index):
        if len(self.path) == 4 and index == len(s):
            self.results.append('.'.join(self.path))
            return

        for i in range(index, len(s)):
            # 剪枝
            if len(self.path) == 3 and int(s[index:]) > 255:
                return

            sub = s[index:i+1]
            if (0 < int(sub) <= 255 and sub[0] != '0') or (int(sub) == 0 and len(sub) == 1):
                self.path.append(sub)
                self.backtracking(s, i+1)
                self.path.pop()
            else:
                return
