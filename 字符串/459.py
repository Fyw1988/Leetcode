def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    l = len(s)
    subl = l // 2
    for i in range(1, subl + 1):
        if l % i != 0:
            continue
        if s[:i] * (l // i) == s:
            return True
    return False


# KMP解法
class Solution:
    def repeatedSubstringPattern(self, s):
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        return False

    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt


# 自己写的KMP，比较啰嗦
class Solution2(object):
    def repeatedSubstringPattern(self, s):
        nxt = [0] * (len(s) + 1)
        if len(s) <= 1: return False
        self.getNext(nxt, s)
        if nxt[-1] >= len(s) // 2 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        else:
            return False

    def getNext(self, nxt, s):
        nxt[0] = -1
        i, j = -1, 0
        while j < len(s):
            if i == -1 or s[i] == s[j]:
                i += 1
                j += 1
                nxt[j] = i
            else:
                i = nxt[i]