# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [root]
        nodes = { root.val: root }
        parents = { root: None }

        while queue:
            queue_curr_level = queue
            queue_next_level = set()

            if x in nodes and y in nodes:
                return parents[nodes[x]] != parents[nodes[y]]
            elif x in nodes and y not in nodes:
                return False
            elif x not in nodes and y in nodes:
                return False
            
            for node in queue_curr_level:
                if node.left:
                    queue_next_level.add(node.left)
                    parents[node.left] = node
                    nodes[node.left.val] = node.left
                if node.right:
                    queue_next_level.add(node.right)
                    parents[node.right] = node
                    nodes[node.right.val] = node.right
            
            queue = queue_next_level

        return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [root]

        while queue:
            queue_curr_level = queue
            queue_next_level = []
            x_present, y_present = False, False
            
            for node in queue_curr_level:
                if node.val == x:
                    x_present = True
                if node.val == y:
                    y_present = True
                
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False

                if node.left:
                    queue_next_level.append(node.left)
                if node.right:
                    queue_next_level.append(node.right)

            if x_present and y_present:
                return True

            queue = queue_next_level

        return False