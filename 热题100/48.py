# 这种写法对于numpy数组是可行的，但是对于列表不可行。列表无法通过matrix[:][i]实现切片
# class Solution(object):
#     def rotate(self, matrix):
#         n = len(matrix)
#         start = 0
#         while start < n // 2:
#             temp = matrix[start][start:n-start]
#             matrix[:][n-start-1], temp = temp, matrix[:][n-start-1]
#             matrix[n-start-1][:], temp = temp[::-1], matrix[n-start-1][:]
#             matrix[:][start], temp = temp, matrix[:][start]
#             matrix[start][:], temp = temp[::-1], matrix[start][:]
#             start += 1
#         return matrix


# 解法一：矩阵旋转等于水平翻转加对角线翻转
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# 解法二：原地翻转，其实这里和上面第一个算法思路是一样的，只不过列表只能实现一个数一个数地旋转
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]