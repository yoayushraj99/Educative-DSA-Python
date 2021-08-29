class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def len(self):
        print(self.length)
        return self.length

    def append(self, value):
        self.length += 1
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            return
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = self.tail.next

    def prepend(self, value):
        self.length += 1
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, position, value):
        self.length += 1
        if position == 0:
            self.prepend(value)
            return
        new_node = Node(value)
        current_node = self.head
        while position > 1:
            current_node = current_node.next
            position -= 1
        new_node.next = current_node.next
        current_node.next = new_node

    def deletion_by_value(self, value):
        self.length -= 1
        current_node = self.head
        prev_node = None
        while current_node.data != value:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = current_node.next

    def deletion_by_position(self, position):
        self.length -= 1
        current_node = self.head
        prev_node = None
        while position > 0:
            prev_node = current_node
            current_node = current_node.next
            position -= 1
        prev_node.next = current_node.next

    def swap_nodes(self, value_1, value_2):
        if value_1 == value_2:
            return
        current_node_1 = self.head
        while current_node_1 and current_node_1.data != value_1:
            current_node_1 = current_node_1.next

        current_node_2 = self.head
        while current_node_2 and current_node_2.data != value_2:
            current_node_2 = current_node_2.next

        if current_node_1 and current_node_2:
            current_node_1.data, current_node_2.data = current_node_2.data, current_node_1.data

        return

    def reverse(self):
        current_node = self.head
        prev = None
        while current_node:
            nxt = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = nxt
        self.head = prev

    def print_nth_from_last(self, n):
        total_length = self.length
        current_node = self.head

        while current_node:
            if total_length == n:
                print(current_node.data)
                return
            total_length -= 1
            current_node = current_node.next

        return

    def count_occurrences(self, value, node):
        if not node:
            return 0
        if node.data == value:
            return 1+self.count_occurrences(value, node.next)
        else:
            return self.count_occurrences(value, node.next)


