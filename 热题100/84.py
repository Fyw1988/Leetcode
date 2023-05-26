class Solution(object):
    def largestRectangleArea(self, heights):
        s = []
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            while s and heights[i] < heights[s[-1]]:
                cur = s.pop()
                if not s:
                    maxArea = max(maxArea, i*heights[cur])
                    break
                maxArea = max(maxArea, (i-s[-1]-1)*heights[cur])
            if i < len(heights)-1:
                s.append(i)
        return maxArea


s = Solution()
print(s.largestRectangleArea([2,4]))