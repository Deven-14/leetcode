class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_arr = list(accumulate(arr, initial=0))
        n = len(arr)
        total_sum = 0

        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                total_sum += prefix_arr[i + l] - prefix_arr[i]
        
        return total_sum


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        return sum(
            (((i + 1) * (n - i) + 1) // 2) * arr[i]
            for i in range(n)
        )

# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/solutions/854184/javacpython-on-time-o1-space-by-lee215-xiqz