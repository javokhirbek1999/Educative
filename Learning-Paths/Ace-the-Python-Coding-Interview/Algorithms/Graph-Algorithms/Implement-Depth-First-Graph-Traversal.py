"""
V = # of vertices
E = # of edges

Time: O(V+E)
Space: O(V)

"""

def dfs(graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    
    result = ""

    visited = [False] * graph.V

    stack = [source]

    while stack:

        vertex = stack.pop()

        result += str(vertex)

        current = graph.graph[vertex]

        while current:
            temp = current.vertex
            if not visited[temp]:
                visited[temp] = True
                stack.append(temp)
            
            current = current.next

    return result
