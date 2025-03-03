class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 = step2 = 0

        for step_cost in cost:
            prev_step2 = step2
            step2 = step_cost + min(step1, step2)
            step1 = prev_step2
        
        return min(step1, step2)