class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, sp] for pos, sp in zip(position, speed)]
        stack = []

        for pos, sp in sorted(pair)[::-1]:
            t = (target-pos) / sp

            if not stack or t > stack[-1]:
                stack.append(t)


        return len(stack)