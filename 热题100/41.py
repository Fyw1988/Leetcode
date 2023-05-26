# 原地哈希
class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return n+1


# 解法二
class Solution2:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = n+1
        for i in range(len(nums)):
            if 1 <= abs(nums[i]) <= n:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return n+1


s = Solution2()
print(s.firstMissingPositive([3,4,-1,1]))