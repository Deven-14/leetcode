from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        digits = Counter()
        chars = Counter(s)
        digits_map = [('z', '0', 'zero'), ('w', '2', 'two'), ('u', '4', 'four'), ('x', '6', 'six'), ('g', '8', 'eight'), ('o', '1', 'one'), ('h', '3', 'three'), ('f', '5', 'five'), ('s', '7', 'seven'), ('i', '9', 'nine')]

        for (unique_char, digit, digit_word) in digits_map:
            count = chars[unique_char]
            if count > 0:
                digits[digit] = count
                for char in digit_word:
                    chars[char] -= count
        
        return "".join([digit * digits[digit] for digit in '0123456789'])
        

from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        chars = Counter(s)
        digits = [0] * 10
        
        digits[0] = chars['z']
        digits[2] = chars['w']
        digits[4] = chars['u']
        digits[6] = chars['x']
        digits[8] = chars['g']
        digits[1] = chars['o'] - digits[0] - digits[2] - digits[4]
        digits[3] = chars['h'] - digits[8]
        digits[5] = chars['f'] - digits[4]
        digits[7] = chars['s'] - digits[6]
        digits[9] = chars['i'] - digits[6] - digits[8] - digits[5]
        
        return "".join([str(digit) * digits[digit] for digit in range(10)])


from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        chars = Counter(s)
        digits = {}
        
        digits['0'] = chars['z']
        digits['2'] = chars['w']
        digits['4'] = chars['u']
        digits['6'] = chars['x']
        digits['8'] = chars['g']
        digits['1'] = chars['o'] - digits['0'] - digits['2'] - digits['4']
        digits['3'] = chars['h'] - digits['8']
        digits['5'] = chars['f'] - digits['4']
        digits['7'] = chars['s'] - digits['6']
        digits['9'] = chars['i'] - digits['6'] - digits['8'] - digits['5']
        
        return "".join([digit * digits[digit] for digit in '0123456789'])
        