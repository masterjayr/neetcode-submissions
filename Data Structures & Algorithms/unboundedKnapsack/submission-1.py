class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # Brute force solution
        return self.dfsHelper(0, profit, weight, capacity)

    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0

        maxProfit = self.dfsHelper(i+1, profit, weight, capacity)

        newCap = capacity - weight[i]

        if newCap >= 0:

            p = profit[i] + self.dfsHelper(i, profit, weight, newCap)

            maxProfit = max(maxProfit, p)

        return maxProfit