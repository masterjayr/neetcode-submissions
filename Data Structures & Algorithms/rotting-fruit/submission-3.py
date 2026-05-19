from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        mins, fresh = 0, 0
        queue = deque()
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r,c])
            

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = dr+r, dc+c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue

                    queue.append([nr,nc])
                    grid[nr][nc] = 2
                    fresh -= 1
            mins += 1
        
        return mins if fresh == 0 else -1
