class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def compare(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            left = compare(p.left, q.left)
            right = compare(p.right, q.right)
            if left and right:
                return True
        return compare(p, q)


# 迭代
# 注意与递归的区别，这里的continue达到递归中return一样的作用
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: return True
        stack = [p, q]
        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append(node1.left)
            stack.append(node2.left)
            stack.append(node1.right)
            stack.append(node2.right)
        return True