class Stack:
    def __init__(self):
        self.stack = []
        self.tmp_stack = []

    def push(self, val):
        if self.stack:
            while self.stack and self.stack[-1]<val:
                popped_val = self.stack.pop()
                self.tmp_stack.append(popped_val)

            self.stack.append(val)

            while self.tmp_stack:
                popped_val = self.tmp_stack.pop()
                self.stack.append(popped_val)
        else:
            self.stack.append(val)

    def pop(self):
        return self.stack.pop()


stack = Stack()
stack.push(3)
stack.push(1)
stack.push(5)
stack.push(4)
stack.push(2)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())