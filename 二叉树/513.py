class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            result = []
            for i in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                result.append(node.val)
        return result[0]


# 递归+回溯
class Solution(object):
    def findBottomLeftValue(self, root):
        results = []

        def helper(root, depth):
            if not root: return 0
            if depth == len(results): results.append([])
            results[depth].append(root.val)
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)

        helper(root, 0)
        return results[-1][0]


# 占用空间更小的递归
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.maxdepth = 0
        self.helper(root, 1)

        return self.result

    def helper(self, root, depth):
        if depth > self.maxdepth:
            self.result = root.val
            self.maxdepth = depth
        if root.left:
            self.helper(root.left, depth + 1)
        if root.right:
            self.helper(root.right, depth + 1)