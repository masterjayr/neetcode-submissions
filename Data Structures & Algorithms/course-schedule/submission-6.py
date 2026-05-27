class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}

        for c1, c2 in prerequisites:
            pre[c1].append(c2)


        visit = set()

        def dfs(i):
            if i in visit:
                return False
            
            if pre[i] ==  []:
                return True

            visit.add(i)
            for nei in pre[i]:
                if not dfs(nei):
                    return False

            visit.remove(i)
            pre[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False 

        return True