class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        prev_end = -1
        poisoned_duration = 0

        for t1 in timeSeries:
            t2 = t1 + duration - 1
            t1 = max(t1, prev_end + 1)
            poisoned_duration += (t2 - t1 + 1)
            prev_end = t2
        
        return poisoned_duration


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        t1 = timeSeries[0]
        poisoned_duration = 0

        for i in range(1, len(timeSeries)):
            t2 = timeSeries[i]
            if t2 - t1 >= duration:
                poisoned_duration += duration
            else:
                poisoned_duration += t2 - t1
            t1 = t2

        poisoned_duration += duration
        return poisoned_duration
