class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        count = 0
        for s in zip(*strs):
            if any(s[i-1] > s[i] for i in range(1, n)):
                count += 1
        return count


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        return sum(1 for s in zip(*strs) if any(s[i-1] > s[i] for i in range(1, n)))


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        return sum(any(s[i-1] > s[i] for i in range(1, n)) for s in zip(*strs))


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(s) != sorted(s) for s in zip(*strs))


