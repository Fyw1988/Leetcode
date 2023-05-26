class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 局部最优：最大的饼干分给满足条件的胃口最大的孩子
        # 总体最优：满足的孩子最多
        g.sort()
        s.sort()
        cur1 = 0
        cur2 = 0
        sum = 0
        while cur1 < len(g) and cur2 < len(s):
            if s[cur2] >= g[cur1]:
                sum += 1
                cur1 += 1
                cur2 += 1
            else:
                cur2 += 1
        return sum

