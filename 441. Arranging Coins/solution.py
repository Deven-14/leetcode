import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, int(math.sqrt(2 * n))

        while l <= r:
            mid = l + (r - l) // 2
            m = (mid * (mid + 1)) // 2
            if m > n:
                r = mid - 1
            elif m < n:
                ans = mid
                l = mid + 1
            else:
                return mid
        
        return ans

            

# min = 1
# for max, lets use the sum of 1st n formula
# n = m(m + 1) / 2
# 2*n = m^2 + m
# 2*n - m = m^2
# m^2 = 2*n - m
# m = sqrt(2*n - m)
# m < sqrt(2*n)
# max = sqrt(2 * n)

import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, int(math.sqrt(2 * n)) # r could be n itself

        while l <= r:
            mid = l + (r - l) // 2
            m = (mid * (mid + 1)) // 2
            if m > n:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        
        return ans

            
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8 * n + 1) - 1) / 2)

# lets use the sum of 1st n formula
# n = m(m + 1) / 2
# 2n = m2 + m
# m2 + m = 2n
# m2 + 2m(1/2) + (1/2)^2 = 2n + (1/2)^2
# (m + 1/2)^2 = (8n + 1) / 4
# m + 1/2 = sqrt(8n + 1) / 2
# m = (sqrt(8n + 1) - 1) / 2