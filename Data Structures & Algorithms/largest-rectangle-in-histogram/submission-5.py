class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i 

            while stack and stack[-1][1] > h:
                stackIdx, stackHeight = stack.pop()
                maxArea = max(maxArea, ((i - stackIdx) * stackHeight))
                start = stackIdx
            
            stack.append([start, h])

        
        for i, h in stack:
            maxArea = max(maxArea, ((len(heights) -i) * h))
        
        return maxArea