class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length += 1

    def prepend(self, data):
        if self.head is None:
            self.append(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def add_after_node(self, value, data):
        curr_node = self.head
        while curr_node:
            if curr_node.next is None and curr_node.data == value:
                self.append(data)
                return
            elif curr_node.data == value:
                new_node = Node(data)
                nxt = curr_node.next
                new_node.prev = curr_node
                new_node.next = nxt
                curr_node.next = new_node
                nxt.prev = new_node
                self.length += 1
                return
            curr_node = curr_node.next

    def add_before_node(self, value, data):
        curr_node = self.head
        prev = None
        while curr_node:
            if curr_node.next is None and curr_node.data == value:
                self.prepend(data)
                return
            elif curr_node.data == value:
                new_node = Node(data)
                new_node.prev = prev
                new_node.next = curr_node
                curr_node.prev = new_node
                prev.next = new_node
                self.length += 1
                return
            prev = curr_node
            curr_node = curr_node.next

    def delete_node(self, value):
        curr_node = self.head
        prev = None
        while curr_node:
            if curr_node.data == value:
                nxt = curr_node.next
                prev.next = nxt
                nxt.prev = prev
                self.length -= 1
                return
            prev = curr_node
            curr_node = curr_node.next

    def reverse(self):
        curr_node = self.head
        tmp = None
        while curr_node:
            tmp = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = tmp
            curr_node = curr_node.prev
        if tmp:
            self.head = tmp.prev
