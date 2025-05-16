class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        for length in range(1, (n // 2) + 1):
            if n % length != 0 or s[length] != s[0]:
                continue
            if s[:length] * (n // length) == s:
                return True
        
        return False


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        for length in range(1, (n // 2) + 1):
            if n % length == 0 and s[length] == s[0] and s[:length] * (n // length) == s:
                return True
        
        return False


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double = s + s
        return s in double[1:-1]