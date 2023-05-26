# 维护一个递增的单调栈
class Solution(object):
    def trap(self, height):
        ans = 0
        stack = list()
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans


# 单调栈写法二
class Solution2(object):
    def trap(self, height):
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur = height[stack.pop()]
                if not stack:
                    break
                ans += (min(height[i], height[stack[-1]]) - cur) * (i - stack[-1] - 1)
            stack.append(i)
        return ans


# 暴力解法，找每个点左边的最高与右边的最高，并与当前高度对比
class Solution3(object):
    def trap(self, height):
        n = len(height)
        water = 0
        left = [0] * n
        right = [0] * n
        for i in range(1, n - 1):
            left[i] = max(left[i - 1], height[i - 1])
        for i in range(n - 2, 0, -1):
            right[i] = max(right[i + 1], height[i + 1])

        for i in range(1, n - 1):
            if min(left[i], right[i]) > height[i]:
                water += min(left[i], right[i]) - height[i]

        return water


# 动态规划
class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans


# s = Solution2()
# print(s.trap([4,2,0,3,2,5]))