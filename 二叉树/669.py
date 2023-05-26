class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root: return None
        left = self.trimBST(root.left, low, high)
        right = self.trimBST(root.right, low, high)
        if root.val >= low and root.val <= high:
            root.left = left
            root.right = right
            return root
        elif left and right:
            cur = left
            while cur.right:
                cur = cur.right
            cur.right = right
            return left
        elif left:
            return left
        return right


# 迭代
class Solution:
    def trimBST(self, root, low, high):
        if not root: return root
        # 处理头结点，让root移动到[L, R] 范围内，注意是左闭右开
        while root and (root.val < low or root.val > high):
            if root.val < low:  # 小于L往右走
                root = root.right
            else:  # 大于R往左走
                root = root.left
        # 此时root已经在[L, R] 范围内，处理左孩子元素小于L的情况
        cur = root
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
        # 此时root已经在[L, R] 范围内，处理右孩子大于R的情况
        cur = root
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        return root

node1 = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(2)
node1.left = node2
node1.right = node3

s = Solution()
s.trimBST(node1, 1, 2)