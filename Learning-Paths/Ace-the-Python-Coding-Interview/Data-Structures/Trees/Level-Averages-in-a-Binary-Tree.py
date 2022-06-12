class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  
  if not root:
    return []

  result = []

  queue = [root]

  while queue:
    level_sum = 0
    c = 0

    max_len = len(queue)

    while max_len > 0:

      node = queue.pop(0)

      level_sum += node.val

      if node.left:
        queue.append(node.left)
      
      if node.right:
        queue.append(node.right)
      
      max_len -= 1
      c += 1
    
    result.append(level_sum/c)

  return result
