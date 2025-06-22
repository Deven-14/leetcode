from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()

        i, n = 0, len(num)
        while i < n and k:
            
            while stack and k and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            
            stack.append(num[i])
            i += 1
        
        stack.extend(num[i:])

        while k:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == "0":
            stack.popleft()

        if not stack:
            return "0"

        return "".join(stack)
        

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [num[0]]

        i, n = 1, len(num)
        while i < n and k:
            if num[i] < stack[-1]:
                while stack and k and num[i] < stack[-1]:
                    stack.pop()
                    k -= 1
            
            stack.append(num[i])
            i += 1
        
        stack.extend(num[i:])
        if k > 0:
            stack = stack[:-k]

        i, n = 0, len(stack)
        while i < n and stack[i] == "0":
            i += 1
        if i > 0:
            stack = stack[i:]

        if not stack:
            return "0"

        return "".join(stack)
        

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [num[0]]

        i, n = 1, len(num)
        while i < n and k:
            while stack and k and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            
            stack.append(num[i])
            i += 1
        
        stack.extend(num[i:])
        if k > 0:
            stack = stack[:-k]

        s = "".join(stack).lstrip('0')
        return s if s else '0'


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [num[0]]

        i, n = 1, len(num)
        while i < n and k:
            if num[i] < stack[-1]:
                while stack and k and num[i] < stack[-1]:
                    stack.pop()
                    k -= 1
            
            stack.append(num[i])
            i += 1
        
        stack.extend(num[i:])
        if k > 0:
            stack = stack[:-k]

        s = "".join(stack).lstrip('0')
        return s if s else '0'
    

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ele in num:
            while stack and k and ele < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(ele)
        
        if k > 0:
            stack = stack[:-k]

        s = "".join(stack).lstrip('0')
        return s if s else '0'


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ele in num:
            while stack and k and ele < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(ele)
        
        while k:
            stack.pop()
            k -= 1
            
        s = "".join(stack).lstrip('0')
        return s if s else '0'