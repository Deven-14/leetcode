from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1
        
        count = 0
        for col in zip(*grid):
            if col in rows:
                count += rows[col]
        
        return count



from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        
        count = 0
        for col in zip(*grid):
            if col in rows:
                count += rows[col]
        
        return count
    

from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        return sum(rows[col] for col in zip(*grid))
    