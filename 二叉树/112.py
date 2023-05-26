# 递归 + 回溯
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        self.results = []
        self.helper(root, 0)
        if targetSum in self.results:
            return True
        else:
            return False

    def helper(self, root, sum):
        if not root:
            self.results.append(0)
            return
        sum += root.val
        if not root.left and not root.right:
            self.results.append(sum)
            return
        if root.left:
            self.helper(root.left, sum)
        if root.right:
            self.helper(root.right, sum)


# 迭代 前序遍历
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return False
        sum = {}
        sum[root] = root.val
        stack = [root]

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if sum[node] == targetSum:
                    return True
            if node.left:
                stack.append(node.left)
                sum[node.left] = sum[node] + node.left.val
            if node.right:
                stack.append(node.right)
                sum[node.right] = sum[node] + node.right.val
        return False


# 迭代写法2 栈同步记录
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return False
        sums = [root.val]
        stack = [root]

        while stack:
            node = stack.pop()
            sum = sums.pop()
            if not node.left and not node.right:
                if sum == targetSum:
                    return True
            if node.left:
                stack.append(node.left)
                sums.append(node.left.val + sum)
            if node.right:
                stack.append(node.right)
                sums.append(node.right.val + sum)
        return False
