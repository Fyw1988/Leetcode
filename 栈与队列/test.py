from collections import deque
# 232
# class MyQueue(object):
#
#     def __init__(self):
#         self.stack_in = []
#         self.stack_out = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.stack_in.append(x)
#
#     def pop(self):
#         """
#         :rtype: int
#         """
#         if self.empty():
#             return None
#         if self.stack_out:
#             return self.stack_out.pop()
#         for _ in range(len(self.stack_in)):
#             self.stack_out.append(self.stack_in.pop())
#         return self.stack_out.pop()
#
#     def peek(self):
#         """
#         :rtype: int
#         """
#         ans = self.pop()
#         self.stack_out.append(ans)
#         return ans
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return not (self.stack_in or self.stack_out)


# 225
# class MyStack(object):
#
#     def __init__(self):
#         self.deque_in = deque()
#         self.deque_out = deque()
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.deque_in.append(x)
#
#     def pop(self):
#         """
#         :rtype: int
#         """
#         for _ in range(len(self.deque_in)-1):
#             self.deque_out.append(self.deque_in.popleft())
#         self.deque_in, self.deque_out = self.deque_out, self.deque_in
#         return self.deque_out.pop()
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         ans = self.pop()
#         self.deque_in.append(ans)
#         return ans
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return not self.deque_in


# 20
# class Solution(object):
#     def isValid(self, s):
#         stack = []
#         for p in s:
#             if p in '[{(':
#                 stack.append(p)
#             elif not stack or not self.match(p, stack.pop()):
#                 return False
#         return len(stack) == 0
#
#     def match(self, right, left):
#         dict = {
#             '[': ']',
#             '{': '}',
#             '(': ')'
#         }
#         if dict[left] == right:
#             return True
#         return False


# 1047
# class Solution(object):
#     def removeDuplicates(self, s):
#         stack = []
#         for str in s:
#             if not stack or str != stack[-1]:
#                 stack.append(str)
#             else:
#                 stack.pop()
#         return ''.join(stack)


# 150
# class Solution(object):
#     def evalRPN(self, tokens):
#         stack = []
#         for s in tokens:
#             if s in '+-*/':
#                 num1 = stack.pop()
#                 num2 = stack.pop()
#                 stack.append(self.calculate(int(num1), int(num2), s))
#             else:
#                 stack.append(s)
#         return int(stack[0])
#
#     def calculate(self, num1, num2, operator):
#         if operator == '+':
#             return num2 + num1
#         elif operator == '-':
#             return num2 - num1
#         elif operator == '*':
#             return num2 * num1
#         else:
#             return int(num2 / num1)   # 实现向0截断


# 239
# class MyQueue:
#     def __init__(self):
#         self.queue = deque()
#
#     def pop(self, value):
#         if self.queue and value == self.queue[0]:
#             self.queue.popleft()
#
#     def push(self, value):
#         while self.queue and value > self.queue[-1]:
#             self.queue.pop()
#         self.queue.append(value)
#
#     def front(self):
#         return self.queue[0]
#
#
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         que = MyQueue()
#         result = []
#         for i in range(k): #先将前k的元素放进队列
#             que.push(nums[i])
#         result.append(que.front()) #result 记录前k的元素的最大值
#         for i in range(k, len(nums)):
#             que.pop(nums[i - k]) #滑动窗口移除最前面元素
#             que.push(nums[i]) #滑动窗口前加入最后面的元素
#             result.append(que.front()) #记录对应的最大值
#         return result
