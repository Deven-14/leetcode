class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
            
        base7 = []

        is_negative = False
        if num < 0:
            num = -num
            is_negative = True
        
        while num:
            num, digit = divmod(num, 7)
            base7.append(str(digit))
        
        if is_negative:
            base7.append("-")
        
        base7.reverse()
        return "".join(base7)
