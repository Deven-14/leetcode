from bisect import bisect_left
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = sorted((spell, i) for i, spell in enumerate(spells))
        potions.sort()

        n = len(spells)
        m = len(potions)
        j = m
        pairs = [-1] * n
        for spell, i in sorted_spells:
            j = bisect_left(potions, ceil(success / spell), 0, j)
            if j == n:
                pairs[i] = 0
            elif j == 0:
                pairs = [ele if ele != -1 else m for ele in pairs]
                break
            else:
                pairs[i] = m - j
        
        return pairs


from bisect import bisect_left
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = sorted((spell, i) for i, spell in enumerate(spells))
        potions.sort()

        n = len(spells)
        m = len(potions)
        j = m
        pairs = [-1] * n
        cache = {}
        for spell, i in sorted_spells:
            
            j = bisect_left(potions, ceil(success / spell), 0, j)
            if j == 0:
                pairs = [ele if ele != -1 else m for ele in pairs]
                break
            else:
                pairs[i] = m - j
        
        return pairs


from bisect import bisect_left
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = sorted((spell, i) for i, spell in enumerate(spells))
        potions.sort()

        n = len(spells)
        m = len(potions)
        j = m
        pairs = [-1] * n
        cache = {}
        for spell, i in sorted_spells:
            if spell in cache:
                pairs[i] = cache[spell]
                continue
            
            j = bisect_left(potions, ceil(success / spell), 0, j)
            if j == 0:
                pairs = [ele if ele != -1 else m for ele in pairs]
                break
            
            pairs[i] = m - j
            cache[spell] = pairs[i]
        
        return pairs


from bisect import bisect_left
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = sorted((spell, i) for i, spell in enumerate(spells))
        potions.sort()

        n = len(spells)
        m = len(potions)
        j = m
        pairs = [-1] * n
        for i, (spell, idx) in enumerate(sorted_spells):
            if i > 0 and sorted_spells[i-1][0] == sorted_spells[i][0]:
                pairs[idx] = pairs[sorted_spells[i-1][1]]
                continue
            
            j = bisect_left(potions, ceil(success / spell), 0, j)
            if j == 0:
                pairs = [ele if ele != -1 else m for ele in pairs]
                break
            
            pairs[idx] = m - j
        
        return pairs


# * 70%


from bisect import bisect_left
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        min_pair, max_pair = float("-inf"), float("inf")
        cache = {}
        for i, spell in enumerate(spells):
            if spell in cache:
                pairs[i] = cache[spell]
            
            elif spell < min_pair:
                pairs[i] = 0
            
            elif spell > max_pair:
                pairs[i] = m
            
            else:
                j = bisect_left(potions, ceil(success / spell))
                if j == m:
                    min_pair = max(min_pair, spell)
                elif j == 0:
                    max_pair = min(max_pair, spell)
                
                pairs[i] = m - j
                cache[spell] = pairs[i]
        
        return pairs


# * 97.7%


from bisect import bisect_left
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = [0] * len(spells)
        max_potion, min_potion = potions[-1], potions[0]
        cache = {}

        for i, spell in enumerate(spells):
            req_potion = ceil(success / spell)

            if req_potion > max_potion:
                pairs[i] = 0
            elif req_potion < min_potion:
                pairs[i] = m
            elif spell in cache:
                pairs[i] = cache[spell]
            else:
                j = bisect_left(potions, req_potion)
                pairs[i] = m - j
                cache[spell] = pairs[i]
        
        return pairs