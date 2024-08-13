class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        palindrome = []
        n = len(s)

        def isPalindrome(s):
            l = len(s)
            l_2 = l // 2
            return s[:l_2] == s[:-l_2-1:-1]

        def backtrack(i=0):
            if i == n:
                palindromes.append(list(palindrome))
                return
            
            for j in range(i, n):
                substring = s[i:j+1]
                if isPalindrome(substring):
                    palindrome.append(substring)
                    backtrack(j+1)
                    palindrome.pop()
        
        backtrack()
        return palindromes


from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        palindrome = []
        n = len(s)

        @cache
        def isPalindrome(l, r):
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            
            if l < r:
                return False
            
            return True

        def backtrack(i=0):
            if i == n:
                palindromes.append(list(palindrome))
                return
            
            for j in range(i, n):
                if isPalindrome(i, j):
                    palindrome.append(s[i:j+1])
                    backtrack(j+1)
                    palindrome.pop()
        
        backtrack()
        return palindromes
                