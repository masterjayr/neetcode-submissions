from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))


        while queue:
            r, c = queue.popleft()

            for dr, dc in neighbors:
                nr, nc = dr+r, dc+c

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 2147483647:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))

        
