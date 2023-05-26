class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.results = []
        self.board = [['.'] * n for _ in range(n)]
        self.backtracking(n, 0)
        return self.results

    def backtracking(self, n, row):
        if row == n:
            result = [''.join(row) for row in self.board]
            self.results.append(result)
            return

        for i in range(n):
            if self.isvalid(self.board, row, i, n):
                self.board[row][i] = 'Q'
                self.backtracking(n, row+1)
                self.board[row][i] = '.'
            else:
                continue

    def isvalid(self, board, row, col, n):
        # 判断左上角
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 判断右上角
        i, j = row-1, col+1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        # 判断垂直方向
        i, j = row-1, col
        while i >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1

        return True

s = Solution()
print(s.solveNQueens(4))

# a = [["Q....","..Q..","....Q",".Q...","...Q."],
#  ["Q....","...Q.",".Q...","....Q","..Q.."],
#  [".Q...","...Q.","Q....","..Q..","....Q"],
#  [".Q...","....Q","..Q..","Q....","...Q."],
#  ["..Q..","Q....","...Q.",".Q...","....Q"],
#  ["..Q..","....Q",".Q...","...Q.","Q...."],
#  ["...Q.","Q....","..Q..","....Q",".Q..."],
#  ["...Q.",".Q...","....Q","..Q..","Q...."],
#  ["....Q",".Q...","...Q.","Q....","..Q.."],
#  ["....Q","..Q..","Q....","...Q.",".Q..."]]
#
# b = [["Q....","..Q..","....Q",".Q...","...Q."],
#  ["Q....","...Q.",".Q...","....Q","..Q.."],
#  [".Q...","...Q.","Q....","..Q..","....Q"],
#  [".Q...","....Q","..Q..","Q....","...Q."],
#  ["..Q..","Q....","...Q.",".Q...","....Q"],
#  ["..Q..","....Q","Q....","...Q.",".Q..."],
#  ["..Q..","....Q",".Q...","...Q.","Q...."],
#  ["...Q.","Q....","..Q..","....Q",".Q..."],
#  ["...Q.",".Q...","....Q","Q....","..Q.."],
#  ["...Q.",".Q...","....Q","..Q..","Q...."],
#  ["....Q",".Q...","...Q.","Q....","..Q.."],
#  ["....Q","..Q..","Q....","...Q.",".Q..."]]
#
# for board in b:
#     if board not in a:
#         print(board)