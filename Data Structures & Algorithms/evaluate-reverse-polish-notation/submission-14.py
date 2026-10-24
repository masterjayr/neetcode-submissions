class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                val = int(t)
                stack.append(val)

        return stack[-1]