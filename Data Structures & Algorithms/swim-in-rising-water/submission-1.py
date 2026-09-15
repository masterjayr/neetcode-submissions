class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t

            for dr, dc in directions:
                neighR, neighC = dr+r, dc + c
                if neighR < 0 or neighC < 0 or neighR == N or neighC == N or (neighR, neighC) in visit:
                    continue
                visit.add((neighR, neighC))
                heapq.heappush(minH, [max(t, grid[neighR][neighC]), neighR, neighC])