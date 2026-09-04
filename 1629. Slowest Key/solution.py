class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        long_key = keysPressed[0]
        long_time = releaseTimes[0]
        prev = 0

        for k, t in zip(keysPressed, releaseTimes):
            if (diff := t - prev) > long_time or (diff == long_time and k > long_key):
                long_key = k
                long_time = diff
            prev = t
        
        return long_key

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max(
            (t2 - t1, k) 
            for t1, t2, k in zip(chain([0], releaseTimes), releaseTimes, keysPressed)
        )[1]

