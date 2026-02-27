from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        
        @cache
        def dp(i, j):
            if i >= n and j >= m:
                return True
            
            char_match = (i < n and j < m and (s[i] == p[j] or p[j] == '.'))

            if j+1 < m and p[j + 1] == '*':
                return (char_match and dp(i + 1, j)) or dp(i, j + 2)
            
            return char_match and dp(i + 1, j + 1)
        
        return dp(0, 0)



from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        
        @cache
        def dp(i, j):
            if j == m:
                return i == n
            
            char_match = (i < n and (s[i] == p[j] or p[j] == '.'))

            if j+1 < m and p[j + 1] == '*':
                return (char_match and dp(i + 1, j)) or dp(i, j + 2)
            
            return char_match and dp(i + 1, j + 1)
        
        return dp(0, 0)


