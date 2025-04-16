from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)

        while min_k < max_k:
            mid_k = (min_k + max_k) // 2

            total_h = sum(ceil(pile / mid_k) for pile in piles)

            if total_h > h: # if time taken is greater then we have to eat faster
                min_k = mid_k + 1
            else:
                max_k = mid_k # if total_h <= h then we can keep reducing and trying (lower bound)
        
        return min_k


from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = ceil(sum(piles) / h), max(piles)

        while min_k < max_k:
            mid_k = (min_k + max_k) // 2

            total_h = sum(ceil(pile / mid_k) for pile in piles)

            if total_h > h: # if time taken is greater then we have to eat faster
                min_k = mid_k + 1
            else:
                max_k = mid_k # if total_h <= h then we can keep reducing and trying (lower bound)
        
        return min_k

