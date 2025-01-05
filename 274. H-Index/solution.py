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


import heapq
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_index = 0
        n = len(citations)
        for citation in citations:
            if citation > n:
                h_index = max(h_index, n)
            else:
                h_index = max(h_index, citation)
            n -= 1
        
        return h_index


# sorting method, O(nlogn) time complexity, O(1) space complexity
import heapq
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for citation in citations:
            if citation >= n:
                return n
            n -= 1
        
        return 0


# counting method, O(n) time complexity, O(n) space complexity
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n_papers = len(citations)
        n_papers_by_citations = [0] * (n_papers + 1)

        for citation in citations:
            n_papers_by_citations[min(citation, n_papers)] += 1
        
        cummulative_papers = 0
        n = len(n_papers_by_citations)
        for n_cited in range(n-1, -1, -1):
            cummulative_papers += n_papers_by_citations[n_cited]
            if cummulative_papers >= n_cited:
                return n_cited