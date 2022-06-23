"""
Time: O(V+E)
Space: O(V)
"""
def transpose(graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: a new transposed graph of the given graph
    """

    new_graph = Graph(graph.V)  # Creating a new graph

    for v in range(graph.V):
        source = v
        current = graph.graph[source]

        while current:
            new_graph.add_edge(current.vertex, source)
            current = current.next

    return new_graph
    
