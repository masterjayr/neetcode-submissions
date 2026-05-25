class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for p1, p2 in prerequisites:
            preMap[p1].append(p2)

        visit = set()

        def dfs(i):
            if i in visit:
                return False
            if preMap[i] == []:
                return True

            visit.add(i)

            for j in preMap[i]:
                if not dfs(j):
                    return False

            visit.remove(i)
            preMap[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True