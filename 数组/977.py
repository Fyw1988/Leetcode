# 双指针
def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0
    right, k = len(nums) - 1, len(nums) - 1
    result = [-1] * len(nums)
    while right >= left:
        if nums[right] ** 2 < nums[left] ** 2:
            result[k] = nums[left] ** 2
            left += 1
        else:
            result[k] = nums[right] ** 2
            right -= 1
        k -= 1
    return result
