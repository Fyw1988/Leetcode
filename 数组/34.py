def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = int(left + ((right - left) / 2))
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            if left == 0 and nums[left] == target:
                pos_left = left - 1
            else:
                pos_left = middle - 1
                while nums[pos_left] == target:
                    pos_left -= 1
            if right == len(nums) - 1 and nums[right] == target:
                pos_right = right + 1
            else:
                pos_right = middle + 1
                while nums[pos_right] == target:
                    pos_right += 1
            return pos_left + 1, pos_right - 1
    return [-1, -1]


# 将上面算法寻找左右边界的过程封装为一个函数可以减少行数：
def searchRange(nums, target):
    def binarySearch(nums, target, lower):
        left, right = 0, len(nums)-1
        ans = len(nums)
        while left <= right:  # 不变量：左闭右闭区间
            middle = left + (right-left) // 2
            # lower为True，执行前半部分，找到第一个大于等于 target的下标 ，否则找到第一个大于target的下标
            if nums[middle] > target or (lower and nums[middle] >= target):
                right = middle - 1
                ans = middle
            else:
                left = middle + 1
        return ans

    leftBorder = binarySearch(nums, target, True)  # 搜索左边界
    rightBorder = binarySearch(nums, target, False) - 1  # 搜索右边界
    if leftBorder <= rightBorder and rightBorder < len(nums) and nums[leftBorder] == target and nums[rightBorder] == target:
        return [leftBorder, rightBorder]
    return [-1, -1]


# 二分法找target位置，然后左右扩展
class Solution(object):
    def searchRange(self, nums, target):
        pos = self.halfSearch(nums, target)
        if pos < 0: return [-1, -1]
        left = right = pos
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left + 1, right - 1]

    def halfSearch(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))




















