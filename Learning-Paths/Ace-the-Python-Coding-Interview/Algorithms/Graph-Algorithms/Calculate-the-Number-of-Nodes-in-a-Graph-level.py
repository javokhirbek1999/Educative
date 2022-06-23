"""
Time: O(V+E)
Space: O(V)
"""

def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    visited = [False] * graph.V
    visited[0] = True

    queue = [0]

    lv = 0

    while queue:


        n = len(queue)

        lv += 1
        
        nodes = 0

        for _ in range(n):

            vert = queue.pop(0)
            nodes += 1
            current = graph.graph[vert]

            while current:
                temp = current.vertex

                if not visited[temp]:
                    visited[temp] = True
                    queue.append(temp)
                
                current = current.next
        if lv == level:
            return nodes
    
    return 0
        
