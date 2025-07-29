from bisect import bisect_left
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        idx = 0
        n = len(heaters)
        max_d = 0

        for house in houses:
            idx = bisect_left(heaters, house, idx)
            if idx == n:
                max_d = max(max_d, house - heaters[idx-1])
            elif idx == 0:
                max_d = max(max_d, heaters[idx] - house)
            else:
                max_d = max(max_d, min(house - heaters[idx-1], heaters[idx] - house))
        
        return max_d


from bisect import bisect_left
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.append(float('inf'))
        heaters.append(float('-inf'))
        heaters.sort()
        houses.sort()

        idx = 0
        max_d = 0

        for house in houses:
            while heaters[idx] < house:
                idx += 1
            max_d = max(max_d, min(house - heaters[idx-1], heaters[idx] - house))
        
        return max_d

