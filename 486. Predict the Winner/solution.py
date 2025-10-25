from functools import cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def will_player1_win(i, j, p1, p2, p1_turn):
            if i > j:
                return p1 >= p2
            
            # player 1 to play optimaly will think about all the choices he can take to win, so 'or'
            # so player 1 can win by taking choice1 or taking choice2
            if p1_turn:
                return will_player1_win(i+1, j, p1+nums[i], p2, not p1_turn) or will_player1_win(i, j-1, p1+nums[j], p2, not p1_turn)
            else: 
                return will_player1_win(i+1, j, p1, p2+nums[i], not p1_turn) and will_player1_win(i, j-1, p1, p2+nums[j], not p1_turn)
                # You may assume that both players are playing optimally.
                # return helper(i+1, j, p1, p2+nums[i], not p1_turn) or helper(i, j-1, p1, p2+nums[j], not p1_turn) --- 'or' is wrong
                # 'and' condidtion because for player 1 to win, player 2 has to lose for all the choices (i.e., player 1 has to win for all the choices player 2 makes, so p2_choice1 & p2_choice2 & etc.)
        
        return will_player1_win(0, len(nums)-1, 0, 0, True)


# 1st way
# https://leetcode.com/problems/predict-the-winner/description/comments/1565119/
# https://leetcode.com/problems/predict-the-winner/description/comments/1989495/


from functools import cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def will_player1_win(i, j):
            if i == j:
                return nums[i]
            
            return max(nums[i] - will_player1_win(i+1, j), nums[j] - will_player1_win(i, j-1))
        
        return will_player1_win(0, len(nums)-1) >= 0

# 1st way
# https://leetcode.com/problems/predict-the-winner/description/comments/1565119/
# https://leetcode.com/problems/predict-the-winner/description/comments/1989495/

# 2nd way - min max
# https://leetcode.com/problems/predict-the-winner/solutions/155217/from-brute-force-to-top-down-dp
# https://leetcode.com/problems/predict-the-winner/solutions/6655465/conquer-optimal-strategy-game-with-pure-recursion-magic

from functools import cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def will_player1_win(i, j):
            if i > j:
                return 0

            if i == j:
                return nums[i]
            
            return max(
                nums[i] + min(will_player1_win(i+2, j), will_player1_win(i+1, j-1)), 
                nums[j] + min(will_player1_win(i, j-2), will_player1_win(i+1, j-1))
            )
        
        p1_score = will_player1_win(0, len(nums)-1)
        p2_score = sum(nums) - p1_score
        return  p1_score >= p2_score

# 1st way
# https://leetcode.com/problems/predict-the-winner/description/comments/1565119/
# https://leetcode.com/problems/predict-the-winner/description/comments/1989495/

# 2nd way - min max
# https://leetcode.com/problems/predict-the-winner/solutions/6655465/conquer-optimal-strategy-game-with-pure-recursion-magic

# 3rd way - min max
# https://leetcode.com/problems/predict-the-winner/solutions/155217/from-brute-force-to-top-down-dp