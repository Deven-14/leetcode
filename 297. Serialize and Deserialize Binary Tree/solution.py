# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root:
                return ('$#', 1)
            
            lt, ln = preorder(root.left)
            rt, rn = preorder(root.right)

            return (f'${ln}|{rn}|{root.val}' + lt + rt, 1 + ln + rn)
        
        return preorder(root)[0]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split('$')
        def decode_preorder_str(i):
            if nodes[i] == '#':
                return None
            
            ln, rn, val = (int(num) for num in nodes[i].split('|'))
            node = TreeNode(val)
            if ln > 0:
                node.left = decode_preorder_str(i + 1)
            if rn > 0:
                node.right = decode_preorder_str(i + ln + 1)
            
            return node
        
        return decode_preorder_str(1) # because of split
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root:
                return ('$#', 1)
            
            lt, ln = preorder(root.left)
            rt, rn = preorder(root.right)

            return (f'${ln}|{root.val}' + lt + rt, 1 + ln + rn)
        
        return preorder(root)[0]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split('$')
        def decode_preorder_str(i):
            if nodes[i] == '#':
                return None
            
            ln, val = nodes[i].split('|')
            node = TreeNode(int(val))
            node.left = decode_preorder_str(i + 1)
            node.right = decode_preorder_str(i + int(ln) + 1)
            
            return node
        
        return decode_preorder_str(1) # because of split
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root:
                return ['$#']
            
            lt = preorder(root.left)
            rt = preorder(root.right)

            return [f'${len(lt)}|{root.val}'] + lt + rt
        
        return "".join(preorder(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split('$')
        def decode_preorder_str(i):
            if nodes[i] == '#':
                return None
            
            ln, val = nodes[i].split('|')
            node = TreeNode(int(val))
            node.left = decode_preorder_str(i + 1)
            node.right = decode_preorder_str(i + int(ln) + 1)
            
            return node
        
        return decode_preorder_str(1) # because of split
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root:
                return ['$#']
            
            lt = preorder(root.left)
            rt = preorder(root.right)

            return [f'${len(lt)}|{root.val}', *lt, *rt]
        
        return "".join(preorder(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split('$')
        def decode_preorder_str(i):
            if nodes[i] == '#':
                return None
            
            ln, val = nodes[i].split('|')
            node = TreeNode(int(val))
            node.left = decode_preorder_str(i + 1)
            node.right = decode_preorder_str(i + int(ln) + 1)
            
            return node
        
        return decode_preorder_str(1) # because of split
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root:
                return '#'
            return f'{root.val}${preorder(root.left)}${preorder(root.right)}'
        
        return preorder(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split('$')
        idx = 0

        def decode_preorder_str():
            nonlocal idx
            if nodes[idx] == '#':
                idx += 1
                return None
            
            node = TreeNode(int(nodes[idx]))
            idx += 1 # next idx is always the left node

            node.left = decode_preorder_str()
            node.right = decode_preorder_str()
            
            return node
        
        return decode_preorder_str()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                res.append('#')
                continue
            
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        
        return "$".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split('$')
        idx = 0

        def decode_preorder_str():
            nonlocal idx
            if nodes[idx] == '#':
                idx += 1
                return None
            
            node = TreeNode(int(nodes[idx]))
            idx += 1 # next idx is always the left node

            node.left = decode_preorder_str()
            node.right = decode_preorder_str()
            
            return node
        
        return decode_preorder_str()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))