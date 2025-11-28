class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 32 bit mask
        max_int = 2 ** 31 - 1 # w.r.t a 32 bit integer (32nd bit is the sign bit)
        
        while b != 0:
            bit_sum_without_carry = (a ^ b) & mask
            carry = ((a & b) & mask) << 1
            a, b = bit_sum_without_carry, carry
        
        return a if a <= max_int else ~(a ^ mask)

# explanation

# a ^ b (Sum without carry): This mimics bitwise addition.
# (a & b) << 1 (Carry): This identifies positions where two 1s are added together, generating a carry, and shifts that carry to the left (to the next significant bit).
# Termination: The recursion stops when b (the carry) becomes 0. Since the carry is constantly shifted to the left (<< 1), the bits will eventually be shifted out of the integer's range (overflow), resulting in 0.

# we also need a mask for python - https://leetcode.com/problems/sum-of-two-integers/solutions/6141561/animated-video-bit-manipulation-masking-d2f4g

# ~(a ^ mask)
# this example assumes an int is 4 bits instead of 32 for easier reading
# mask = 1111
# a =    1100 # python treats this as 12 in unsigned format
# # ~ is the 2s complement operator in python. ~x = -x-1 
# flipped_bits = a ^ mask = 0011
# ~flipped_bits = ~(a ^ mask) = 1100 # python now treats this as -4
# we re-flip back the bits using python's two complement operator to force python to treat the number as a signed, negative value

# flipped_bits = a ^ mask = 0011 - this works because of the below The "Odometer" Analogy


# negative numbers

# 1. The "Odometer" Analogy
# Imagine an old-school mechanical car odometer (mileage counter) that only has 4 digits. It reads 0000.
# If you drive forward 1 mile, it clicks to 0001.
# Key Concept: If you drive backward 1 mile from 0000, what happens? It rolls back to 9999.
# In this mechanical system, 9999 behaves exactly like -1.If you start at 0002 and add 9999 (which is our mechanical -1):
# 2 + 9999 = 10001
# But the odometer only has 4 digits! So the 1 on the left falls off (overflows), and you are left with 0001. The math worked: 2 + (-1) = 1.

