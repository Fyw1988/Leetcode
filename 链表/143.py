class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        # 定位链表中间
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 翻转链表后半段
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp

        # 重排链表
        while node and node.next:
            temp1 = head.next
            temp2 = node.next
            node.next = head.next
            head.next = node
            head = temp1
            node = temp2