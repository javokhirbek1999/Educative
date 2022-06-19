def is_disjoint(list1, list2):
    
    t = {i:i for i in list1}

    i = len(list2)

    while i != 0:
        p = list2.pop()

        if p in t:
            return False
        
        i -= 1

    return True
