# 这种二维数组的写法执行起来非常慢
class Solution:
    def canPartition(self, nums) -> bool:
        cap = sum(nums)
        if cap % 2 != 0: return False
        cap = cap // 2 + 1
        dp = [[0 for _ in range(cap)] for _ in range(len(nums))]
        # dp = [[0] * cap] * len(nums) 这种定义会出错，因为二维数组中每一行是浅复制，某一个值改了每行中的这个值都会变
        # 初始化dp数组
        for j in range(cap):
            dp[0][j] = 0 if nums[0] > j else nums[0]
        for i in range(1, len(nums)):
            for j in range(1, cap):
                if nums[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
        print(dp)
        return dp[-1][-1] == cap-1

# s = Solution()
# print(s.canPartition([1,2,5]))


# 滚动算法
class Solution:
    def canPartition(self, nums) -> bool:
        target = sum(nums)
        if target % 2 == 1: return False
        target //= 2
        dp = [0] * (target + 1)
        for i in range(len(nums)):
            # 倒序遍历，先更新后面的，因为后面的值需要依据前面的值更新
            # 对于容量小于nums[i]的，不需要更新
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return target == dp[target]