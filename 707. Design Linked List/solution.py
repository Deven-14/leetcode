class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0, self.head)
        self.head.next = self.tail
        self.len = 0
    
    def _getNode(self, index: int) -> Node:
        node = self.head
        index += 1 #
        while index:
            node = node.next
            index -= 1
        return node

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        return self._getNode(index).val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        next = self.head.next
        node.prev, node.next = self.head, next
        next.prev, self.head.next = node, node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prev = self.tail.prev
        node.prev, node.next = prev, self.tail
        prev.next, self.tail.prev = node, node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return 
        node = self._getNode(index)
        prev = node.prev
        new_node = Node(val, prev, node)
        prev.next, node.prev = new_node, new_node
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return 
        node = self._getNode(index)
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.len -= 1
        
class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0, self.head)
        self.head.next = self.tail
        self.len = 0
    
    def _getNode(self, index: int) -> Node:
        node = self.head
        for _ in range(index + 1):
            node = node.next
        return node

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        return self._getNode(index).val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        next = self.head.next
        node.prev, node.next = self.head, next
        next.prev, self.head.next = node, node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prev = self.tail.prev
        node.prev, node.next = prev, self.tail
        prev.next, self.tail.prev = node, node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return 
        node = self._getNode(index)
        prev = node.prev
        new_node = Node(val, prev, node)
        prev.next, node.prev = new_node, new_node
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return 
        node = self._getNode(index)
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.len -= 1
        
class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


