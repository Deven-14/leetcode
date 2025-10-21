class Solution:
    def sumZero(self, n: int) -> List[int]:
        m = n // 2
        if n % 2 == 1:
            return list(range(-m, m+1))
        else:
            return list(range(-m, 0)) + list(range(1, m+1))