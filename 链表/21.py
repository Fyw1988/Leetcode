class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1
        cur2 = list2
        ans = ListNode()
        dummyhead = ListNode(next=ans)
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                ans.next = ListNode(cur1.val)
                ans = ans.next
                while cur1.next and cur1.val == cur1.next.val:
                    cur1 = cur1.next
                    ans.next = ListNode(cur1.val)
                    ans = ans.next
                cur1 = cur1.next
            else:
                ans.next = ListNode(cur2.val)
                ans = ans.next
                while cur2.next and cur2.val == cur2.next.val:
                    cur2 = cur2.next
                    ans.next = ListNode(cur2.val)
                    ans = ans.next
                cur2 = cur2.next
        if cur1: ans.next = cur1
        if cur2: ans.next = cur2
        return dummyhead.next.next

a1 = ListNode(9)
a2 = ListNode(9, a1)
a3 = ListNode(1, a2)
a4 = ListNode(-4, a3)
a5 = ListNode(-6, a4)
a6 = ListNode(-9, a5)
a7 = ListNode(-10, a6)

b1 = ListNode(8)
b2 = ListNode(8, b1)
b3 = ListNode(7, b2)
b4 = ListNode(0, b3)
b5 = ListNode(-3, b4)
b6 = ListNode(-5, b5)

s = Solution()
c = s.mergeTwoLists(a7, b6)
print(c)