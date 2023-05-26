class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxRoot = 0
        self.helper(root, 0)
        return self.maxRoot

    def helper(self, root, sum):
        if not root: return 0
        sum += root.val
        if not root.left and not root.right:
            if sum > self.maxRoot:
                self.maxRoot = sum
        if root.left:
            self.helper(root.left, sum)
        if root.right:
            self.helper(root.right, sum)