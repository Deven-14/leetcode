from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        divisors_sum = 1
        sqrt_num = int(sqrt(num))

        for i in range(2, sqrt_num):
            if num % i == 0:
                divisors_sum += i + num // i
        
        if num % sqrt_num == 0:
            if sqrt_num * sqrt_num == num:
                divisors_sum += sqrt_num
            else:
                divisors_sum += sqrt_num + num // sqrt_num
        
        return divisors_sum == num