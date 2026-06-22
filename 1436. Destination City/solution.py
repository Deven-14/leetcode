class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = paths[0][0]
        paths = { a: b for a, b in paths }

        while city in paths:
            city = paths[city]
        
        return city