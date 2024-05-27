class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = [ # * Instead of using a dictionary to map int to roman, since there are only few values, we can use arrays and tuples directly.
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        roman_num = ""

        for value, symbol in int_to_roman:
            quotient, num = divmod(num, value)
            roman_num += quotient * symbol
        
        return roman_num