# 迭代（层序遍历）
# 数据结构从队列变成栈写法差不多，只是遍历顺序变了，从BFS变为DFS
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        from collections import deque
        que = deque([root])
        result = 0

        while que:
            node = que.popleft()
            if node.left:
                if node.left.left or node.left.right:
                    que.append(node.left)
                else:
                    result += node.left.val
            if node.right:
                if node.right.left or node.right.right:
                    que.append(node.right)
        return result


# 递归写法（后序遍历）
class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)  # 右
        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaf_val = root.left.val

        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum  # 中


class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaf_val = root.left.val
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)  # 右
        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum  # 中