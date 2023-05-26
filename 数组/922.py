class Solution(object):
    def sortArrayByParityII(self, nums):
        even, odd = 0, 1
        while even < len(nums):
            if nums[even] % 2:
                while odd < len(nums) and nums[odd] % 2 != 0:
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
        return nums


s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))