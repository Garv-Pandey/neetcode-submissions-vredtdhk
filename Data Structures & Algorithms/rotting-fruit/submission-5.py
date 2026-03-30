class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        frest_count = 0
        rotten_count = 0

        def add_fruit(r, c):
            if (r<0 or c<0
            or r>=len(grid) or c>=len(grid[0])
            or (r,c) in visited
            or grid[r][c] == 0):
                return None
            
            visited.add((r,c))
            q.append((r,c))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))
                    rotten_count += 1
                
                elif grid[row][col] == 1:
                    frest_count += 1

        
        print(f"frest before start: {frest_count}")
        minute = -1 # becuase first iteration gets already rottern fruits
        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                print(row, col, grid[row][col])
                if (grid[row][col]) == 1:
                    frest_count-=1
                grid[row][col] = 2

                add_fruit(row-1, col)
                add_fruit(row+1, col)
                add_fruit(row, col-1)
                add_fruit(row, col+1)

            minute += 1
            
        
        print(f"frest after start: {frest_count}")
        print(grid)

        if not rotten_count and not frest_count:
            return 0

        return minute if not frest_count else -1