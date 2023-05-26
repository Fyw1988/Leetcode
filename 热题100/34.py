class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return self.findEdge(nums, mid)
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return [-1, -1]

    def findEdge(self, nums, cur):
        left, right = cur, cur
        while left > 0 and nums[left] == nums[left-1]:
            left -= 1
        while right < len(nums)-1 and nums[right] == nums[right+1]:
            right += 1
        return [left, right]


s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))