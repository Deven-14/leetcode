class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        laps = sum(
            rounds[i] - rounds[i - 1] if rounds[i] > rounds[i - 1] else (n - rounds[i - 1] + rounds[i])
            for i in range(1, len(rounds))
        )
        last_lap_completed_sectors = laps % n

        return sorted(
            rounds[0] + i if rounds[0] + i <= n else (rounds[0] + i) % n
            for i in range(last_lap_completed_sectors + 1)
        )


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first = rounds[0]
        last = rounds[-1]

        if last >= first:
            return list(range(first, last + 1))
        
        return list(range(1, last + 1)) + list(range(first, n + 1))

