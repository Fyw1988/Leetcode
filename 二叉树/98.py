class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorder(root)
        for i in range(len(inorder)-1):
            if inorder[i].val < inorder[i+1].val:
                continue
            return False
        return True

    def inorder(self, root):
        if not root: return []
        return self.inorder(root.left) + [root] + self.inorder(root.right)


# 递归 不需要定义数组来存储遍历节点
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 规律: BST的中序遍历节点数值是从小到大.
        cur_max = -float("INF")

        def __isValidBST(root: TreeNode) -> bool:
            nonlocal cur_max

            if not root:
                return True

            is_left_valid = __isValidBST(root.left)
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            is_right_valid = __isValidBST(root.right)

            return is_left_valid and is_right_valid

        return __isValidBST(root)


# 递归 避免初始化最小值
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 规律: BST的中序遍历节点数值是从小到大.
        pre = None

        def __isValidBST(root: TreeNode) -> bool:
            nonlocal pre

            if not root:
                return True

            is_left_valid = __isValidBST(root.left)
            if pre and pre.val >= root.val: return False
            pre = root
            is_right_valid = __isValidBST(root.right)

            return is_left_valid and is_right_valid

        return __isValidBST(root)


# 迭代 中序遍历的基础上改的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre and cur.val <= pre.val: # 比较当前节点和前节点的值的大小
                    return False
                pre = cur
                cur = cur.right
        return True