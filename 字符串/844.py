# 双指针一
class Solution(object):
    def backspaceCompare(self, s, t):
        i, j = len(s)-1, len(t)-1
        while i >= 0 or j >= 0:
            if i >= 0 and s[i] == '#':
                back1 = 2
                while back1 and i >= 0:
                    i -= 1
                    if s[i] == '#':
                        back1 += 1
                    else:
                        back1 -= 1
            if j >= 0 and t[j] == '#':
                back2 = 2
                while back2 and j >= 0:
                    j -= 1
                    if t[j] == '#':
                        back2 += 1
                    else:
                        back2 -= 1
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return i == j