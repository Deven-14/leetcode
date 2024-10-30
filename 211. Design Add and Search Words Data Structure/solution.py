class Node:

    def __init__(self):
        self.word_end = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - 97

            if not node.children[index]:
                node.children[index] = Node()
            
            node = node.children[index]
        
        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.root
        n = len(word)

        def helper(node, i):
            if not node:
                return False
            
            if i == n:
                return node.word_end
            
            if word[i] != ".":
                index = ord(word[i]) - 97
                node = node.children[index]
                return helper(node, i+1)
                
            for node in node.children:
                if helper(node, i+1):
                    return True
            
            return False
                
        return helper(node, 0)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class Node:

    def __init__(self):
        self.word_end = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - 97

            if not node.children[index]:
                node.children[index] = Node()
            
            node = node.children[index]
        
        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.root
        n = len(word)

        def helper(node, i):
            if i == n:
                return node.word_end
            
            if word[i] != ".":
                index = ord(word[i]) - 97
                node = node.children[index]
                return bool(node) and helper(node, i+1)
                
            for node in node.children:
                if node and helper(node, i+1):
                    return True
            
            return False
                
        return helper(node, 0)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class Node:

    def __init__(self):
        self.word_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.root
        n = len(word)

        def helper(node, i):
            if i == n:
                return node.word_end
            
            if word[i] != ".":
                if word[i] in node.children:
                    node = node.children[word[i]]
                    return helper(node, i+1)
                
                return False
               
            for node in node.children.values():
                if helper(node, i+1):
                    return True
            
            return False
                
        return helper(node, 0)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)