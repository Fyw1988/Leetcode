class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 冒泡，O(n^2)，超时
class Solution(object):
    def sortList(self, head):
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        for passnum in range(n-1, 0, -1):
            exchanges = True
            cur1, cur2 = head, head.next
            while passnum > 0:
                if cur2.val < cur1.val:
                    cur1.val, cur2.val = cur2.val, cur1.val
                    exchanges = False
                cur1, cur2 = cur1.next, cur2.next
                passnum -= 1
            if exchanges: break
        return head


# 归并排序
class Solution(object):
    def sortList(self, head):
        # 归
        def sortFunc(head, tail):
            if not head:
                return head
            if head.next == tail:  # tail是不处理的，排序head到tail的前一个节点
                head.next = None
                return head
            slow, fast = head, head
            while fast != tail:
                slow, fast = slow.next, fast.next
                if fast != tail:
                    fast = fast.next
            return merge(sortFunc(head, slow), sortFunc(slow, tail))
        # 并
        def merge(head1, head2):
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

        return sortFunc(head, None)


# 归并排序，自底向上实现，空间O(1)
class Solution:
    def sortList(self, head):
        def merge(head1, head2):
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head
        # 计算链表长度
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        # 按照子串长度为1、2、4...进行合并
        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                # head1代表第一个长为subLength的子串的头节点
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                # head2代表第二个长为subLength的子串的头节点
                head2 = curr.next
                curr.next = None  # 把待合并的第一个子串与第二个子串切割
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:   # 如果curr为None，代表待合并的第二个子串已经为None
                    succ = curr.next  # succ记录下一个子串的头节点，为下个while循环的归并做准备
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next


class Solution:
    def sortList(self, head):
        # 求链表长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # 循环，自底向上归并
        subLength = 1
        dummy = ListNode(next=head)
        while subLength < length:
            pre, cur = dummy, dummy.next
            while cur:
                # 切割第一段子串
                head1 = cur
                for _ in range(1, subLength):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                head2 = cur.next
                cur.next = None
                cur = head2
                for _ in range(1, subLength):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                succ = None  # 记录下一段子链表头节点
                if cur:
                    succ = cur.next
                    cur.next = None
                cur = succ
                merged = self.merge(head1, head2)
                pre.next = merged
                while pre and pre.next:
                    pre = pre.next
                pre.next = cur
            subLength *= 2
        return dummy.next

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