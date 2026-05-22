from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0


        # def dfs(r, c):
        #     if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0:
        #         return 0

        #     visited.add((r,c))
        #     res = 1
        #     res += dfs(r+1, c)
        #     res += dfs(r-1, c)
        #     res += dfs(r, c+1)
        #     res += dfs(r, c - 1)

        #     return res
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            area = 1
            while q:
                r, c = q.popleft()

                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited or grid[nr][nc] == 0:
                        continue 

                    visited.add((nr,nc))
                    q.append((nr,nc))
                    area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))

        return maxArea
        