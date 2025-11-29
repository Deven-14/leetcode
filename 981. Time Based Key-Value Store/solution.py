from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append(value)
        self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.time[key], timestamp)
        return "" if idx == 0 else self.map[key][idx-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)