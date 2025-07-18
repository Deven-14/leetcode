# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = 40
        while result >= 40:
            result = 7 * (rand7() - 1) + (rand7() - 1)
        
        return result % 10 + 1


# https://leetcode.com/problems/implement-rand10-using-rand7/solutions/150301/three-line-java-solution-the-idea-can-be-generalized-to-implement-randm-using-randn