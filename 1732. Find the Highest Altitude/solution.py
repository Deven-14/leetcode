class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0

        for alt_gain in gain:
            altitude += alt_gain
            if altitude > max_altitude:
                max_altitude = altitude
        
        return max_altitude


from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))