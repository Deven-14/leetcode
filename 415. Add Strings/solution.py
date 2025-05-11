from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num3 = []
        carry = 0

        for digit1, digit2 in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            carry, digit3 = divmod(int(digit1) + int(digit2) + carry, 10)
            num3.append(str(digit3))
        
        if carry:
            num3.append("1")
        
        num3.reverse()
        return "".join(num3)
    

from itertools import zip_longest
from collections import deque
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num3 = deque()
        carry = 0

        for digit1, digit2 in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            carry, digit3 = divmod(int(digit1) + int(digit2) + carry, 10)
            num3.appendleft(str(digit3))
        
        if carry:
            num3.appendleft("1")
        
        return "".join(num3)
    

from itertools import zip_longest
from collections import deque
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num3 = deque()
        carry = 0

        for digit1, digit2 in zip_longest(reversed(num1), reversed(num2), fillvalue="0"):
            carry, digit3 = divmod(int(digit1) + int(digit2) + carry, 10)
            num3.appendleft(str(digit3))
        
        if carry:
            num3.appendleft("1")
        
        return "".join(num3)


from itertools import zip_longest
from collections import deque
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num3 = deque()
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            carry, digit3 = divmod(digit1 + digit2 + carry, 10)
            num3.appendleft(str(digit3))
            i -= 1
            j -= 1
        
        if carry:
            num3.appendleft("1")
        
        return "".join(num3)