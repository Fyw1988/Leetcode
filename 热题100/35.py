# 左闭右开
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while right > left:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left