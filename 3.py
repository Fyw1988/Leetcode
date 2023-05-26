# 滑动窗口法 O(n) 只能打败30%python用户，估计是因为用的字典，查找键值耗时较长
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    滑动窗口
    """
    if not s: return 0
    slow, fast = 0, 0
    maxlen = 1
    d = dict()
    while fast < len(s):
        if s[fast] not in d.keys() or d[s[fast]] == 0:
            maxlen = max(maxlen, fast - slow + 1)
            d[s[fast]] = 1
        else:
            while d[s[fast]] > 0:
                d[s[slow]] -= 1
                slow += 1
            d[s[fast]] += 1
        fast += 1
    return maxlen


# 官方滑动窗口
# 同样是O(n)，这个写法耗时只有上面那个的一半，但是空间复杂度略微高一点
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
