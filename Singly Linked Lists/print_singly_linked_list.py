class printList:
    def __init__(self, node=None):
        self.node = node

    def print(self):
        curr_node = self.node
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
