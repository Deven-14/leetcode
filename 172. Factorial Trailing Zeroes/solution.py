class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing_zeros = 0
        while n:
            t = n // 5
            trailing_zeros += t
            n = t
        
        return trailing_zeros