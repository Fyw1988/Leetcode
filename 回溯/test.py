# 77
# class Solution(object):
#     def __init__(self):
#         self.results = []
#         self.path = []
#
#     def combine(self, n, k):
#         nums = [i for i in range(1, n+1)]
#         self.backtracking(nums, k, k, startIndex=0)
#         return self.results
#
#     def backtracking(self, nums, k, need, startIndex):
#         if len(self.path) == k:
#             self.results.append(self.path[:])
#             return
#
#         for i in range(startIndex, len(nums)-need+1):
#             self.path.append(nums[i])
#             self.backtracking(nums, k, need-1, i+1)
#             self.path.pop()


# 217
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def combinationSum3(self, k, n):
#         nums = [i for i in range(1, 10)]
#         self.backtracking(nums, k, n, 0)
#         return self.results
#
#     def backtracking(self, nums, k, n, startIndex):
#         if len(self.path) == k and sum(self.path) == n:
#             self.results.append(self.path[:])
#             return
#         # 剪枝
#         if sum(self.path) >= n or len(self.path) >= k:
#             return
#         lastIndex = len(nums) - (k - len(self.path)) + 1
#
#         for i in range(startIndex, lastIndex):
#             self.path.append(nums[i])
#             self.backtracking(nums, k, n, i+1)
#             self.path.pop()


# 17
# 从同一个集合里取数和从不同的集合里取数，index的含义与作用也有所不同
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#         self.letter_map = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#
#     def letterCombinations(self, digits):
#         if not digits: return []
#         self.backtracking(digits, 0)
#         return self.results
#
#     def backtracking(self, digits, index):
#         if len(self.path) == len(digits):
#             self.results.append(''.join(self.path[:]))
#             return
#
#         for i in self.letter_map[digits[index]]:
#             self.path.append(i)
#             self.backtracking(digits, index+1)
#             self.path.pop()


# 39
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def combinationSum(self, candidates, target):
#         self.backtracking(candidates, target, 0)
#         return self.results
#
#     def backtracking(self, candidates, target, startIndex):
#         if sum(self.path) == target:
#             self.results.append(self.path[:])
#             return
#
#         # 剪枝
#         if sum(self.path) > target:
#             return
#
#         for i in range(startIndex, len(candidates)):
#             self.path.append(candidates[i])
#             self.backtracking(candidates, target, i)
#             self.path.pop()


# 40
# 关键在于去重
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def combinationSum2(self, candidates, target):
#         candidates.sort()
#         self.backtracking(candidates, target, 0)
#         return self.results
#
#     def backtracking(self, candidates, target, startIndex):
#         if sum(self.path) == target:
#             self.results.append(self.path[:])
#             return
#
#         for i in range(startIndex, len(candidates)):
#             if i > startIndex and candidates[i] == candidates[i-1]:
#                 continue
#             if sum(self.path) + candidates[i] > target:
#                 continue
#             self.path.append(candidates[i])
#             self.backtracking(candidates, target, i+1)
#             self.path.pop()


# # 131
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def partition(self, s):
#         self.backtracking(s, 0)
#         return self.results
#
#     def backtracking(self, s, startIndex):
#         if startIndex == len(s):
#             self.results.append(self.path[:])
#             return
#
#         for i in range(startIndex, len(s)):
#             if self.isPalindrome(s[startIndex:i+1]):
#                 self.path.append(s[startIndex:i+1])
#                 self.backtracking(s, i+1)
#                 self.path.pop()
#             else:
#                 continue
#
#     def isPalindrome(self, s):
#         return s == s[::-1]


# 93
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def restoreIpAddresses(self, s):
#         self.backtracking(s, 0)
#         return self.results
#
#     def backtracking(self, s, startIndex):
#         if len(self.path) == 4 and startIndex == len(s):
#             self.results.append('.'.join(self.path))
#             return
#         elif len(self.path) != 4 and startIndex == len(s):
#             return
#
#         lastIndex = min(len(s), startIndex+3)
#         if s[startIndex] == '0':
#             self.path.append('0')
#             self.backtracking(s, startIndex+1)
#             self.path.pop()
#             return
#
#         for i in range(startIndex, lastIndex):
#             if int(s[startIndex:i+1]) <= 255 and len(self.path) < 4:
#                 self.path.append(s[startIndex:i+1])
#                 self.backtracking(s, i+1)
#                 self.path.pop()
#             else:
#                 return


# 78
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def subsets(self, nums):
#         for i in range(len(nums)+1):
#             self.backtracking(nums, i, 0)
#         return self.results
#
#     def backtracking(self, nums, k, startIndex):
#         if len(self.path) == k:
#             self.results.append(self.path[:])
#             return
#
#         for i in range(startIndex, len(nums)):
#             self.path.append(nums[i])
#             self.backtracking(nums, k, i+1)
#             self.path.pop()


# 90
# 树层去重
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def subsetsWithDup(self, nums):
#         nums.sort()
#         self.backtracking(nums, 0)
#         return self.results
#
#     def backtracking(self, nums, startIndex):
#         self.results.append(self.path[:])
#         if startIndex == len(nums):
#             return
#
#         for i in range(startIndex, len(nums)):
#             if i > startIndex and nums[i] == nums[i-1]:
#                 continue
#             self.path.append(nums[i])
#             self.backtracking(nums, i+1)
#             self.path.pop()


# 491
# set去重与used数组去重两种写法
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def findSubsequences(self, nums):
#         self.backtracking(nums, 0)
#         return self.results
#
#     def backtracking(self, nums, startIndex):
#         if len(self.path) >= 2:
#             self.results.append(self.path[:])
#
#         usage_list = set()
#         for i in range(startIndex, len(nums)):
#             if nums[i] in usage_list:
#                 continue
#             else:
#                 usage_list.add(nums[i])
#             if not self.path or nums[i] >= self.path[-1]:
#                 self.path.append(nums[i])
#                 self.backtracking(nums, i+1)
#                 self.path.pop()


