# A binary search tree is a tree data structure in which nodes are arranged according to the BST property which is as follows:
#
# The value of the left child of any node in a binary search tree will be less than whatever value we have in that node, and
# the value of the right child of a node will be greater than the value in that node.

# Note: If there aren’t exactly two children, the reference to the non-existent child will contain null value.

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        curr_node = self.root
        new_node = Node(value)
        while curr_node:
            if value > curr_node.data:
                # Go right
                if not curr_node.right:
                    curr_node.right = new_node
                    return
                curr_node = curr_node.right
            else:
                # Go left
                if not curr_node.left:
                    curr_node.left = new_node
                    return
                curr_node = curr_node.left

    def search(self, value):
        curr_node = self.root
        while curr_node:
            if value < curr_node.data:
                curr_node = curr_node.left
            elif curr_node.data == value:
                return "Found Yaa!"
            else:
                curr_node = curr_node.right
        return "Try something else 😑."

    def print_bst(self, node, arr):
        if node:
            arr.append(node.data)
            arr = self.print_bst(node.left, arr)
            arr = self.print_bst(node.right, arr)
        return arr


bst = BinarySearchTree(5)
bst.insert(10)
bst.insert(12)
bst.insert(9)
bst.insert(4)
bst.insert(50)
print(bst.print_bst(bst.root, []))
print(bst.search(51))
