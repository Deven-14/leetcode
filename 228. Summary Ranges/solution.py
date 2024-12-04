class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            
            j = i+1
            while j < n and nums[j-1]+1 == nums[j]:
                j += 1
            
            end = nums[j-1]
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{end}")
            
            i = j
        
        return ranges