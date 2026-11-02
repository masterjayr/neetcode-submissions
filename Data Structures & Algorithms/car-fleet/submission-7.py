class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        posAndSpeed = sorted(zip(position, speed))[::-1]
        stack = []
        for p, s in posAndSpeed:
            # s = d / t, t = d/s
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)