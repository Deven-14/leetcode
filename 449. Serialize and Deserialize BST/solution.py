# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return "#"
        
        return f"{root.val}${self.serialize(root.left)}${self.serialize(root.right)}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes = deque(data.split('$'))

        def helper():
            node = nodes.popleft()
            if node == "#":
                return None
            
            root = TreeNode(int(node))
            root.left = helper()
            root.right = helper()

            return root

        return helper()
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        nodes = []

        def preorder(node):
            if not node:
                nodes.append("#")
                return 
            
            nodes.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return "$".join(nodes)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes = deque(data.split('$'))

        def helper():
            node = nodes.popleft()
            if node == "#":
                return None
            
            root = TreeNode(int(node))
            root.left = helper()
            root.right = helper()

            return root

        return helper()
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans