class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = None  # 虚拟节点
    fast = head
    while fast:
        temp = fast.next
        fast.next = cur
        cur = fast
        fast = temp
    return cur

# 代码随想录写法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre


# 另一种翻转思路
class Solution2(object):
    def reverseList(self, head):
        if not head: return
        dummyhead = ListNode(next=head)
        pre, cur = dummyhead, head
        while cur.next:
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummyhead.next


class Solution3(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = None  # 虚拟节点
        fast = head
        while fast:
            fast.next, fast, cur = cur, fast.next, fast
            # cur, fast, fast.next = fast, fast.next, cur
        return cur


s1 = ListNode(val=5)
s2 = ListNode(val=4,next=s1)
s3 = ListNode(val=3,next=s2)
s4 = ListNode(val=2,next=s3)
s5 = ListNode(val=1,next=s4)
s = Solution2()
print(s.reverseList(s5))
