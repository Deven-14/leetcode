from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        @cache
        def dp(i, j):
            if j == m:
                return 1
            
            if i == n:
                return 0
            
            return dp(i + 1, j) + (dp(i + 1, j + 1) if s[i] == t[j] else 0)
        
        return dp(0, 0)
        
            
from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        @cache
        def dp(i, j):
            if j == m:
                return 1
            
            if i == n or (n - i) < (m - j): # pruning - early stopping
                return 0
            
            return dp(i + 1, j) + (dp(i + 1, j + 1) if s[i] == t[j] else 0)
        
        return dp(0, 0)
        
            
