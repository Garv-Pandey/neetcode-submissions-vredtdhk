class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = defaultdict(set)
        seen_col = defaultdict(set)
        seen_box = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if (board[row][col] in seen_row[row]
                or board[row][col] in seen_col[col]
                or board[row][col] in seen_box[(row//3, col//3)]):
                    return False

                seen_row[row].add(board[row][col])
                seen_col[col].add(board[row][col])
                seen_box[(row//3, col//3)].add(board[row][col])

        return True