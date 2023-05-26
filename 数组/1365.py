# 暴力双循环
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            for j in range(n):
                if nums[j] < nums[i] and j != i:
                    ans[i] += 1
        return ans


# 哈希表，空间换时间
class Solution2:
    def smallerNumbersThanCurrent(self, nums):
        res = nums[:]
        hash = dict()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            hash[nums[i]] = i
        for i in range(len(res)):
            res[i] = hash[res[i]]
        return res


s = Solution2()
print(s.smallerNumbersThanCurrent([7,7,7,7]))