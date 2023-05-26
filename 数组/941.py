class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3: return False
        if arr[0] > arr[1]: return False
        if arr[-1] > arr[-2]: return False
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] < arr[i-1]:
                for j in range(i, len(arr)):
                    if arr[j] >= arr[j-1]:
                        return False
                break

        return True


# 双指针
class Solution:
    def validMountainArray(self, arr) -> bool:
        left, right = 0, len(arr) - 1

        while left < len(arr) - 1 and arr[left + 1] > arr[left]:
            left += 1

        while right > 0 and arr[right - 1] > arr[right]:
            right -= 1

        return left == right and right != 0 and left != len(arr) - 1