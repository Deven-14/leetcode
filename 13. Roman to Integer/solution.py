class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        num = roman_to_int[s[0]]
        prev = num

        for symbol in s[1:]:
            value = roman_to_int[symbol]
            if value > prev:
                num -= 2 * prev
            num += value
            prev = value
        
        return num

# * since the current value depends on the next value and not the previous value, we should prefer using that instead of the previous value for better performance.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        
        num = 0

        for i in range(len(s)-1):
            curr_val, next_val = roman_to_int[s[i]], roman_to_int[s[i+1]]
            if curr_val < next_val:
                num -= curr_val
            else:
                num += curr_val
        
        num += roman_to_int[s[-1]]

        return num
