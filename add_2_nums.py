l1 = [2, 4, 3]
l2 = [5, 6, 4]


def addTwoNumbers(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    n = n1 if n1 <= n2 else n2
    sum = []
    ten = 0
    for i in range(n):
        s = l1[i]+l2[i]+ten
        bits = s % 10
        ten = (s - bits) / 10
        sum.append(int(bits))
    if n1 == n2:
        if ten > 0:
            sum.append(int(ten))
    elif n1 > n2:
        for i in range(n, n1):
            s = l1[i] + ten
            bits = s % 10
            ten = (s - bits) / 10
            sum.append(int(bits))
        if ten > 0:
            sum.append(int(ten))
    else:
        for i in range(n, n2):
            s = l2[i] + ten
            bits = s % 10
            ten = (s - bits) / 10
            sum.append(int(bits))
        if ten > 0:
            sum.append(int(ten))
    return sum

sum = addTwoNumbers(l1, l2)
print(sum)