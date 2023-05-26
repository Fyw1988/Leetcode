class Solution(object):
    def pivotIndex(self, nums):
        numSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if numSum - leftSum - nums[i] == leftSum:
                return i
            leftSum += nums[i]
        return -1


s = Solution()
print(s.pivotIndex([-1,-1,-1,-1,-1,0]))

