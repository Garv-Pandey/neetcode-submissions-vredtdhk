class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_visited = defaultdict(set)
        col_visited = defaultdict(set)
        box_visited = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                if (board[r][c] in row_visited[r]
                or board[r][c] in col_visited[c]
                or board[r][c] in box_visited[(r//3, c//3)]):
                    return False
                
                row_visited[r].add(board[r][c])
                col_visited[c].add(board[r][c])
                box_visited[(r//3,c//3)].add(board[r][c])

        return True