class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, n = 0, len(data)

        while i < n:
            
            if (data[i] >> 7) == 0:
                i += 1
                continue
            
            if (data[i] >> 6) < 3 or (data[i] >> 3) > 30:
                return False

            bin_data = bin(data[i])[2:]
            j = 0

            ones = 0
            while j < 8 and bin_data[j] == '1':
                ones += 1
                j += 1
            
            ones -= 1
            i += 1
            while i < n and ones and (data[i] >> 6) == 2:
                i += 1
                ones -= 1
            
            if ones:
                return False
        
        return True

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, n = 0, len(data)

        while i < n:
            
            if (data[i] >> 7) == 0:
                i += 1
                continue
            
            if (data[i] >> 6) < 3 or (data[i] >> 3) > 30:
                return False

            if (data[i] >> 4) == 15:
                ones = 3
            elif (data[i] >> 5) == 7:
                ones = 2
            else:
                ones = 1
            
            i += 1
            while i < n and ones and (data[i] >> 6) == 2:
                i += 1
                ones -= 1
            
            if ones:
                return False
        
        return True

