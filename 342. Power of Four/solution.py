from math import log10
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        x = log10(n) / log10(4)
        return x == int(x)


# return (n & n - 1) == 0 and (n - 1) % 3 == 0