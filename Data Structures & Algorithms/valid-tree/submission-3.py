class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # valid tree - fully connected, no loops

        adj = {i: [] for i in range(n)}

        for p1,p2 in edges:
            adj[p1].append(p2)
            adj[p2].append(p1)
        visit = set()
        def dfs(i, prevNode):
            if i in visit:
                return False
            
            visit.add(i)

            for j in adj[i]:
                if j == prevNode:
                    continue
                
                if not dfs(j, i):
                    return False


            return True

        return dfs(0, -1) and n == len(visit)


        


