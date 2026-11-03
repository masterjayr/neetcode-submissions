class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        inf = (2**31) - 1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != inf:
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1

