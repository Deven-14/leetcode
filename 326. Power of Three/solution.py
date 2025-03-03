import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        x = math.log10(n) / math.log10(3)
        return x == int(x)

# logb(a) = logc(a) / logc(b)
# log10 is accurate, log(x, base) gives approx

# another solution with loops

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1
