# 思路正确，但是超时
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = 0
        for i in range(len(ratings)):
            curLeft = i
            curRight = i
            while curLeft > 0:
                if ratings[curLeft] > ratings[curLeft - 1]:
                    left += 1
                    curLeft -= 1
                else:
                    break
            while curRight < len(ratings) - 1:
                if ratings[curRight] > ratings[curRight + 1]:
                    right += 1
                    curRight += 1
                else:
                    break
            res += 1 + max(left, right)
            left = 0
            right = 0
        return res


# 不超时，但是代码屎山
class Solution2(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        cur = 0
        while cur < len(ratings) - 1:
            if ratings[cur] > ratings[cur + 1]:
                right += 1
                cur += 1
            else:
                break
        res = max(left, right) + 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left += 1
                right = 0
                cur = i
                while cur < len(ratings) - 1:
                    if ratings[cur] > ratings[cur + 1]:
                        right += 1
                        cur += 1
                    else:
                        break
            elif ratings[i] == ratings[i-1]:
                left = 0
                right = 0
                cur = i
                while cur < len(ratings) - 1:
                    if ratings[cur] > ratings[cur + 1]:
                        right += 1
                        cur += 1
                    else:
                        break
            else:
                left = 0
                right -= 1
            res += max(left, right) + 1

        return res


class Solution3(object):
    def candy(self, ratings):
        res = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = max(res[i-1] + 1, res[i])
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i+1] + 1, res[i])
        return sum(res)

s = Solution3()
print(s.candy([1,2,2]))