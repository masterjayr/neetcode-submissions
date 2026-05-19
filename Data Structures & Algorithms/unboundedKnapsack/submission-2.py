class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # Memoization DP
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.dfsHelper(0, profit, weight, capacity, cache)

    def dfsHelper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0

        if cache[i][capacity] != -1:
            return cache[i][capacity]

        cache[i][capacity] = self.dfsHelper(i+1, profit, weight, capacity, cache)

        newCap = capacity - weight[i]

        if newCap >= 0:

            p = profit[i] + self.dfsHelper(i, profit, weight, newCap, cache)

            cache[i][capacity] = max(cache[i][capacity], p)

        return cache[i][capacity]