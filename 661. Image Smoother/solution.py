class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        smoother_img = [[0] * n for _ in range(m)]

        for i in range(1, m-1):
            for j in range(1, n-1):
                smoother_img[i][j] = int(sum([
                        img[i-1][j-1], img[i-1][j], img[i-1][j+1],
                        img[i][j-1], img[i][j], img[i][j+1],
                        img[i+1][j-1], img[i+1][j], img[i+1][j+1]
                    ]) // 9)
        
        for k, l in [(range(m), [0, n-1]), ([0, m-1], range(1, n-1))]:
            for i in k:
                for j in l:
                    i1, i2 = (i-1) >= 0, (i+1) < m
                    j1, j2 = (j-1) >= 0, (j+1) < n
                    count = 1
                    total = img[i][j]
                    
                    if i1 and j1:
                        total += img[i-1][j-1]
                        count += 1
                    
                    if i1:
                        total += img[i-1][j]
                        count += 1
                    
                    if i1 and j2:
                        total += img[i-1][j+1]
                        count += 1
                    
                    if j1:
                        total += img[i][j-1]
                        count += 1
                    
                    if j2:
                        total += img[i][j+1]
                        count += 1
                    
                    if i2 and j1:
                        total += img[i+1][j-1]
                        count += 1
                    
                    if i2:
                        total += img[i+1][j]
                        count += 1
                    
                    if i2 and j2:
                        total += img[i+1][j+1]
                        count += 1
                    
                    smoother_img[i][j] = int(total // count)

        return smoother_img



class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        smoother_img = [[0] * n for _ in range(m)]

        for i in range(1, m-1):
            for j in range(1, n-1):
                smoother_img[i][j] = int((
                        img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] +
                        img[i][j-1] + img[i][j] + img[i][j+1] +
                        img[i+1][j-1] + img[i+1][j] + img[i+1][j+1]
                    ) // 9)
        
        for k, l in [(range(m), [0, n-1]), ([0, m-1], range(1, n-1))]:
            for i in k:
                for j in l:
                    i1, i2 = (i-1) >= 0, (i+1) < m
                    j1, j2 = (j-1) >= 0, (j+1) < n
                    count = 1
                    total = img[i][j]
                    
                    if i1 and j1:
                        total += img[i-1][j-1]
                        count += 1
                    
                    if i1:
                        total += img[i-1][j]
                        count += 1
                    
                    if i1 and j2:
                        total += img[i-1][j+1]
                        count += 1
                    
                    if j1:
                        total += img[i][j-1]
                        count += 1
                    
                    if j2:
                        total += img[i][j+1]
                        count += 1
                    
                    if i2 and j1:
                        total += img[i+1][j-1]
                        count += 1
                    
                    if i2:
                        total += img[i+1][j]
                        count += 1
                    
                    if i2 and j2:
                        total += img[i+1][j+1]
                        count += 1
                    
                    smoother_img[i][j] = int(total // count)

        return smoother_img