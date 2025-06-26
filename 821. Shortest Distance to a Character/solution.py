class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx = s.find(c)
        distance = list(range(idx, -1, -1))
        start = idx + 1

        while (end := s.find(c, start)) != -1:
            diff = (end - start)
            mid = diff // 2
            distance.extend(range(1, mid+1))
            if diff % 2 == 1:
                distance.append(mid + 1)
            distance.extend(range(mid, -1, -1))
            start = end + 1
        
        diff = len(s) - start
        distance.extend(range(1, diff+1))

        return distance

