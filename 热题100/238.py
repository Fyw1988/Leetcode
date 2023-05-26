class Solution:
    def productExceptSelf(self, nums):
        hash = [1] * len(nums)
        ans = [1] * len(nums)
        sum_ = 1
        # 前缀表
        for i in range(1, len(nums)):
            sum_ *= nums[i-1]
            hash[i] = sum_
        sum_ = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = sum_ * hash[i]
            sum_ *= nums[i]
        return ans


