from math import prod
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        unique_digits = 10
        i = 2
        t1, t2 = 9, 9
        while i <= n:
            t1 = t1 * t2
            t2 = t2 - 1
            unique_digits += t1
            i += 1
        
        return unique_digits

# _ 10
# _ _ = 9,9  (first 9 coz we can't include 0, then select any 1, remaining 8..... then 8 + 1 = 9, 1 for 0, second 9)
# _ _ _ = 9,9,9 (first 9, same as above, second 9 same as above, third 8 coz 2 out of 10 are already selected)