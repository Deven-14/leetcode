class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        
        length, nums = 1, 9
        total_digits = 9
        prev_digits = 0
        while total_digits < n:
            length += 1
            nums *= 10
            prev_digits = total_digits
            total_digits += nums * length
        
        start, end = 10 ** (length - 1), int("9" * length)
        l, r = start, end
        while l <= r:
            mid = (l + r) // 2
            mid_digits_start = prev_digits + (mid - start) * length + 1
            mid_digits_end = mid_digits_start + length - 1

            if mid_digits_start <= n <= mid_digits_end:
                return int(str(mid)[n - mid_digits_start])
            
            elif mid_digits_start > n:
                r = mid - 1
            
            else:
                l = mid + 1


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        
        length, start, length_nums = 1, 1, 9
        digits = length * length_nums
        while n > digits:
            n -= digits
            length += 1
            length_nums *= 10
            start *= 10
            digits = length * length_nums
        
        rem = n % length
        num = (start - 1) + n // length + (1 if rem > 0 else 0)
        idx = -1 if rem == 0 else (rem-1)
        return int(str(num)[idx])
        
        