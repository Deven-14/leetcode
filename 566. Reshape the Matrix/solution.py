from itertools import chain
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        iterator = chain.from_iterable(mat)
        return [[next(iterator) for _ in range(c)] for _ in range(r)]