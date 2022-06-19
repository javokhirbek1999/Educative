def is_subset(list1, list2):

    t = len(list2)

    for i in range(len(list1)):
        temp = list1[i:i+t]
        if temp == list2:
            return True
    return False
