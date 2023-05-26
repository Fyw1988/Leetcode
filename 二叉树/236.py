class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 回溯，暴力解法，没错但超时
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.paths = []
        path = []
        self.getpath(root, p, q, path)
        for i in range(len(self.paths[0]) - 1, -1, -1):
            if self.paths[0][i] in self.paths[1]:
                return self.paths[0][i]

    def getpath(self, root, p, q, path):
        if not root: return
        path.append(root)
        if root.val == p.val:
            self.paths.append(path[:])
        if root.val == q.val:
            self.paths.append(path[:])
        self.getpath(root.left, p, q, path)
        self.getpath(root.right, p, q, path)
        path.pop()


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = []
        path = [root]
        def dfs(root):
            if not root: return
            if root.val in [p.val,q.val]:
                a.append(list(path))
            for node in [root.left,root.right]:
                path.append(node)
                dfs(node)
                path.pop()
        dfs(root)
        i=0
        while i<min(len(a[0]),len(a[1])) and a[0][i].val==a[1][i].val:
            i+=1
        return a[0][i-1]


class Solution3:
    """二叉树的最近公共祖先 递归法"""
    # 如果有公共祖先节点，就返回这个最近公共祖先节点；如果没有最近公共祖先节点，就返回目标节点；如果连目标节点都没，就返回None
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        return right












n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(1)
n4 = TreeNode(6)
n5 = TreeNode(2)
n6 = TreeNode(0)
n7 = TreeNode(8)
n8 = TreeNode(7)
n9 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9

s = Solution1()
s.lowestCommonAncestor(n1, n2, n3)