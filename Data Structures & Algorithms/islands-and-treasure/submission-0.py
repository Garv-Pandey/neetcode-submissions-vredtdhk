class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()
        q = deque()

        def add_room(r, c):
            if (r<0 or c<0
            or r>=len(grid) or c>=len(grid[0])
            or (r,c) in visited
            or grid[r][c] == -1):
                return None
            
            visited.add((r,c))
            q.append((r,c))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance

                add_room(r-1, c)
                add_room(r, c-1)
                add_room(r+1, c)
                add_room(r, c+1)
            
            distance += 1