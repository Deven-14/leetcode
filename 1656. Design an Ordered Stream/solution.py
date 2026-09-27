class OrderedStream:

    def __init__(self, n: int):
        self.map = [None] * (n + 1)
        self.idx = 1
        self.n = n + 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.map[idKey] = value
        ans = []
        while self.idx < self.n and self.map[self.idx]:
            ans.append(self.map[self.idx])
            self.idx += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


class OrderedStream:

    def __init__(self, n: int):
        self.map = [None] * (n + 2)
        self.idx = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.map[idKey] = value
        ans = []
        while self.map[self.idx]:
            ans.append(self.map[self.idx])
            self.idx += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


class OrderedStream:

    def __init__(self, n: int):
        self.map = [None] * (n + 2)
        self.idx = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.map[idKey] = value
        ans = []
        i = self.idx
        while self.map[i]:
            ans.append(self.map[i])
            i += 1
        self.idx = i
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

