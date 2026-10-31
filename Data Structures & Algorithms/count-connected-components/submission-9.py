class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(n)}
        self.rank = {i: i for i in range(n)}

    def find(self, n):
        curr = n
        while curr != self.par[curr]:
            self.par[n] = self.par[self.par[curr]]
            curr = self.par[n]
        return curr

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False #cannot union already have same parent
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += 1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
            self.rank[p2] += 1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uF = UnionFind(n)

        res = n

        for e1, e2 in edges:
            if uF.union(e1, e2):
                res -= 1

        return res
        