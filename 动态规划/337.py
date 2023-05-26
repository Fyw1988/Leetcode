class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 后序遍历
class Solution:
    def rob(self, root) -> int:
        return max(self.postorder(root))

    def postorder(self, root):
        if not root: return [0, 0]
        dp1 = self.postorder(root.left)
        dp2 = self.postorder(root.right)

        dp = [0, 0]
        dp[0] = max(dp1)+max(dp2)
        dp[1] = dp1[0] + dp2[0] + root.val
        return dp