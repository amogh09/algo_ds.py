from algo_ds.doubly_linked_node import DNode

class DoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_at_front(self, node):
        if self.head == None:
            self.head = node
            node.next = None
            node.prev = None
            return

        self.head.insert_before(node)
        self.head = node

    def insert_at_end(self, node):
        if self.head == None:
            self.head = node
            node.next = node.prev = None
            return

        self.head.insert_at_end(node)

    def reverse(self):
        if self.head == None:
            return
        last = None
        n = self.head
        while n != None:
            n_prev = n.prev
            n_next = n.next
            n.next = n_prev
            n.prev = n_next
            last = n
            n = n.prev
        self.head = last

    def quick_sort(self):
        if self.head == None:
            return
        last = self.head
        while last.next != None:
            last = last.next
        DNode.quick_sort(self.head, last)

    def merge(l1, l2):
        n1 = l1.head
        n2 = l2.head
        merged_head = DNode.merge(n1, n2)
        return DoublyLinkedList(merged_head)

    def merge_sort(self):
        self.head = DNode.merge_sort(self.head)

    def __str__(self):
        if self.head == None:
            return ""
        ret = ""
        n = self.head
        while n != None:
            ret += str(n) + " -> "
            n = n.next
        ret += "None"
        return ret
