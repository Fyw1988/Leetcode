import random


# 归并排序
class Solution:
    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def sortArray(self, nums):
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


# 归并排序：比较习惯的写法
class Solution(object):
    def sortArray(self, nums):
        def sort(nums, i, j):
            if j == i + 1:
                return nums[i:j]
            mid = (i + j) // 2
            return merge(sort(nums, i, mid), sort(nums, mid, j))

        def merge(nums1, nums2):
            ans = []
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    ans.append(nums1[i])
                    i += 1
                else:
                    ans.append(nums2[j])
                    j += 1
            return ans + nums1[i:] + nums2[j:]

        return sort(nums, 0, len(nums))


# 快速排序
class Solution3(object):
    def sortArray(self, nums):
        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left

        def randompartition(nums, left, right):
            pos = random.randint(left, right)
            nums[pos], nums[left] = nums[left], nums[pos]
            return partition(nums, left, right)

        def fastsort(nums, left, right):
            if left >= right:
                return
            pos = randompartition(nums, left, right)
            fastsort(nums, left, pos-1)
            fastsort(nums, pos+1, right)

        fastsort(nums, 0, len(nums)-1)
        return nums


# 堆排序
class Solution4(object):
    def sortArray(self, nums):
        def maxHeap(nums, i, end):  # 设置某一个节点
            sub = 2 * i + 1
            while sub <= end:
                if sub < end and nums[sub+1] > nums[sub]:
                    sub += 1
                if nums[sub] > nums[i]:
                    nums[i], nums[sub] = nums[sub], nums[i]
                    i = sub
                    sub = 2 * i + 1
                else:
                    break

        n = len(nums)
        for i in range(n//2-1, -1, -1):
            maxHeap(nums, i, n-1)
        for i in range(n-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            maxHeap(nums, 0, i-1)

        return nums

s = Solution4()
print(s.sortArray(nums = [5,1,1,2,0,0]))