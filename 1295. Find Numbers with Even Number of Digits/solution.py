class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) & 1 == 0)



from math import log10
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if (int(log10(num)) + 1) & 1 == 0)

# n = x^y
# log n = y log x
# y = log n / log x
# y = log x (n) - log to base x of n

# log 10 (127) = y
# 127 = 10^y
# we are trying to identify what is the 10th power to represent n, if it is 10^0, then 1 digit, 10^1.x would be 2 digits, etc.
# power == y, (int(y) + 1) % 2
# ==> (int(log 10 (127)) + 1) % 2