class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


# 利用完全二叉树性质，时间复杂度为O(logn)*O(logn)
class Solution(object):
    def countNodes(self, root):
        if not root: return 0
        leftDepth = 0
        rightDepth = 0
        left = root.left
        right = root.right
        while left:
            left = left.left
            leftDepth += 1
        while right:
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return (2 ** leftDepth) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1