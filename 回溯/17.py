class Solution1(object):
    def __init__(self):
        self.answers = []
        self.answer = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nnums = len(digits)
        if nnums == 0: return []
        self.backtrack(digits, 0, nnums)
        return self.answers

    def backtrack(self, digits, startindex, nnums):
        if len(self.answer) == nnums:
            self.answers.append(self.answer)
            return

        for i in range(startindex, nnums):  # 这里这个循环是没有必要的，因为每个数字字符都是一定要取对应字母的，所以i只能取0.代码随想录给的答案其实可以看成这个算法的剪枝，所以用时要少一些
            for j in range(len(self.letter_map[digits[i]])):
                self.answer += self.letter_map[digits[i]][j]
                self.backtrack(digits, i + 1, nnums)
                self.answer = self.answer[:-1]


class Solution2:
    def __init__(self):
        self.answers = []
        self.answer = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        # self.answers.clear()
        if not digits: return []
        self.backtracking(digits, 0)
        return self.answers

    def backtracking(self, digits, index):
        # 回溯函数没有返回值
        # Base Case
        if index == len(digits):  # 当遍历穷尽后的下一层时
            self.answers.append(self.answer)
            return
            # 单层递归逻辑
        letters = self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter  # 处理
            self.backtracking(digits, index + 1)  # 递归至下一层
            self.answer = self.answer[:-1]  # 回溯


s = Solution1()
print(s.letterCombinations('23'))