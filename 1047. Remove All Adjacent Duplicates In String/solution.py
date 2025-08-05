class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i, n = 0, len(s)

        while i < n:
            if stack and s[i] == stack[-1]:
                stack.pop()
                i += 1

            else:
                stack.append(s[i])
                i += 1
        
        return "".join(stack)


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
    

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
    