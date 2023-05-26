def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    def reverse(str):
        left = 0
        right = len(str) - 1
        while left < right:
            str[left], str[right] = str[right], str[left]
            left += 1
            right -= 1
        return str

    res = list(s)
    n = len(s) // (2*k)
    for i in range(n):
        res[2 * i * k:(2 * i + 1) * k] = reverse(res[2 * i * k:(2 * i + 1) * k])
    if 0 < len(s) % (2*k) <= k:
        res[2 * n * k:] = reverse(res[2 * n * k:])
    elif len(s) % (2*k) > k:
        res[2 * n * k:(2 * n + 1) * k] = reverse(res[2 * n * k:(2 * n + 1) * k])

    return ''.join(res)


# 上面的切片太麻烦，代码随想录写法：
def reverseStr(s, k):
    """
    1. 使用range(start, end, step)来确定需要调换的初始位置
    2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
    3. 用切片整体替换，而不是一个个替换.
    """
    def reverse_substring(text):
        left, right = 0, len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    res = list(s)

    for cur in range(0, len(s), 2 * k):
        res[cur: cur + k] = reverse_substring(res[cur: cur + k])

    return ''.join(res)


# 一种更为pythonic的写法（其实也是双指针）
def reverseStr(s, k):
    # Two pointers. Another is inside the loop.
    p = 0
    while p < len(s):
        p2 = p + k
        # Written in this could be more pythonic.
        s = s[:p] + s[p: p2][::-1] + s[p2:]
        p = p + 2 * k
    return s


# 二刷
class Solution(object):
    def reverseStr(self, s, k):
        ans = list(s)
        left, right = 0, 0
        while right < len(s)-1:
            while right-left+1 < 2*k and right < len(s)-1:
                right += 1
            mid = left + k - 1 if right-left+1 >= k else right
            self.reverse(ans, left, mid)
            left = right + 1
        return ''.join(ans)

    def reverse(self, s, i, j):
        left, right = i, j
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


s = Solution()
print(s.reverseStr(s = "a", k = 2))