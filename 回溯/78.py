class Solution(object):
    def __init__(self):
        self.results = [[]]
        self.path = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.backtracking(nums, 0)
        return self.results

    def backtracking(self, nums, index):
        if index == len(nums):
            return

        for i in range(index, len(nums)):
            self.path.append(nums[i])
            self.results.append(self.path[:])
            self.backtracking(nums, i+1)
            self.path.pop()