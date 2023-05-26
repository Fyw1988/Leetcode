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