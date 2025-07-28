from collections import deque
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = list(s)
        queue = deque()

        while stack:
            stack2 = [stack.pop()]
            
            while stack2:
                char = stack.pop()
                queue.appendleft(char)
                if char == ')':
                    stack2.append(char)
                else:
                    stack2.pop()
            
            queue.popleft()
        
        return "".join(queue)
                    
            

from collections import deque
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0

        for char in s:
            if char == '(':
                count += 1
            if count > 1:
                ans.append(char)
            if char == ')':
                count -= 1
        
        return "".join(ans)