# 简单粗暴
class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    self.set(matrix, i, j, rows, cols)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 2 ** 31:
                    matrix[i][j] = 0
        return matrix

    def set(self, matrix, row, col, rows, cols):
        i = 0
        while i < cols:
            if matrix[row][i] != 0:
                matrix[row][i] = 2 ** 31
            i += 1
        i = 0
        while i < rows:
            if matrix[i][col] != 0:
                matrix[i][col] = 2 **31
            i += 1