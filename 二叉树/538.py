class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum = [0]
        self.getsum(root, sum)
        return root

    def getsum(self, root, sum):
        if not root: return 0
        self.getsum(root.right, sum)
        root.val = root.val + sum[-1]
        sum.append(root.val)
        self.getsum(root.left, sum)


class Solution:
    def __init__(self):
        self.count = 0

    def convertBST(self, root):
        if root == None:
            return
        '''
        倒序累加替换：  
        '''
        # 右
        self.convertBST(root.right)

        # 中
        # 中节点：用当前root的值加上pre的值
        self.count += root.val

        root.val = self.count

        # 左
        self.convertBST(root.left)

        return root