class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] < nums[-1]:
                right = pivot
            else:
                left = pivot + 1
        return nums[left]