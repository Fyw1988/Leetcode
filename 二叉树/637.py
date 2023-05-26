class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        results = []
        if not root: return []
        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            result = 0
            for i in range(size):
                root = que.popleft()
                result += root.val
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)
            results.append(float(result)/size)
        return results
