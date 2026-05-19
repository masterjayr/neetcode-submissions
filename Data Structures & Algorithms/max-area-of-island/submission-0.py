from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1
            neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while q:
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        (nr, nc) in visited or
                        grid[nr][nc] == 0
                    ):
                        continue

                    visited.add((nr, nc))
                    area += 1
                    q.append((nr, nc))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
