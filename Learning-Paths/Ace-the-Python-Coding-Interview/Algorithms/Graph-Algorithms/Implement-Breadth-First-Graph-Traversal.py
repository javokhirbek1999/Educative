"""
v = # of vertices
e = # of edges

Time: O(v+e)
Space: O(v)

"""
def bfs(graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """

    # Write your code here!
    result = ""

    visited = [False] * graph.V
    visited[source] = True

    queue = [source]

    while queue:

        vert = queue.pop(0)

        result+=str(vert)

        current = graph.graph[vert]

        while current:
            if not visited[current.vertex]:
                visited[current.vertex] = True
                queue.append(current.vertex)
            
            current = current.next

    return result
