class Solution(object):
    def __init__(self):
        self.directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        m, n = len(board), len(board[0])
        if m == 0:
            return False
        mark = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        # 回溯
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True

        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == \
                    word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False


class Solution(object):
    def __init__(self):
        self.directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        m, n = len(board), len(board[0])
        self.mark = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.mark[i][j] = 1
                    if self.backtracking(board, word[1:], i, j):
                        return True
                    else:
                        self.mark[i][j] = 0
        return False

    def backtracking(self, board, word, i, j):
        if not word:
            return True

        for direct in self.directs:
            cur_i, cur_j = i + direct[0], j + direct[1]
            if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and self.mark[cur_i][cur_j] == 0:
                if board[cur_i][cur_j] == word[0]:
                    self.mark[cur_i][cur_j] += 1
                    if self.backtracking(board, word[1:], cur_i, cur_j):
                        return True
                    self.mark[cur_i][cur_j] -= 1
        return False