# 这种解法空间使用率很低，只用了一个长度为out的数组，但是没用用到哈希表的思想
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ins = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            if nums1[i] not in ins:
                ins.append(nums1[i])
    return ins


# 使用了哈希表思想的解法
class Solution:
    def intersection(self, nums1, nums2):
        val_dict = {}
        ans = []
        for num in nums1:
            val_dict[num] = 1

        for num in nums2:
            if num in val_dict.keys() and val_dict[num] == 1:
                ans.append(num)
                val_dict[num] = 0

        return ans
