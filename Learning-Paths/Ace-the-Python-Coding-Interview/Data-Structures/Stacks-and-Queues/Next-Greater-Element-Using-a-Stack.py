from Stack import MyStack

def next_greater_element(lst):

    stack = []

    res = [-1]*len(lst)

    for i in range(len(lst)-1, -1, -1):

        while stack and stack[-1] <= lst[i]:
            stack.pop()
        

        if stack:
            res[i] = stack[-1]
        
        stack.append(lst[i])
    
    return res

