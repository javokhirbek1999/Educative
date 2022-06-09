"""
Time: O(n)
Space: O(1)
"""
def find_max_sum_sublist(lst): 
  
  current_max, global_max = lst[0], lst[0]

  for current in lst:

    if current_max < 0:
      current_max = current
    else:
      current_max += current
    
    if global_max < current_max:
      global_max = current_max
  
  return global_max
