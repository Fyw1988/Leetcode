def FourSum(nums, target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    if not nums:
        return False
    size = len(nums)
    ans = []
    for i in range(size):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        while j < size:
            k = j + 1
            z = size - 1
            while k < z:
                if nums[i] + nums[j] + nums[k] + nums[z] > target:
                    z -= 1
                elif nums[i] + nums[j] + nums[k] + nums[z] < target:
                    k += 1
                else:
                    ans.append([nums[i], nums[j], nums[k], nums[z]])
                    k += 1
                    z -= 1
                    while nums[k] == nums[k-1] and k < z:
                        k += 1
                    while nums[z] == nums[z+1] and k < z:
                        z -= 1
            j += 1
            while nums[j] == nums[j - 1] and j < size:
                j += 1
    return ans


# 哈希表法
def fourSum(nums, target):
    # use a dict to store value:showtimes
    hashmap = dict()
    for n in nums:
        if n in hashmap:
            hashmap[n] += 1
        else:
            hashmap[n] = 1

    ans = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                val = target - (nums[i] + nums[j] + nums[k])
                if val in hashmap:
                    # make sure no duplicates.
                    count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                    if hashmap[val] > count:
                        ans_tmp = tuple(sorted([nums[i], nums[j], nums[k], val]))
                        ans.add(ans_tmp)
                    else:
                        continue
    return list(ans)

print(fourSum([1, 1, 1, 1, 1, 1], 4))