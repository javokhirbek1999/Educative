"""
Complexities:
  Time: O(n)
  Space: O(n)
"""
def find_sum(lst, k):
    # Write your code here
    d = {k-lst[i]:i for i in range(len(lst))}

    for i in range(len(lst)):
        if lst[i] in d and i != d[lst[i]]:
            return [lst[i], lst[d[lst[i]]]]
