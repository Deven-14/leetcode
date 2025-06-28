class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for char in s:
            if char != '#':
                stack1.append(char)
            elif stack1:
                stack1.pop()
                
        for char in t:
            if char != '#':
                stack2.append(char)
            elif stack2:
                stack2.pop()
        
        return stack1 == stack2


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s) - 1, len(t) - 1
        c1, c2 = 0, 0

        while p1 >= 0 or p2 >= 0:
            if p1 >= 0 and s[p1] == '#':
                c1 += 1
                p1 -= 1
                
            elif p2 >= 0 and t[p2] == '#':
                c2 += 1
                p2 -= 1
            
            elif p1 >= 0 and c1 > 0:
                c1 -= 1
                p1 -= 1
            
            elif p2 >= 0 and c2 > 0:
                c2 -= 1
                p2 -= 1

            elif (p1 < 0 and p2 >= 0) or (p1 >= 0 and p2 < 0) or s[p1] != t[p2]:
                return False
                
            else:
                p1 -= 1
                p2 -= 1
        
        return p1 < 0 and p2 < 0