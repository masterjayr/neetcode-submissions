class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        cleared = set()
        res = []
        def dfs(i):
            if i in visit:
                return False
            
            if i in cleared:
                return True

            visit.add(i)

            for nei in adj[i]:
                if not dfs(nei):
                    return False

            visit.remove(i)
            cleared.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res

        