class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise_distance, counter_clockwise_distance = 0, 0
        
        idx = start
        n = len(distance)
        while idx != destination:
            clockwise_distance += distance[idx]
            idx = (idx + 1) % n
        
        idx = destination
        n = len(distance)
        while idx != start:
            counter_clockwise_distance += distance[idx]
            idx = (idx + 1) % n
        
        return min(clockwise_distance, counter_clockwise_distance)


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance = sum(distance)

        if start <= destination:
            d1 = sum(distance[start:destination])
            d2 = total_distance - d1
        else:
            d1 = sum(distance[destination:start])
            d2 = total_distance - d1
        
        return min(d1, d2)


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        d1 = sum(distance[start:destination])
        d2 = sum(distance[:start]) + sum(distance[destination:])
        return min(d1, d2)


