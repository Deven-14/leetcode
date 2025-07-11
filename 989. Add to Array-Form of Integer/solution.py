from collections import deque
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        new_num = deque()

        for digit in num[::-1]:
            carry, new_digit = divmod(digit + carry, 10)
            new_num.appendleft(new_digit)

        if carry == 0:
            return list(new_num)
        
        for digit in str(carry)[::-1]:
            new_num.appendleft(int(digit))
        
        return list(new_num)

from collections import deque
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        new_num = deque()

        for i in range(len(num)-1, -1, -1):
            digit = num[i]
            carry, new_digit = divmod(digit + carry, 10)
            new_num.appendleft(new_digit)

        if carry == 0:
            return list(new_num)
        
        for digit in str(carry)[::-1]:
            new_num.appendleft(int(digit))
        
        return list(new_num)


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        new_num = []

        for i in range(len(num)-1, -1, -1):
            digit = num[i]
            carry, new_digit = divmod(digit + carry, 10)
            new_num.append(new_digit)

        if carry == 0:
            new_num.reverse()
            return list(new_num)
        
        for digit in str(carry)[::-1]:
            new_num.append(int(digit))
        
        new_num.reverse()
        return list(new_num)


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        carry = k
        i, n = 0, len(num)

        while carry and i < n:
            carry, digit = divmod(num[i] + carry, 10)
            num[i] = digit
            i += 1
        
        if carry == 0:
            num.reverse()
            return num
        
        while carry:
            carry, digit = divmod(carry, 10)
            num.append(digit)
        
        num.reverse()
        return num