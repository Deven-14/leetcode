class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        total = alice + bob
        half = total // 2
        bobSet = set(bobSizes)
        
        for aliceSize in set(aliceSizes):
            if (t := bob + aliceSize) < half:
                continue
            bobSize = t - half
            if bobSize in bobSet:
                return [aliceSize, bobSize]
        

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        total = alice + bob
        half = total // 2
    
        sumA = alice
        sumB = bob
        sizesA = set(aliceSizes)
        sizesB = set(bobSizes)
        
        if alice > bob:
            sumA, sumB = sumB, sumA
            sizesA, sizesB = sizesB, sizesA

        for sizeA in sizesA:
            sizeB = sumB + sizeA - half
            if sizeB in sizesB:
                return [sizeA, sizeB] if bob > alice else [sizeB, sizeA]
        

# * We need to find a swap such that:
# sum_of_candy_a - A[i] + B[j] == sum_of_candy_b - B[j] + A[i]
# sum_of_candy_a - sum_of_candy_b == 2A[i] - 2B[j]
# diff/2 = A[i] - B[j]
# for each A find in B if there is a  A[i] - diff/2
# https://leetcode.com/problems/fair-candy-swap/solutions/161269/c-java-python-straight-forward


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        sizesA = set(aliceSizes)
        sizesB = set(bobSizes)
        
        for sizeA in sizesA:
            if (sizeA - diff) in sizesB:
                return [sizeA, sizeA - diff]
