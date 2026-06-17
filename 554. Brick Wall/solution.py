
# ! out of memory
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        wall_width = sum(wall[0])
        bricks_edges = [0] * (wall_width + 1)

        for wall_row in wall:
            j = 0

            for brick_width in wall_row:
                j += brick_width
                bricks_edges[j] += 1
                        
        return n - max(bricks_edges[:-1])
            
      
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        brick_edges = Counter()

        for wall_row in wall:
            brick_edge = 0
            for brick_width in wall_row:
                brick_edge += brick_width
                brick_edges[brick_edge] += 1
        
        del brick_edges[brick_edge] # last edge
        if not brick_edges:
            return n
        
        max_brick_edges_crossed = brick_edges.most_common(1)[0][1]
        min_crossed_bricks = n - max_brick_edges_crossed
        return min_crossed_bricks
        

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        brick_edges = Counter()

        for wall_row in wall:
            brick_edge = 0
            for brick_width in wall_row:
                brick_edge += brick_width
                brick_edges[brick_edge] += 1
        
        del brick_edges[brick_edge] # last edge
        if not brick_edges:
            return n
        
        max_brick_edges_crossed = max(brick_edges.values())
        min_crossed_bricks = n - max_brick_edges_crossed
        return min_crossed_bricks
        