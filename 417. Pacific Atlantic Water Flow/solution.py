class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_ocean = set()
        atlantic_ocean = set()
        m, n = len(heights), len(heights[0])

        def can_flow(r, c, ocean):
            if (r, c) in ocean:
                return 
            
            ocean.add((r, c))
            height = heights[r][c]
            r1, r2 = r-1, r+1
            c1, c2 = c-1, c+1

            if r2 < m and height <= heights[r2][c]:
                can_flow(r2, c, ocean)
            if r1 >= 0 and height <= heights[r1][c]:
                can_flow(r1, c, ocean)
            if c2 < n and height <= heights[r][c2]:
                can_flow(r, c2, ocean)
            if c1 >= 0 and height <= heights[r][c1]:
                can_flow(r, c1, ocean)
        
        for i in range(m):
            can_flow(i, 0, pacific_ocean)
            can_flow(i, n-1, atlantic_ocean)
        
        for j in range(n):
            can_flow(0, j, pacific_ocean)
            can_flow(m-1, j, atlantic_ocean)
                
        return list(pacific_ocean & atlantic_ocean)

        