class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        m = n // 2
        if s[:m] == s[:-m-1:-1]:
            return 1
        
        return 2


# since it is subsequences
# the answer can be either 1 or 2
# 1 if 's' is a perfect palindrome
# 2 - by deleting all 'a' 1 step and deleting all 'b' another step
