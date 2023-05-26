class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 双指针去重
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        nums = nums[:slow+1]

        if len(nums) == 1: return 1

        cur1 = 0
        cur2 = 1
        cur3 = 2
        l = 2
        result = [nums[cur1], nums[cur2]]
        while cur3 < len(nums):
            if nums[cur3] - nums[cur2] > 0 > nums[cur2] - nums[cur1] or nums[cur3] - nums[cur2] < 0 < nums[cur2] - nums[cur1]:
                l += 1
                cur1 = cur2
                cur2 = cur3
                result.append(nums[cur3])
            cur3 += 1

        return result


class Solution2(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        preC,curC,res = 0,0,1  #题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC !=0:  #差值为0时，不算摆动
                res += 1
                preC = curC  #如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
                result.append(nums[i])
        return result, res, len(result)


a = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
s1 = Solution()
s2 = Solution2()
print(s1.wiggleMaxLength(a))
print(s2.wiggleMaxLength(a))