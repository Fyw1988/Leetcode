def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    def calculate(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        else:
            return int(num1 / num2)   # 实现向0截断

    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(token)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(calculate(int(num1), int(num2), token))
    return int(stack[0])


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def calculate(num1, num2, operator):
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            else:
                return int(num1 / num2)   # 实现向0截断

        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(calculate(int(num1), int(num2), token))
        return int(stack[0])

s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(s.evalRPN(tokens))