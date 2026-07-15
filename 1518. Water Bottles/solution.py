class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numDrink = 0
        numEmpty = 0
        while numBottles:
            numDrink += numBottles
            numBottles, numEmpty = divmod(numBottles + numEmpty, numExchange)
        
        return numDrink