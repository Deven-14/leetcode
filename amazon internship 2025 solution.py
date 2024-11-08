from itertools import accumulate
def maximize(memory):
    memory.sort(reverse=True)
    return sum(accumulate(memory))

# print(maximize([3, 1, -2])) # 15

def getTotalOfferPeriods(sales):
    count = 0
    for i in range(len(sales)-2):
        for j in range(i+2, len(sales)):
            min_val = min(sales[i], sales[j])
            max_val = max(sales[i+1:j])
            if min_val > max_val:
                count += 1
        
    return count

# def getTotalOfferPeriods(sales):
#     stack = []
#     count = 0

#     for i in range(len(sales)):
#         while stack and sales[stack[-1]] >= sales[i]:
#             top = stack.pop()
#             if stack:
#                 count += 1
#         stack.append(i)

#     return count

def getTotalOfferPeriods2(sales):
    count = 0
    for i in range(len(sales)-2):
        max_val = sales[i+1]
        for j in range(i+2, len(sales)): # put space to clear the yellow line
            min_val = min(sales[i], sales[j])
            max_val = max(max_val, sales[j-1])
            if min_val > max_val:
                count += 1
        
    return count


def getTotalOfferPeriods3(sales):
    min_val = list(accumulate(sales, min))


print(getTotalOfferPeriods([3, 2, 8, 6]))
print(getTotalOfferPeriods([5, 2, 1, 3, 6]))
print(getTotalOfferPeriods([10, 6, 8, 5, 11, 9]))
print(getTotalOfferPeriods([9, 5, 2, 1, 3, 6, 7, 7, 7, 8]))
