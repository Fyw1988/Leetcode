def fourSumCount(nums1, nums2, nums3, nums4):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type nums3: List[int]
    :type nums4: List[int]
    :rtype: int
    """
    ab = dict()
    size = len(nums1)
    ans = 0
    for i in range(size):
        for j in range(size):
            ab[nums1[i] + nums2[j]] = ab.get(nums1[i] + nums2[j], 0) + 1
    for i in range(size):
        for j in range(size):
            if -nums3[i] - nums4[j] in ab:
                ans += ab[-nums3[i] - nums4[j]]
    return ans


def fourSumCount(nums1, nums2, nums3, nums4):
    # use a dict to store the elements in nums1 and nums2 and their sum
    hashmap = dict()
    for n1 in nums1:
        for n2 in nums2:
            if n1 + n2 in hashmap:
                hashmap[n1 + n2] += 1
            else:
                hashmap[n1 + n2] = 1

    # if the -(a+b) exists in nums3 and nums4, we shall add the count
    count = 0
    for n3 in nums3:
        for n4 in nums4:
            key = - n3 - n4
            if key in hashmap:
                count += hashmap[key]
    return count