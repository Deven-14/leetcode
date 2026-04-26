class Solution:
    def countArrangement(self, n: int) -> int:
        perm = list(range(1, n + 1))
        
        def permutations(i):
            if i >= n:
                return 1
            
            total_count = 0
            for j in range(i, n):
                perm[i], perm[j] = perm[j], perm[i]

                if not (perm[i] % (i + 1) == 0 or (i + 1) % perm[i] == 0):
                    perm[i], perm[j] = perm[j], perm[i]
                    continue

                total_count +=  permutations(i + 1)
                perm[i], perm[j] = perm[j], perm[i]
            
            return total_count
        
        return permutations(0)


class Solution:
    def countArrangement(self, n: int) -> int:
        perm = list(range(1, n + 1))
        
        def permutations(i):
            if i >= n:
                return 1
            
            total_count = 0
            t = i + 1
            for j in range(i, n):
                if not (perm[j] % t == 0 or t % perm[j] == 0):
                    continue

                perm[i], perm[j] = perm[j], perm[i]
                total_count += permutations(i + 1)
                perm[i], perm[j] = perm[j], perm[i]
            
            return total_count
        
        return permutations(0)



class Solution:
    def countArrangement(self, n: int) -> int:
        perm = list(range(1, n + 1))
        count = 0
        
        def permutations(i):
            if i >= n:
                nonlocal count
                count += 1
                return
            
            t = i + 1
            for j in range(i, n):
                if not (perm[j] % t == 0 or t % perm[j] == 0):
                    continue

                perm[i], perm[j] = perm[j], perm[i]
                permutations(i + 1)
                perm[i], perm[j] = perm[j], perm[i]
                    
        permutations(0)
        return count



class Solution:
    def countArrangement(self, n: int) -> int:
        perm = list(range(1, n + 1))
        count = 0
        beautiful_arrangements = [[j % i == 0 or i % j == 0 for j in range(1, n + 1)] for i in range(1, n + 1)]
        
        def permutations(i):
            if i >= n:
                nonlocal count
                count += 1
                return
            
            for j in range(i, n):
                if not beautiful_arrangements[i][perm[j]-1]:
                    continue

                perm[i], perm[j] = perm[j], perm[i]
                permutations(i + 1)
                perm[i], perm[j] = perm[j], perm[i]
                    
        permutations(0)
        return count



class Solution:
    def countArrangement(self, n: int) -> int:
        perm = list(range(1, n + 1))
        count = 0
        beautiful_arrangements = [[j % i == 0 or i % j == 0 for j in range(1, n + 1)] for i in range(1, n + 1)]
        
        def permutations(pos, mask):
            if pos > n:
                nonlocal count
                count += 1
                return
            
            for num in range(1, n + 1):
                if (mask & (1 << num)) != 0:
                    continue
                if not beautiful_arrangements[pos-1][num-1]:
                    continue
                permutations(pos + 1, mask | (1 << num))
                    
        permutations(1, 0)
        return count



class Solution:
    def countArrangement(self, n: int) -> int:
        perm = list(range(1, n + 1))
        beautiful_arrangements = [[j % i == 0 or i % j == 0 for j in range(1, n + 1)] for i in range(1, n + 1)]
        
        @cache
        def permutations(pos, mask):
            if pos > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                if (mask & (1 << num)) != 0:
                    continue
                if not beautiful_arrangements[pos-1][num-1]:
                    continue
                count += permutations(pos + 1, mask | (1 << num))
            
            return count
                    
        return permutations(1, 0)


