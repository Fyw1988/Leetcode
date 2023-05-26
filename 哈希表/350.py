# 判断数组一语数组二的交集，也就是判断数组一中的元素是否在数组二中，一眼哈希法
# 这题由于既要判断数的种类，又要判断出现次数，所以没有像lc349那样的简单逃课解法，使用数组的话只能老老实实定义长度为1001的数组，较为占用空间
# 由此可看出，349只是恰好有一种简单解法而已，一般的哈希问题还是要按照标准解法来进行
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    val1 = dict()
    ans = []
    for i in range(len(nums1)):
        val1[nums1[i]] = val1.get(nums1[i], 0) + 1  # nums1中数值的种类与出现的次数
    for i in range(len(nums2)):
        if nums2[i] in val1.keys() and val1[nums2[i]] > 0:
            ans.append(nums2[i])
            val1[nums2[i]] -= 1
    return ans
