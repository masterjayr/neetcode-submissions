class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        cycle = set()

        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True

            cycle.add(i)

            for pre in adj[i]:
                if not dfs(pre):
                    return False
            
            cycle.remove(i)
            visit.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True