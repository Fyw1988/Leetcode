# 代码随想录解法
def detectCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # 如果相遇
        if slow == fast:
            p = head
            q = slow
            while p != q:
                p = p.next
                q = q.next
            # 你也可以return q
            return p

    return None


# 按照下面的写法会超时，其实由于每个while循环都会判断p与q是否相等，因此while循环里的if语句完全是多余的，相当于多判断了一次
# 但是这样理论上来说运算量也不会大太多，不太理解为什么会超时
def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            p, q = head, fast
            while p != q:
                p = p.next
                q = q.next
                if p == q:
                    return p
    return None