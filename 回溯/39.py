class Solution(object):
    def __init__(self):
        self.path = []
        self.results = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        index = 0
        candidates.sort()
        self.backtracking(candidates, target, index)
        return self.results

    def backtracking(self, candidates, target, index):
        # 终止条件
        if sum(self.path) == target:
            self.results.append(self.path[:])
            return
        # 剪枝
        if sum(self.path) > target:
            return

        for i in range(index, len(candidates)):
            self.path.append(candidates[i])
            self.backtracking(candidates, target, i)
            self.path.pop()


# 这个写法只要20ms，是上面的1/5
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum(self, candidates, target):
        '''
        因为本题没有组合数量限制，所以只要元素总和大于target就算结束
        '''
        # 为了剪枝需要提前进行排序
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target, sum_, start_index):
        # Base Case
        if sum_ == target:
            self.paths.append(self.path[:]) # 因为是shallow copy，所以不能直接传入self.path
            return
        # 单层递归逻辑
        # 如果本层 sum + condidates[i] > target，就提前结束遍历，剪枝
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target:
                return
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)  # 因为无限制重复选取，所以不是i-1
            sum_ -= candidates[i]   # 回溯
            self.path.pop()        # 回溯