
# ! Memory limit exceeded

from random import randint
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.indexes = [[i, j] for i in range(m) for j in range(n)]

    def flip(self) -> List[int]:
        index = randint(0, len(self.indexes) - 1)
        val = self.indexes[index]
        self.indexes[index] = self.indexes[-1]
        self.indexes.pop()
        return val

    def reset(self) -> None:
        self.indexes = [[i, j] for i in range(self.m) for j in range(self.n)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()


from random import randint
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total_eles = m * n
        self.eles = self.total_eles
        self.indexes = {}

    def flip(self) -> List[int]:
        self.eles -= 1
        index = randint(0, self.eles)
        val = self.indexes[index] if index in self.indexes else index
        self.indexes[index] = self.indexes[self.eles] if self.eles in self.indexes else self.eles
        return [val // self.n, val % self.n]

    def reset(self) -> None:
        self.eles = self.total_eles
        self.indexes = {}
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()


from random import randint
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total_eles = m * n
        self.eles = self.total_eles
        self.indexes = {}

    def flip(self) -> List[int]:
        self.eles -= 1
        index = randint(0, self.eles)
        val = self.indexes.get(index, index)
        self.indexes[index] = self.indexes.get(self.eles, self.eles)
        return [val // self.n, val % self.n]

    def reset(self) -> None:
        self.eles = self.total_eles
        self.indexes = {}
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()


from random import randint
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total_eles = m * n
        self.eles = self.total_eles
        self.indexes = {}

    def flip(self) -> List[int]:
        self.eles -= 1
        index = randint(0, self.eles)
        val = self.indexes.get(index, index)
        self.indexes[index] = self.indexes.get(self.eles, self.eles)
        return [val // self.n, val % self.n]

    def reset(self) -> None:
        self.eles = self.total_eles
        self.indexes.clear()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()