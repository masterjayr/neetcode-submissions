class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N) } #index i is [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        minH = [[0, 0]]
        visitSet = set()

        while len(visitSet) < N:
            cost, node = heapq.heappop(minH)
            if node in visitSet:
                continue
            visitSet.add(node)
            res += cost

            for neighCost, neighNode in adj[node]:
                if neighNode not in visitSet:
                    heapq.heappush(minH, [neighCost, neighNode])

        return res
