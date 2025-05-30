class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_indices = { s: i for i, s in enumerate(score) }
        score.sort(reverse=True)
        
        n = len(score)
        places = [None] * n

        idx = score_indices[score[0]]
        places[idx] = "Gold Medal"

        if n == 1:
            return places

        idx = score_indices[score[1]]
        places[idx] = "Silver Medal"
        
        if n == 2:
            return places
        
        idx = score_indices[score[2]]
        places[idx] = "Bronze Medal"

        if n == 3:
            return places
        
        for i in range(3, n):
            place = i + 1
            idx = score_indices[score[i]]
            places[idx] = str(place)
        
        return places
            

        