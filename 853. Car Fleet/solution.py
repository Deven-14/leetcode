class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp = list(zip(position, speed))
        pos_sp.sort(reverse=True)

        fleets = 0
        prev_t = 0
        for pos, sp in pos_sp:
            t = (target - pos) / sp
            if t > prev_t:
                fleets += 1
                prev_t = t
        
        return fleets


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp = list(zip(position, speed))
        pos_sp.sort(reverse=True)

        fleets = 0
        prev_t = 0
        for pos, sp in pos_sp:
            if (t := (target - pos) / sp) > prev_t:
                fleets += 1
                prev_t = t
        
        return fleets


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp = list(zip(position, speed))
        pos_sp.sort(reverse=True, key=lambda x: x[0])

        fleets = 0
        prev_t = 0
        for pos, sp in pos_sp:
            t = (target - pos) / sp
            if t > prev_t:
                fleets += 1
                prev_t = t
        
        return fleets


