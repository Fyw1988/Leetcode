class Solution(object):
    def canJump(self, nums):
        i = 0
        if len(nums) == 1: return True
        while i < len(nums):
            max_step = 0
            next_step = 0
            for step in range(1, nums[i]+1):
                if i + step >= len(nums)-1:
                    return True
                if step + nums[i+step] > max_step:
                    next_step = step
                    max_step = step + nums[i+step]
            if not next_step:
                return False
            i += next_step


# 上面的写法理论上是O(n^2)的复杂度
class Solution(object):
    def canJump(self, nums):
        cur, cover = 0, nums[0]
        while cur <= cover:
            cover = max(nums[cur]+cur, cover)
            if cover >= len(nums)-1:
                return True
            cur += 1
        return False