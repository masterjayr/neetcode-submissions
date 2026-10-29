class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # speed = distance - pos / time
        # speed = 3, distance = 10 - 1 => 9
        # ts = d, t = d / s
        # t1 = 9 / 3 -> 3
        # t2 = 10-4 / 2 => 3
        # both get there at 3 mins meaning they met okay

        # (1,3), (4, 2) -> sorted
        # (4,2), (1,3) -> reversed
        # tion, speed)]
        pairs = sorted(zip(position, speed))[::-1]
        stack =[]

        for p,s in pairs:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



