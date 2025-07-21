class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        bits = []
        div_by_5 = []

        for bit in nums:
            bits.append(str(bit))
            num = int("".join(bits), 2)
            div_by_5.append(num % 5 == 0)
        
        return div_by_5


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        div_by_5 = []

        for bit in nums:
            num <<= 1
            num |= bit
            div_by_5.append(num % 5 == 0)
        
        return div_by_5


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        div_by_5 = []

        for bit in nums:
            num = (num << 1) | bit
            div_by_5.append(num % 5 == 0)
        
        return div_by_5


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        div_by_5 = []

        for bit in nums:
            num = ((num << 1) | bit) % 5
            div_by_5.append(num == 0)
        
        return div_by_5


# Observe that we only care about the remainder, not the actual number.
# Use the fact that (ab + c)%d is same as ((a%d)(b%d) + c%d)%d.
# We now have the relation new_number%5 = ((old_number%5)*2 + d)%5;
# This tells us the if we provide the modulo of the old_number instead of the original number, we'll get the modulo of the new number.
# This would prevent overflows, since new_number is the equivalent representation of the original number in the modular arithemtic of 5.