# 哈希
class Solution2:
    def uniqueOccurrences(self, arr) -> bool:
        t = {}
        for num in arr:
            t[num] = t.get(num, 0) + 1
        ans = set(t.values())

        return len(ans) == len(t)


#
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        ref = dict()

        for i in range(len(arr)):
            ref[arr[i]] = ref.get(arr[i], 0) + 1

        value_list = sorted(ref.values())

        for i in range(len(value_list) - 1):
            if value_list[i + 1] == value_list[i]:
                return False

        return True