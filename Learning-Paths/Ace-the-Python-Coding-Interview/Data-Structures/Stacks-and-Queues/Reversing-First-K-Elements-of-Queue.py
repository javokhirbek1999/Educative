from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):

    if queue.is_empty() or k > queue.size() or k < 0:
        return None

    stack = MyStack()

    for i in range(k):
        stack.push(queue.dequeue())
    
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    
    for i in range(queue.size()-k):
        queue.enqueue(queue.dequeue())
    
    return queue
    
