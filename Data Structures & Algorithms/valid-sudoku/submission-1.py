class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = dict()
        col_hash = dict()
        sector_hash = dict()

        for row in range(0, 9):
            for col in range(0, 9):

                if board[row][col] == ".":
                    continue

                # print(f"({row}, {col}) : {board[row][col]}")
                row_ele = row_hash.get(row, [])
                col_ele = col_hash.get(col, [])
                sector_ele = sector_hash.get(tuple([row // 3, col // 3]), [])
                # print(row_ele)
                # print(col_ele)
                # print(sector_ele)

                if (
                    board[row][col] in row_ele
                    or board[row][col] in col_ele
                    or board[row][col] in sector_ele
                ):
                    return False

                row_ele.append(board[row][col])
                col_ele.append(board[row][col])
                sector_ele.append(board[row][col])

                row_hash[row] = row_ele
                col_hash[col] = col_ele
                sector_hash[tuple([row // 3, col // 3])] = sector_ele

        return True