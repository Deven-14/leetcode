from collections import deque
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied_customers = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        max_grumpy_customer_batch = 0
        batch = deque()
        for i in range(minutes):
            if grumpy[i] == 1:
                max_grumpy_customer_batch += customers[i]
                batch.append(i)
        
        grumpy_customer_batch = max_grumpy_customer_batch
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                while batch and (i - batch[0]) >= minutes:
                    grumpy_customer_batch -= customers[batch[0]]
                    batch.popleft()

                batch.append(i)
                grumpy_customer_batch += customers[i]
                max_grumpy_customer_batch = max(grumpy_customer_batch, max_grumpy_customer_batch)
        
        satisfied_customers += max_grumpy_customer_batch
        return satisfied_customers


from collections import deque
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied_customers = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        max_grumpy_customer_batch = 0
        batch = deque()
        for i in range(minutes):
            if grumpy[i] == 1:
                max_grumpy_customer_batch += customers[i]
                batch.append(i)
        
        grumpy_customer_batch = max_grumpy_customer_batch
        for i in range(minutes, len(customers)):
            if batch and batch[0] == (i - minutes):
                grumpy_customer_batch -= customers[batch[0]]
                batch.popleft()

            if grumpy[i] == 1:
                batch.append(i)
                grumpy_customer_batch += customers[i]
                max_grumpy_customer_batch = max(grumpy_customer_batch, max_grumpy_customer_batch)
        
        satisfied_customers += max_grumpy_customer_batch
        return satisfied_customers


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied_customers = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        max_grumpy_customer_batch = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        
        grumpy_customer_batch = max_grumpy_customer_batch
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] == 1:
                grumpy_customer_batch -= customers[i - minutes]

            if grumpy[i] == 1:
                grumpy_customer_batch += customers[i]
                max_grumpy_customer_batch = max(grumpy_customer_batch, max_grumpy_customer_batch)
        
        satisfied_customers += max_grumpy_customer_batch
        return satisfied_customers
