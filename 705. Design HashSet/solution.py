class MyHashSet:

    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:

    def __init__(self):
        self.prime = 1009
        self.set = [[] for _ in range(self.prime)]
    
    def _hash(self, key):
        return key % self.prime

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set[self._hash(key)].append(key)

    def remove(self, key: int) -> None:
        try:
            idx = self.set[self._hash(key)].index(key)
            self.set[self._hash(key)].pop(idx)
        except ValueError:
            pass

    def contains(self, key: int) -> bool:
        try:
            self.set[self._hash(key)].index(key)
            return True
        except ValueError:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:

    def __init__(self):
        self.prime = 10007
        self.set = [[] for _ in range(self.prime)]
    
    def _hash(self, key):
        return key % self.prime

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set[self._hash(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set[self._hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.set[self._hash(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:

    def __init__(self):
        self.prime = 10007
        self.set = [[] for _ in range(self.prime)]

    def add(self, key: int) -> None:
        hash = key % self.prime
        if key not in self.set[hash]:
            self.set[hash].append(key)

    def remove(self, key: int) -> None:
        hash = key % self.prime
        if key in self.set[hash]:
            self.set[hash].remove(key)

    def contains(self, key: int) -> bool:
        hash = key % self.prime
        return key in self.set[hash]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# * this can also be done using linked lists to avoid clashes instead of list()
# * we can also use BST instead of linked lists to reduce to search and delete time to O(logn) from O(N), this will also increase insert time from O(1) to O(logn)
