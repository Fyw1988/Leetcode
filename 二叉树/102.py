class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        if not root: return results

        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            result = []
            for i in range(size):
                root = que.popleft()
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)
                result.append(root.val)
            results.append(result)
        return results


# 迭代写法
# depth记录节点所处的层数，每进入一次递归，说明层数加一，depth加一
class Solution(object):
    def levelOrder(self, root):
        ans = []
        def helper(root, depth):  # root代表将要添加进ans的节点，depth代表这个节点所处的层数
            if not root:
                return []
            if len(ans) == depth: ans.append([])
            ans[depth].append(root.val)
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)
        helper(root, 0)
        return ans