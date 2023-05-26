# 暴力双循环 O(n^2)
def removeElement1(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    size = len(nums)
    for i in range(size):
        i -= (len(nums) - size)  # 数组移除元素后变短，需要更新指针
        if nums[i] == val:
            for j in range(i+1, size):
                nums[j-1] = nums[j]
            size -= 1
    return size


# 双指针
def removeElement2(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    fast = 0
    slow = 0
    size = len(nums)
    while fast < size:
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


# 反向双指针
def removeElement3(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    first = 0
    second = len(nums) - 1
    while first <= second:
        if nums[first] == val:
            nums[first] = nums[second]
            second -= 1
        else:
            first += 1
    return first