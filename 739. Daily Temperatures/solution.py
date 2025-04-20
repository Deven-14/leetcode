class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        answer = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while monotonic_stack and temperature > temperatures[monotonic_stack[-1]]:
                idx = monotonic_stack.pop()
                answer[idx] = i - idx
            monotonic_stack.append(i)

        return answer