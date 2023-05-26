class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 根据前序确定根节点
        root = TreeNode()
        root.val = preorder[0]

        # 根据根节点切割中序数组
        pos = inorder.index(root.val)
        inorderleft = inorder[:pos]
        inorderright = inorder[pos+1:]
        # 切割前序数组
        preorderleft = preorder[1:len(inorderleft)+1]
        preorderright = preorder[len(inorderleft)+1:]
        # 递归
        root.left = self.buildTree(preorderleft, inorderleft)
        root.right = self.buildTree(preorderright, inorderright)

        return root