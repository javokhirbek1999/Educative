from collections import defaultdict

def is_strongly_connected(graph):
    """
    Finds if the graph is strongly connected or not
    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    
    A directed graph is strongly connected if there is a path between any two pairs of vertices.
    """
    
    for i in range(graph.V):
        if not graph.graph[i]:
            return False
    
    return True
    
