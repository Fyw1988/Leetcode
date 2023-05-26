# 暴力双指针
class Solution:
    def maxArea(self, height) -> int:
        ans = 0
        for i in range(len(height)-1):
            j = i+1
            while j < len(height):
                ans = max(ans, (j-i)*min(height[i], height[j]))
                j += 1
        return ans


# 双指针
class Solution2:
    def maxArea(self, height) -> int:
        ans = 0
        cur1, cur2 = 0, len(height)-1
        while cur2 > cur1:
            ans = max(ans, (cur2-cur1)*min(height[cur1], height[cur2]))
            if height[cur1] < height[cur2]:
                cur1 += 1
            else:
                cur2 -= 1
        return ans


