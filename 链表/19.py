class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummyhead = ListNode(next=head)
    fast = dummyhead
    slow = dummyhead
    while n+1 > 0:
        fast = fast.next
        n -= 1
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummyhead.next
