class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, base=2)
        b = int(b, base=2)
        return bin(a+b)[2:]