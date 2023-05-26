# 前序
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.depth = 100000
        self.helper(root, 0)
        return self.depth

    def helper(self, root, d):
        if not root: return
        if not root.left and not root.right:
            if self.depth > d+1:
                self.depth = d+1
        if root.left:
            self.helper(root.left, d + 1)
        if root.right:
            self.helper(root.right, d + 1)


# 后序
class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1
