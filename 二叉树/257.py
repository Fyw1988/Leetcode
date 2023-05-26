# 递归加回溯
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        results = []
        path = ''
        self.getpath(root, path, results)
        return results

    def getpath(self, root, path, results):
        path += str(root.val)
        if not root.left and not root.right:
            results.append(path)

        if root.left:
            self.getpath(root.left, path + '->', results)
        if root.right:
            self.getpath(root.right, path + '->', results)


# 迭代
# 层序遍历的基础上改的
class Solution(object):
    def binaryTreePaths(self, root):
        if not root: return []
        from collections import deque
        que = deque([root])
        paths = deque([str(root.val)])  # 用一个队列同步记录路径
        results = []

        while que:
            node = que.popleft()
            path = paths.popleft()
            if not node.left and not node.right:
                results.append(path)
            if node.left:
                que.append(node.left)
                paths.append(path + '->' + str(node.left.val))
            if node.right:
                que.append(node.right)
                paths.append(path + '->' + str(node.right.val))
        return results


class Solution(object):
    def binaryTreePaths(self, root):
        if not root: return []
        from collections import deque
        que = [root]
        paths = [str(root.val)]  # 用一个队列同步记录路径
        results = []

        while que:
            node = que.pop()
            path = paths.pop()
            if not node.left and not node.right:
                results.append(path)
            if node.left:
                que.append(node.left)
                paths.append(path + '->' + str(node.left.val))
            if node.right:
                que.append(node.right)
                paths.append(path + '->' + str(node.right.val))
        return results