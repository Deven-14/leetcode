from itertools import groupby
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for k, g in groupby(s):
            match k:
                case 'A':
                    absent += len(list(g))
                    if absent >= 2: return False
                case 'L':
                    if len(list(g)) >= 3:
                        return False
        
        return True


from itertools import groupby
class Solution:
    def checkRecord(self, s: str) -> bool:
        t = s.split("A")
        if len(t) > 2:
            return False
        
        t = s.split("LLL")
        if len(t) > 1:
            return False
        
        return True