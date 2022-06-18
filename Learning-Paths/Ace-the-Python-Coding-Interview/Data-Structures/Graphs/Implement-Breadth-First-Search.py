def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices

    queue = [source]

    while queue:

        vert = queue.pop(0)
        
        result += str(vert)

        current = g.array[vert].head_node

        while current:
            queue.append(current.data)
            current = current.next_element

    return result
