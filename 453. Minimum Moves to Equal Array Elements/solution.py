class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)


# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/comments/1576546/

# Let's imagine the first element setting an initial task for itself - I have to catch up with my neighbor (i.e. second) element. So what does it do - increments itself and all other elements, except the second one of course, by the exact difference between itself and the second element.

# If the array was "1, 5, 6, 7" then the array change to "5 5 10 11".

# Next, the first element expands it's horizons a bit and looks at the element just beyond the second one - the third element. It must catch up with the third element. So: every element, except the third element is upgraded by the difference between the first element and the third one. As a result, the array now is - "10 10 10 16".

# Finally, only one element left that's towering above everyone else - the last element. In the final step, the array is modified to "16 16 16 16".

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/comments/1567574/

# There are n elements, after reordering, the minimum element is a(1), the maximum element is a(n), we have a(1) <= a(2) <= a(3) <= ... <= a(n).
# We set the solution is m, after m moves, all the elements will be the same value, that is a(1) + m, so the other (n-1) element will add a(1) + m - a(i) times, we know that m moves will introduce m * (n - 1) to the array's total sums. we can have the equation:
# m * (n - 1) = m + a(1) + m - a(2) + a(1) + m - a(3) +... + a(1) + m - a(n)
# => m * n - m = m * n + (n - 1) * a(1) - a(2) - a(3) -... - a(n)
# => m = a(2) + a(3) + ... + a(n) - (n - 1) * a(1)
# => m = Sum - n * Min