class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if que:
                    cur.next = que[0]
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            cur.next = None

        return root


# O(1)空间复杂度，递归写法
class Solution(object):
    def connect(self, root):
        # 需要注意的是这里需要把递归写在新定义的函数dfs里是因为这题需要有返回值，不然直接把connect作为递归函数即可
        def dfs(node):
            if not node or not node.left: return
            node.left.next=node.right
            if node.next: node.right.next=node.next.left
            dfs(node.left)
            dfs(node.right)

        cur=root
        dfs(cur)
        return root