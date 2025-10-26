class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next([k, n-k] for k in range(n) if '0' not in f'{k}{n-k}')


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a, b = 0, n
        base = 1
        while n > 1:
            split = 1
            if (n - split) % 10 == 0:
                split += 1
            a += split * base
            b -= split * base
            base *= 10
            n = (n - split) // 10
        
        return [a, b]