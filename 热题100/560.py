# 回溯
# 回溯行不通，这个求的是数组，题目要求的是子数组
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def subarraySum(self, nums, k):
#         self.backtracking(nums, k, 0, 0)
#         return self.results
#
#     def backtracking(self, nums, k, startIndex, _sum):
#         if _sum == k:
#             self.results.append(self.path[:])
#             return
#
#         for i in range(startIndex, len(nums)):
#             if _sum + nums[i] > k:
#                 continue
#             _sum += nums[i]
#             self.path.append(nums[i])
#             self.backtracking(nums, k, i+1, _sum)
#             self.path.pop()
#             _sum -= nums[i]


# 暴力枚举，O(n^2)，会超时
class Solution(object):
    def subarraySum(self, nums, k):
        ans = 0
        for cur1 in range(len(nums)):
            sum_ = 0
            for cur2 in range(cur1, len(nums)):
                sum_ += nums[cur2]
                if sum_ == k:
                    ans += 1
        return ans


# 前缀表，O(n)
class Solution2(object):
    def subarraySum(self, nums, k):
        dic = {0: 1}
        sums, res = 0, 0
        for num in nums:
            sums += num
            res += dic.get(sums - k, 0)
            dic[sums] = dic.get(sums, 0) + 1
        return res