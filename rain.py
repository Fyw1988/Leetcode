# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:34:46 2022

@author: fyw
"""

height = [0,1,0,2,0,0,1,3,2,1,2,1]


def trap(height):
    ans = 0
    left, right = 0, len(height) - 1
    leftMax = rightMax = 0

    while left < right:
        leftMax = max(leftMax, height[left])
        rightMax = max(rightMax, height[right])
        if height[left] < height[right]:
            ans += leftMax - height[left]
            left += 1
        else:
            ans += rightMax - height[right]
            right -= 1

    return ans


ans = trap(height)
print(ans)
