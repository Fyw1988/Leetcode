def threeSum1(nums):
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
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = size - 1
        while j < k:
            if nums[i] + nums[j] > -nums[k]:
                k -= 1
            elif nums[i] + nums[j] < -nums[k]:
                j += 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
                while nums[k] == nums[k+1] and k > j:
                    k -= 1
    return ans


# 代码随想录
def threeSum2(nums):
    ans = []
    n = len(nums)
    nums.sort()
    # 找出a + b + c = 0
    # a = nums[i], b = nums[left], c = nums[right]
    for i in range(n):
        left = i + 1
        right = n - 1
    # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
        if nums[i] > 0:
            break
        if i >= 1 and nums[i] == nums[i - 1]:  # 去重a
            continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                ans.append([nums[i], nums[left], nums[right]])
        # 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
                while left != right and nums[left] == nums[left + 1]:
                    left += 1
                while left != right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return ans


# 哈希表法
def threeSum3(nums):
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
            val = - nums[i] - nums[j]
            if val in hashmap:
                # make sure no duplicates.
                count = (nums[i] == val) + (nums[j] == val)
                if hashmap[val] > count:
                    ans_tmp = tuple(sorted([nums[i], nums[j], val]))
                    ans.add(ans_tmp)
                else:
                    continue
    return list(ans)


# 二刷
# 双指针，难点在于去重。遍历时对于每个指针都要考虑去重操作
class Solution(object):
    def threeSum(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ans


s = Solution()
print(s.threeSum([0,0,0]))