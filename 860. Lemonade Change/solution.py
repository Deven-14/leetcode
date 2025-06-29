class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5, change10 = 0, 0
        i, n = 0, len(bills)

        while i < n and change5 >= 0 and change10 >= 0:
            match bills[i]:
                case 5:
                    change5 += 1
                case 10:
                    change5 -= 1
                    change10 += 1
                case 20:
                    change5 -= 1
                    if change10 > 0:
                        change10 -= 1
                    else:
                        change5 -= 2
            i += 1
        
        return i == n and change5 >= 0 and change10 >= 0
    


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5, change10 = 0, 0
        i, n = 0, len(bills)

        while i < n and change5 >= 0 and change10 >= 0:
            match bills[i]:
                case 5:
                    change5 += 1
                case 10:
                    change5 -= 1
                    change10 += 1
                case 20 if change10 > 0:
                    change5 -= 1
                    change10 -= 1
                case 20:
                    change5 -= 3
            i += 1
        
        return i == n and change5 >= 0 and change10 >= 0
    


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5, change10 = 0, 0
        i, n = 0, len(bills)

        while i < n and change5 >= 0 and change10 >= 0:
            match bills[i]:
                case 5:
                    change5 += 1
                case 10:
                    change5 -= 1
                    change10 += 1
                case 20 if change10 > 0:
                    change5 -= 1
                    change10 -= 1
                case _:
                    change5 -= 3
            i += 1
        
        return i == n and change5 >= 0 and change10 >= 0