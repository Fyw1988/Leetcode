# 写滑动窗口，两个while循环，第一个无条件更新右指针，第二个更新左指针
# 右指针更新完后，更新窗口的情况，然后就可以根据窗口情况来更新左窗口了（如果窗口符合情况则更新左指针，寻找下一个符合情况的窗口，否则继续更新右指针，直到找到符合情况的窗口）
def minWindow(s, t):
    # 滑动窗口 + 用一个need字典 + 一个match变量记录完成匹配的字符数量
    m, n = len(s), len(t)
    need = dict()  # 需要的字符数
    win = dict()  # 只记录有效的字符数量
    for x in t:  need[x] = need.get(x, 0) + 1  # get()没有的话返回0
    match = 0  # 完成匹配的字符数量
    start, min_len = 0, m + 1   # 因为这题需要返回最短字符串，因此需要start来记录开始位置
    left, right = 0, 0   # 滑动窗口双指针
    while right < m:
        if s[right] in need:  # 只统计t需要的
            win[s[right]] = win.get(s[right], 0) + 1
            if win[s[right]] == need[s[right]]:  # 记录第一次完成匹配的字符数
                match += 1
        while match == len(need):  # 如果匹配的字符数，到达need的字符数，尝试缩小窗口
            if right - left + 1 < min_len:
                min_len = right - left + 1  # [left, right]闭区间
                start = left
            if s[left] in win:  # 只需要更新在win中有效字符数量
                win[s[left]] -= 1
                if win[s[left]] < need[s[left]]:  # 如果导致当前字符数量不够了，则有效匹配字符数减一
                    match -= 1
            left += 1
        right += 1
    if min_len == m + 1: return ""  # 无法覆盖
    return s[start:start + min_len]


# 二刷
class Solution(object):
    def minWindow(self, s, t):
        hash1 = {}
        hash2 = {}
        for i in t: hash1[i] = hash1.get(i, 0) + 1
        match = 0
        minL = len(s)
        slow = 0
        index = [0, -1]
        for fast in range(len(s)):
            if s[fast] in hash1:
                hash2[s[fast]] = hash2.get(s[fast], 0) + 1
                if hash2[s[fast]] == hash1[s[fast]]:
                    match += 1
            while match == len(hash1):
                if fast-slow+1 <= minL:
                    minL = fast-slow+1
                    index = [slow, fast]
                if s[slow] in hash1:
                    hash2[s[slow]] -= 1
                    if hash2[s[slow]] < hash1[s[slow]]:
                        match -= 1
                slow += 1
        return s[index[0]:index[1]+1]
