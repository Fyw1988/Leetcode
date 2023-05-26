def removeDuplicates(nums):
    fast = 0
    slow = 0
    size = len(nums)
    while fast < size:
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1


# 上面这个双指针写了很久，感觉思路不是很清晰，参考答案的双指针写法：
def removeDuplicates(nums):
    if not nums:
        return 0
    n = len(nums)
    fast = slow = 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow
