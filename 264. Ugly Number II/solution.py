import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        ugly_nums = set()
        
        while len(ugly_nums) < n:
            num = heappop(heap)
            if num in ugly_nums:
                continue
            ugly_nums.add(num)
            heappush(heap, num * 2)
            heappush(heap, num * 3)
            heappush(heap, num * 5)
        
        return num


import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set([1])
        ugly_nums = 0
        
        while ugly_nums < n:
            num = heappop(heap)
            ugly_nums += 1
            if (m := num * 2) not in visited:
                heappush(heap, m)
                visited.add(m)
            if (m := num * 3) not in visited:
                heappush(heap, m)
                visited.add(m)
            if (m := num * 5) not in visited:
                heappush(heap, m)
                visited.add(m)
        
        return num


# https://leetcode.com/problems/ugly-number-ii/solutions/5649364/ugly-number-ii

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1

        idx_mul_of_2, idx_mul_of_3, idx_mul_of_5 = 0, 0, 0
        next_mul_of_2, next_mul_of_3, next_mul_of_5 = 2, 3, 5

        for i in range(1, n):
            next_ugly_num = min(next_mul_of_2, next_mul_of_3, next_mul_of_5)
            ugly_nums[i] = next_ugly_num

            if next_ugly_num == next_mul_of_2:
                idx_mul_of_2 += 1
                next_mul_of_2 = ugly_nums[idx_mul_of_2] * 2
            if next_ugly_num == next_mul_of_3:
                idx_mul_of_3 += 1
                next_mul_of_3 = ugly_nums[idx_mul_of_3] * 3
            if next_ugly_num == next_mul_of_5:
                idx_mul_of_5 += 1
                next_mul_of_5 = ugly_nums[idx_mul_of_5] * 5

        return ugly_nums[n-1]