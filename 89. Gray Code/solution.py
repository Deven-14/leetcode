class Solution:
    def grayCode(self, n: int) -> List[int]:
        sequence = [0]
        n_bit_gray_code = ["0"] * n
        n_bit_sequence = [n_bit_gray_code.copy()]

        for i in range(n-1, -1, -1):
            for j in range(len(n_bit_sequence)-1, -1, -1):
                next_n_bit_sequence = n_bit_sequence[j].copy()
                next_n_bit_sequence[i] = "1"
                n_bit_sequence.append(next_n_bit_sequence)
                sequence.append(int("".join(next_n_bit_sequence), 2))
        
        return sequence


class Solution:
    def grayCode(self, n: int) -> List[int]:
        sequence = [0]

        for i in range(n):
            bit_to_change = 1 << i
            for j in range(len(sequence)-1, -1, -1):
                code = sequence[j] | bit_to_change
                sequence.append(code)
        
        return sequence