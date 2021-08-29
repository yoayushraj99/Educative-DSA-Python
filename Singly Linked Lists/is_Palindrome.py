from Linked_List_Implementation import LinkedList

l1 = LinkedList()
l1.append('r')
l1.append('a')
l1.append('d')
l1.append('a')
l1.append('r')

l2 = LinkedList()
l2.append('A')
l2.append('B')
l2.append('C')

# Using String


def is_palindrome(node):
    string = ''
    curr_node = node.head
    while curr_node:
        string += curr_node.data
        curr_node = curr_node.next
    return string == string[::-1]


print(is_palindrome(l1))
print(is_palindrome(l2))
