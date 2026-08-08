from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l <= r:
            value = (l + r) ** 2 - 2 * l * r
            if value == c:
                return True
            elif value > c:
                r -= 1
            else:
                l += 1
        
        return False
        
# a2 + b2 = c
# (a + b)2 - 2ab = c
# max: b = 0, a2 = c
# => a = sqrt(c)
# range (0, int(sqrt(c)))


from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l <= r:
            value = l ** 2 + r ** 2
            if value == c:
                return True
            elif value > c:
                r -= 1
            else:
                l += 1
        
        return False
        
# a2 + b2 = c
# (a + b)2 - 2ab = c
# max: b = 0, a2 = c
# => a = sqrt(c)
# range (0, int(sqrt(c)))

# a2 + b2 = c
# max: b = 0, a2 = c
# => a = sqrt(c)
# range (0, int(sqrt(c)))


from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l <= r:
            value = l * l + r * r
            if value == c:
                return True
            elif value > c:
                r -= 1
            else:
                l += 1
        
        return False
        
# a2 + b2 = c
# (a + b)2 - 2ab = c
# max: b = 0, a2 = c
# => a = sqrt(c)
# range (0, int(sqrt(c)))

# a2 + b2 = c
# max: b = 0, a2 = c
# => a = sqrt(c)
# range (0, int(sqrt(c)))


from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        halfc = int(sqrt(c))

        while i <= halfc:
            count = 0
            while c % i == 0:
                count += 1
                c //= i
            if i % 4 == 3 and count % 2 != 0:
                return False
            i += 1
        
        return c % 4 != 3
        
# a2 + b2 = c
# (a + b)2 - 2ab = c
# max: b = 0, a2 = c
# => a = sqrt(c)
# range (0, int(sqrt(c)))

# a2 + b2 = c
# max: b = 0, a2 = c
# => a = sqrt(c)
# range (0, int(sqrt(c)))

