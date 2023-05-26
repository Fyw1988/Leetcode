# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder: return None
        # 根据后序数组确定根节点
        root = TreeNode()
        root.val = postorder[-1]
        # 寻找切割点
        pos = inorder.index(root.val)
        # 切割中序
        inorderleft = inorder[:pos]
        inorderright = inorder[pos+1:]
        # 切割后序
        postorderleft = postorder[:len(inorderleft)]
        postorderright = postorder[len(inorderleft):-1]

        # 迭代
        root.left = self.buildTree(inorderleft, postorderleft)
        root.right = self.buildTree(inorderright, postorderright)

        return root