class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = collections.defaultdict(set)
        col_seen = collections.defaultdict(set)
        box_seen = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if (
                    board[row][col] in row_seen[row]
                    or board[row][col] in col_seen[col]
                    or board[row][col] in box_seen[(row // 3, col // 3)]
                ):
                    print(False)
                    return False

                # value = row_seen.get(row, {})
                row_seen[row].add(board[row][col])
                # row_seen[row] = value

                # value = col_seen.get(col, {})
                col_seen[col].add(board[row][col])
                # col_seen[col] = value

                # value = box_seen.get((row // 3, col // 3), {})
                box_seen[(row // 3, col // 3)].add(board[row][col])
                # box_seen[((row // 3, col // 3))] = value

        print(True)
        return True
