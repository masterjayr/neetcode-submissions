class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit = set()
        

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)

            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            
            return True

        return dfs(0, -1) and len(visit) == n
            