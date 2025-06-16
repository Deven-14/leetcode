import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        
        heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
        if len(self.heap) < k:
            heapq.heappush(self.heap, float("-inf"))

    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.heap = nums[-k:]
        
        if len(self.heap) < k:
            heapq.heappush(self.heap, float("-inf"))

    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)