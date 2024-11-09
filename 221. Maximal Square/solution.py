# 4500 ms
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums = [int("".join(row), 2) for row in matrix]

        def max_sub_len(num):
            l = 0
            max_l = 0
            for bit in bin(num)[2:]:
                if bit == "0":
                    l = 0
                else:
                    l += 1
                max_l = max(max_l, l)
            
            return max_l
        
        n = len(nums)
        max_square = 0
        for i in range(n):
            num = nums[i]
            for j in range(i+1, n):
                num &= nums[j]
                max_l = max_sub_len(num)
                if max_l > j-i:
                    max_square = max(j-i+1, max_square)
        
        if max_square == 0:
            return 1 if any(num > 0 for num in nums) else 0
        
        return max_square ** 2

# 4000 ms            
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums = [int("".join(row), 2) for row in matrix]

        def max_sub_len(num):
            l = 0
            max_l = 0
            for bit in bin(num)[2:]:
                if bit == "0":
                    l = 0
                else:
                    l += 1
                max_l = max(max_l, l)
            
            return max_l
        
        n = len(nums)
        max_square = 0
        for i in range(n):
            num = nums[i]
            for j in range(i+1, n):
                num &= nums[j]
                max_l = max_sub_len(num)
                if max_l > j-i:
                    max_square = max(j-i+1, max_square)
                else:
                    break
        
        if max_square == 0:
            return 1 if any(num > 0 for num in nums) else 0
        
        return max_square ** 2

# 1000 ms            
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums = [int("".join(row), 2) for row in matrix]

        def max_sub_len(num):
            l = 0
            max_l = 0
            for bit in bin(num)[2:]:
                if bit == "0":
                    l = 0
                else:
                    l += 1
                max_l = max(max_l, l)
            
            return max_l
        
        n = len(nums)
        max_square = 0
        for i in range(n):
            num = nums[i]
            if max_square >= (n-i):
                break
            for j in range(i+1, n):
                num &= nums[j]
                max_l = max_sub_len(num)
                if max_l > j-i:
                    max_square = max(j-i+1, max_square)
                else:
                    break
        
        if max_square == 0:
            return 1 if any(num > 0 for num in nums) else 0
        
        return max_square ** 2

# DP solution 75 ms
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            dp[i][0] = int(matrix[i][0])
        
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return max(max(row) for row in dp) ** 2
