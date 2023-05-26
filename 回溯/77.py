# 剪枝的版本(40ms)
class Solution(object):
    def combine(self, n, k):
        result = []
        path = []
        def backtracking(n, k, startidx):
            if len(path) == k:
                result.append(path[:])
                return

            # 剪枝， 最后k - len(path)个节点直接构造结果，无需递归
            last_startidx = n - (k - len(path)) + 1

            for x in range(startidx, last_startidx + 1):
                path.append(x)
                backtracking(n, k, x + 1)  # 递归
                path.pop()  # 回溯

        backtracking(n, k, 1)
        return result


# 无剪枝的版本(400ms)
class Solution:
    def combine(self, n, k):
        # 全局变量
        res = []
        path = []
        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n + 1):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return res
