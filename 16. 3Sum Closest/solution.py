class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_to_target = nums[0] + nums[1] + nums[2]
        diff = abs(target - closest_to_target)
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if target >= 0 and nums[i] > target:
                break
            
            j, k = i+1, n-1
            while j < k:
                sum_i_j_k = nums[i] + nums[j] + nums[k]
                curr_diff = abs(target - sum_i_j_k)
                
                if curr_diff < diff:
                    diff = curr_diff
                    closest_to_target = sum_i_j_k
                
                if sum_i_j_k > target:
                    k -= 1
                elif sum_i_j_k < target:
                    j += 1
                else:
                    return target
        
        return closest_to_target