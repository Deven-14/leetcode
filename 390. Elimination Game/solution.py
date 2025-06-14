class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = list(range(1, n+1))

        flip = False
        while len(arr) > 1:
            if flip:
                m = len(arr)
                arr = arr[::2] if m % 2 == 0 else arr[1::2]
            else:
                arr = arr[1::2]
            flip = not flip
        
        return arr[0]


# ! MEMORY LIMIT EXCEEDED


class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        step = 1
        head = 1
        
        while n > 1:
            if left or n % 2 == 1:
                head += step
            n = n // 2
            step = step * 2
            left = not left
        
        return head