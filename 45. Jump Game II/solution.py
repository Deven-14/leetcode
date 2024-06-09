class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        i, last = 0, len(nums)-1

        n_jump = 1
        j = i + nums[i]
        while j < last:
            max_idx = j
            max_jump = j + nums[j]

            for k in range(i + 1, j):
                if (jump := k + nums[k]) > max_jump:
                    max_idx, max_jump = k, jump

            i, j = max_idx, max_jump
            n_jump += 1
        
        return n_jump
