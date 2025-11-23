from functools import cache
class Solution:

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        @cache
        def helper(i, open_parenthesis):
            if i >= n:
                return open_parenthesis == 0
            
            if open_parenthesis < 0:
                return False
            
            if s[i] == '(':
                return helper(i + 1, open_parenthesis + 1)

            if s[i] == ')':
                if open_parenthesis <= 0:
                    return False
                return helper(i + 1, open_parenthesis - 1)

            # s[i] == '*'
            return helper(i + 1, open_parenthesis + 1) or helper(i + 1, open_parenthesis - 1) or helper(i + 1, open_parenthesis) # 3 cases, one as '(', ')', or ''
            
        return helper(0, 0)



from functools import cache
class Solution:

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        @cache
        def helper(i, open_parenthesis):
            if i >= n:
                return open_parenthesis == 0
            
            if open_parenthesis < 0:
                return False
            
            if s[i] == '(':
                return helper(i + 1, open_parenthesis + 1)

            if s[i] == ')':
                return helper(i + 1, open_parenthesis - 1)

            # s[i] == '*'
            return helper(i + 1, open_parenthesis + 1) or helper(i + 1, open_parenthesis - 1) or helper(i + 1, open_parenthesis) # 3 cases, one as '(', ')', or ''
            
        return helper(0, 0)



class Solution:

    def checkValidString(self, s: str) -> bool:
        open_min, open_max = 0, 0

        for paren in s:
            if paren == '(':
                open_min += 1
                open_max += 1
            elif paren == ')':
                open_min -= 1
                open_max -= 1
            else:
                open_min -= 1
                open_max += 1
            
            if open_max < 0:
                return False
            
            open_min = max(open_min, 0)
        
        return open_min == 0

# https://leetcode.com/problems/valid-parenthesis-string/solutions/543521/java-count-open-parenthesis-on-time-o1-s-j6vt