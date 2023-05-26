class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        node = TreeNode(val)
        if not root: return node
        if not root.right and root.val < val:
            root.right = node
        if not root.left and root.val > val:
            root.left = node
        # 前序遍历
        if val > root.val:
            self.insertIntoBST(root.right, val)
        if val < root.val:
            self.insertIntoBST(root.left, val)

        return root


# 迭代法
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = None  # 此步可以省略
        cur = root

        # 用while循环不断地找新节点的parent
        while cur:
            parent = cur  # 首先保存当前非空节点作为下一次迭代的父节点
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left

        # 运行到这意味着已经跳出上面的while循环,
        # 同时意味着新节点的parent已经被找到.
        # parent已被找到, 新节点已经ready. 把两个节点黏在一起就好了.
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root


#
class Solution(object):
    def insertIntoBST(self, root, val):
        # 返回更新后的以当前root为根节点的新树，方便用于更新上一层的父子节点关系链

        # Base Case
        if not root: return TreeNode(val)

        # 单层递归逻辑:
        if val < root.val:
            # 将val插入至当前root的左子树中合适的位置
            # 并更新当前root的左子树为包含目标val的新左子树
            root.left = self.insertIntoBST(root.left, val)

        if root.val < val:
            # 将val插入至当前root的右子树中合适的位置
            # 并更新当前root的右子树为包含目标val的新右子树
            root.right = self.insertIntoBST(root.right, val)

        # 返回更新后的以当前root为根节点的新树
        return root