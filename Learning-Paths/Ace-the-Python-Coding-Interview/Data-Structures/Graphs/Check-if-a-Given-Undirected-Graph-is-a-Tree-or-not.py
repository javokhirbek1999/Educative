def is_tree(g):
    # Write your code here
    
    visited = [False] * g.vertices


    if check_cycle(g, 0, visited, -1):
        return False
    

    for i in range(len(visited)):
        if not visited[i]:
            return False
    
    return True


def check_cycle(g, node, visited, parent):

    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node

    while adjacent:

        if not visited[adjacent.data]:
            if check_cycle(g, adjacent.data, visited, node):
                return True
        
        # if adjacent is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            return True
        adjacent = adjacent.next_element
    
    return False
