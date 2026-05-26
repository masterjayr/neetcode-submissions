class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (N + 1)


        def find(n):
            res = n
            while res != par[res]:
                par[n] = par[par[n]]
                res = par[n]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]

        return [-1, -1]
