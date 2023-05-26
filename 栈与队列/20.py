def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    def match(s, t):
        left = "({["
        right = ")}]"
        return left.index(t) == right.index(s)

    stack = []
    for i in s:
        if i in "([{":
            stack.append(i)
        else:
            if not stack: return False
            balance = match(i, stack.pop())
            if not balance: return False
    return not stack