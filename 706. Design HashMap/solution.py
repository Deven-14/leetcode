class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.prime = 10007
        self.dict = [[] for _ in range(self.prime)]

    def _hash(self, key):
        return key % self.prime

    def put(self, key: int, value: int) -> None:
        idx = self.index(key)
        if idx == -1:
            self.dict[self._hash(key)].append(Pair(key, value))
        else:
            self.dict[self._hash(key)][idx].value = value

    def index(self, key) -> int:
        for i, pair in enumerate(self.dict[self._hash(key)]):
            if pair.key == key:
                return i
        return -1

    def get(self, key: int) -> int:
        for pair in self.dict[self._hash(key)]:
            if pair.key == key:
                return pair.value
        return -1

    def remove(self, key: int) -> None:
        idx = self.index(key)
        if idx != -1:
            self.dict[self._hash(key)].pop(idx)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class MyHashMap:

    def __init__(self):
        self.prime = 10007
        self.dict = [[] for _ in range(self.prime)]

    def _hash(self, key):
        return key % self.prime

    def put(self, key: int, value: int) -> None:
        idx = self.index(key)
        if idx == -1:
            self.dict[self._hash(key)].append((key, value))
        else:
            self.dict[self._hash(key)][idx] = (key, value)

    def index(self, key) -> int:
        for i, (pkey, _) in enumerate(self.dict[self._hash(key)]):
            if pkey == key:
                return i
        return -1

    def get(self, key: int) -> int:
        for (pkey, value) in self.dict[self._hash(key)]:
            if pkey == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        idx = self.index(key)
        if idx != -1:
            self.dict[self._hash(key)].pop(idx)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class MyHashMap:

    def __init__(self):
        self.prime = 1007
        self.dict = [[] for _ in range(self.prime)]

    def _hash(self, key):
        return key % self.prime

    def put(self, key: int, value: int) -> None:
        idx = self.index(key)
        if idx == -1:
            self.dict[self._hash(key)].append((key, value))
        else:
            self.dict[self._hash(key)][idx] = (key, value)

    def index(self, key) -> int:
        for i, (pkey, _) in enumerate(self.dict[self._hash(key)]):
            if pkey == key:
                return i
        return -1

    def get(self, key: int) -> int:
        for (pkey, value) in self.dict[self._hash(key)]:
            if pkey == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        idx = self.index(key)
        if idx != -1:
            self.dict[self._hash(key)].pop(idx)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)