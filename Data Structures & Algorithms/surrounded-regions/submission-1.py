class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board)-1, len(board[0])-1
        visited = set()
        

        def dfs(row, col):
            if (row<0 or col<0
            or row>ROW or col>COL
            or (row,col) in visited
            or board[row][col] == "X"):
                return
            
            visited.add((row,col))
            board[row][col] = "T"

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
    
        for col in range(len(board[0])):
            dfs(0, col)
            dfs(ROW, col)
        for row in range(len(board)):
            dfs(row, 0)
            dfs(row, COL)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                
                elif board[row][col] == "T":
                    board[row][col] = "O"
        
            