class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = medium = float("inf")

        for large in nums:
            if large <= small:
                small = large
            elif large <= medium:
                medium = large
            else: 
                return True
        
        return False

# this solution is possible because
# ex: 5, 6, 4, 7
# small = 5, medium = 6, large = 4
# when this happens small becomes 4, 
# then large = 7 and large > 4 and 6
# but then here index order is wrong 2, 1, 3
# but if we notice, since we didn't remove medium, there existed a small < medium before small changed to 4
# and hence for that large = 7 and medium = 6, small = 4, 7 > 6 also implies there existed some small < 6 before medium's index (1) and hence medium exists