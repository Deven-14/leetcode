class Node:

    def __init__(self):
        self.word_end = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - 97

            if not node.children[index]:
                node.children[index] = Node()
            
            node = node.children[index]
        
        node.word_end = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - 97
            node = node.children[index]
            if not node:
                return False
        
        return node.word_end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - 97
            node = node.children[index]
            if not node:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)