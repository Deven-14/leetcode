import string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ascii_letters = set(string.ascii_letters)
        letters = list(s)

        n = len(s)
        i, j = 0, n-1
        while i < n and letters[i] not in ascii_letters:
            i += 1

        while i < j and letters[j] not in ascii_letters:
            j -= 1

        while i < j:
            letters[i], letters[j] = letters[j], letters[i]
            i += 1
            j -= 1

            while letters[i] not in ascii_letters:
                i += 1
            
            while letters[j] not in ascii_letters:
                j -= 1
        
        return "".join(letters)