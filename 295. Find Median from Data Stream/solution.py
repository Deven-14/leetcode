import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []        

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return
        
        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        n, m = len(self.max_heap), len(self.min_heap)
        if n > (m+1):
            max_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_num)
        elif m > (n+1):
            min_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_num)
        
    def findMedian(self) -> float:
        n, m = len(self.max_heap), len(self.min_heap)
        if n == m:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        return -self.max_heap[0] if n > m else self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []        

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            max_num = -heapq.heappushpop(self.max_heap, -num)
            heapq.heappush(self.min_heap, max_num)
        else:
            min_num = heapq.heappushpop(self.min_heap, num)
            heapq.heappush(self.max_heap, -min_num)
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()