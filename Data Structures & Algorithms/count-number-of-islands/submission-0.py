from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r,c))
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in visited or grid[nr][nc] == "0":
                        continue

                    visited.add((nr,nc))
                    q.append((nr,nc)) 

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands


