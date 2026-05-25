class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for p1, p2 in prerequisites:
            preMap[p1].append(p2)
            
        visit = set()
        output = []
        def dfs(i):
            if i in visit:
                return False

            if preMap[i] == []:
                if i not in output:
                    output.append(i)
                return True

            visit.add(i)
            for j in preMap[i]:
                if not dfs(j):
                    return False

            visit.remove(i)
            preMap[i] = []
            output.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i): return []

        return output