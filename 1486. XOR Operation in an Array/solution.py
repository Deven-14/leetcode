class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for j in range(start, start + 2 * n, 2):
            result ^= j
        return result
