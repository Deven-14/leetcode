class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        
        def helper(i, j, sum):
            if i == n:
                return sum
            
            sum += triangle[i][j]
            sum1 = helper(i+1, j, sum)
            sum2 = helper(i+1, j+1, sum)
            return min(sum1, sum2)
        

        min_sum = helper(0, 0, 0)
        return min_sum

# ! ABOVE SOLUTION TIMED OUT

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        
        for i in range(1, n):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        
        return min(triangle[-1])

# * AWESOME SOLUTION