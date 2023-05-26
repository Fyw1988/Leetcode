# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    def getLength(Node):
        size = 0
        while Node:
            size += 1
            Node = Node.next
        return size

    cur1 = headA
    cur2 = headB
    size1 = getLength(headA)
    size2 = getLength(headB)
    s = max(size1, size2) - min(size1, size2)
    if size2 > size1:
        while s > 0:
            cur2 = cur2.next
            s -= 1
    else:
        while s > 0:
            cur1 = cur1.next
            s -= 1
    while cur1:
        if cur1 == cur2:
            return cur1
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1


# 代码随想录版本
def getIntersectionNode(headA, headB):
    lenA, lenB = 0, 0
    cur = headA
    while cur:         # 求链表A的长度
        cur = cur.next
        lenA += 1
    cur = headB
    while cur:         # 求链表B的长度
        cur = cur.next
        lenB += 1
    curA, curB = headA, headB
    if lenA > lenB:     # 让curB为最长链表的头，lenB为其长度
        curA, curB = curB, curA
        lenA, lenB = lenB, lenA
    for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
        curB = curB.next
    while curA:         #  遍历curA 和 curB，遇到相同则直接返回
        if curA == curB:
            return curA
        else:
            curA = curA.next
            curB = curB.next
    return None