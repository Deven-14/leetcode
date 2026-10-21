class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        return [first] + [(first := first ^ ele) for ele in encoded]


class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        return [(first := first ^ ele) for ele in [0] + encoded]


class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        decoded = [first]
        for ele in encoded:
            decoded.append(decoded[-1] ^ ele)
        return decoded
