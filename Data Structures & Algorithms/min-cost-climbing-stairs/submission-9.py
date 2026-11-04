class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # further optimizing
        one, two = 0, 0

        for i in range(len(cost) -1, -1, -1):
            temp = one
            one = cost[i] + min(one, two)
            two = temp

        return min(one, two)

