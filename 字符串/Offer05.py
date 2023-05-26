# 这题依然是双指针
def replaceSpace1(s):
    counter = s.count(' ')

    res = list(s)
    # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
    res.extend([' '] * counter * 2)

    # 原始字符串的末尾，拓展后的末尾
    left, right = len(s) - 1, len(res) - 1

    while left >= 0:
        if res[left] != ' ':
            res[right] = res[left]
            right -= 1
        else:
            # [right - 2, right), 左闭右开
            res[right - 2: right + 1] = '%20'
            right -= 3
        left -= 1
    return ''.join(res)


# 一种简洁写法
# 这种其实是最容易想到的方法的实现。只不过由于正向遍历会导致字符串填充后索引发生变化。所以采用反向遍历反向填充的方法来实现
def replaceSpace2(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    for e, i in enumerate(s[::-1]):
        print(i, e)
        if i == " ":
            s = s[: n - (e + 1)] + "%20" + s[n - e:]
        print("")
    return s


# 二刷
class Solution(object):
    def replaceSpace(self, s):
        ans = list(s)
        for i in range(len(ans)):
            if ans[i] == ' ':
                ans[i] = '%20'
        return ''.join(ans)


s = Solution()
print(s.replaceSpace("We are happy."))