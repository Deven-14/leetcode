class Node:
    def __init__(self):
        self.children = {}
        self.is_word_end = False
        self.word = None

class Trie:
    def __init__(self, words):
        self.root = Node()
        self.add_words(words)
    
    def add_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.is_word_end = True
        node.word = word
    
    def add_words(self, words):
        for word in words:
            self.add_word(word)
    
    def search(self):
        words = []
        
        def helper(node):
            for char in string.ascii_lowercase:
                if char in node.children and node.children[char].is_word_end:
                    words.append(node.children[char].word)
                    helper(node.children[char])
        
        helper(self.root)
        if not words:
            return ""
        words.sort(key=lambda x: (-len(x), x))
        return words[0]


class Solution:
    def longestWord(self, words: list[str]) -> str:
        trie = Trie(words)
        return trie.search()