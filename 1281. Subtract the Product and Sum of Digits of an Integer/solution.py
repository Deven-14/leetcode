import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        return math.prod(digits) - sum(digits)
