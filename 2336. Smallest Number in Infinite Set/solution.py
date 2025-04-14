import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.queue = []
        self.queue_set = set()

    def popSmallest(self) -> int:
        if not self.queue:
            ele = self.smallest
            self.smallest += 1
            return ele
        
        ele = heapq.heappop(self.queue)
        self.queue_set.remove(ele)
        return ele

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.queue_set:
            heapq.heappush(self.queue, num)
            self.queue_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)