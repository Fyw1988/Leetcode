class Solution(object):
    def __init__(self):
        self.results = [[]]
        self.path = []

    def subsetsWithDup(self, nums):
        nums.sort()
        self.backtracking(nums, 0)
        return self.results

    def backtracking(self, nums, index):
        if index == len(nums):
            return

        for i in range(index, len(nums)):
            # 去重操作
            if i > index and nums[i] == nums[i-1]:
                continue

            self.path.append(nums[i])
            self.results.append(self.path[:])
            self.backtracking(nums, i+1)
            self.path.pop()
