class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 关键在于虚拟头+双指针
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    res = ListNode(next=head)
    cur = res
    fast = head
    while fast and fast.next:
        temp = fast.next.next
        cur.next = fast.next
        fast.next.next = fast
        fast.next = temp
        cur = fast
        fast = temp
    return res.next


# 代码随想录简洁写法
# 不预先定义两个指针，把需要判断的指针留在while循环里定义，这样就可以省一句if判断语句
def swapPairs(self, head: ListNode) -> ListNode:
    res = ListNode(next=head)
    pre = res

    # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
    while pre.next and pre.next.next:
        cur = pre.next
        post = pre.next.next

        # pre，cur，post对应最左，中间的，最右边的节点
        cur.next = post.next
        post.next = cur
        pre.next = post

        pre = pre.next.next
    return res.next