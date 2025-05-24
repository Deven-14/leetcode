from collections import deque
class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = [char for substring in s.split("-") for char in substring]
        queue = deque()
        stop = len(chars)
        start = stop - k
        while start >= 0:
            queue.appendleft("".join(chars[start:stop]))
            start, stop = start - k, start
        
        if stop > 0:
            queue.appendleft("".join(chars[:stop]))
        
        return "-".join(queue).upper()


from collections import deque
class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = [char for char in s if char.isalnum()]
        queue = deque()
        stop = len(chars)
        start = stop - k
        while start >= 0:
            queue.appendleft("".join(chars[start:stop]))
            start, stop = start - k, start
        
        if stop > 0:
            queue.appendleft("".join(chars[:stop]))
        
        return "-".join(queue).upper()


from collections import deque
class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace('-', '').upper()
        queue = deque()
        stop = len(chars)
        start = stop - k
        while start >= 0:
            queue.appendleft("".join(chars[start:stop]))
            start, stop = start - k, start
        
        if stop > 0:
            queue.appendleft("".join(chars[:stop]))
        
        return "-".join(queue)
    

class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace('-', '').upper()
        batches = []
        first_stop = len(chars) % k or k # **********

        batches.append("".join(chars[:first_stop]))
        for idx in range(first_stop, len(chars), k):
            batches.append("".join(chars[idx:idx + k]))

        return "-".join(batches)


