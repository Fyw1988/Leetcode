class Solution:
    def findLength(self, nums1, nums2) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        result = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                dp[i][j] = dp[i-1][j-1] + 1 if nums1[i-1] == nums2[j-1] else 0
                result = max(result, dp[i][j])

        return result


class Solution:
    def findLength(self, A, B) -> int:
        dp = [0] * (len(B) + 1)
        result = 0
        for i in range(1, len(A)+1):
            for j in range(len(B), 0, -1):
                if A[i-1] == B[j-1]:
                    dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0 #注意这里不相等的时候要有赋0的操作
                result = max(result, dp[j])
        return result


s = Solution()
print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))