class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

        return self.stack.append(val)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.min_stack[-1]

stack = Stack();
stack.push(2)
stack.push(10)
stack.push(9)
stack.push(1)
stack.push(5)
stack.push(6)

print(stack.min(), stack.pop())
