from collections import deque
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        queue = deque([(rCenter, cCenter)])
        visited = set()
        ans = []

        while queue:
            point = queue.popleft()
            if point in visited:
                continue
            
            visited.add(point)
            ans.append(point)

            r, c = point
            r1, c1 = r-1, c-1
            r2, c2 = r+1, c+1
            if r1 >= 0:
                queue.append((r1, c))
            
            if r2 < rows:
                queue.append((r2, c))
            
            if c1 >= 0:
                queue.append((r, c1))
            
            if c2 < cols:
                queue.append((r, c2))
                    
        return ans


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = [(r, c) for r in range(rows) for c in range(cols)]
        ans.sort(key=lambda p: abs(p[0] - rCenter) + abs(p[1] - cCenter))
        return ans