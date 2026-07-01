class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(arr) == Counter(target)


# reversing the order
# if we consider sub array of size 2
# then reversing == swap
# if we can swap any 2 eles next to each other
# then you can move any ele to any position
# we only have to check if we have the 
# number of elements