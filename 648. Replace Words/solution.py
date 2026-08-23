class Node:
    def __init__(self):
        self.children = {}
        self.word_end = False
        self.word = None
    
class Trie:
    def __init__(self, words):
        self.root = Node()
        self.insert_all(words)

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.word_end = True
        node.word = word

    def insert_all(self, words):
        for word in words:
            self.insert(word)
    
    def prefix(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
            if node.word_end:
                return node.word
        
        return None
            

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie(dictionary)
        new_sentence = []

        for word in sentence.split():
            root = trie.prefix(word)
            new_sentence.append(
                root if root != None else word
            )
        
        return " ".join(new_sentence)





class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        char_to_roots = defaultdict(list)
        for word in dictionary:
            char_to_roots[word[0]].append(word)
        
        new_sentence = []
        for word in sentence.split():
            roots = char_to_roots[word[0]]
            for root in roots:
                if word.startswith(root):
                    new_sentence.append(root)
                    break
            else:
                new_sentence.append(word)
        
        return " ".join(new_sentence)





class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        char_to_roots = defaultdict(list)
        for word in dictionary:
            char = word[0]
            for root in char_to_roots[char]:
                if word.startswith(root):
                    break
            else:
                char_to_roots[char].append(word)
        
        new_sentence = []
        for word in sentence.split():
            roots = char_to_roots[word[0]]
            for root in roots:
                if word.startswith(root):
                    new_sentence.append(root)
                    break
            else:
                new_sentence.append(word)
        
        return " ".join(new_sentence)



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        char_to_roots = defaultdict(list)
        for word in dictionary:
            char = word[0]
            if not char_to_roots[char] or not word.startswith(char_to_roots[char][-1]):
                char_to_roots[char].append(word)
        
        new_sentence = []
        for word in sentence.split():
            roots = char_to_roots[word[0]]
            for root in roots:
                if word.startswith(root):
                    new_sentence.append(root)
                    break
            else:
                new_sentence.append(word)
        
        return " ".join(new_sentence)


import bisect
from collections import defaultdict

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        char_to_roots = defaultdict(list)
        for word in dictionary:
            char = word[0]
            if not char_to_roots[char] or not word.startswith(char_to_roots[char][-1]):
                char_to_roots[char].append(word)
        

        def root(word):
            if word[0] not in char_to_roots:
                return word

            char = word[0]
            arr = char_to_roots[char]
            idx = bisect.bisect_right(arr, word)
            idx -= 1
            if idx < 0 or not word.startswith(arr[idx]):
                return word
            
            return arr[idx]
        
        return " ".join(root(word) for word in sentence.split())