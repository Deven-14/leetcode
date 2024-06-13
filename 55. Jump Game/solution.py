class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        i, last = 0, len(nums)-1

        j = i + nums[i]
        while j < last and nums[i] != 0:
            max_idx = j
            max_jump = j + nums[j]

            for k in range(i + 1, j):
                if (jump := k + nums[k]) > max_jump:
                    max_idx, max_jump = k, jump

            i, j = max_idx, max_jump
        
        if j >= last:
            return True

        return False
