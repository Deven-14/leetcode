from itertools import groupby
class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 0
        for _, group in groupby(s):
            max_length = max(max_length, len(list(group)))
        
        return max_length
    
from itertools import groupby
class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 0
        curr_char = s[0]
        length = 0

        for char in s:
            if char != curr_char:
                max_length = max(max_length, length)
                length = 1
                curr_char = char
            else:
                length += 1
        
        max_length = max(max_length, length)
        return max_length


