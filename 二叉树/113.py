class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution1(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        path = []
        self.paths = []
        self.getpath(root, path, targetSum)
        return self.paths

    def getpath(self, root, path, target):
        if not root: return
        path.append(root.val)
        if sum(path) == target and not root.left and not root.right:
            self.paths.append(path[:])
        self.getpath(root.left, path, target)
        self.getpath(root.right, path, target)
        path.pop()


# 迭代
class Solution2(object):
    def pathSum(self, root, targetSum):
        if not root: return []
        stack = [root]
        paths = [[root.val]]
        results = []

        while stack:
            node = stack.pop()
            path = paths.pop()
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    results.append(path[:])
            if node.left:
                stack.append(node.left)
                paths.append(path + [node.left.val])
            if node.right:
                stack.append(node.right)
                paths.append(path + [node.right.val])

        return results


n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(5)
n10 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n4.left = n9
n4.right = n10

s = Solution2()
s.pathSum(n1, 22)