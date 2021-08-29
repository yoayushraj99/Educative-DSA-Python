from Linked_List_Implementation import LinkedList


l1 = LinkedList()
l1.append(1)
l1.append(4)
l1.append(5)

l2 = LinkedList()
l2.append(5)
l2.append(6)
l2.append(7)


def sum(node1, node2):
    curr_node_1 = node1.head
    curr_node_2 = node2.head
    n = 0
    num1 = 0
    num2 = 0

    while curr_node_1 and curr_node_2:
        num1 += (curr_node_1.data*10**n)
        num2 += (curr_node_2.data*10**n)
        n += 1
        curr_node_1 = curr_node_1.next
        curr_node_2 = curr_node_2.next

    total = num1 + num2
    return total


print(sum(l1, l2))


