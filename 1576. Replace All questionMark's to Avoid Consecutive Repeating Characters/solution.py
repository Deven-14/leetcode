class Solution:
    def modifyString(self, s: str) -> str:
        letters = list(s)
        n = len(s)
        last = n - 1
        start = 0
        while start < n and (idx := s.find('?', start)) != -1:
            if idx == 0:
                letters[0] = 'a' if n < 2 or letters[1] != 'a' else 'b'
            elif idx == last:
                letters[-1] = 'a' if letters[-2] != 'a' else 'b'
            elif letters[idx - 1] != 'a' and letters[idx + 1] != 'a':
                letters[idx] = 'a'
            elif letters[idx - 1] != 'b' and letters[idx + 1] != 'b':
                letters[idx] = 'b'
            else:
                letters[idx] = 'c'
            
            start = idx + 1
        
        return "".join(letters)