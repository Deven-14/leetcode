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
            
            for j in range(i+1, n-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                sum_i_j = nums[i] + nums[j]
                if target >= 0 and sum_i_j > target:
                    break
                
                left, right = j+1, n-1
                while left <= right:
                    mid = (left + right) // 2
                    sum_i_j_k = sum_i_j + nums[mid]
                    curr_diff = abs(target - sum_i_j_k)
                    
                    if curr_diff < diff:
                        diff = curr_diff
                        closest_to_target = sum_i_j_k
                    
                    if sum_i_j_k > target:
                        right = mid-1
                    elif sum_i_j_k < target:
                        left = mid+1
                    else:
                        return target
        
        return closest_to_target