def find_second_maximum(lst):
    
    first, second = float('-inf'), float('-inf')


    for i in range(len(lst)):

        if lst[i] > first:
            second = first
            first = lst[i]
        
        elif lst[i] > second and lst[i] != first:
            second = lst[i]
    
    if second == float('-inf'):
        return 
    return second
