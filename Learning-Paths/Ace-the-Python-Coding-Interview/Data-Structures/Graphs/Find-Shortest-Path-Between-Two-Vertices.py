def find_min(g, source, destination):
    # Write your code here
    
    visited = [False] * g.vertices
    distance = [0] * g.vertices

    queue = [source]

    while queue:

        vert = queue.pop(0)

        current = g.array[vert].head_node

        while current:
            if not visited[current.data]:
                visited[current.data] = True
                distance[current.data] = distance[vert] + 1
                queue.append(current.data)
                if current.data == destination:
                    return distance[current.data]
            current = current.next_element
    
    return -1
