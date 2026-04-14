
# ! TIME LIMIT EXCEEDED

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        
        def is_word_present(i, j, word, wi, wl, visited):
            if wi == wl:
                return True
            
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or word[wi] != board[i][j]:
                return False

            visited.add((i, j))

            for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if is_word_present(x, y, word, wi + 1, wl, visited):
                    return True
            
            visited.remove((i, j))
            return False
        
        def search_word(word):
            l = len(word)
            for i in range(n):
                for j in range(m):
                    if word[0] == board[i][j]:
                        if is_word_present(i, j, word, 0, l, set()):
                            return True

            return False

        words_in_board = []
        for word in words:
            if search_word(word):
                words_in_board.append(word)
        
        return words_in_board


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False
        self.word = None
        self.references = 0

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.insert_words(words)
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.references += 1
        
        node.is_word_end = True
        node.word = word
    
    def insert_words(self, words):
        for word in words:
            self.insert(word)
    
    def search_in_board(self, board):
        n, m = len(board), len(board[0])
        found = []

        def remove_references(word):
            node = self.root

            for char in word:
                node = node.children[char]
                node.references -= 1

        def backtrack(i, j, node, visited):
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or board[i][j] not in node.children:
                return
            
            node = node.children[board[i][j]]
            
            if node.is_word_end:
                found.append(node.word)
                remove_references(node.word)
                node.is_word_end = False
            
            if node.references == 0:
                return

            visited.add((i, j))
            for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                backtrack(x, y, node, visited)
            visited.remove((i, j))
        
        for i in range(n):
            for j in range(m):
                backtrack(i, j, self.root, set())
        
        return found


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie(words)
        return t.search_in_board(board)



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.references = 0

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.insert_words(words)
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.references += 1
        
        node.word = word
    
    def insert_words(self, words):
        for word in words:
            self.insert(word)
    
    def search_in_board(self, board):
        n, m = len(board), len(board[0])
        found = []

        def remove_references(word):
            node = self.root

            for char in word:
                node = node.children[char]
                node.references -= 1

        def backtrack(i, j, node):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] not in node.children:
                return
            
            char = board[i][j]
            node = node.children[char]
            
            if node.word:
                found.append(node.word)
                remove_references(node.word)
                node.word = None
            
            if node.references == 0:
                return

            board[i][j] = '#'
            for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                backtrack(x, y, node)
            board[i][j] = char
        
        node = self.root
        for i in range(n):
            for j in range(m):
                if board[i][j] in node.children:
                    backtrack(i, j, node)
        
        return found


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie(words)
        return t.search_in_board(board)



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.insert_words(words)
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.word = word
    
    def insert_words(self, words):
        for word in words:
            self.insert(word)
    
    def search_in_board(self, board):
        n, m = len(board), len(board[0])
        found = []

        def backtrack(i, j, parent):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] not in parent.children:
                return
            
            char = board[i][j]
            node = parent.children[char]
            
            if node.word:
                found.append(node.word)
                node.word = None

            board[i][j] = '#'
            for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                backtrack(x, y, node)
            board[i][j] = char

            if not node.children: # no more children
                del parent.children[char]
        
        node = self.root
        for i in range(n):
            for j in range(m):
                if board[i][j] in node.children:
                    backtrack(i, j, node)
        
        return found


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie(words)
        return t.search_in_board(board)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.insert_words(words)
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.word = word
    
    def insert_words(self, words):
        for word in words:
            self.insert(word)
    
    def search_in_board(self, board):
        n, m = len(board), len(board[0])
        found = []

        def backtrack(i, j, parent):
            char = board[i][j]
            if board[i][j] not in parent.children:
                return
            node = parent.children[char]
            
            if node.word:
                found.append(node.word)
                node.word = None

            board[i][j] = '#'
            
            if i > 0: backtrack(i - 1, j, node)
            if i < n-1: backtrack(i + 1, j, node)
            if j > 0: backtrack(i, j - 1, node)
            if j < m-1: backtrack(i, j + 1, node)

            board[i][j] = char

            if not node.children: # no more children, pruning
                del parent.children[char]
        
        node = self.root
        for i in range(n):
            for j in range(m):
                if board[i][j] in node.children:
                    backtrack(i, j, node)
        
        return found


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie(words)
        return t.search_in_board(board)
