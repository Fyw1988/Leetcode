# 376
# 贪心
# 其实这题我再见也想到了梯度，但是想着求每个点左右的梯度，这样就会遇到许多问题
# preC记录摆动子序列中的最后一个元素的右梯度，curC记录当前点右边的梯度
# 精髓在于只根据当前点的右梯度与子序列中最后一个点的右梯度来判断是否加入摆动序列
# res=1，可以理解为按照逻辑，不管怎样nums[-1]都应该加入摆动序列
# class Solution:
#     def wiggleMaxLength(self, nums):
#         preC, curC, res = 0, 0, 1  #题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
#         for i in range(len(nums) - 1):
#             curC = nums[i + 1] - nums[i]
#             if curC * preC <= 0 and curC != 0:  #差值为0时，不算摆动
#                 res += 1
#                 preC = curC  #如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
#         return res


# 53
# class Solution:
#     def maxSubArray(self, nums):
#         maxSum = -10**4-1
#         curSum = 0
#         for i in range(len(nums)):
#             curSum += nums[i]
#             maxSum = max(curSum, maxSum)
#             if curSum < 0:
#                 curSum = 0
#         return maxSum


# 122
# class Solution:
#     def maxProfit(self, prices):
#         ans = 0
#         for i in range(1, len(prices)):
#             if prices[i] - prices[i-1] > 0:
#                 ans += prices[i] - prices[i-1]
#         return ans


# 1005
# class Solution(object):
#     def largestSumAfterKNegations(self, nums, k):
#         nums.sort(key=abs, reverse=True)
#         for i in range(len(nums)):
#             if k > 0 and nums[i] < 0:
#                 nums[i] *= -1
#                 k -= 1
#         nums[-1] *= (-1) ** k
#         return sum(nums)


# 134
# class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         start = 0
#         curSum = 0
#         totalSum = 0
#         for i in range(len(gas)):
#             curSum += gas[i] - cost[i]
#             totalSum += gas[i] - cost[i]
#             if curSum < 0:
#                 curSum = 0
#                 start = i + 1
#         if totalSum < 0: return -1
#         return start


# 135
# class Solution(object):
#     def candy(self, ratings):
#         candys = [1] * len(ratings)
#         for i in range(len(ratings)-1):
#             if ratings[i+1] > ratings[i]:
#                 candys[i+1] = candys[i] + 1
#         for i in range(len(ratings)-1, 0, -1):
#             if ratings[i-1] > ratings[i]:
#                 candys[i-1] = max(candys[i] + 1, candys[i-1])
#         return sum(candys)


# 860
# class Solution(object):
#     def lemonadeChange(self, bills):
#         changes = [0] * 2
#         for i in range(len(bills)):
#             if bills[i] == 5:
#                 changes[0] += 1
#             elif bills[i] == 10 and changes[0] > 0:
#                 changes[1] += 1
#                 changes[0] -= 1
#             elif bills[i] == 20:
#                 if changes[1] > 0 and changes[0] > 0:
#                     changes[1] -= 1
#                     changes[0] -= 1
#                 elif changes[0] > 2:
#                     changes[0] -= 3
#                 else:
#                     return False
#             else:
#                 return False
#         return True


# 406
# 先根据身高从高到低排序，再去考虑相对关系
# 先安排高的，再安排矮的，因为矮的插到高的前面不会对第二个顺序产生影响
# class Solution(object):
#     def reconstructQueue(self, people):
#         people.sort(key=lambda x: [-x[0], x[1]])
#         ans = []
#         for p in people:
#             ans.insert(p[1], p)
#         return ans


# 452
# class Solution(object):
#     def findMinArrowShots(self, points):
#         points.sort(key=lambda x: x[0])
#         ans = 1
#         left, right = points[0][0], points[0][1]
#         for i in range(1, len(points)):
#             if points[i][0] > right:
#                 ans += 1
#                 left = points[i][0]
#                 right = points[i][1]
#             else:
#                 left = max(left, points[i][0])
#                 right = min(right, points[i][1])
#         return ans


# 435
# 其实右边界排序更好理解，当发生区间重合，优先删除右边界更靠右的区间，这样后面的区间发生重合的概率更小
# 但这里左边界排序也是一样的原理，依然优先删除右边界更大的区间，代码依然可以AC
# class Solution(object):
#     def eraseOverlapIntervals(self, intervals):
#         intervals.sort(key=lambda x: x[0])
#         # print(intervals)
#         ans = 0
#         right = -10e5
#         for interval in intervals:
#             if interval[0] >= right:
#                 right = interval[1]
#             else:
#                 right = min(right, interval[1])
#                 ans += 1
#         return ans


# 56
# class Solution(object):
#     def merge(self, intervals):
#         intervals.sort(key=lambda x: x[0])
#         area = [intervals[0][0], intervals[0][1]]
#         ans = []
#         for i in range(1, len(intervals)):
#             if intervals[i][0] > area[1]:
#                 ans.append(area)
#                 area = intervals[i]
#             else:
#                 area = [min(area[0], intervals[i][0]), max(area[1], intervals[i][1])]
#         ans.append(area)
#         return ans


# 738
# class Solution(object):
#     def monotoneIncreasingDigits(self, n):
#         nums = []
#         while n != 0:
#             nums.append(n % 10)
#             n = n // 10
#         ans = 0
#         for i in range(len(nums)-1):
#             if nums[i] < nums[i+1]:
#                 for j in range(i+1):
#                     nums[j] = 9
#                 nums[i+1] -= 1
#         for i in range(len(nums)-1, -1, -1):
#             ans = ans * 10 + nums[i]
#         return ans


# 968
# 0：未被照亮 1：安装相机 2：被照亮
# 当左右子树都为2的时候，此时根节点可能不安装相机，被父节点照亮，也可能安装相机，自己照亮自己
# 当这种情况发生时，优先选择不安装，体现了贪心的思路
# 另外贪心的思路也体现在：不在叶子节点上安装摄像头
# class Solution:
#     def minCameraCover(self, root):
#         self.cameras = 0
#         self.helper(root)
#         if root.val == 0:
#             self.cameras += 1
#         return self.cameras
#
#     def helper(self, root):
#         if not root.left and not root.right:
#             return
#         if root.left:
#             self.helper(root.left)
#             if root.left.val == 0:
#                 root.val = 1
#             elif root.left.val == 1:
#                 root.val = 2
#         if root.right:
#             self.helper(root.right)
#             if root.right.val == 0:
#                 root.val = 1
#             elif root.right.val == 1 and root.val != 1:
#                 root.val = 2
#         if root.val == 1:
#             self.cameras += 1