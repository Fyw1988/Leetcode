class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements1(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    while head and head.val == val:
        head = head.next
    if not head:
        return head
    n = head
    while n.next:
        if n.next.val == val:
            n.next = n.next.next
        else:
            n = n.next
    return head


# 上面那个写法思路基本是对的，就是方法略有错误，错在对于头节点就为待删除节点的链表的处理不正确。新设置一个指向头节点的空节点可以解决这个问题
def removeElements2(head: ListNode, val: int) -> ListNode:
    dummy_head = ListNode(next=head) #添加一个虚拟节点
    cur = dummy_head
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next #删除cur.next节点
        else:
            cur = cur.next
    return dummy_head.next


# 二刷
class Solution(object):
    def removeElements(self, head, val):
        start = ListNode(next=head)
        cur = start
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return start.next


n7 = ListNode(6)
n6 = ListNode(5, n7)
n5 = ListNode(4, n6)
n4 = ListNode(3, n5)
n3 = ListNode(6, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

s = Solution()
print(s.removeElements(n1, 6))
