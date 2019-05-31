import sys
       
class MinStack:

    def __init__(self):
        self.min_stack = [sys.maxsize]
        self.stack = []

    def push(self, x: int) -> None:
        min_val = self.min_stack[-1]
        if x < min_val:
            min_val = x

        self.stack.append(x)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

minStack = MinStack()

minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
print(minStack.top())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
minStack.push(2147483647)
print(minStack.top())
print(minStack.getMin())
minStack.push(-2147483648)
print(minStack.top())
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())



