def removeDuplicates1(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for i in s:
        if stack:
            t = stack.pop()
            if i != t:
                stack.append(t)
                stack.append(i)
        else: stack.append(i)
    return "".join(stack)


# 拓展：双指针
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]

            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1

        return ''.join(res[0: slow])


print(removeDuplicates1("aaaaaaaaa"))
