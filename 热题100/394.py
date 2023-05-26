class Solution(object):
    def decodeString(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                word = ''
                while stack and stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()
                repeat = ''
                while stack and stack[-1].isdigit():  # .isdigit() 判断字符是否是数字字符
                    repeat = stack.pop() + repeat
                for _ in range(int(repeat)):
                    stack.append(word)
            else:
                stack.append(s[i])
        return ''.join(stack)


s = Solution()
print(s.decodeString("3[a]2[bc]"))