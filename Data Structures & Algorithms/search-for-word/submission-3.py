class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(word_index, r, c):
            if (r < 0 or r >= len(board)
            or c < 0 or c >= len(board[0])
            or board[r][c] != word[word_index]
            or (r,c) in path):
                return False

            if word_index == len(word) -1:
                return True
            
            
            path.add((r,c))
            top = dfs(word_index+1, r, c-1)
            left = dfs(word_index+1, r-1, c)
            bottom = dfs(word_index+1, r, c+1)
            right = dfs(word_index+1, r+1, c)
            path.remove((r,c))

            return top or left or bottom or right

        
        path = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != word[0]:
                    continue
                
                if dfs(0, r, c):
                    return True
        
        return False
                