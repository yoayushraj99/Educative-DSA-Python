from Linked_List_Implementation import LinkedList
from print_singly_linked_list import printList


l1 = LinkedList()
l1.append('A')
l1.append('B')
l1.append('C')
l1.append('D')


def rotate(node, k):
    p = node.head
    count = 0
    while p and count < k:
        p = p.next
        count += 1
    q = node.tail
    q.next = node.head
    node.head = p.next
    p.next = None


rotate(l1, 2)
printList(l1.head).print()
