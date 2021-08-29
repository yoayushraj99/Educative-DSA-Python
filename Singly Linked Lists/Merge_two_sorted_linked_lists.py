from Linked_List_Implementation import LinkedList, Node
from print_singly_linked_list import printList

linked_list_1 = LinkedList()
linked_list_1.append(1)
linked_list_1.append(3)
linked_list_1.append(5)
linked_list_1.append(7)

linked_list_2 = LinkedList()
linked_list_2.append(4)
linked_list_2.append(6)
linked_list_2.append(9)
linked_list_2.append(11)


def merge_sorted(l1, l2):
    if not l1 and not l2:
        return

    if not l1 and l2:
        return l2
    elif not l2 and l1:
        return l1

    if l1.data < l2.data:
        return Node(l1.data, merge_sorted(l1.next, l2))
    else:
        return Node(l2.data, merge_sorted(l2.next, l1))


merged = printList(merge_sorted(linked_list_1.head, linked_list_2.head))
merged.print()
