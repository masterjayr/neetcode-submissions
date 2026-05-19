import heapq

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False 
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True



class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []

        for n1, n2, w in edges:
            heapq.heappush(minHeap, [w, n1, n2])

        unionFind = UnionFind(n)
        mst = []
        res = 0
        while len(mst) < n-1:
            if not minHeap:
                return -1 
            w, n1, n2 = heapq.heappop(minHeap)

            if not unionFind.union(n1,n2):
                continue

            mst.append([n1, n2])
            res += w
        return res