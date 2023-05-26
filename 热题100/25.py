class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        # 求链表长度
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        nums = l // k  # 翻转次数

        dummyhead = pre = ListNode(next=head)
        cur1, cur2 = None, head
        for _ in range(nums):
            c = k
            while c:
                temp = cur2.next
                cur2.next = cur1
                cur1, cur2 = cur2, temp
                c -= 1
            pre.next.next = cur2
            temp = pre.next
            pre.next = cur1
            pre = temp
            cur1 = pre
        return dummyhead.next
