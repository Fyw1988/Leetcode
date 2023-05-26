class Solution(object):
    def jump(self, nums):
        cur, ans = 0, 0
        while cur < len(nums)-1:
            maxRange, nextStep = 0, 0
            if cur + nums[cur] >= len(nums)-1:
                return ans + 1
            for step in range(1, nums[cur]+1):
                if step + nums[cur+step] > maxRange:
                    nextStep = step
                    maxRange = step + nums[cur+step]
            cur += nextStep
            ans += 1
        return 0


s = Solution()
print(s.jump([2,3,1,1,4]))