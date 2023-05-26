class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        if not root: return []
        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            result = []
            for i in range(size):
                root = que.popleft()
                result.append(root.val)
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)
            results.append(max(result))
        return results


# 递归
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []

        def helper(root, depth):
            if not root: return []
            if depth == len(results): results.append([])
            results[depth].append(root.val)
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)
        helper(root, 0)
        for i in range(len(results)):
            results[i] = max(results[i])
        return results
