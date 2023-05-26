# 这种属于是最直观的方法了
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        return [None]

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        Tree1 = self.preorderTraversal(root)
        self.invertTree(root)
        Tree2 = self.preorderTraversal(root)
        if Tree1 == Tree2:
            return True
        return False


# 后序遍历，判断左右子树
class Solution(object):
    def isSymmetric(self, root):
        def compare(left, right):
            if not left and right: return False
            if not right and left: return False
            if not left and not right: return True
            if right.val != left.val: return False
            outside = compare(left.left, right.right)
            inside = compare(left.right, right.left)
            if inside and outside:
                return True
            return False
        return compare(root.left, root.right)


# 树中的递归都能用迭代来实现
class Solution(object):
    def isSymmetric(self, root):
        if not root: return False
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left and not right:
                continue
            if not left or not right or right.val != left.val:
                return False
            stack.append(left.right)
            stack.append(right.left)
            stack.append(left.left)
            stack.append(right.right)  # 与前序遍历不同的是，这里的顺序不重要，只要是比较了对称的节点就行
        return True


# 层序遍历
class Solution(object):
    def isSymmetric(self, root):
        if not root: return False
        from collections import deque
        que = deque([root.left, root.right])

        while que:
            left = que.popleft()
            right = que.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            que.append(left.left)
            que.append(right.right)
            que.append(left.right)
            que.append(right.left)
        return True