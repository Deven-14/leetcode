class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        visited = set()
        stack = [(sr, sc, image[sr][sc])]
        m, n = len(image), len(image[0])

        while stack:
            sr, sc, original_color = stack.pop()
            if (sr, sc) in visited:
                continue
            
            image[sr][sc] = color
            visited.add((sr, sc))
            if (sr + 1) < m and image[sr + 1][sc] == original_color:
                stack.append((sr + 1, sc, image[sr + 1][sc]))

            if (sr - 1) >= 0 and image[sr - 1][sc] == original_color:
                stack.append((sr - 1, sc, image[sr - 1][sc]))
            
            if (sc + 1) < n and image[sr][sc + 1] == original_color:
                stack.append((sr, sc + 1, image[sr][sc + 1]))
            
            if (sc - 1) >= 0 and image[sr][sc - 1] == original_color:
                stack.append((sr, sc - 1, image[sr][sc - 1]))

        return image


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        visited = set()
        stack = [(sr, sc, image[sr][sc])]
        m, n = len(image), len(image[0])

        while stack:
            sr, sc, original_color = stack.pop()
            if (sr, sc) in visited:
                continue
            
            image[sr][sc] = color
            visited.add((sr, sc))
            
            if (dr := sr + 1) < m and image[dr][sc] == original_color:
                stack.append((dr, sc, image[dr][sc]))

            if (dr := sr - 1) >= 0 and image[dr][sc] == original_color:
                stack.append((dr, sc, image[dr][sc]))
            
            if (dc := sc + 1) < n and image[sr][dc] == original_color:
                stack.append((sr, dc, image[sr][dc]))
            
            if (dc := sc - 1) >= 0 and image[sr][dc] == original_color:
                stack.append((sr, dc, image[sr][dc]))

        return image
