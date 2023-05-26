class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        if val < root.val:
            return self.searchBST(root.left, val)


# 迭代 中序遍历
class Solution(object):
    def searchBST(self, root, val):
        if not root: return None
        stack = [root]

        while stack:
            node = stack.pop()
            if val == node.val:
                return node
            if val > node.val:
                if node.right:
                    stack.append(node.right)
                else:
                    return None
                continue
            if val < node.val:
                if node.left:
                    stack.append(node.left)
                else:
                    return None
                continue