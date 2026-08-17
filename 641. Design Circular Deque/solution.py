class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [0] * k
        self.front = self.rear = -1
        self.n = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.n) % self.n
        
        self.q[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.n
        
        self.q[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.n
        
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.n) % self.n
        
        return True  

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.n == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()



class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [0] * k
        self.front = self.rear = 0
        self.size = 0
        self.n = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front = (self.front - 1 + self.n) % self.n
        self.q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.n
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.rear = (self.rear - 1 + self.n) % self.n
        self.size -= 1
        return True  

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.rear - 1 + self.n) % self.n
        return self.q[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.n


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

