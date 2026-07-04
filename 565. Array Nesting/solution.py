
# ! 7%, 200ms
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        def dfs(i, cycle):
            if i in cycle:
                return 0
            
            cycle[i] = 1
            if i == nums[i]:
                return 1
            
            cycle[i] = 1 + dfs(nums[i], cycle)
            return cycle[i]
        
        max_count = 0
        cycle = dict()
        for num in nums:
            count = dfs(num, cycle)
            max_count = max(max_count, count)
        
        return max_count


# ! 40% 100ms
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_count = 0
        cycle = set()

        for num in nums:
            count = 0

            while num not in cycle and num != nums[num]:
                cycle.add(num)
                num = nums[num]
                count += 1

            max_count = max(max_count, count)
        
        return max(1, max_count)


# ! 67% 63ms
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)

        while nums_set:
            num = nums_set.pop()
            count = 1

            while nums[num] in nums_set:
                num = nums[num]
                nums_set.remove(num)
                count += 1

            max_count = max(max_count, count)
        
        return max_count


# ! 77% 55ms
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)

        while nums_set and len(nums_set) > max_count:
            num = nums_set.pop()
            count = 1

            while nums[num] in nums_set:
                num = nums[num]
                nums_set.remove(num)
                count += 1

            max_count = max(max_count, count)
        
        return max_count


# * 97% 39ms
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_count = 1
        visited = [False] * len(nums)

        for num in nums:
            if visited[num]:
                continue
            
            count = 1
            visited[num] = True
            while not visited[nums[num]]:
                num = nums[num]
                visited[num] = True
                count += 1

            max_count = max(max_count, count)
        
        return max_count


