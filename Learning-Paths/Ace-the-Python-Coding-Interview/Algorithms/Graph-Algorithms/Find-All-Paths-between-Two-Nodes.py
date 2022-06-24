"""
V = # of vertices
E = # of edges

Time: O(V+E)
Space: O(V)
"""

import copy  # For deep copy if needed

def find_all_paths(graph, source, destination):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    
    queue = [[source]]

    while queue:

        path = queue.pop()

        vert = path[-1]

        if vert == destination:
            print(path)
        
        current = graph.graph[vert]

        while current:
            new_path = list(path)
            new_path.append(current.vertex)
            queue.append(new_path)
            current = current.next
           
