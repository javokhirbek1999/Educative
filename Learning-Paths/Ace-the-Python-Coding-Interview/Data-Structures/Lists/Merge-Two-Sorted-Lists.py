"""
Two-Pointer Approach

Complexities:
  Time: O(n)
  Space: O(n)

"""
def merge(list1, list2):

    l1_index = 0
    l2_index= 0
    result_index = 0

    result = []

    for i in range(len(list1)+len(list2)):
        result.append(i)
    
    while l1_index < len(list1) and l2_index < len(list2):

        if list1[l1_index] < list2[l2_index]:
            result[result_index] = list1[l1_index]
            l1_index += 1
            result_index += 1
        else:
            result[result_index] = list2[l2_index]
            l2_index += 1
            result_index += 1
        
    
    while l1_index < len(list1):
        result[result_index] = list1[l1_index]
        l1_index += 1
        result_index += 1
    
    while l2_index < len(list2):
        result[result_index] = list2[l2_index]
        l2_index += 1
        result_index += 1
    
    return result
