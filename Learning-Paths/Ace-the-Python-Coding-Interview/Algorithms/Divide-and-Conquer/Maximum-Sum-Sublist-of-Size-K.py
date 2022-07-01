import math

def max_sub_list_of_size_k(lst, k):
  """
  Finds a maximum sum of a sub-list of given window size k 
  :param lst: List of integers
  :param k: Window size of the list
  :return: Returns the maximum sum of a sub-list of given window size k
  """
  mx = -math.inf

  for i in range(len(lst)-k+1):
    window_sum = 0
    for j in range(i, i+k):
      window_sum += lst[j]
    
    mx = max(mx, window_sum)
  
  return mx
