from collections import deque
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
            
        n = num if num >= 0 else (num + (1 << 32))
        queue = deque()
        chars = "0123456789abcdef"

        while n:
            n, r = divmod(n, 16)
            queue.appendleft(chars[r])
        
        return "".join(queue)