class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0 

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        

        mins = 0

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue

                    
                    grid[nr][nc] = 2
                    q.append([nr,nc])
                    fresh -= 1
            mins += 1
        
        return mins if fresh == 0 else -1
