class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        nums.sort()
        triplets = []
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0: # * stop iterating if the first num is positive as nums ahead will all positive (sorted list) and the sum will be > 0
                break
            
            for j in range(i+1, n-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                sum_i_j = nums[i] + nums[j]
                if sum_i_j > 0: # * stop iterating if the sum is positive as nums ahead will all positive (sorted list) and the sum will be > 0
                    break

                rem = -sum_i_j
                if rem in nums_set and (rem > nums[j] or rem == nums[j+1]): # * here binary search can also be applied
                    triplets.append([nums[i], nums[j], rem])
        
        return triplets
