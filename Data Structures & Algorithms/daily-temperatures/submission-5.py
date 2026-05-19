class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                stackIdx, stackVal = stack.pop()
                noOfDays = i - stackIdx
                res[stackIdx] = noOfDays

            stack.append((i, val))

        return res