class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        s = num_people * (num_people + 1) // 2
        if candies <= s:
            i = 1
            j = 0
            distributes = [0] * num_people
            while candies >= i:
                distributes[j] = i
                candies -= i
                i += 1
                j += 1
            
            if candies > 0:
                distributes[j] = candies

            return distributes
        
        n = num_people
        s = n * (n + 1) // 2
        diff = s
        loops = 0

        while candies >= diff:
            loops += 1
            candies -= diff
            n += num_people
            prev_s = s
            s = (n * (n + 1) // 2)
            diff = s - prev_s
        
        t = loops - 1
        loop_candies = num_people * (t * (t + 1) // 2)
        distributes = [loop_candies + i * loops for i in range(1, num_people + 1)]

        i = (n - num_people) + 1
        j = 0
        while candies >= i:
            distributes[j] += i
            candies -= i
            i += 1
            j += 1
        
        if candies > 0:
            distributes[j] += candies
        
        return distributes