class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        
        stack = []
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            elif bracket in ")]}" and len(stack) > 0:
                open_bracket = stack.pop()
                bracket_pair = open_bracket + bracket
                if bracket_pair not in ["()", "[]", "{}"]:
                    return False
            else:
                return False
        
        if len(stack) > 0:
            return False
        
        return True


class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        
        bracket_pair = {")": "(", "]": "[", "}": "{"}
        
        stack = []
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            elif len(stack) > 0 and stack[-1] == bracket_pair[bracket]:
                stack.pop()
            else:
                return False
        
        if len(stack) > 0:
            return False
        
        return True


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
                
        stack = []
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            elif len(stack) > 0 and stack[-1]+bracket in ["()", "[]", "{}"]:
                stack.pop()
            else:
                return False
        
        if len(stack) > 0:
            return False
        
        return True