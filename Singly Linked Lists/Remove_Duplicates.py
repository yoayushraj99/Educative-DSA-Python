from Linked_List_Implementation import LinkedList
from print_singly_linked_list import printList

l1 = LinkedList()
l1.append(1)
l1.append(4)
l1.append(5)
l1.append(2)
l1.append(5)
l1.append(9)


def remove_duplicates(l):
    curr_node = l.head
    dup_dict = dict()
    prev = None
    while curr_node:
        if curr_node.data in dup_dict:
            # Remove Node
            prev.next = curr_node.next
        else:
            # Have not Encountered Element before
            dup_dict[curr_node.data] = 1
            prev = curr_node
        curr_node = prev.next

    return


remove_duplicates(l1)
printList(l1.head).print()
