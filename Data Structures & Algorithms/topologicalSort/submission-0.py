class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        
        for i in range(n):
            adj[i] = []

        for src, dst in edges:
            adj[src].append(dst)

        visit = set()
        path = set()
        topSort = []
        

        def dfs(src, adj, visit, path, topSort):
            if src in path:
                return False
            if src in visit:
                return True

            
            path.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor, adj, visit, path, topSort):
                    return False
                    
            visit.add(src)
            path.remove(src)
            topSort.append(src)
            return True

        for i in range(n):
            if i not in visit:
                if not dfs(i, adj, visit, path, topSort):
                    return []

        topSort.reverse()
        return topSort 