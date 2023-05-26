class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n),O(1)
class Solution(object):
    def isPalindrome(self, head):
        cur = head
        L = 0
        while cur:
            L += 1
            cur = cur.next
        pos = L // 2
        slow = head
        while pos > 0:
            slow = slow.next
            pos -= 1
        fast = slow.next
        while fast:
            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp
        cur1, cur2 = head, slow
        num = L // 2
        while num > 0:
            if cur1.val != cur2.val:
                return False
            cur1, cur2 = cur1.next, cur2.next
            num -= 1
        return True


# 代码随想录写法
class Solution:
    def isPalindrome(self, head) -> bool:
        fast = slow = head

        # find mid point which including (first) mid point into the first half linked list
        # slow走一步，fast走两步，fast走到末尾的时候slow刚好走到链表中央
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None

        # reverse second half linked list
        # 这个翻转链表写的太巧妙了，真的牛
        while slow:
            slow.next, slow, node = node, slow.next, slow

        # compare reversed and original half; must maintain reversed linked list is shorter than 1st half
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


# n4 = ListNode(1)
# n3 = ListNode(2, n4)
# n2 = ListNode(2, n3)
# n1 = ListNode(1, n2)
# s = Solution()
# print(s.isPalindrome(n1))