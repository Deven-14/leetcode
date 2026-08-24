class Solution:
    def minSteps(self, n: int) -> int:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        dp = list(range(n + 1))
        dp[1] = 0

        for i in range(2, n + 1):
            if primes[i]:
                c = 2 # copy (1) and paste (1)
                for j in range(i + i, n + 1, i):
                    primes[i] = False
                    dp[j] = min(dp[j], dp[i] + c)
                    c += 1 # for next paste
        
        return dp[n]
            


class Solution:
    def minSteps(self, n: int) -> int:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        dp = list(range(n + 1))
        dp[1] = 0

        for i in range(2, n + 1):
            if primes[i]:
                c = 2 # copy (1) and paste (1)
                for j in range(i + i, min(i * i + 1, n + 1), i):
                    primes[i] = False
                    dp[j] = min(dp[j], dp[i] + c)
                    c += 1 # for next paste
        
        return dp[n]

# SofE starts at i * i
# here we ended at i * i
# coz of how SofE works



class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        prime = 2
        while n > 1:
            while n % prime == 0:
                count += prime
                n //= prime
            prime += 1
        
        return count

# n = 36, 2 * 2 * 3 * 2
# 1 * 2 = 2 (c + p)
# 2 * 2 = 4 (c + p)
# 4 * 3 = 12 (c + p + p)
# 12 * 3 = 36 (c + p + p)
# i.e. sum(all prime factor)