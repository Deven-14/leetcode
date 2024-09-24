class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(int(i) for i in bin(n)[2:])

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for i in bin(n):
            if i == "1":
                c += 1
        return c

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for _ in range(32):
            if n & 1 == 1:
                c += 1
            n = n >> 1
        return c

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            if n & 1 == 1:
                c += 1
            n = n >> 1
        return c

