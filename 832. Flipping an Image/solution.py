class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        invert = (1, 0)
        fliped_image = [[invert[bit] for bit in row[::-1]] for row in image]
        return fliped_image