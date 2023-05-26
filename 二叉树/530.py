class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
# 注意：这题不存在空树的情况
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 定义局部变量记录上个节点值
        pre = None

        def getMin(root):
            nonlocal pre
            if not root: return 100000
            minleft = getMin(root.left)
            if pre:
                minmiddle1 = root.val-pre.val
                pre = root
            else:
                minmiddle1 = 100000
                pre = root
            minright = getMin(root.right)
            minmiddle2 = pre.val - root.val
            return min(minleft, minright, minmiddle1, minmiddle2)
        return getMin(root)


# 迭代
class Solution(object):
    def getMinimumDifference(self, root):
        cur = root
        stack = []
        pre = None
        minval = 10000

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    minval = min(cur.val-pre.val, minval)
                pre = cur
                cur = cur.right
        return minval