"""
Complexities:
  Time: O(n)
  Space: O(n)
"""
def remove_even(lst):
    return [i for i in lst if i % 2 != 0]
