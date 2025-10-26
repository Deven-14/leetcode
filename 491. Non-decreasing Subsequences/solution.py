class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = []
        subsequences_set = set()
        n = len(nums)

        def backtrack(i, subsequence=[]):
            if i > n:
                return
            
            if len(subsequence) > 1 and (t := tuple(subsequence)) not in subsequences_set:
                subsequences.append(list(subsequence))
                subsequences_set.add(t)

            for j in range(i, n):
                if nums[j] >= subsequence[-1]:
                    subsequence.append(nums[j])
                    backtrack(j+1, subsequence)
                    subsequence.pop()

        for i, num in enumerate(nums):
            backtrack(i+1, [num])
        return subsequences


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = []
        subsequences_set = set()
        n = len(nums)

        def backtrack(i, subsequence=[]):
            if i > n:
                return
            
            if len(subsequence) > 1:
                subsequences.append(list(subsequence))

            for j in range(i, n):
                if nums[j] >= subsequence[-1]:
                    subsequence.append(nums[j])
                    backtrack(j+1, subsequence)
                    subsequence.pop()

        for i, num in enumerate(nums):
            backtrack(i+1, [num])
            
        return list({tuple(subsequence) for subsequence in subsequences})
            

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = set()
        n = len(nums)

        def backtrack(i, subsequence=[]):
            if i > n:
                return
            
            if len(subsequence) > 1:
                subsequences.add(tuple(subsequence))

            for j in range(i, n):
                if nums[j] >= subsequence[-1]:
                    subsequence.append(nums[j])
                    backtrack(j+1, subsequence)
                    subsequence.pop()

        for i, num in enumerate(nums):
            backtrack(i+1, [num])

        return [list(x) for x in subsequences]


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = set()
        n = len(nums)

        def backtrack(i, subsequence=[]):
            if len(subsequence) > 1:
                subsequences.add(tuple(subsequence))
            
            if i >= n:
                return

            if not subsequence or nums[i] >= subsequence[-1]:
                subsequence.append(nums[i])
                backtrack(i+1, subsequence)
                subsequence.pop()
            
            backtrack(i+1, subsequence)

        backtrack(0)
        return [list(x) for x in subsequences]



class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = set()
        n = len(nums)

        def backtrack(i, subsequence=[]):
            if len(subsequence) > 1:
                subsequences.add(tuple(subsequence))

            for j in range(i, n):
                if nums[j] >= subsequence[-1]:
                    subsequence.append(nums[j])
                    backtrack(j+1, subsequence)
                    subsequence.pop()

        for i, num in enumerate(nums):
            backtrack(i+1, [num])

        return [list(x) for x in subsequences]