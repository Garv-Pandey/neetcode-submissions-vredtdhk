class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # creating trie for target words

        trie = {}
        for word in words:
            level = trie
            for char in word:
                if char not in level:
                    level[char] = {}
                
                level = level[char]
            
            level['*'] = {}
        
        print (trie)

        ROW, COL = len(board), len(board[0])
        visited_box = set()
        result = []
        def dfs(r, c, level, current_word):
            if (r < 0 or c < 0
            or r == ROW or c == COL
            or (r,c) in visited_box
            or board[r][c] not in level):
                return None

            visited_box.add((r,c))

            current_word += board[r][c]
            if board[r][c] in level:
                level = level[board[r][c]]

            if '*' in level:
                result.append(current_word)

            dfs(r+1, c, level, current_word)
            dfs(r, c-1, level, current_word)
            dfs(r-1, c, level, current_word)
            dfs(r, c+1, level, current_word)

            visited_box.remove((r,c))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie, "")
                
        return list(set(result))


        