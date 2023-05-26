# 迭代 层序遍历
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        from collections import deque
        que = deque([root])
        depth = 0
        while que:
            depth += 1
            size = len(que)
            for i in range(size):
                root = que.popleft()
                if root.children:
                    for node in root.children:
                        que.append(node)
        return depth


# 递归 前序遍历(中左右)
class Solution(object):
    def maxDepth(self, root):
        self.depth = 0
        self.helper(root, 0)
        return self.depth

    def helper(self, root, d):
        if not root: return 0
        if d + 1 > self.depth: self.depth = d + 1
        if root.children:
            for node in root.children:
                self.helper(node, d+1)


# 递归 后序遍历(左右中)
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        maxChildren = []
        for node in root.children:
            maxChildren.append(self.maxDepth(node))
        return max(maxChildren) + 1