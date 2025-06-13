class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        n2 = n // 2
        
        def is_palindrome(i, j):
            while i <= j and s[i] == s[j]:
                i += 1
                j -= 1
            
            return i > j
        
        i, j = 0, n-1
        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        
        if i > j:
            return True
        
        return is_palindrome(i+1, j) or is_palindrome(i, j-1)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        n2 = n // 2
        
        def is_palindrome(i, j):
            l = j - i + 1
            l2 = l // 2
            return s[i:i+l2] == s[j:j-l2:-1]
        
        i, j = 0, n-1
        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        
        if i > j:
            return True
        
        return is_palindrome(i+1, j) or is_palindrome(i, j-1)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(i, j):
            l = j - i + 1
            l2 = l // 2
            return s[i:i+l2] == s[j:j-l2:-1]
        
        n = len(s)
        i, j = 0, n-1
        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        
        return i > j or is_palindrome(i+1, j) or is_palindrome(i, j-1)


class Solution:
    def validPalindrome(self, s: str) -> bool:        
        n = len(s)
        i, j = 0, n-1
        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        
        return i > j or s[i+1:j+1] == s[j:i:-1] or s[i:j] == s[j-1:i-1 if i-1 >= 0 else None:-1]
