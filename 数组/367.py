def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    left = 0
    right = num + 1
    while left < right:
        middle = left + (right - left) // 2
        if middle * middle < num:
            left = middle + 1  # 这里我一开始犯了个错误，注意二分查找开区间写法是左闭右开，所以left=middle+1
        elif middle * middle > num:
            right = middle
        else:
            return True
    return False

a = 14
b = isPerfectSquare(14)