class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minabs = 10e4
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            if abs(nums[i]) < minabs:
                minabs = abs(nums[i])
        if k == 0 or k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - 2 * minabs


s = Solution()
print(s.largestSumAfterKNegations([2,-3,-1,5,-4], 2))
