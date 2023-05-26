from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        hash = defaultdict(list)

        for s in strs:
            hash[''.join(sorted(s))].append(s)

        return list(hash.values())


class Solution2:
    def groupAnagrams(self, strs):
        hash = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for letter in s:
                key[ord(letter)-ord('a')] += 1
            hash[tuple(key)].append(s)
        return list(hash.values())


