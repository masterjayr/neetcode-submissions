class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def backtrack(i):
            if i in cache:
                return cache[i]

            if i >= len(cost):
                return 0

            cache[i] = cost[i] + min(backtrack(i+1), backtrack(i+2))
        
            return cache[i]
        

        return min(backtrack(0), backtrack(1))