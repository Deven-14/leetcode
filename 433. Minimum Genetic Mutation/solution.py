from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        bank = set(bank)
        visited = set()

        if endGene not in bank:
            return -1

        while queue:
            gene, count = queue.popleft()
            visited.add(gene)
            if gene == endGene:
                return count
            
            chars = list(gene)
            for i in range(8):
                t = chars[i]
                for char in 'ACGT':
                    chars[i] = char
                    modified_gene = "".join(chars)
                    if modified_gene in bank and modified_gene not in visited:
                        queue.append((modified_gene, count + 1))
                chars[i] = t

        return -1
