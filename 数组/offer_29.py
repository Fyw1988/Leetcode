# 这题和前面的54几乎完全一样
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix: return []
    nums = []
    startX, startY = 0, 0
    offset = 1
    row, col = len(matrix), len(matrix[0])
    while offset <= min(row, col)/2:
        for i in range(startY, col - offset):
            nums.append(matrix[startX][i])
        for i in range(startX, row - offset):
            nums.append(matrix[i][col-offset])
        for i in range(col - offset, startY, -1):
            nums.append(matrix[row-offset][i])
        for i in range(row - offset, startX, -1):
            nums.append(matrix[i][startY])
        offset += 1
        startX += 1
        startY += 1
    if min(row, col) % 2 != 0:
        if col > row:
            for i in range(startY, col - offset + 1):
                nums.append(matrix[startX][i])
        elif row > col:
            for i in range(startX, row - offset + 1):
                nums.append(matrix[i][col-offset])
        else:
            nums.append(matrix[startX][startY])
    return nums