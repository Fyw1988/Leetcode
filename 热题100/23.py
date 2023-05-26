class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists: return None
        while len(lists) > 1:
            nums = len(lists) // 2
            while nums:
                head1 = lists.pop()
                head2 = lists.pop()
                head = self.merge(head1, head2)
                lists.insert(0, head)
                nums -= 1
        return lists[0]

    def merge(self, head1, head2):
        dummy = cur = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 if head1 else head2
        return dummy.next