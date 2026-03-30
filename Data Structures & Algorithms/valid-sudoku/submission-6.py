class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_visited = defaultdict(set)
        columns_visited = defaultdict(set)
        boxes_visited = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                if (board[r][c] in rows_visited[r]
                or board[r][c] in columns_visited[c]
                or board[r][c] in boxes_visited[r//3,c//3]):
                    return False

                rows_visited[r].add(board[r][c])
                columns_visited[c].add(board[r][c])
                boxes_visited[r//3,c//3].add(board[r][c])

        return True