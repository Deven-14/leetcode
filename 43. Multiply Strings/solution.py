from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        i = len(num2) - 1
        num3 = 0
        mul = 1

        while i >= 0:

            j = len(num1) - 1
            num = int(num2[i])
            carry = 0
            num3_partial = 0
            mul_partial = 1
            while j >= 0:
                carry, res = divmod(num * int(num1[j]) + carry, 10)
                num3_partial = res * mul_partial + num3_partial
                mul_partial *= 10
                j -= 1
            
            if carry:
                num3_partial = carry * mul_partial + num3_partial

            num3 = num3_partial * mul + num3
            mul *= 10
            i -= 1
        
        return str(num3)



from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        i = len(num2) - 1
        num3 = 0
        mul = 1
        cache = {}

        while i >= 0:
            num = int(num2[i])

            if num not in cache:
                j = len(num1) - 1
                carry = 0
                num3_partial = 0
                mul_partial = 1
                while j >= 0:
                    carry, res = divmod(num * int(num1[j]) + carry, 10)
                    num3_partial = res * mul_partial + num3_partial
                    mul_partial *= 10
                    j -= 1
                
                if carry:
                    num3_partial = carry * mul_partial + num3_partial
                
                cache[num] = num3_partial

            num3 = cache[num] * mul + num3
            mul *= 10
            i -= 1
        
        return str(num3)
        

from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        m, n = len(num1), len(num2)
        num3 = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + num3[p2] # carry

                a, b = divmod(total, 10)
                num3[p1] += a
                num3[p2] = b
        
        return "".join(str(num) for num in num3).lstrip('0')
    

from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        num1 = [int(num) for num in num1]
        num2 = [int(num) for num in num2]
        m, n = len(num1), len(num2)
        num3 = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = num1[i] * num2[j]
                p1 = i + j
                p2 = p1 + 1
                total = mul + num3[p2] # carry

                a, b = divmod(total, 10)
                num3[p1] += a
                num3[p2] = b
        
        return "".join(str(num) for num in num3).lstrip('0')



from collections import deque
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        num1 = [int(num) for num in num1]
        num2 = [int(num) for num in num2]
        m, n = len(num1), len(num2)
        num3 = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = num1[i] * num2[j]
                p1 = i + j
                p2 = p1 + 1
                a, b = divmod(mul + num3[p2], 10)
                num3[p1] += a
                num3[p2] = b
        
        return "".join(str(num) for num in num3).lstrip('0')