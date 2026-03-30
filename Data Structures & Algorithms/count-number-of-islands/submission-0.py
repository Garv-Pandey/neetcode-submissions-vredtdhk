class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0
            or r >= len(grid) or c >= len(grid[0])
            or (r,c) in visited 
            or grid[r][c] == "0"):
                return None
            
            visited.add((r,c))

            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r, c+1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    island_count += 1
                    dfs(row, col)
            
        return island_count
