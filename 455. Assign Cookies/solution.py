class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        n, m = len(g), len(s)
        count = 0

        while i < n and j < m:
            if s[j] >= g[i]:
                count += 1
                j += 1
                i += 1
            else:
                j += 1
        
        return count
    

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        n, m = len(g), len(s)
        count = 0

        while i < n and j < m:
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        
        return count