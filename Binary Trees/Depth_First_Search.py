# There are three common ways to traverse a tree in depth-first order:
#
# 1. In-order
# 2. Pre-order
# 3. Post-order

from binary_tree_implementation import tree


# Pre-order Traversal

def pre_order(start, array):
    """Root->Left->Right"""
    if start:
        array.append(start.value)
        array = pre_order(start.left, array)
        array = pre_order(start.right, array)
    return array

# Post-order Traversal

def post_order(start, array):
    """Right->Left->Root"""
    if start:
        array = pre_order(start.left, array)
        array = pre_order(start.right, array)
        array.append(start.value)
    return array

# In-order Traversal

def in_order(start, array):
    """Left->Root->Right"""
    if start:
        array = pre_order(start.left, array)
        array.append(start.value)
        array = pre_order(start.right, array)
    return array

# tree
#           1
#        /    \
#       2      3
#      / \    / \
#     5   6  7   9
#
print(pre_order(tree.root, []))
# [1, 2, 5, 6, 3, 7, 9]
print(post_order(tree.root, []))
# [2, 5, 6, 3, 7, 9, 1]
print(in_order(tree.root, []))
# [2, 5, 6, 1, 3, 7, 9]
