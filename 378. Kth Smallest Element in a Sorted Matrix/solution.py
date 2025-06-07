import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][0], 0, 0)]
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()

        while k:
            ele, i, j = heapq.heappop(heap)
            i2, j2 = i+1, j+1
            if i2 < ROWS and (i2, j) not in visited:
                heapq.heappush(heap, (matrix[i2][j], i2, j))
                visited.add((i2, j))
            if j2 < COLS and (i, j2) not in visited:
                heapq.heappush(heap, (matrix[i][j2], i, j2))
                visited.add((i, j2))
            k -= 1
        
        return ele


from heapq import merge
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return list(merge(*matrix))[k-1]


import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][0], 0, 0)]
        ROWS, COLS = len(matrix), len(matrix[0])
        matrix[0][0] = None

        while k:
            ele, i, j = heapq.heappop(heap)
            i2, j2 = i+1, j+1
            if i2 < ROWS and matrix[i2][j] != None:
                heapq.heappush(heap, (matrix[i2][j], i2, j))
                matrix[i2][j] = None
            if j2 < COLS and matrix[i][j2] != None:
                heapq.heappush(heap, (matrix[i][j2], i, j2))
                matrix[i][j2] = None
            k -= 1
        
        return ele


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        def countLessOrEqual(x): # O(n) way to count 
            total = 0
            c = COLS - 1

            for row in matrix:
                while c >= 0 and row[c] > x:
                    c -= 1
                total += (c + 1)
            
            return total
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) < k: # lower bound
                left = mid + 1
            else: # >= k
                right = mid
        
        return left