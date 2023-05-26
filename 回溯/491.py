class Solution(object):
    def __init__(self):
        self.results = []
        self.path = []

    def findSubsequences(self, nums):
        self.backtracking(nums, 0)
        return self.results

    def backtracking(self, nums, index):
        if index == len(nums):
            return

        used = set()
        for i in range(index, len(nums)):
            # 去重
            if nums[i] in used:
                continue
            else:
                used.add(nums[i])

            if self.path and nums[i] < self.path[-1]:
                continue
            else:
                self.path.append(nums[i])
                if len(self.path) > 1:
                    self.results.append(self.path[:])
                self.backtracking(nums, i+1)
                self.path.pop()


class Solution2:
    def __init__(self):
        self.paths = []
        self.path = []

    def findSubsequences(self, nums):
        '''
        本题求自增子序列，所以不能改变原数组顺序
        '''
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, start_index):
        # 收集结果，同78.子集，仍要置于终止条件之前
        if len(self.path) >= 2:
            # 本题要求所有的节点
            self.paths.append(self.path[:])

        # Base Case（可忽略）
        if start_index == len(nums):
            return

        # 单层递归逻辑
        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = set()
        # 同层横向遍历
        for i in range(start_index, len(nums)):
            # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
            if (self.path and nums[i] < self.path[-1]) or nums[i] in usage_list:
                continue
            usage_list.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

s2 = Solution2()
s = Solution()
r1 = s2.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
r2 = s.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
print(r1 == r2)
print(len(r1))
print(len(r2))
for i in r1:
    if i not in r2:
        print(i)