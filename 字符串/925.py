class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        cur1, cur2 = 0, 0
        while cur1 < len(name) and cur2 < len(typed):
            if name[cur1] == typed[cur2]:
                cur1 += 1
                cur2 += 1
                if (cur1 < len(name) and name[cur1] != name[cur1 - 1]) or cur1 == len(name):
                    while cur2 < len(typed) and typed[cur2] == typed[cur2 - 1]:
                        cur2 += 1
            else:
                return False
        if cur1 == len(name) and cur2 == len(typed):
            return True
        return False


# 代码随想录
class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
        # If the current letter matches, move as far as possible
            if typed[j] == name[i]:
                while j+1 < len(typed) and typed[j] == typed[j+1]:
                    j += 1
                    # special case when there are consecutive repeating letters
                    if i+1 < len(name) and name[i] == name[i+1]:
                        i += 1
                else:
                    j += 1
                    i += 1
            else:
                return False
        return i == len(name) and j == len(typed)


s = Solution2()
print(s.isLongPressedName('saeed', 'ssaaedd'))
