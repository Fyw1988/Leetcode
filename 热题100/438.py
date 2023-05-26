# 超时边缘
class Solution:
    def findAnagrams(self, s: str, p: str):
        ans = []
        p = ''.join(sorted(p))
        k = len(p)
        for i in range(len(s)-k+1):
            if ''.join(sorted(s[i:i+k])) == p:
                ans.append(i)
        return ans


#
class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans

