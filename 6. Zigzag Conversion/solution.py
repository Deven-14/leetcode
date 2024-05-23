class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s

        arr = []
        length = len(s)
        v_length = numRows * 2 - 1
        v_gap = v_length - 2

        # first row
        start = 0
        while start < length:
            arr.append(s[start])
            start += v_gap + 1
        v_gap -= 2
        v_reverse_gap = 1

        # between rows
        for i in range(1, numRows-1):
            start = i
            gap = v_gap 
            
            while start < length:
                arr.append(s[start])
                start += gap + 1
                gap = v_gap if gap is not v_gap else v_reverse_gap
            
            v_gap -= 2
            v_reverse_gap += 2

        # last row
        start = numRows-1
        while start < length:
            arr.append(s[start])
            start += v_reverse_gap + 1

        output = "".join(arr)
        return output
