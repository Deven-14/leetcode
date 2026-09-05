# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, node, idx):
        self.tn = node
        self.idx = idx
    
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([Node(root, 1)])
        max_width = 1

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()

            start, end = queue[0], queue[-1]
            max_width = max(max_width, end.idx - start.idx + 1)

            while curr_level_queue:
                node = curr_level_queue.popleft()

                if node.tn.left:
                    next_level_queue.append(Node(node.tn.left, 2 * node.idx - 1))

                if node.tn.right:
                    next_level_queue.append(Node(node.tn.right, 2 * node.idx))
            
            queue = next_level_queue

        return max_width



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        max_width = 1

        while queue:
            curr_level_queue = queue
            next_level_queue = deque()

            (_, start), (_, end) = queue[0], queue[-1]
            max_width = max(max_width, end - start + 1)

            while curr_level_queue:
                node, idx = curr_level_queue.popleft()

                if node.left:
                    next_level_queue.append((node.left, 2 * idx - 1))

                if node.right:
                    next_level_queue.append((node.right, 2 * idx))
            
            queue = next_level_queue

        return max_width

