class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n_bin = bin(n)
        return n_bin[2] == "1" and int(n_bin[3:] or 0) == 0