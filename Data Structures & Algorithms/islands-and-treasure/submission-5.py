class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi-search bfs
        q = collections.deque()
        inf = (2**31) - 1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
        level = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != inf:
                        continue

                    grid[nr][nc] = level + 1
                    q.append([nr, nc])
            level += 1



        


