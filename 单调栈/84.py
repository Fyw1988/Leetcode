# 单调栈
class Solution:
    def largestRectangleArea(self, heights) -> int:
        maxRec = 0
        heights.append(0)
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                cur = stack.pop()
                if not stack:
                    maxRec = max(maxRec, heights[cur] * i)
                    break
                maxRec = max(maxRec, (i-stack[-1]-1)*heights[cur])
            if i < len(heights)-1:
                stack.append(i)
        return maxRec


# 双指针
class Solution:
    def largestRectangleArea(self, heights) -> int:
        size = len(heights)
        # 两个DP数列储存的均是下标index
        min_left_index = [0] * size
        min_right_index = [0] * size
        result = 0

        # 记录每个柱子的左侧第一个矮一级的柱子的下标
        min_left_index[0] = -1  # 初始化防止while死循环
        for i in range(1, size):
            # 以当前柱子为主心骨，向左迭代寻找次级柱子
            temp = i - 1
            while temp >= 0 and heights[temp] >= heights[i]:
                # 当左侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
                temp = min_left_index[temp]
            # 当找到左侧矮一级的目标柱子时
            min_left_index[i] = temp

        # 记录每个柱子的右侧第一个矮一级的柱子的下标
        min_right_index[size - 1] = size  # 初始化防止while死循环
        for i in range(size - 2, -1, -1):
            # 以当前柱子为主心骨，向右迭代寻找次级柱子
            temp = i + 1
            while temp < size and heights[temp] >= heights[i]:
                # 当右侧的柱子持续较高时，尝试这个高柱子自己的次级柱子（DP
                temp = min_right_index[temp]
            # 当找到右侧矮一级的目标柱子时
            min_right_index[i] = temp

        for i in range(size):
            area = heights[i] * (min_right_index[i] - min_left_index[i] - 1)
            result = max(area, result)

        return result

# s = Solution()
# print(s.largestRectangleArea([2,4]))