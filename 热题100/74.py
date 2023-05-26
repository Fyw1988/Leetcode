class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left, right = 0, len(row)
                while left < right:
                    mid = (left+right) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        right = mid
                    else:
                        left = mid+1
                return False
        return False


s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))