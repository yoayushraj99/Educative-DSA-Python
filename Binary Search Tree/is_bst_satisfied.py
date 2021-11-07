# The BST property states that every node on the right subtree has to be larger than the current node, and
# every node on the left subtree has to be smaller than the current node.

from binary_search_tree_implementation import BinarySearchTree


def is_bst_satisfied(node):
    def check(node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True

        val = node.data
        if val <= lower or val >= upper:
            return False
        if not check(node.right, val, upper):
            return False
        if not check(node.left, lower, val):
            return False

        return True

    return check(node)


