
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    val = dict()
    for i in range(len(nums)):
        if nums[i] not in val.keys():
            val[nums[i]] = [i]
        else:
            val[nums[i]].append(i)
    for i in range(len(nums)):
        if target - nums[i] in val.keys() and 2*nums[i] != target:
            ans = [i, val[target-nums[i]][0]]
        elif 2*nums[i] == target and len(val[nums[i]]) > 1:
            ans = [val[target-nums[i]][0], val[target-nums[i]][1]]
    return ans


# 代码随想录标解
def twoSum(nums, target):
    records = dict()

    for index, value in enumerate(nums):
        if target - value in records:   # 遍历当前元素，并在map中寻找是否有匹配的key
            return [records[target - value], index]
        records[value] = index    # 遍历当前元素，并在map中寻找是否有匹配的key
    return []


# 二刷
class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            if hash.get(target-nums[i], -1) >= 0:
                return [i, hash[target-nums[i]]]
            hash[nums[i]] = i


s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))