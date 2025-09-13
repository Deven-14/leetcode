from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        pairs = defaultdict(list)
        min_diff = float("inf")

        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            pairs[diff].append([arr[i-1], arr[i]])
            min_diff = min(diff, min_diff)
        
        return pairs[min_diff]


from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        pairs = []
        min_diff = float("inf")

        for i in range(1, len(arr)):
            if (diff := abs(arr[i] - arr[i-1])) < min_diff:
                pairs = [[arr[i-1], arr[i]]]
                min_diff = min(diff, min_diff)

            elif diff == min_diff:
                pairs.append([arr[i-1], arr[i]])

        return pairs
    

from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        pairs = []
        min_diff = float("inf")

        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff > min_diff:
                continue

            elif diff < min_diff:
                pairs = [[arr[i-1], arr[i]]]
                min_diff = min(diff, min_diff)

            elif diff == min_diff:
                pairs.append([arr[i-1], arr[i]])

        return pairs


from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        pairs = []
        min_diff = float("inf")

        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff > min_diff:
                continue

            elif diff < min_diff:
                pairs = [[arr[i-1], arr[i]]]
                min_diff = diff 

            elif diff == min_diff:
                pairs.append([arr[i-1], arr[i]])

        return pairs


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        pairs = []
        min_diff = float("inf")

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff > min_diff:
                continue

            elif diff < min_diff:
                pairs = [[arr[i-1], arr[i]]]
                min_diff = diff 

            elif diff == min_diff:
                pairs.append([arr[i-1], arr[i]])

        return pairs