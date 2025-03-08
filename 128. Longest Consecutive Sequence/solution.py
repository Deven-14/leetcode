class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        parents = {}
        counts = {}

        def get_collapsing_parent(num):
            if num not in parents:
                return None
            
            if parents[num] is None:
                return num
            
            curr = num
            while parents[curr] is not None:
                curr = parents[curr]
            
            parent = curr
            while parents[num] is not None:
                temp = parents[num]
                parents[num] = parent
                num = temp
            
            return parent


        for num in nums: 
            if num in parents:
                continue

            parents[num] = None
            counts[num] = 1

            if (parent := get_collapsing_parent(num-1)) is not None:
                parents[num] = parent
                counts[parent] += 1
            else:
                parent = num
            
            if (child := num+1) in parents:
                parents[child] = parent
                counts[parent] += counts[child]
                counts[child] = 1
            
            longest_length = max(longest_length, counts[parent])
    
        return longest_length


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        parents = {}
        counts = {}

        def get_collapsing_parent(num):
            if num not in parents:
                return None
            
            if parents[num] is None:
                return num
            
            while parents[num] is not None:
                num = parents[num]

            return num


        for num in nums: 
            if num in parents:
                continue

            parents[num] = None
            counts[num] = 1

            if (parent := get_collapsing_parent(num-1)) is not None:
                parents[num] = parent
                counts[parent] += 1
            else:
                parent = num
            
            if (child := num+1) in parents:
                parents[child] = parent
                counts[parent] += counts[child]
                counts[child] = 1
            
            longest_length = max(longest_length, counts[parent])
    
        return longest_length


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest_length = 1
        consecutive_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                consecutive_length += 1
            elif nums[i] != nums[i-1]:
                longest_length = max(consecutive_length, longest_length)
                consecutive_length = 1
        
        longest_length = max(consecutive_length, longest_length)
        return longest_length


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in nums:
                count = 1
                while (num + count) in num_set:
                    count += 1
                longest = max(longest, count)
        
        return longest

# above will time out as for num in nums, it should be for num in num_set (to remove duplicates)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num-1) not in num_set:
                count = 1
                while (num + count) in num_set:
                    count += 1
                longest = max(longest, count)
        
        return longest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num-1) not in num_set:
                next_num = num + 1
                while next_num in num_set:
                    next_num += 1
                count = next_num - num
                longest = max(longest, count)
        
        return longest
        