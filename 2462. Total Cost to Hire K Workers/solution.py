class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []

        i, j = candidates, max(candidates, len(costs) - candidates)
        heap.extend((costs[c], c) for c in range(i))
        heap.extend((costs[c], c) for c in range(j, len(costs)))

        heapq.heapify(heap)

        total_costs = 0
        while k:
            cost, c = heapq.heappop(heap)
            
            total_costs += cost
            if c < i:
                if i < j:
                    heapq.heappush(heap, (costs[i], i))
                    i += 1
            elif c >= j:
                if i < j:
                    j -= 1
                    heapq.heappush(heap, (costs[j], j))
            
            k -= 1
        
        return total_costs



class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []

        i, j = candidates, max(candidates, len(costs) - candidates)
        heap.extend((costs[c], c) for c in range(i))
        heap.extend((costs[c], c) for c in range(j, len(costs)))

        heapq.heapify(heap)

        total_costs = 0
        while k:
            cost, c = heapq.heappop(heap)
            
            total_costs += cost
            if i < j:
                if c < i:
                    heapq.heappush(heap, (costs[i], i))
                    i += 1
                elif c >= j:
                    j -= 1
                    heapq.heappush(heap, (costs[j], j))
            
            k -= 1
        
        return total_costs


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []

        i, j = candidates, max(candidates, len(costs) - candidates)
        heap.extend((costs[c], c) for c in range(i))
        heap.extend((costs[c], c) for c in range(j, len(costs)))

        heapq.heapify(heap)

        total_costs = 0
        while k:
            cost, c = heapq.heappop(heap)
            total_costs += cost
            k -= 1
            if i >= j:
                break
            
            if c < i:
                heapq.heappush(heap, (costs[i], i))
                i += 1
            elif c >= j:
                j -= 1
                heapq.heappush(heap, (costs[j], j))
            
        while k:
            cost, c = heapq.heappop(heap)
            total_costs += cost
            k -= 1
        
        return total_costs


# * 30-40%
# * comparing tuples in costlier than comparing integers (in heap operations)

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i, j = candidates, max(candidates, len(costs) - candidates)
        lheap = costs[:i]
        rheap = costs[j:]

        heapq.heapify(lheap)
        heapq.heapify(rheap)

        total_costs = 0
        while k and lheap and rheap:
            if lheap[0] <= rheap[0]:
                cost = heapq.heappop(lheap)
                total_costs += cost

                if i < j:
                    heapq.heappush(lheap, costs[i])
                    i += 1
            else:
                cost = heapq.heappop(rheap)
                total_costs += cost

                if i < j:
                    j -= 1
                    heapq.heappush(rheap, costs[j])
            
            k -= 1
        
        while k and lheap:
            cost = heapq.heappop(lheap)
            total_costs += cost
            k -= 1
        
        while k and rheap:
            cost = heapq.heappop(rheap)
            total_costs += cost
            k -= 1
        
        return total_costs



class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i, j = candidates, max(candidates, len(costs) - candidates)
        lheap = costs[:i]
        rheap = costs[j:]

        heapq.heapify(lheap)
        heapq.heapify(rheap)

        total_costs = 0
        while k and lheap and rheap:
            if lheap[0] <= rheap[0]:
                cost = heapq.heappop(lheap)
                total_costs += cost

                if i < j:
                    heapq.heappush(lheap, costs[i])
                    i += 1
            else:
                cost = heapq.heappop(rheap)
                total_costs += cost

                if i < j:
                    j -= 1
                    heapq.heappush(rheap, costs[j])
            
            k -= 1
        
        heap = lheap or rheap
        while k and heap:
            cost = heapq.heappop(heap)
            total_costs += cost
            k -= 1
        
        return total_costs



class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if n < (2 * candidates + k): # every element is touched, so we can just use sort
            costs.sort()
            return sum(costs[:k])

        i, j = candidates, len(costs) - candidates
        lheap = costs[:i]
        rheap = costs[j:]

        heapq.heapify(lheap)
        heapq.heapify(rheap)

        total_costs = 0
        while k:
            if lheap[0] <= rheap[0]:
                cost = heapq.heapreplace(lheap, costs[i])
                total_costs += cost
                i += 1
                
            else:
                j -= 1
                cost = heapq.heapreplace(rheap, costs[j])
                total_costs += cost
            
            k -= 1
        
        return total_costs