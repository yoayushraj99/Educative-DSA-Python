# The height of a node is the number of edges on the longest path between that node and a leaf. The height of a leaf node is 0.
# Recursively defined, the height of a node is one greater than the max of its right and left children’s height.

#          1
#        /   \ 2
#       2      3
#    1 / \    / \
#     5   6  7   9
#     0

from binary_tree_implementation import tree


def height(node):
    if node is None:
        return -1
    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


print(height(tree.root))
