# 哈希表
# list转set是O(n)的时间复杂度，set中的in操作是O(1)的时间复杂度
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums: return 0
        nums = set(nums)
        maxL = 1
        for num in nums:
            if num-1 not in nums:
                i = 1
                while num+i in nums:
                    maxL = max(maxL, i+1)
                    i += 1
        return maxL