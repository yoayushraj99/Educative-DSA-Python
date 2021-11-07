from Doubly_linked_list_implementation import DoublyLinkedList
import time


x = DoublyLinkedList()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.prepend(5)

time_0 = time.time()


def pair_sum(node, sum_val):
    pairs = []
    p = node.head
    while p:
        q = p.next
        while q:
            if p.data + q.data == sum_val:
                pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
            q = q.next
        p = p.next
    return pairs


total_time = time.time() - time_0

print(pair_sum(x, 5))
print(total_time)
