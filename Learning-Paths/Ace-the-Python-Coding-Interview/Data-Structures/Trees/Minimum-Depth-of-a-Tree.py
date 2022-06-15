def find_minimum_depth(root):

  if not root:
    return 0

  queue = [root]

  min_level = 0

  while queue:

    min_level += 1

    max_len = len(queue)

    for _ in range(max_len):

      node = queue.pop(0)

      if not node.left and not node.right:
        return min_level
      
      if node.left:
        queue.append(node.left)
      
      if node.right:
        queue.append(node.right)
  
  return min_level
