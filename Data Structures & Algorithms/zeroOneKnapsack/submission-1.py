class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        return self.maxProfitHelper(0, profit, weight, capacity)

    def maxProfitHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0

        maxProfit = self.maxProfitHelper(i + 1, profit, weight, capacity)

        newCap = capacity - weight[i]

        if newCap >= 0:
            p = profit[i] + self.maxProfitHelper(i + 1, profit, weight, newCap)

            maxProfit = max(maxProfit, p)

        return maxProfit

    