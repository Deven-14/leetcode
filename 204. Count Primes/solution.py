from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        c = 0
        for i in range(2, n):
            j = 2
            n = int(sqrt(i))+1
            
            while i % j != 0 and j < n:
                j += 1
            
            if j == n:
                c += 1
        
        return c

# TIME limit exceeded

from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        c = 0
        primes = []

        for i in range(2, n):

            j = 0
            m = len(primes)
            while j < m and i % primes[j] != 0:
                j += 1
            
            if j == m:
                primes.append(i)
                c += 1
        
        return c

# TIME limit exceeded

class Solution:
    def countPrimes(self, n: int) -> int:
        c = 0
        primes = [True] * n

        i = 2
        while i < n:
            c += 1

            j = i + i
            while j < n:
                primes[j] = False
                j += i

            i = i + 1
            while i < n and not primes[i]:
                i += 1
        
        return c

# Use Sieve of Eratosthenes.

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n

        p = 2
        p_square = p * p
        while p_square < n:

            if primes[p] == True:
                for i in range(p_square, n, p):
                    primes[i] = False

            p += 1
            p_square = p * p
        
        c = 0
        for i in range(2, n):
            if primes[i]:
                c += 1
            
        return c


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n

        p = 2
        p_square = p * p
        while p_square < n:

            if primes[p] == True:
                primes[p_square:n:p] = [False] * ((n-1)//p - p + 1)

            p += 1
            p_square = p * p
        
        c = 0
        for i in range(2, n):
            if primes[i]:
                c += 1
            
        return c