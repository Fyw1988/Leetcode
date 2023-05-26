class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 寻找根节点
        root = TreeNode()
        root.val = max(nums)

        # 寻找切割位置
        pos = nums.index(root.val)
        # 切割，递归
        numsleft = nums[:pos]
        numsright = nums[pos+1:]
        root.left = self.constructMaximumBinaryTree(numsleft)
        root.right = self.constructMaximumBinaryTree(numsright)

        return root