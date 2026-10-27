class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        return Counter(sum(int(n) for n in str(num)) for num in range(lowLimit, highLimit + 1)).most_common(1)[0][1]