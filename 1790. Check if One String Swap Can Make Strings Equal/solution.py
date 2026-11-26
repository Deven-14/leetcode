class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        diffs = [(a, b) for a, b in zip(s1, s2) if a != b]
        if len(diffs) != 2:
            return False
        
        return diffs[0][0] == diffs[1][1] and diffs[0][1] == diffs[1][0]
