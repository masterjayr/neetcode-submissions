import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []

        
        for src, dst, weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, weight])

        
        minHeap = []

        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])

        mst = []
        visit = set()
        visit.add(0)
        total = 0                   
        while minHeap and len(visit) < n:

            weight, n1, n2 = heapq.heappop(minHeap)

            if n2 in visit:
                continue
            mst.append([n1, n2])
            visit.add(n2)
            total += weight
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])


        return total if len(visit) == n else -1