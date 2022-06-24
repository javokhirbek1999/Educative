def connected_components(graph):
    """
    Function to find the connected components
    :param graph: The graph
    :return: returns a list of connected components
    """

    visited = [False] * graph.V
    res = []

    for v in range(graph.V):
        if not visited[v]:
            res.append(dfs(graph, v, visited))
    
    
    return res


# Helper Function of DFS. Might be useful
def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a list
    """

    graph = copy.deepcopy(g)

    # Create a stack for DFS
    stack = []

    # Result list
    result = []

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack[-1]
        stack.pop()

        if not visited[source]:
            result.append(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next

    return result
