from itertools import product
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        heap = [(nums1[i]+nums2[0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        pairs = []

        while len(pairs) < k:
            _, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            j += 1
            if j < m:
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
        
        return pairs

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        heap = [(nums1[0]+nums2[0], 0, 0)]
        heapq.heapify(heap)
        pairs = []

        while k:
            _, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            
            if j+1 < m:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
            
            if j == 0 and i+1 < n:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
            
            k -= 1
        
        return pairs