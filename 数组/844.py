# 另类双指针，前面的双指针都是两个指针遍历一个数组，这里双指针分别遍历两个数组，起初打算把双指针用在一个字符串上，开始就陷入误区
# 对于这题而言，比较两个字符串是否相同，采用遍历逐个比较就好，但由于退格符的存在，反向遍历比正向遍历要简单很多（如果是跳格符就正向遍历）
# 由于不同字符串长度可能不同，而且退格的情况可能不同，所以一个指针无法同时遍历两个字符串，因此此处需要采用双指针（即每个字符串单独一个指针）
# 总结出一条规律，一般从后往前遍历都用while循环实现，而正序遍历则往往用for循环实现
def backspaceCompare(S, T):
    i, j = len(S) - 1, len(T) - 1
    skipS = skipT = 0

    while i >= 0 or j >= 0:
        while i >= 0:
            if S[i] == "#":
                skipS += 1
                i -= 1
            elif skipS > 0:
                skipS -= 1
                i -= 1
            else:
                break
        while j >= 0:
            if T[j] == "#":
                skipT += 1
                j -= 1
            elif skipT > 0:
                skipT -= 1
                j -= 1
            else:
                break
        if i >= 0 and j >= 0:
            if S[i] != T[j]:
                return False
        elif i >= 0 or j >= 0:  # 两个字符串有且只有一个先遍历完了，就返回false
            return False
        i -= 1
        j -= 1

    return True