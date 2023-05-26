class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid] < nums[0]:
                    right = mid
                else:
                    if target >= nums[0]:
                        right = mid
                    else:
                        left = mid + 1
            else:
                if nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    if target >= nums[0]:
                        right = mid
                    else:
                        left = mid + 1
        return -1


s = Solution()
print(s.search(nums = [4,5,6,7,0,1,2], target = 0))