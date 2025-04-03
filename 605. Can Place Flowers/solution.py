from itertools import groupby
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0
        groups = [(k, list(g)) for k, g in groupby(flowerbed)]

        if len(groups) == 1 and groups[0][0] == 0:
            x = len(groups[0][1])
            if x % 2 == 1:
                x += 1
            empty += x // 2
            return empty >= n
        
        if groups[0][0] == 0:
            x = len(groups[0][1])
            if x % 2 == 0:
                x += 1
            empty += x // 2

        for i in range(1, len(groups)-1):
            if groups[i][0] == 0:
                x = len(groups[i][1])
                if x % 2 == 0:
                    x -= 1
                empty += x // 2
            
        if len(groups) > 1 and groups[-1][0] == 0:
            x = len(groups[-1][1])
            if x % 2 == 0:
                x += 1
            empty += x // 2
        
        return empty >= n


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        last = l-1
        for i in range(l):
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == last) or (flowerbed[i+1] == 0)

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            
            if n <= 0:
                return True
        
        return n <= 0


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        flowerbed = [0, *flowerbed, 0]
        for i in range(1, l+1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            if n <= 0:
                return True
        
        return n <= 0


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        flowerbed = [0, *flowerbed, 0]
        for i in range(1, l+1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0