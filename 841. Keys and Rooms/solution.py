from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = { 0 }
        queue = deque(rooms[0])
        n = len(rooms)

        while queue:
            room = queue.popleft()

            if room in visited:
                continue
            
            visited.add(room)
            if len(visited) == n:
                return True
            
            queue.extend(rooms[room])

        return False
