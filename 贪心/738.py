class Solution:
    def monotoneIncreasingDigits(self, n):
        # 拆分
        div = n // 10
        remain = n % 10
        res = [remain]
        while div != 0:
            remain = div % 10
            res.append(remain)
            div = div // 10

        # 单调递增
        for i in range(len(res)-1):
            if res[i] < res[i+1]:
                res[i+1] -= 1
                res[0:i+1] = [9] * (i + 1)

        # 合并成数字
        ans = 0
        for i in range(len(res)):
            ans += res[i] * (10**i)

        return ans


# 更简洁的写法
class Solution2:
    def monotoneIncreasingDigits(self, n):
        a = list(str(n))
        for i in range(len(a)-1,0,-1):
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i)  #python不需要设置flag值，直接按长度给9就好了
        return int("".join(a))

s = Solution()
print(s.monotoneIncreasingDigits(989998))