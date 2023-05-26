class Solution:
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        stack = []
        new_nums = nums + nums
        for i in range(len(new_nums)):
            while stack and new_nums[i] > nums[stack[-1]]:
                res[stack[-1]] = new_nums[i]
                stack.pop()
            if i < len(nums):
                stack.append(i)
        return res


class Solution:
    def nextGreaterElements(self, nums):
        dp = [-1] * len(nums)
        stack = []
        for i in range(len(nums)*2):
            while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):
                    dp[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
            stack.append(i%len(nums))
        return dp


s = Solution()
print(s.nextGreaterElements([1,2,3,4,3]))