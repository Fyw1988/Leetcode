class Solution:
    def partitionLabels(self, s):
        section = {}
        for i in range(len(s)):
            if not section.get(s[i]):
                section[s[i]] = [i, i]
            else:
                section[s[i]][1] = i
        ans = []
        left, right = 0, 0
        for key, value in section.items():
            if value[0] <= right:
                right = max(right, value[1])
            else:
                ans.append(right-left+1)
                left, right = value[0], value[1]
        ans.append(right-left+1)
        return ans


# 哈希表记录每个字母出现的最远范围
# 当指针追上范围的时候，代表可以从此处分割
class Solution:
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