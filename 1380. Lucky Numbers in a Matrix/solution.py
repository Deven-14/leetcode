class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_eles = set(min(row) for row in matrix)
        max_eles = set(max(col) for col in zip(*matrix))
        return list(min_eles & max_eles)