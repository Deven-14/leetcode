from itertools import zip_longest
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        
        for abit, bbit, cbit, rbit in zip_longest(format(a, 'b')[::-1], format(b, 'b')[::-1], format(c, 'b')[::-1], format(((a | b) ^ c), 'b')[::-1], fillvalue = '0'):
            if rbit == '1':
                if cbit == '1':
                    count += 1
                elif abit == '0' or bbit == '0':
                    count += 1
                else:
                    count += 2
        
        return count


from itertools import zip_longest
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        
        rbits = format(((a | b) ^ c), 'b')
        n = len(rbits)
        abits = format(a, f'0{n}b')
        bbits = format(b, f'0{n}b')
        cbits = format(c, f'0{n}b')

        for i in range(-1, -n-1, -1):
            if rbits[i] == '1':
                if cbits[i] == '1':
                    count += 1
                elif abits[i] == '0' or bbits[i] == '0':
                    count += 1
                else:
                    count += 2
        
        return count


