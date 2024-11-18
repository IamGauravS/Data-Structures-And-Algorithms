class TrieNode:
    def __init__(self):
        self.isWord = 0
        self.data = [None] * 26
        self.isUsed = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currNode = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if currNode.data[ind] is None:
                currNode.data[ind] = TrieNode()
            currNode = currNode.data[ind]
            currNode.isUsed += 1
        currNode.isWord += 1

    def countWordsEqualTo(self, word):
        currNode = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if currNode.data[ind] is None:
                return 0
            currNode = currNode.data[ind]
        return currNode.isWord

    def countWordsStartingWith(self, prefix):
        currNode = self.root
        for ch in prefix:
            ind = ord(ch) - ord('a')
            if currNode.data[ind] is None:
                return 0
            currNode = currNode.data[ind]
        return currNode.isUsed

    def erase(self, word):
        self._eraseHelper(self.root, word, 0)

    def _eraseHelper(self, node, word, index):
        if index == len(word):
            node.isWord -= 1
            node.isUsed -= 1
            return

        ch = word[index]
        ind = ord(ch) - ord('a')

        if node.data[ind] is not None:
            self._eraseHelper(node.data[ind], word, index + 1)
            node.isUsed -= 1

            # Remove the child node if it's no longer in use
            if node.data[ind].isUsed == 0:
                node.data[ind] = None
