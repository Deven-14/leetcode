from collections import deque
import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        ints_to_alpha = {str(num): char for num, char in zip(range(1, 27), string.ascii_lowercase)}
        stack = deque()
        
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                stack.appendleft(ints_to_alpha[s[i-2:i]])
                i -= 3
            else:
                stack.appendleft(ints_to_alpha[s[i]])
                i -= 1
        
        return "".join(stack)
