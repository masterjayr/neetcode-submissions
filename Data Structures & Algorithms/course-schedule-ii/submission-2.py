class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        N = numCourses
        preMap = {i: [] for i in range(N)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        visit, cycle = set(), set()
        output = []
        def dfs(crs):

            if crs in cycle:
                return False

            if crs in visit:
                return True

            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        

        for crs in preMap:
            if not dfs(crs):
                return []

        return output