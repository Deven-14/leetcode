from functools import cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @cache
        def dfs(l, r):
            if l == r:
                return 0
            
            if r == l + 1:
                return l
            
            min_value = float("inf")
            for mid in range(l+1, r):
                lower = dfs(l, mid - 1)
                higher = dfs(mid + 1, r)

                max_value = mid + max(lower, higher)
                min_value = min(min_value, max_value)
            
            return min_value
        
        return dfs(1, n)


from functools import cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        inf = float("inf")
        
        @cache
        def dfs(l, r):
            if l == r:
                return 0
            
            if r == l + 1:
                return l
            
            min_value = inf
            for mid in range(l+1, r):
                lower = dfs(l, mid - 1)
                higher = dfs(mid + 1, r)

                max_value = mid + max(lower, higher)
                min_value = min(min_value, max_value)
            
            return min_value
        
        return dfs(1, n)


from functools import cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        inf = float("inf")
        
        @cache
        def dfs(l, r):
            if l == r:
                return 0
            
            if r == l + 1:
                return l
            
            if r == l + 2:
                return l + 1
            
            min_value = inf
            for mid in range(l+1, r):
                lower = dfs(l, mid - 1)
                higher = dfs(mid + 1, r)

                max_value = mid + max(lower, higher)
                min_value = min(min_value, max_value)
            
            return min_value
        
        return dfs(1, n)


from functools import cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        inf = float("inf")
        
        @cache
        def dfs(l, r):
            if l == r:
                return 0
            
            if r == l + 1:
                return l
            
            min_value = inf
            for mid in range((l + r) // 2, r):
                lower = dfs(l, mid - 1)
                higher = dfs(mid + 1, r)

                max_value = mid + max(lower, higher)
                min_value = min(min_value, max_value)
            
            return min_value
        
        return dfs(1, n)
                