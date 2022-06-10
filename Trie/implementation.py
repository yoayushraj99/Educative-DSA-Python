class TrieNode:
    def __init__(self, ch):
        self.data = ch
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def _charToIndex(self, ch):
        # Private helper function to convert character to ASCII index
        return ord(ch)-ord('a')

    def insertUtil(self, root, word):
        # Base case
        if len(word) == 0:
            root.isEndOfWord = True
            return

        index = self._charToIndex(word[0])
        # If present
        if root.children[index] is not None:
            child = root.children[index]
        else:
            # If absent
            child = TrieNode(word[0])
            root.children[index] = child

        # Recursion
        self.insertUtil(child, word[1:])

    def insert(self, word: str) -> None:
        self.insertUtil(self.root, word)

    def searchUtil(self, root, word):
        # Base Case
        if len(word) == 0:
            return root.isEndOfWord

        index = self._charToIndex(word[0])
        # Present
        if root.children[index] is not None:
            child = root.children[index]
        else:
            return False
        self.searchUtil(child, word[1:])

    def search(self, word: str) -> bool:
        return self.searchUtil(self.root, word)

    def startsWithUtil(self, root, word):
        if len(word) == 0:
            return True

        index = self._charToIndex(word[0])
        # present
        if root.children[index] is not None:
            child = root.children[index]
        else:
            return False
        self.startsWithUtil(child, word[1:])

    def startWith(self, prefix: str) -> bool:
        return self.startsWithUtil(self.root, prefix)