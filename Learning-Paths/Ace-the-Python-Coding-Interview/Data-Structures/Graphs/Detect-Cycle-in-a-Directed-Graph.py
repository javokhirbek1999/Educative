def detect_cycle(g): 
  
  if not g:
    return False

  source = g.array[0].head_node.data
  stack = [source]
  visited = {source:1}

  while stack:

    vert = stack.pop()

    current = g.array[vert].head_node

    while current:
      if current.data in visited:
        return True
      stack.append(current.data)
      visited[current.data] = 1
      current = current.next_element
  return False
