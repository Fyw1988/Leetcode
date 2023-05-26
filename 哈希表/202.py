# 第一时间想到的暴力解法，但是会陷入无限循环，所以需要一个哈希表来记录这个值，如果这个值第二次出现说明陷入了无限循环，返回False
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    val = dict()
    val[n] = 1
    while n != 1:
        nums = []
        while n > 10:
            nums.append(n % 10)
            n = n // 10
        if n == 10:
            nums.append(1)
        else:
            nums.append(n)
        n = 0
        for i in range(len(nums)):
            n += nums[i] ** 2
        if n in val.keys():
            return False
        val[n] = 1

    return True


# 标解
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(num):
            sum_ = 0

            # 从个位开始依次取，平方求和
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_

        # 记录中间结果
        record = set()

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True

            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)


# 二刷，字典哈希
class Solution(object):
    def isHappy(self, n):
        hash = {}
        while n != 1:
            sum = 0
            while n != 0:
                sum += (n % 10) ** 2
                n = n // 10
            n = sum
            if hash.get(n, 0):
                return False
            else:
                hash[n] = 1
        return True