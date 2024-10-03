class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        squares = [i ** 2 for i in range(10)]

        while n != 1:

            s = 0
            m = n
            while m:
                i = m % 10
                s += squares[i]
                m = m // 10
            
            if s in visited:
                return False
            
            visited.add(s)
            n = s
        
        return True