class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)

        chars[:k] = chars[k-1::-1]
        k2 = k * 2
        start = k2
        end = k + k2
        
        while start < n:
            chars[start:end] = chars[end-1:start-1:-1]
            start += k2
            end += k2
        
        return "".join(chars)