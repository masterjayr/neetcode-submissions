class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {")": "(", "}": "{", "]":"["}

        stack = []
        for c in s:
            if stack and c in closedToOpen:
                if stack[-1] != closedToOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return True if not stack else False