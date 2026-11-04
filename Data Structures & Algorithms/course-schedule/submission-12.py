class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses) }

        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        visit = set()
        cleared = set()

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
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True