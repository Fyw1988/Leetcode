def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    m = [[0] * n for _ in range(n)]  # 构建螺旋矩阵
    startX, startY = 0, 0
    offset = 1
    count = 1
    while offset <= n/2:
        for i in range(startY, n-offset):
            m[startX][i] = count
            count += 1
        for i in range(startX, n-offset):
            m[i][n - offset] = count
            count += 1
        for i in range(n - offset, startY, -1):  # 从右至左
            m[n - offset][i] = count
            count += 1
        for i in range(n - offset, startX, -1):
            m[i][startY] = count
            count += 1
        offset += 1
        startX += 1
        startY += 1
    if n % 2 != 0:
        m[n//2][n//2] = count
    return m


# 螺旋数组二刷
class Solution(object):
    def generateMatrix(self, n):
        ans = [[0] * n for _ in range(n)]
        startIndex, endIndex = 0, n - 1
        num = 1
        while startIndex < n // 2:
            for j in range(startIndex, endIndex):
                ans[startIndex][j] = num
                num += 1
            for i in range(startIndex, endIndex):
                ans[i][endIndex] = num
                num += 1
            for j in range(endIndex, startIndex, -1):
                ans[endIndex][j] = num
                num += 1
            for i in range(endIndex, startIndex, -1):
                ans[i][startIndex] = num
                num += 1
            startIndex += 1
            endIndex -= 1
        if n % 2:
            ans[startIndex][startIndex] = n ** 2
        return ans


s = Solution()
print(s.generateMatrix(4))