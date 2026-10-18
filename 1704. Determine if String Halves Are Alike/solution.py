class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        n = len(s) // 2
        a, b = s[:n], s[n:]
        return sum(1 for c in a if c in vowels) == sum(1 for c in b if c in vowels)