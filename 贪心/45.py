# 贪心 在每个范围内都踩能够跳的最远的格子
class Solution(object):
    def jump(self, nums):
        step = 0
        cur = 0
        while cur < len(nums) - 1:
            if cur + nums[cur] >= len(nums) - 1: return step + 1
            far = [i + j for i, j in zip(nums[cur + 1:cur + nums[cur] + 1], [i for i in range(1, nums[cur]+1)])]
            choice = far.index(max(far))
            cur += choice + 1
            step += 1
        return step


# 贪心算法--扩充疆域
class Solution:
    def jump(self, nums):
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance:
                if curDistance != len(nums) - 1:
                    ans += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1: break
        return ans


# DP
