# 704. 二分查找

# 左闭右闭
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + ((right - left) / 2)
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


# 左开右闭
def search(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        middle = left + ((right - left) / 2)
        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1
