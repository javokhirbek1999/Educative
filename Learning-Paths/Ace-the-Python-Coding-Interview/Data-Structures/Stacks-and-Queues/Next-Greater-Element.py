from Stack import MyStack

def next_greater_element(lst):

    for i in range(len(lst)):
        lst[i] = find_next_greater(i, lst)
    
    return lst
    

def find_next_greater(current_index, lst):

    for i in range(current_index+1, len(lst)):
        if lst[i] > lst[current_index]:
            return lst[i]
    
    return -1

