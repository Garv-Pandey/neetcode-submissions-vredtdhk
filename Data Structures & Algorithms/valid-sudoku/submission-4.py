class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue

                if (board[row][col] in seen_rows[row] 
                or board[row][col] in seen_cols[col]
                or board[row][col] in seen_boxes[row//3, col//3]):
                    return False

                seen_rows[row].add(board[row][col])
                seen_cols[col].add(board[row][col])
                seen_boxes[(row//3,col//3)].add(board[row][col])

        return True