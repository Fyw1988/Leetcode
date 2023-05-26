class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
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
                if root.children:
                    for j in range(len(root.children)):
                        que.append(root.children[j])
            results.append(result)
        return results


# 递归写法
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        results = []
        if not root: return []

        def helper(root, depth):
            if depth == len(results): results.append([])
            results[depth].append(root.val)
            if root.children:
                for i in range(len(root.children)):
                    helper(root.children[i], depth+1)
        helper(root, 0)
        return results