
# * best solution
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [ele for ele, count in Counter(nums).most_common(k)]

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(count, ele) for ele, count in Counter(nums).items()]
        heapq.heapify(heap)
        return [ele for _, ele in heapq.nlargest(k, heap)] # or with -count and heappop until k