class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        elif n == 2:
            return True
        
        first, second = False, True
        for i in range(3, n+1):
            first, second = second, not (second if i & 1 else (first and second))
        
        return second

# if odd -> not of i-1 (second) coz n % 1 == 0
# if even -> not of ((i-1) and (i-2)) coz n % 1 == 0 or n % 2 == 0