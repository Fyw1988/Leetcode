class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    num = 0
    ans = ListNode()
    dummyhead = ListNode(next=ans)
    cur1 = l1
    cur2 = l2
    while cur1 and cur2:
        ans.next = ListNode((cur1.val + cur2.val + num) % 10)
        ans = ans.next
        num = (cur1.val + cur2.val + num) // 10
        cur1 = cur1.next
        cur2 = cur2.next
        if cur1 and cur2:
            continue
        elif cur1 and not cur2:
            ans.next = cur1
            ans = ans.next
        elif cur2 and not cur1:
            ans.next = cur2
            ans = ans.next
        else:
            if num:
                ans.next = ListNode(num)
            return dummyhead.next.next
        while ans.next:
            val = ans.val
            ans.val = (ans.val + num) % 10
            num = (val + num) // 10
            ans = ans.next
        val = ans.val
        ans.val = (ans.val + num) % 10
        num = (val + num) // 10
        if num: ans.next = ListNode(num)
    return dummyhead.next.next


# 上面分类讨论了半天，写了一个多小时
# 下面是力扣评论区给的python代码，我真的太菜了
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = 0

        while carry or l1 or l2:
            val = carry

            if l1: l1, val = l1.next, l1.val + val
            if l2: l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)
            # 这行连等等价于：
            # curr.next  = ListNode(val)
            # curr = curr.next

        return head.next


class Solution3(object):
    def addTwoNumbers(self, l1, l2):
        head = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val=val)
            cur = cur.next
        return head.next


a1 = ListNode(9)
a2 = ListNode(9, a1)
a3 = ListNode(9, a2)
a4 = ListNode(9, a3)
a5 = ListNode(9, a4)
a6 = ListNode(9, a5)
a7 = ListNode(9, a6)


b1 = ListNode(9)
b2 = ListNode(9, b1)
b3 = ListNode(9, b2)
b4 = ListNode(9, b3)

s = Solution3()
c = s.addTwoNumbers(a7, b4)
print(c.val)
print(c.next.val)
print(c.next.next.val)
print(c.next.next.next.val)
print(c.next.next.next.next.val)
print(c.next.next.next.next.next.val)
print(c.next.next.next.next.next.next.val)
print(c.next.next.next.next.next.next.next.val)