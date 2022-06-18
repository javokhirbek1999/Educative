def check_path(g, source, destination):
    
    if not g:
        return False
    
    queue = [source]

    visited = [False] * g.vertices
    visited[source] = True

    while queue:

        vert = queue.pop(0)

        if vert == destination:
            return True
        
        current = g.array[vert].head_node

        while current:

            if not visited[current.data]:
                visited[current.data] = True
                queue.append(current.data)
            current = current.next_element
        
    return False
