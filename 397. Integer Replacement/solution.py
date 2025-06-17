from functools import cache
class Solution:
    def integerReplacement(self, n: int) -> int:
        
        @cache
        def helper(n):
            if n == 1:
                return 0
            
            if n % 2 == 0:
                return 1 + helper(n // 2)
            
            return 1 + min(helper(n + 1), helper(n - 1))
        
        return helper(n)