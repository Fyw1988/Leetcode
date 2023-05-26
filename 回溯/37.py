class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        return self.backTracking(board)

    def backTracking(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if self.isValid(i, j, str(num), board):
                            board[i][j] = str(num)
                            if self.backTracking(board): return True
                            board[i][j] = '.'
                    return False
        return True

    def isValid(self, row, col, num, board):
        # 检查每一行
        i, j = 0, col
        while i < len(board):
            if board[i][j] == num:
                return False
            i += 1

        # 检查每一列
        i, j = row, 0
        while j < len(board[0]):
            if board[i][j] == num:
                return False
            j += 1

        # 检查所在九宫格
        startX, startY = row // 3, col // 3
        for i in range(startX*3, (startX+1)*3):
            for j in range(startY*3, (startY+1)*3):
                if board[i][j] == num:
                    return False

        return True


# 官方题解
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board):
        # 若有解，返回True；若无解，返回False
        for i in range(len(board)): # 遍历行
            for j in range(len(board[0])):  # 遍历列
                # 若空格内已有数字，跳过
                if board[i][j] != '.': continue
                for k in range(1, 10):
                    if self.is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtracking(board): return True
                        board[i][j] = '.'
                # 若数字1-9都不能成功填入空格，返回False无解
                return False
        return True # 有解

    def is_valid(self, row, col, val, board):
        # 判断同一行是否冲突
        for i in range(9):
            if board[row][i] == str(val):
                return False
        # 判断同一列是否冲突
        for j in range(9):
            if board[j][col] == str(val):
                return False
        # 判断同一九宫格是否有冲突
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True
