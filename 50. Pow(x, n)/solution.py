from functools import cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @cache
        def helper(i):
            if i == 0:
                return 1
                
            if i == 1:
                return x
            
            if i % 2 == 0:
                t = helper(i // 2)
                return t * t
            
            return x * helper(i - 1)
        
        if n > 0:
            return helper(n)
        
        return 1 / helper(-n)



from functools import cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @cache
        def helper(i):
            if i == 1:
                return x
            
            if i % 2 == 0:
                t = helper(i // 2)
                return t * t
            
            return x * helper(i - 1)
        
        if n == 0:
            return 1

        if n > 0:
            return helper(n)
        
        return 1 / helper(-n)
