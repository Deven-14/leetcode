# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s.isdigit():
            return NestedInteger(int(s))
        
        stack = []
        i, n = 0, len(s)
        
        while i < n:
            char = s[i]
            if char == '[':
                stack.append('[')
                i += 1

            elif char == ']':
                
                nested_int = NestedInteger()
                elems = []

                while stack[-1] != '[':
                    elems.append(stack.pop())

                while elems:
                    nested_int.add(elems.pop())

                stack.pop()
                stack.append(nested_int)
                i += 1
            
            elif char == '-' or char.isdigit():
                j = i + 1
                while j < n and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                i = j
                
                nested_int = NestedInteger(num)
                stack.append(nested_int)
            
            if i < n and s[i] == ",":
                i += 1
                        
        return stack.pop()
                
                
