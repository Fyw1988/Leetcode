def reverseLeftWords(s, n):
    """
    :type s: str
    :type n: int
    :rtype: str
    """
    s = s[n:] + s[0:n]
    return s


# 上面那种写法太没意思了，采用和上一题一样的双反转的模式
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        def reverse_sub(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        res = list(s)
        end = len(res) - 1
        reverse_sub(res, 0, n - 1)
        reverse_sub(res, n, end)
        reverse_sub(res, 0, end)
        return ''.join(res)