"""
Time: O(n)
Space: O(1)
"""
def fruits_into_baskets(fruits):
  
  windowStart = 0 

  vis = {}

  max_fruits = 0

  for windowEnd in range(len(fruits)):

    right_fruit = fruits[windowEnd]

    if right_fruit not in vis:
      vis[right_fruit] = 0
    
    vis[right_fruit] += 1

    while len(vis) > 2:
      left_fruit = fruits[windowStart]

      vis[left_fruit] -= 1

      if vis[left_fruit] == 0:
        vis.pop(left_fruit)
      
      windowStart += 1
    
    max_fruits = max(max_fruits, windowEnd - windowStart + 1)
  
  return max_fruits



