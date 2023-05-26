class Solution(object):
    def __init__(self):
        self.path = []
        self.results = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        self.backtracking(nums, length)
        return self.results

    def backtracking(self, nums, length):
        if len(self.path) == length:
            self.results.append(self.path[:])
            return

        used = set()
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            else:
                used.add(nums[i])

            self.path.append(nums[i])
            self.backtracking(nums[:i]+nums[i+1:], length)
            self.path.pop()