class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            unique = set()
            for number in row:
                if number != "." and number in unique:
                    return False
                unique.add(number)
        
        # check columns:
        for i in range(9):
            unique = set()
            for j in range(9):
                number = board[j][i]
                if number != "." and number in unique:
                    return False
                unique.add(number)
        
        # check inner boxes
        index_ranges = [(0, 3), (3, 6), (6, 9)]
        inner_boxes = [(row, col) for row in index_ranges for col in index_ranges]

        for ((start_row, stop_row), (start_col, stop_col)) in inner_boxes:
            unique = set()
            for i in range(start_row, stop_row):
                for j in range(start_col, stop_col):
                    number = board[i][j]
                    if number != "." and number in unique:
                        return False
                    unique.add(number)
        
        return True
