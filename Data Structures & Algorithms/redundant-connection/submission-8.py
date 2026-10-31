class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[n]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            else:
                par[p2] = p1
                rank[p1] += 1

            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2] 