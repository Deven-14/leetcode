class Node:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, product):
        node = self.root
        for char in product:
            idx = ord(char) - 97
            if not node.children[idx]:
                node.children[idx] = Node()
            node = node.children[idx]
        
        node.word_end = True
    
    def extend(self, products):
        for product in products:
            self.insert(product)
        
    def top3(self, node, suggestions, suggestion):
        if not node:
            return
        
        if node.word_end:
            suggestions.append(list(suggestion))
        
        for idx, child_node in enumerate(node.children):
            if len(suggestions) >= 3:
                break
            if not child_node:
                continue
            
            suggestion.append(chr(idx + 97))
            self.top3(child_node, suggestions, suggestion)
            suggestion.pop()
        

    def search(self, searchWord):
        suggested_products = []
        node = self.root
        prefix = []

        for char in searchWord:
            idx = ord(char) - 97
            prefix.append(char)
            suggestions = []
            if not node.children[idx]:
                break
            
            self.top3(node.children[idx], suggestions, prefix)
            suggested_products.append(["".join(suggestion) for suggestion in suggestions])
            node = node.children[idx]
        
        suggested_products.extend([[] for _ in range(len(searchWord) - len(suggested_products))])
        
        return suggested_products

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        trie.extend(products)
        return trie.search(searchWord)


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False
        self.words = []

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, product):
        node = self.root
        for char in product:
            idx = ord(char) - 97
            if not node.children[idx]:
                node.children[idx] = Node()
            node = node.children[idx]

            if len(node.words) < 3:
                node.words.append(product)
        
        node.word_end = True
    
    def extend(self, products):
        products.sort()
        for product in products:
            self.insert(product)
        
    def search(self, searchWord):
        suggested_products = []
        node = self.root

        for char in searchWord:
            idx = ord(char) - 97
            if not node.children[idx]:
                break
            
            node = node.children[idx]
            suggestions = node.words
            suggested_products.append(suggestions)
        
        suggested_products.extend([[] for _ in range(len(searchWord) - len(suggested_products))])
        
        return suggested_products

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        trie.extend(products)
        return trie.search(searchWord)


from bisect import bisect_left
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggested_products = []
        idx = 0
        n = len(products)

        for i in range(len(searchWord)):
            sub_search_word = searchWord[:i+1]
            idx = bisect_left(products, sub_search_word, lo=idx)

            suggestions = []
            for j in range(idx, min(idx + 3, n)):
                if sub_search_word == products[j][:i + 1]:
                    suggestions.append(products[j])
            
            suggested_products.append(suggestions)
        
        return suggested_products

