# This is also Known as Level-Order traversal

from binary_tree_implementation import tree


def levelorder_traversal(node):
    array = []
    queue = [node]
    while len(queue) > 0:
        node = queue.pop(0)
        array.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return array

# tree
#           1
#        /    \
#       2      3
#      / \    / \
#     5   6  7   9
#
print(levelorder_traversal(tree.root))
# [1, 2, 3, 5, 6, 7, 9]
