import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = math.ceil(len(b) / len(a))
        return n if b in a * n else (n + 1 if b in a * (n + 1) else -1)