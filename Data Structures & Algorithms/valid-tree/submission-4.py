class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        adj= {i: [] for i in range(n)}

        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)         


        


