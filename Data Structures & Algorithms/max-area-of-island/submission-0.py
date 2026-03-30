class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        visited = set()
        curr_area = 0
        def dfs(r,c):
            if (r<0 or c<0
            or r>=len(grid) or c>=len(grid[0])
            or (r,c) in visited
            or grid[r][c] == 0):
                return None 
            
            nonlocal curr_area
            curr_area += 1
            visited.add((r,c))

            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r,c+1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col)
                    result = max(result, curr_area)
                    curr_area = 0
        
        return result
