class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        rem_nums = Counter(nums)
        seq_end = Counter()

        for num in nums:
            if not rem_nums[num]:
                continue
            rem_nums[num] -= 1
            if seq_end[num - 1] > 0:
                seq_end[num - 1] -= 1
                seq_end[num] += 1
            elif rem_nums[num + 1] and rem_nums[num + 2]:
                rem_nums[num + 1] -= 1
                rem_nums[num + 2] -= 1
                seq_end[num + 2] += 1
            else:
                return False
        
        return True 