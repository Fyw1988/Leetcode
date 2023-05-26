def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    left = 0
    right = x
    while left <= right:
        middle = left + (right - left) // 2
        if middle * middle > x:
            right = middle - 1
        elif middle * middle < x:
            left = middle + 1
        else:
            return middle
    return right
