class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 707
# class MyLinkedList(object):
#
#     def __init__(self):
#         self.dummyhead = Node()
#         self.size = 0
#
#     def get(self, index):
#         """
#         :type index: int
#         :rtype: int
#         """
#         cur = self.dummyhead.next
#         i = 0
#         while cur:
#             if i == index:
#                 return cur.val
#             else:
#                 i += 1
#                 cur = cur.next
#         return -1
#
#     def addAtHead(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         newnode = Node(val=val, next=self.dummyhead.next)
#         self.dummyhead.next = newnode
#         self.size += 1
#
#     def addAtTail(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         cur = self.dummyhead
#         while cur.next:
#             cur = cur.next
#         cur.next = Node(val=val)
#         self.size += 1
#
#     def addAtIndex(self, index, val):
#         """
#         :type index: int
#         :type val: int
#         :rtype: None
#         """
#         if index > self.size: return
#         cur = self.dummyhead
#         i = 0
#         while cur:
#             if i == index:
#                 cur.next = Node(val=val, next=cur.next)
#                 break
#             i += 1
#             cur = cur.next
#         self.size += 1
#
#     def deleteAtIndex(self, index):
#         """
#         :type index: int
#         :rtype: None
#         """
#         if index >= self.size: return
#         cur = self.dummyhead
#         i = 0
#         while cur.next:
#             if i == index:
#                 cur.next = cur.next.next
#                 break
#             else:
#                 cur = cur.next
#                 i += 1
#         self.size -= 1


# 206
# class Solution(object):
#     def reverseList(self, head):
#         slow = None
#         fast = head
#         while fast:
#             temp = fast.next
#             fast.next = slow
#             slow = fast
#             fast = temp
#         return slow


# 24
# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         dummyhead = Node(next=head)
#         if not head: return
#         slow, fast, temp = head, head.next, dummyhead
#         while slow and fast:
#             slow.next = fast.next
#             fast.next = slow
#             temp.next = fast
#             if slow.next:
#                 temp = slow
#                 fast = slow.next.next
#                 slow = slow.next
#             else:
#                 return dummyhead.next
#         return dummyhead.next


# 142
# class Solution(object):
#     def detectCycle(self, head):
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 cur1 = head
#                 cur2 = slow
#                 while cur1 != cur2:
#                     cur1 = cur1.next
#                     cur2 = cur2.next
#                 return cur1
#         return None