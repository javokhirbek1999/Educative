def num_edges(g):
    
    c = 0

    for i in range(g.vertices):
        current = g.array[i].head_node
        while current:
            c += 1
            current = current.next_element
    
    return c//2
