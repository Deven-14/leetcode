class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        strn = str(n)[::-1]
        m = (len(strn) - 1) // 3

        dotstr = ""
        i = 0

        while m:
            dotstr += strn[i:i + 3] + "."
            i += 3
            m -= 1
        dotstr += strn[i:]
        
        return dotstr[::-1]
    
class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(',', '.')