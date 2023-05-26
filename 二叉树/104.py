# 前序遍历
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.helper(root, 0)
        return self.depth

    def helper(self, root, d):
        if not root: return
        if self.depth < d+1:
            self.depth = d+1
        if root.left:
            self.helper(root.left, d + 1)
        if root.right:
            self.helper(root.right, d + 1)


# 后序遍历
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        maxleft = self.maxDepth(root.left)
        maxright = self.maxDepth(root.right)
        return max(maxleft, maxright) + 1