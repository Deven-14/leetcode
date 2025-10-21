class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"
        freq_idx = 2
        num = 1

        while len(s) < n:
            freq = int(s[freq_idx])
            if num == 1 and freq == 1:
                s += "1"
                num = 2
            elif num == 2 and freq == 2:
                s += "22"
                num = 1
            elif num == 2 and freq == 1:
                s += "2"
                num = 1
            elif num == 1 and freq == 2:
                s += "11"
                num = 2

            freq_idx += 1
        
        return s[:n].count('1')


class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        freq_idx = 2
        num = 1

        while len(s) < n:
            freq = s[freq_idx]
            if num == 1 and freq == 1:
                s.append(1)
                num = 2
            elif num == 2 and freq == 2:
                s.append(2)
                s.append(2)
                num = 1
            elif num == 2 and freq == 1:
                s.append(2)
                num = 1
            elif num == 1 and freq == 2:
                s.append(1)
                s.append(1)
                num = 2

            freq_idx += 1
        
        return s[:n].count(1)