def count_paths_rec(currentNode, S, currentPath):

  if not currentNode:
    return 0
  
  currentPath.append(currentNode.val)
  pathCount, pathSum = 0, 0

  if not currentNode.left and not currentNode.right:

    for i in range(len(currentPath)-1, -1, -1):

      pathSum += currentPath[i]

      if pathSum == S:
        pathCount += 1
    
  
  pathCount += count_paths_rec(currentNode.left, S, currentPath)
  pathCount += count_paths_rec(currentNode.right, S, currentPath)

  currentPath.pop()

  return pathCount

def count_paths(root, S):
  return count_paths_rec(root, S, [])
