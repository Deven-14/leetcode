from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = Counter((a, b) if a <= b else (b, a) for a, b in dominoes)
        return sum(n * (n - 1) // 2 for n in dominoes.valuesa())


# nC2 = n * (n - 1) // 2

        