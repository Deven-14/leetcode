class Solution:
    def reformat(self, s: str) -> str:
        letters, digits = [], []
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        
        a, b = (letters, digits) if len(letters) >= len(digits) else (digits, letters)
        if len(a) - len(b) > 1:
            return ""
        
        res = [None] * (len(digits) + len(letters))
        res[::2] = a
        res[1::2] = b
        return "".join(res)


class Solution:
    def reformat(self, s: str) -> str:
        letters, digits = [char for char in s if char.isalpha()], [char for char in s if char.isdigit()]
        
        a, b = (letters, digits) if len(letters) >= len(digits) else (digits, letters)
        if len(a) - len(b) > 1:
            return ""
        
        res = [None] * (len(digits) + len(letters))
        res[::2] = a
        res[1::2] = b
        return "".join(res)


