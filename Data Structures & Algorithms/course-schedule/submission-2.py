class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}

        visit = set()

        for c1, c2 in prerequisites:
            pre[c1].append(c2)

        def dfs(crs):
            if crs in visit:
                return False

            if pre[crs] == []:
                return True

            visit.add(crs)
            for c in pre[crs]:
                if not dfs(c): return False

            visit.remove(crs)
            pre[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
