class Solution(object):
    def canJump(self, nums):
        jump = True
        i = 0
        while i < len(nums)-1 and jump:
            if nums[i] == 0:
                jump = False
                cur = i
                while cur >= 0:
                    if nums[cur] > i - cur:
                        jump = True
                        break
                    cur -= 1
            i += 1
        return jump


# 贪心--扩展领土
class Solution:
    def canJump(self, nums):
        cover = 0
        if len(nums) == 1: return True
        i = 0
        # python不支持动态修改for循环中变量,使用while循环代替
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False