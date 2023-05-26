class Node(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = Node()  # 这个是自己定义的虚拟节点头
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if 0 <= index < self.size:
            current = self.head
            while index > 0:
                current = current.next
                index -= 1
            return current.val
        else:
            return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.size > 0:
            newnode = Node(val)
            newnode.next = self.head
            self.head = newnode
        else:
            self.head.val = val
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.size > 0:
            n = self.size
            current = self.head
            while n > 1:
                current = current.next
                n -= 1
            current.next = Node(val)
        else:
            self.head.val = val
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        elif index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            while index > 1:
                current = current.next
                index -= 1
            newnode = Node(val)
            newnode.next = current.next
            current.next = newnode
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if 0 < index < self.size:
            current = self.head
            while index > 1:
                current = current.next
                index -= 1
            current.next = current.next.next
        elif index == 0:
            self.head = self.head.next
        else:
            return
        self.size -= 1

a = MyLinkedList()
a.addAtHead(7)
a.addAtHead(2)
a.addAtHead(1)
a.addAtIndex(3, 0)
a.deleteAtIndex(2)
a.addAtHead(6)
a.addAtTail(4)
a.get(4)
a.addAtHead(4)
a.addAtIndex(5, 0)
a.addAtHead(6)

n = a.size
current = a.head
print(n)
while n > 0:
    print(current.val)
    current = current.next
    n -= 1


# 代码随想录答案
# 单链表
class Node(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = Node()
        self.size = 0  # 设置一个链表长度的属性，便于后续操作，注意每次增和删的时候都要更新

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while (index):
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        cur = self.head
        while (cur.next):
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return

        node = Node(val)
        pre = self.head
        while (index):
            pre = pre.next
            index -= 1
        node.next = pre.next
        pre.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while (index):
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1