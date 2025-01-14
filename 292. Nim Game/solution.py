class Solution:
    def canWinNim(self, n: int) -> bool:
        nim1 = nim2 = nim3 = True
        nim4 = True
        i = 3
        while i < n:
            nim4 = not nim3 or not nim2 or not nim1
            nim3, nim2, nim1 = nim4, nim3, nim2
            i += 1
        
        return nim4

# timelimit exceeded

class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n % 4 == 0