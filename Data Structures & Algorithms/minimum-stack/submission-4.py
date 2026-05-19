class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, val if not self.minStack else self.minStack[-1])
        self.minStack.append(minVal)

    def top(self) -> int:
        return self.stack[-1]

    def pop(self) -> None:  
        self.stack.pop()
        self.minStack.pop()

    def getMin(self) -> int:
        return self.minStack[-1]