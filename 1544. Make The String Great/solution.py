class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        n = len(s)
        stack = []

        while i < n:
            if stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        
        return "".join(stack)

        
