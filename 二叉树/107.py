class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        results = []
        if not root: return results
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
            results.append(result)
        return results[::-1]