class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub_sequence = [nums[0]]
        
        def binary_search(ele):
            l, r = 0, len(sub_sequence)-1

            while l <= r:
                mid = (l+r) // 2
                if sub_sequence[mid] == ele:
                    return mid
                elif sub_sequence[mid] < ele:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return l
        
        for i in range(1, len(nums)):
            if sub_sequence[-1] < nums[i]:
                sub_sequence.append(nums[i])
            else:
                idx = binary_search(nums[i])
                sub_sequence[idx] = nums[i]
        
        return len(sub_sequence)
        