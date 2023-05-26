class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        # 切割数组
        pos = len(nums) / 2
        root = TreeNode(nums[pos])
        root.left = self.sortedArrayToBST(nums[:pos])
        root.right = self.sortedArrayToBST(nums[pos+1:])
        return root


# 迭代
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0: return None
        root = TreeNode()  # 初始化
        nodeSt = [root]
        leftSt = [0]
        rightSt = [len(nums)]

        while nodeSt:
            node = nodeSt.pop()  # 处理根节点
            left = leftSt.pop()
            right = rightSt.pop()
            mid = left + (right - left) // 2
            node.val = nums[mid]

            if left < mid:  # 处理左区间
                node.left = TreeNode()
                nodeSt.append(node.left)
                leftSt.append(left)
                rightSt.append(mid)

            if right > mid + 1:  # 处理右区间
                node.right = TreeNode()
                nodeSt.append(node.right)
                leftSt.append(mid + 1)
                rightSt.append(right)

        return root