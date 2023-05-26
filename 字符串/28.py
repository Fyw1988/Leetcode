def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle: return 0
    n = len(needle)
    left, right = 0, n
    while right <= len(haystack):
        if haystack[left:right] == needle:
            return left
        left += 1
        right += 1
    return -1


# KMP算法
# 前缀表减一
class Solution:
    def strStr(self, haystack, needle):
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p+1] != haystack[j]:
                p = next[p]
            if needle[p+1] == haystack[j]:
                p += 1
            if p == a-1:
                return j-a+1
        return -1

    def getnext(self, a, needle):  # (-1, 0, -1, 0, 1, -1)
        next = ['' for _ in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            while (k > -1 and needle[k+1] != needle[i]):
                k = next[k]
            if needle[k+1] == needle[i]:
                k += 1
            next[i] = k
        return next


# KMP算法实现2
# 前缀表后移
class Solution2:
    def strStr(self, haystack, needle):
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        i = j = 0
        next = self.getnext(a, needle)  # 获取needle的前缀数组
        while i < b and j < a:
            if j == -1 or needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == a:
            return i-j
        else:
            return -1

    def getnext(self, a, needle):   # (-1, 0, 1, 0, 1, 2)
        next = ['' for _ in range(a)]
        j, k = 0, -1
        next[0] = k
        while j < a-1:
            if k == -1 or needle[k] == needle[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next


# 前缀表减一：实现二
class Solution3:
    def strStr(self, haystack, needle):
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        i, j = 0, -1
        while i < b and j < a-1:
            if j >= 0 and needle[j+1] != haystack[i]:
                j = next[j]
            elif j < 0 and needle[j+1] != haystack[i]:
                i += 1
            else:
                j += 1
                i += 1
        if j == a-1:
            return i-a
        return -1

    def getnext(self, a, needle):  # (-1, 0, -1, 0, 1, -1)
        next = ['' for _ in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            while k > -1 and needle[k+1] != needle[i]:
                k = next[k]
            if needle[k+1] == needle[i]:
                k += 1
            next[i] = k
        return next


# 使用原来的前缀表
class Solution4(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        i, j = 0, 0
        while i < b and j < a:
            if j > 0 and needle[j] != haystack[i]:
                j = next[j-1]
            elif j == 0 and needle[j] != haystack[i]:
                i += 1
            else:
                j += 1
                i += 1
        if j == a:
            return i-a
        return -1

    def getnext(self, needle):  # (0, 1, 0, 1, 2, 0)
        next = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j >= 1 and needle[i] != needle[j]:
                j = next[j-1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j
        return next
