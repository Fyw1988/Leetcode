class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                res[nums1.index(nums2[stack[-1]])] = nums2[i]
                stack.pop()
            if nums2[i] in nums1:
                stack.append(i)
        return res


s = Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))