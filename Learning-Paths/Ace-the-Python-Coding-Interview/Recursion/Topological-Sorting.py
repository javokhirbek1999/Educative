import graph as g

def sortUtil(vertex, graph, visited, stack):
  
  visited[vertex] = True

  if vertex in graph:
    for neighbor in graph[vertex]:
      if not visited[neighbor]:
        sortUtil(neighbor, graph, visited, stack)
  
  stack.insert(0, vertex)

def topologicalSort(myGraph):

  gr = myGraph.graph

  visited = [False] * (myGraph.vertices)
  print(visited)
  stack = []

  for vertex in range(myGraph.vertices):
    if not visited[vertex]:
      sortUtil(vertex, gr, visited, stack)
  
  return stack
