import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1
        idx_of_multiples_of_primes = dict.fromkeys(primes, 0)
        next_multiples = [(num, num) for num in primes]
        heapq.heapify(next_multiples)

        i = 1
        while i < n:
            next_ugly_num, prime = heapq.heappop(next_multiples)
            if ugly_nums[i-1] != next_ugly_num:
                ugly_nums[i] = next_ugly_num
                i += 1

            idx_of_multiples_of_primes[prime] += 1

            idx_of_multiple = idx_of_multiples_of_primes[prime]

            next_multiple = ugly_nums[idx_of_multiple] * prime

            heapq.heappush(next_multiples, (next_multiple, prime))
        
        return ugly_nums[-1]


import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1
        idx_of_multiples_of_primes = [0] * n
        next_multiples = [(num, i) for i, num in enumerate(primes)]
        heapq.heapify(next_multiples)

        i = 1
        while i < n:
            next_ugly_num, idx_of_prime = heapq.heappop(next_multiples)
            if ugly_nums[i-1] != next_ugly_num:
                ugly_nums[i] = next_ugly_num
                i += 1

            idx_of_multiples_of_primes[idx_of_prime] += 1
            idx_of_multiple = idx_of_multiples_of_primes[idx_of_prime]
            next_multiple = ugly_nums[idx_of_multiple] * primes[idx_of_prime]
            heapq.heappush(next_multiples, (next_multiple, idx_of_prime))
        
        return ugly_nums[-1]


import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1
        idx_of_multiples_of_primes = [0] * n
        next_multiples = [(num, i) for i, num in enumerate(primes)]

        i = 1
        while i < n:
            next_ugly_num, idx_of_prime = heapq.heappop(next_multiples)
            if ugly_nums[i-1] != next_ugly_num:
                ugly_nums[i] = next_ugly_num
                i += 1

            idx_of_multiples_of_primes[idx_of_prime] += 1
            idx_of_multiple = idx_of_multiples_of_primes[idx_of_prime]
            next_multiple = ugly_nums[idx_of_multiple] * primes[idx_of_prime]
            heapq.heappush(next_multiples, (next_multiple, idx_of_prime))
        
        return ugly_nums[-1]


import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1
        next_multiples = [(num, num, 0) for num in primes]

        i = 1
        while i < n:
            next_ugly_num, prime, idx_of_mul_of_prime = heapq.heappop(next_multiples)
            if ugly_nums[i-1] != next_ugly_num:
                ugly_nums[i] = next_ugly_num
                i += 1
            next_multiple = ugly_nums[idx_of_mul_of_prime] * prime
            heapq.heappush(next_multiples, (next_multiple, prime, idx_of_mul_of_prime+1))
        
        return ugly_nums[-1]


import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]

        for i in range(n):
            num = heapq.heappop(ugly_nums)
            for prime in primes:
                heapq.heappush(ugly_nums, num * prime)
                if num % prime == 0: break
        
        return num