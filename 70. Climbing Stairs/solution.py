class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        stairs = [0] * n
        stairs[0] = 1
        stairs[1] = 2

        for i in range(2, n):
            stairs[i] = stairs[i-1] + stairs[i-2]
        
        return stairs[n-1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a, b = 1, 2 # we don't need before values, just the last value, so use variables instead of arrays
        for i in range(2, n):
            a, b = b, a + b
        
        return b