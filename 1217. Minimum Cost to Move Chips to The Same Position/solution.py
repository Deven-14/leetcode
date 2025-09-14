from collections import Counter
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counts = Counter(position)
        odds, evens = 0, 0

        for pos, count in counts.items():
            if pos & 1 == 1:
                odds += count
            else:
                evens += count
        
        return min(odds, evens)
