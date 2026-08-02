class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.front, self.rear = -1, -1
        self.n = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.n
        
        self.q[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.n
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.n == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.front = 0
        self.currSize = 0
        self.n = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        rear = (self.front + self.currSize) % self.n
        self.q[rear] = value
        self.currSize += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.currSize == 1:
            self.front = 0
        else:
            self.front = (self.front + 1) % self.n
        
        self.currSize -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.front + self.currSize) % self.n - 1]

    def isEmpty(self) -> bool:
        return self.currSize == 0

    def isFull(self) -> bool:
        return self.currSize == self.n


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.front = 0
        self.currSize = 0
        self.n = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        rear = (self.front + self.currSize) % self.n
        self.q[rear] = value
        self.currSize += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.n
        self.currSize -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.front + self.currSize) % self.n - 1]

    def isEmpty(self) -> bool:
        return self.currSize == 0

    def isFull(self) -> bool:
        return self.currSize == self.n


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

