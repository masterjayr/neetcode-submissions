class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []

        for i, h in enumerate(heights):
            currIndex = i
            while stack and h < stack[-1][0]:
                stackHeight, stackIdx = stack.pop()
                currIndex = stackIdx
                area = stackHeight * (i - stackIdx)
                maxA = max(maxA, area)
            stack.append([h, currIndex])

        
        for h, i in stack:
            area = h * (len(heights) - i)
            maxA = max(maxA, area)

        return maxA