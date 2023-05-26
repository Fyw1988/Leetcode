def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            if fast > slow:
                nums[fast] = 0
            slow += 1
        fast += 1
    return nums


# 双赋值语句简化上面的算法：
def moveZeroes(nums):
    n = len(nums)
    left = right = 0
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
