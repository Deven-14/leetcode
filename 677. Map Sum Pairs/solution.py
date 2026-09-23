class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.keys = {}
    
    def insert(self, key, val):
        node = self.root
        existing_key = key in self.keys
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if existing_key:
                node.val -= self.keys[key]
            node.val += val
        self.keys[key] = val
    
    def search(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.val

class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)