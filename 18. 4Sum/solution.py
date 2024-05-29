class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_set = set(nums)
        nums.sort()
        quadruplets = []
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if target > 0 and nums[i] > target:
                break
            
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                sum_i_j = nums[i] + nums[j]
                if target > 0 and sum_i_j > target:
                    break

                for k in range(j+1, n-1):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    
                    sum_i_j_k = sum_i_j + nums[k]
                    if target > 0 and sum_i_j_k > target:
                        break

                    rem = target - sum_i_j_k
                    if rem in nums_set and (rem > nums[k] or rem == nums[k+1]):
                        quadruplets.append([nums[i], nums[j], nums[k], rem])
        
        return quadruplets


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if target > 0 and nums[i] > target:
                break
            
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                sum_i_j = nums[i] + nums[j]
                if target > 0 and sum_i_j > target:
                    break

                k, l = j+1, n-1
                while k < l:
                    sum_i_j_k_l = sum_i_j + nums[k] + nums[l]
                    if sum_i_j_k_l > target:
                        l -= 1
                    elif sum_i_j_k_l < target:
                        k += 1
                    else:
                        quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < n and nums[k] == nums[k-1]:
                            k += 1
                        while l > 0 and nums[l] == nums[l+1]:
                            l -= 1

        return quadruplets