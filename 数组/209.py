def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    i = j = 0
    sum = 0
    result = 10e5
    while j < len(nums):
        sum += nums[j]
        while sum >= target:
            result = min(result, j-i+1)
            sum = sum - nums[i]
            i += 1
        j += 1
    return result if result < 10e5 else 0


# 二刷
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, right = 0, 0
        sum = 0
        l = 10e5
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                l = min(l, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1

        return 0 if l > len(nums) else l


s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))