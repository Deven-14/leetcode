class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        first, second = 0, 1
        for _ in range(2, n+1):
            first, second = second, first+second
        
        return second


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        first, second = 0, 1
        for _ in range(2, n+1):
            first, second = second, first+second
        
        return second