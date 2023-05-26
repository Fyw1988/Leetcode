import random
import heapq


# 构建一个heapq的时间复杂度是O(nlogn)，显然是不符合题目要求的
class Solution(object):
    def findKthLargest(self, nums, k):
        deque = []
        for i in range(len(nums)):
            heapq.heappush(deque, nums[i])
        for _ in range(len(nums)-k+1):
            ans = heapq.heappop(deque)
        return ans


# 快排
class Solution2:
    def findKthLargest(self, nums, k):

        def partition(arr, low, high):
            pivot = arr[low]  # 选取最左边为pivot

            left, right = low, high  # 双指针
            while left < right:

                while left < right and arr[right] >= pivot:  # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]  # 并将其移动到left处

                while left < right and arr[left] <= pivot:  # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]  # 并将其移动到right处

            arr[left] = pivot  # pivot放置到中间left=right处
            return left

        def randomPartition(arr, low, high):
            pivot_idx = random.randint(low, high)  # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]  # pivot放置到最左边
            return partition(arr, low, high)  # 调用partition函数

        def topKSplit(arr, low, high, k):
            # mid = partition(arr, low, high)                   # 以mid为分割点【非随机选择pivot】
            mid = randomPartition(arr, low, high)  # 以mid为分割点【随机选择pivot】
            if mid == k - 1:  # 第k小元素的下标为k-1
                return arr[mid]  # 【找到即返回】
            elif mid < k - 1:
                return topKSplit(arr, mid + 1, high, k)  # 递归对mid右侧元素进行排序
            else:
                return topKSplit(arr, low, mid - 1, k)  # 递归对mid左侧元素进行排序

        n = len(nums)
        return topKSplit(nums, 0, n - 1, n - k + 1)  # 第k大元素即为第n-k+1小元素


# 堆排序
class Solution3:
    def findKthLargest(self, nums, k):
        def maxHepify(arr, i, end):  # 大顶堆
            j = 2 * i + 1  # j为i的左子节点【建堆时下标0表示堆顶】
            while j <= end:  # 自上而下进行调整
                if j + 1 <= end and arr[j + 1] > arr[j]:  # i的左右子节点分别为j和j+1
                    j += 1  # 取两者之间的较大者

                if arr[i] < arr[j]:  # 若i指示的元素小于其子节点中的较大者
                    arr[i], arr[j] = arr[j], arr[i]  # 交换i和j的元素，并继续往下判断
                    i = j  # 往下走：i调整为其子节点j
                    j = 2 * i + 1  # j调整为i的左子节点
                else:  # 否则，结束调整
                    break

        n = len(nums)

        # 建堆【大顶堆】
        for i in range(n // 2 - 1, -1, -1):  # 从第一个非叶子节点n//2-1开始依次往上进行建堆的调整
            maxHepify(nums, i, n - 1)

        # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
        # k-1次重建堆（堆顶元素），或 k次交换到尾部（倒数第k个元素）
        for j in range(n - 1, n - k - 1, -1):
            nums[0], nums[j] = nums[j], nums[0]  # 堆顶元素（当前最大值）放置到尾部j
            maxHepify(nums, 0, j - 1)  # j-1变成尾部，并从堆顶0开始调整堆

        return nums[-k]


# 快排
class Solution:
    def findKthLargest(self, nums, k):

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
            nums[left], nums[pos] = nums[pos], nums[left]
            return partition(nums, left, right)

        def fastsort(nums, left, right, k):
            pos = randompartition(nums, left, right)
            if pos == k - 1:
                return nums[pos]
            elif pos > k - 1:
                return fastsort(nums, left, pos-1, k)
            else:
                return fastsort(nums, pos+1, right, k)

        return fastsort(nums, 0, len(nums)-1, len(nums)-k+1)


# 堆排
class Solution:
    def findKthLargest(self, nums, k):
        # 使某一个非叶子节点以及其子树有序
        def maxHeap(nums, i, end):
            left = 2 * i + 1
            while left <= end:
                if left + 1 <= end and nums[left+1] > nums[left]:
                    left += 1
                if nums[left] > nums[i]:
                    nums[i], nums[left] = nums[left], nums[i]
                    i = left
                    left = 2 * i + 1
                else:
                    break
        # 建立最大堆
        n = len(nums)
        for i in range(n//2-1, -1, -1):
            maxHeap(nums, i, n-1)

        for j in range(n-1, n-k-1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            maxHeap(nums, 0, j-1)
        return nums[-k]