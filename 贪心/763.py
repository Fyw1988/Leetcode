class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        area = {}
        for i in range(len(s)):
            if s[i] not in area:
                area[s[i]] = [i, i]
            else:
                area[s[i]][1] = i
        rg = None
        for value in area.values():
            if not rg: rg = value
            if value[0] > rg[1]:
                res.append(rg[1]-rg[0]+1)
                rg = value
            else:
                rg[1] = max(value[1], rg[1])
        res.append(rg[1] - rg[0] + 1)
        return res


class Solution2:
    def partitionLabels(self, s):
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i
        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result


s = Solution2()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
# print(s.partitionLabels("ababcbacadefegdehijhklij"))