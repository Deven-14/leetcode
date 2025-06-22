from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = Counter(stones)
        total = 0
        for jewel in jewels:
            total += counts[jewel]
        return total