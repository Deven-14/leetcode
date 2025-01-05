class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        h_index = 0

        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= (n-mid):
                h_index = max(h_index, n-mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return h_index