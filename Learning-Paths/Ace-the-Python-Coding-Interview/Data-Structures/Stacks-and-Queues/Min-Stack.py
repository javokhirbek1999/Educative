# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()

from Stack import MyStack

class MinStack:
    # Constructor
    def __init__(self):
        self.stack = MyStack()
        self.minStack = MyStack()


    def pop(self):
        if self.stack.is_empty():
            return
        self.stack.pop()
        self.minStack.pop()

    # Pushes value into new stack
    def push(self, value):
        self.stack.push(value)

        if self.stack.is_empty() or self.minStack.is_empty():
            self.minStack.push(value)
        else:
            self.minStack.push(min(value, self.minStack.peek()))

    # Returns minimum value from new stack in constant time
    def min(self):
        return self.minStack.peek() if not self.minStack.is_empty() else -1

