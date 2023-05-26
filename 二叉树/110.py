# 双递归
# 后序遍历求深度，然后递归判断每个节点对应的树是否平衡
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        balance = self.getdepth(root.left) - self.getdepth(root.right)
        return abs(balance) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getdepth(self, root):
        if not root: return 0
        return max(self.getdepth(root.left), self.getdepth(root.right)) + 1


#
class Solution:
    def isBalanced(self, root):
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root):
        # Base Case
        if not root:
            return 0
        # 左
        if (left_height := self.get_height(root.left)) == -1:
            return -1
        # 右
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        # 中
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)