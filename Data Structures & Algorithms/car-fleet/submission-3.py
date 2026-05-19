class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [(pos, sp) for pos, sp in zip(position, speed)]
        stack = []

        for pos, sp in sorted(fleet)[::-1]:
            time = (target - pos) / sp

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)