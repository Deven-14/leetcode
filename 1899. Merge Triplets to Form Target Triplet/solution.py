class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        a1, b1, c1 = 0, 0, 0

        for a2, b2, c2 in triplets:
            if a2 <= x and b2 <= y and c2 <= z:
                a1, b1, c1 = max(a1, a2), max(b1, b2), max(c1, c2)
            if a1 == x and b1 == y and c1 == z:
                return True
        
        return False
        
