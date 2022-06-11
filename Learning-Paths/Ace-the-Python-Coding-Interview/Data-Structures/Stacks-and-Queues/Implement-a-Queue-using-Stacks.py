from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.secondary_stack = MyStack()


    # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        self.main_stack.push(value)

    # Removes Element From Queue
    def dequeue(self):
        if self.main_stack.is_empty():
            return None
        while not self.main_stack.is_empty():
            self.secondary_stack.push(self.main_stack.pop())
        
        item = self.secondary_stack.pop()
        
        while not self.secondary_stack.is_empty():
            self.main_stack.push(self.secondary_stack.pop())
        
        return item
