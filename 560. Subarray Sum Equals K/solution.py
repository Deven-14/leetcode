class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = Counter()
        count = 0
        curr_sum = 0
        prefix_sums[0] = 1

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            prefix_sums[curr_sum] += 1
        
        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = Counter()
        count = 0
        curr_sum = 0
        prefix_sums[0] = 1

        for num in nums:
            curr_sum += num
            count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1
        
        return count


# reduced to 19ms from 50m (7% to 99.85%)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            count += prefix_sums.get(curr_sum - k, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
        return count