# 46
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def permute(self, nums):
#         used = [0] * len(nums)
#         self.backtracking(nums, used, 0)
#         return self.results
#
#     def backtracking(self, nums, used, sum_):
#         if sum_ == len(nums):
#             self.results.append(self.path[:])
#             return
#
#         for i in range(len(nums)):
#             if used[i] == 0:
#                 self.path.append(nums[i])
#                 used[i] = 1
#                 sum_ += 1
#                 self.backtracking(nums, used, sum_)
#                 self.path.pop()
#                 used[i] = 0
#                 sum_ -= 1


# 47
# 因为是全排列，也可以先排序方便去重
# class Solution(object):
#     def __init__(self):
#         self.path = []
#         self.results = []
#
#     def permuteUnique(self, nums):
#         self.used = [0] * len(nums)
#         self.backtracking(nums, self.used, 0)
#         return self.results
#
#     def backtracking(self, nums, used, sum_):
#         if sum_ == len(nums):
#             self.results.append(self.path[:])
#             return
#
#         used2 = set()
#         for i in range(len(nums)):
#             if used[i] == 0 and nums[i] not in used2:
#                 used2.add(nums[i])
#                 self.path.append(nums[i])
#                 used[i] = 1
#                 sum_ += 1
#                 self.backtracking(nums, used, sum_)
#                 self.path.pop()
#                 used[i] = 0
#                 sum_ -= 1


# 332
class Solution(object):
    def __init__(self):
        self.path = ['JFK']

    def findItinerary(self, tickets):
        from collections import defaultdict
        tickets_dict = defaultdict(list)
        for ticket in tickets:
            tickets_dict[ticket[0]].append(ticket[1])
        for airport in tickets_dict:
            tickets_dict[airport].sort()
        self.backtracking(tickets_dict, len(tickets)+1, 'JFK')
        return self.path

    def backtracking(self, tickets, l, start):
        if len(self.path) == l:
            return True

        for _ in tickets[start]:
            airport = tickets[start].pop(0)
            self.path.append(airport)
            if self.backtracking(tickets, l, airport):
                return True
            self.path.pop()
            tickets[start].append(airport)


# 51
# class Solution(object):
#     def __init__(self):
#         self.results = []
#
#     def solveNQueens(self, n):
#         self.board = [['.'] * n for _ in range(n)]
#         self.backtracking(n, 0)
#         return self.results
#
#     def backtracking(self, n, index):
#         if index == n:
#             temp_res = []
#             for temp in self.board:
#                 temp_str = "".join(temp)
#                 temp_res.append(temp_str)
#             self.results.append(temp_res)
#             return
#
#         for i in range(n):
#             if self.test(self.board, n, index, i):
#                 self.board[index][i] = 'Q'
#                 self.backtracking(n, index+1)
#                 self.board[index][i] = '.'
#
#     def test(self, board, n, row, col):
#         i, j = row, col
#         while i > 0:
#             if board[i-1][j] == 'Q':
#                 return False
#             i -= 1
#
#         i, j = row-1, col-1
#         while i >= 0 and j >= 0:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j -= 1
#
#         i, j = row - 1, col + 1
#         while i >= 0 and j < n:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j += 1
#
#         return True


# 52
# class Solution(object):
#     def __init__(self):
#         self.ans = 0
#
#     def totalNQueens(self, n):
#         self.board = [['.'] * n for _ in range(n)]
#         self.backtracking(n, 0)
#         return self.ans
#
#     def backtracking(self, n, index):
#         if index == n:
#             self.ans += 1
#             return
#
#         for i in range(n):
#             if self.test(self.board, index, i, n):
#                 self.board[index][i] = 'Q'
#                 self.backtracking(n, index+1)
#                 self.board[index][i] = '.'
#
#     def test(self, board, row, col, n):
#         i, j = row, col
#         while i >= 0:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#
#         i, j = row, col
#         while i >= 0 and j >= 0:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j -= 1
#
#         i, j = row, col
#         while i >= 0 and j < n:
#             if board[i][j] == 'Q':
#                 return False
#             i -= 1
#             j += 1
#
#         return True


# 37
# class Solution(object):
#     def solveSudoku(self, board):
#         n = len(board[0])
#         self.backtracking(board)
#         return board
#
#     def backtracking(self, board) -> bool:
#         # 若有解，返回True；若无解，返回False
#         for i in range(len(board)): # 遍历行
#             for j in range(len(board[0])):  # 遍历列
#                 # 若空格内已有数字，跳过
#                 if board[i][j] != '.': continue
#                 for k in range(1, 10):
#                     if self.is_valid(i, j, k, board):
#                         board[i][j] = str(k)
#                         if self.backtracking(board): return True
#                         board[i][j] = '.'
#                 # 若数字1-9都不能成功填入空格，返回False无解
#                 return False
#         return True # 有解
#
#     def is_valid(self, row, col, val, board):
#         for i in range(9):
#             if board[row][i] == str(val):
#                 return False
#         # 判断同一列是否冲突
#         for j in range(9):
#             if board[j][col] == str(val):
#                 return False
#         # 判断同一九宫格是否有冲突
#         start_row = (row // 3) * 3
#         start_col = (col // 3) * 3
#         for i in range(start_row, start_row + 3):
#             for j in range(start_col, start_col + 3):
#                 if board[i][j] == str(val):
#                     return False
#         return True


