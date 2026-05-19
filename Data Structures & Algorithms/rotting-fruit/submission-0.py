from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        mins, fresh = 0, 0

        def addToQueue(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r == ROWS or c == COLS  or grid[r][c] != 1:
                return 
            
            fresh -= 1
            grid[r][c] = 2
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addToQueue(r+1, c)
                addToQueue(r-1, c)
                addToQueue(r, c+1)
                addToQueue(r, c-1)

            mins += 1

        return mins if fresh == 0 else -1

