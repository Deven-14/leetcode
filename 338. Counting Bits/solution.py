import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        ans = [0]
        power = math.log2(n)
        power_of_2 = 1

        for _ in range(int(power)):
            ans.extend(1 + num_of_1s for num_of_1s in ans[:power_of_2])
            power_of_2 *= 2
        
        remainder = n - power_of_2
        ans.extend(1 + num_of_1s for num_of_1s in ans[:remainder + 1])
        return ans


# another solution
# class Solution {
# public:
#     vector<int> countBits(int n) {
#         vector<int> dp(n+1, 0);
#         int off = 1;
#         for(int i=1; i<=n; i++){
#             if(off*2 == i) off = i;
#             dp[i] = 1 + dp[i - off];
#         }
#         return dp;
#     }
# };