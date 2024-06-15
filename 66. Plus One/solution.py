class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        new_digits = [0] + digits
        i = len(new_digits) - 1
        while new_digits[i] == 9:
            new_digits[i] = 0
            i -= 1
        
        new_digits[i] += 1
        if new_digits[0] == 0:
            return new_digits[1:]
        
        return new_digits