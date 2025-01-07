import math
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i * i for i in range(1, int(math.sqrt(n))+1)]

        dp = [0] * (n+1)
        dp[1] = 1

        for num in range(2, n+1):
            dp_num = num
            for perfect_square in perfect_squares:
                if num < perfect_square:
                    break
                dp_num = min(dp_num, dp[num - perfect_square] + 1)
            dp[num] = dp_num
        
        return dp[n]


import math
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i * i for i in range(1, int(math.sqrt(n))+1)]

        visited = {n}
        remainders = [n]

        level = 0
        while remainders:
            level += 1
            new_remainders = []
            for num in remainders:
                for perfect_square in perfect_squares:
                    if num < perfect_square:
                        break
                    remainder = num - perfect_square
                    if remainder == 0:
                        return level
                    if remainder not in visited:
                        visited.add(remainder)
                        new_remainders.append(remainder)
                     
            remainders = new_remainders  
        return -1


# another solution is to perform the calculation once for all the numbers and store it in a class variable and then directly access the class variable and return the result - hack when we space and the n value is not large