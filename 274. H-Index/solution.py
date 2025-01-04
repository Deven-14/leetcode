import heapq
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        heapq.heapify(citations)
        n = len(citations)

        while citations:
            citation = heapq.heappop(citations)
            if citation > n:
                h_index = max(h_index, n)
            else:
                h_index = max(h_index, citation)
            n -= 1
                
        return h_index
            