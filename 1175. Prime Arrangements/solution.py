from math import factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        primes[0] = False
        primes[1] = False

        for i in range(2, n + 1):
            if primes[i] == False:
                continue
            
            for j in range(i + i, n + 1, i):
                primes[j] = False
        
        no_of_primes = sum(primes)
        no_of_non_primes = n - no_of_primes
        mod = (10 ** 9) + 7
        return ((factorial(no_of_primes) % mod) * (factorial(no_of_non_primes) % mod)) % mod


from math import factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        primes[0] = False
        primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i] == False:
                continue
            
            for j in range(i * i, n + 1, i):
                primes[j] = False
        
        no_of_primes = sum(primes)
        no_of_non_primes = n - no_of_primes
        mod = (10 ** 9) + 7
        return ((factorial(no_of_primes) % mod) * (factorial(no_of_non_primes) % mod)) % mod