class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root: return False
        stack = [root]
        while stack:
            cur = stack.pop()
            if self.compare(cur, subRoot):
                return True
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)

        return False

    def compare(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        left = self.compare(p.left, q.left)
        right = self.compare(p.right, q.right)
        return left and right


# 递归写法
class Solution(object):
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)


class Solution(object):
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        return self.isSameTree(s, t) or left or right

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)