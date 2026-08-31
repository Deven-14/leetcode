class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_occr = { }
        first_occr = { }
        for i, c in enumerate(s):
            if c not in first_occr:
                first_occr[c] = i
            last_occr[c] = i
        
        max_diff = -1
        for c in string.ascii_lowercase:
            if c in first_occr and first_occr[c] != last_occr[c]:
                max_diff = max(max_diff, last_occr[c] - first_occr[c] - 1)
        
        return max_diff