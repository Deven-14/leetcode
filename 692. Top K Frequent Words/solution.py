class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = Counter(words)
        max_heap = [(-count, key) for key, count in counts.items()]
        heapq.heapify(max_heap)

        keys = []
        while k:
            _, key = heapq.heappop(max_heap)
            keys.append(key)
            k -= 1
        
        return keys
        

# max_heap directly doesn't work because
# ["love","i"]
# count will be correct 
# but the keys also will be in reverse lexicographical order
# we want ["i","love"]
# count should be greatest 
# but the words in lexicograhical order
# so min heap with -count (so max heap)
# but this - min heap will let the words
# be in lexicographical order

