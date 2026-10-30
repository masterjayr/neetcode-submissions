class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        cleared = set()

        def dfs(i):
            if i in visit:
                return False
            if i in cleared:
                return True

            visit.add(i)

            for pre in adj[i]:
                if not dfs(pre):
                    return False
            
            visit.remove(i)
            cleared.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True