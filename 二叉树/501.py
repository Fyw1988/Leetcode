class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 迭代 中序遍历
class Solution(object):
    def findMode(self, root):
        ans = []
        fre = 1
        fremax = 1
        pre = None
        cur = root
        stack = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and pre.val == cur.val:
                    fre += 1
                else:
                    fre = 1
                if fre == fremax:
                    ans.append(cur.val)
                if fre > fremax:
                    ans = [cur.val]
                    fremax = fre

                pre = cur
                cur = cur.right

        return ans


# 递归
class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root):
        if not root: return None
        self.search_BST(root)
        return self.result

    def search_BST(self, cur):
        if not cur: return None
        self.search_BST(cur.left)
        # 第一个节点
        if not self.pre:
            self.count = 1
        # 与前一个节点数值相同
        elif self.pre.val == cur.val:
            self.count += 1
            # 与前一个节点数值不相同
        else:
            self.count = 1
        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)

        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]  # 清空self.result，确保result之前的的元素都失效

        self.search_BST(cur.right)