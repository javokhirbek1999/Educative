"""
Time: O(n)
Space: O(1)

"""
def rearrange(lst):
    left_most_index = 0

    for current_index in range(len(lst)):

        if lst[current_index] < 0:

            if current_index != left_most_index:
                lst[current_index], lst[left_most_index] = lst[left_most_index], lst[current_index]
            
            left_most_index += 1
    
    return lst
