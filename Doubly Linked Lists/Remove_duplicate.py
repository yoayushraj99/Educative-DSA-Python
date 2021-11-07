from Doubly_linked_list_implementation import DoublyLinkedList

x = DoublyLinkedList()
x.append(2)
x.append(2)
x.append(2)
x.append(2)
x.prepend(2)


def remove_dup(node):
    dict = {}
    prev = None
    curr_node = node.head
    while curr_node:
        if curr_node.data in dict:
            nxt = curr_node.next
            prev.next = nxt
            if nxt:
                nxt.prev = prev
            node.length -= 1
        else:
            dict[curr_node.data] = 1
            prev = curr_node
        curr_node = curr_node.next


remove_dup(x)
x.print_list()
