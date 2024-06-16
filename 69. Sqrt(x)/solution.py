class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        i = 1
        j = x // 2
        while i <= j:
            mid = (i + j) // 2
            min_square = mid * mid
            max_square = (mid+1) * (mid+1)
            if min_square <= x < max_square:
                return mid
            elif min_square > x:
                j = mid - 1
            else:
                i = mid + 1
        
