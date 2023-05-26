class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = root.right
            while node.left:
                node = node.left
            node.left = root.left
            root = root.right
        return root


# 普通二叉树
class Solution:
    def deleteNode(self, root, key):
        if not root: return root
        if root.val == key:
            if not root.right:  # 这里第二次操作目标值：最终删除的作用
                return root.left
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            root.val, tmp.val = tmp.val, root.val  # 这里第一次操作目标值：交换目标值其右子树最左面节点。

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root


# 迭代法
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == key:
                if not node.left:
                    return root.right
                if not root.right:
                    return root.left
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                root = root.right

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)