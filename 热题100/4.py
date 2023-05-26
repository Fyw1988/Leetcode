class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if (n1+n2) % 2 == 0:
            return (self.getKthElement((n1+n2)//2, nums1, nums2) + self.getKthElement((n1+n2)//2+1, nums1, nums2)) / 2
        else:
            return self.getKthElement((n1+n2)//2+1, nums1, nums2)

    def getKthElement(self, k, nums1, nums2):
        index1, index2 = 0, 0
        while k > 0:
            if index1 == len(nums1):
                return nums2[index2 + k - 1]
            if index2 == len(nums2):
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            pos = k // 2 - 1
            newIndex1, newIndex2 = min(index1+pos, len(nums1)-1), min(index2+pos, len(nums2)-1)
            if nums1[newIndex1] <= nums2[newIndex2]:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1