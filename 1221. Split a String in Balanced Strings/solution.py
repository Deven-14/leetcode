class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_strings = 0
        r, l = 0, 0

        for char in s:
            if char == 'R':
                r += 1
            else:
                l += 1
            if r == l:
                r = l = 0
                balanced_strings += 1
        
        return balanced_strings