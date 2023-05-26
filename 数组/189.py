# 超时
class Solution:
    def rotate(self, nums, k) -> None:
        for _ in range(k):
            slow, fast = 0, 1
            while fast < len(nums):
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1


#
class Solution2:
    def rotate(self, nums, k) -> None:
        if k >= len(nums): k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        return nums

    def reverse(self, nums, i, j):
        while j >= i:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


s = Solution2()
print(s.rotate([1,2,3,4,5,6,7], 3))